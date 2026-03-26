"""PyTorch 초심자용 보충 파일.

이 파일은 PyTorch가 무엇인지, 텐서와 모델 학습이 어떤 흐름으로 진행되는지,
그리고 하이퍼파라미터가 결과에 어떤 영향을 주는지 한 번에 설명하기 위한 보충 자료다.
"""

import pandas as pd
# pandas는 CSV 데이터를 읽어 입력값과 정답을 표 형태로 다루기 위해 사용한다.

import torch
# torch는 텐서 계산, 자동미분, 신경망 학습 전체를 담당하는 핵심 라이브러리다.

from torch import nn
# nn은 선형층, 활성화 함수, 손실 함수처럼 신경망 구성요소를 가져오기 위해 불러온다.

from torch.utils.data import DataLoader, TensorDataset
# TensorDataset과 DataLoader는 데이터를 배치 단위로 나누어 학습시키기 위해 사용한다.

from sklearn.model_selection import train_test_split
# train_test_split은 학습용과 평가용 데이터를 분리해 일반화 성능을 확인하기 위해 사용한다.

from sklearn.preprocessing import StandardScaler
# StandardScaler는 입력값 크기를 맞춰 학습을 더 안정적으로 만들기 위해 사용한다.

torch.manual_seed(42)
print("=== PyTorch 보충: 초심자용 입문과 하이퍼파라미터 ===")

# 학생 학습 데이터를 사용하면 입력 특징과 합격 여부를 분류 문제로 쉽게 설명할 수 있다.
df = pd.read_csv("data/student_learning_extended.csv")
X = df[['study_hours', 'practice_hours', 'sleep_hours']]
y = df['passed']

# 먼저 train/test를 나누어 학습하지 않은 데이터로 성능을 확인한다.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 표준화는 각 특징의 단위를 맞춰 optimizer가 덜 흔들리게 해 준다.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# PyTorch는 numpy 배열 대신 tensor를 사용하므로 float32, int64 형식을 명시한다.
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.to_numpy(), dtype=torch.int64)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.to_numpy(), dtype=torch.int64)

# TensorDataset은 입력값과 정답을 짝지어 주고, DataLoader는 배치 단위로 꺼내 준다.
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# nn.Module을 상속하면 우리가 원하는 신경망 구조를 직접 정의할 수 있다.
class SimpleClassifier(nn.Module):
    def __init__(self, hidden_units: int = 16):
        super().__init__()
        # hidden_units는 은닉층 너비를 정하는 하이퍼파라미터다.
        self.network = nn.Sequential(
            nn.Linear(3, hidden_units),
            nn.ReLU(),
            nn.Linear(hidden_units, 2),
        )

    def forward(self, x):
        # forward는 입력이 모델을 통과해 출력 점수(logit)로 바뀌는 경로를 정의한다.
        return self.network(x)


def train_once(hidden_units: int, learning_rate: float, batch_size: int, epochs: int) -> dict:
    # 하이퍼파라미터를 바꾸면 학습 속도와 최종 성능이 달라지는 모습을 비교할 수 있다.
    torch.manual_seed(42)
    loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    model = SimpleClassifier(hidden_units=hidden_units)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for _ in range(epochs):
        model.train()
        for batch_X, batch_y in loader:
            # gradient를 초기화하지 않으면 이전 배치의 기울기가 누적되므로 먼저 0으로 만든다.
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            # backward는 손실을 기준으로 각 가중치의 기울기를 계산한다.
            loss.backward()
            # step은 계산된 기울기로 실제 가중치를 한 번 업데이트한다.
            optimizer.step()

    model.eval()
    with torch.no_grad():
        logits = model(X_test_tensor)
        preds = torch.argmax(logits, dim=1)
        acc = (preds == y_test_tensor).float().mean().item()

    return {
        'hidden_units': hidden_units,
        'learning_rate': learning_rate,
        'batch_size': batch_size,
        'epochs': epochs,
        'accuracy': round(acc, 4),
    }

# 기본 설정으로 먼저 한 번 돌려 보며 전체 흐름을 확인한다.
base_result = train_once(hidden_units=16, learning_rate=0.01, batch_size=32, epochs=120)
print("\n[실습 1] 기본 설정 결과")
print(base_result)

# learning rate를 바꾸면 너무 느리거나 너무 큰 업데이트가 어떤 차이를 만드는지 볼 수 있다.
lr_results = [
    train_once(hidden_units=16, learning_rate=0.001, batch_size=32, epochs=120),
    train_once(hidden_units=16, learning_rate=0.01, batch_size=32, epochs=120),
    train_once(hidden_units=16, learning_rate=0.05, batch_size=32, epochs=120),
]
print("\n[실습 2] learning_rate 비교")
for row in lr_results:
    print(row)

# batch size는 한 번에 몇 개 샘플을 보고 업데이트할지 정하는 하이퍼파라미터다.
batch_results = [
    train_once(hidden_units=16, learning_rate=0.01, batch_size=16, epochs=120),
    train_once(hidden_units=16, learning_rate=0.01, batch_size=64, epochs=120),
    train_once(hidden_units=16, learning_rate=0.01, batch_size=256, epochs=120),
]
print("\n[실습 3] batch_size 비교")
for row in batch_results:
    print(row)

# hidden_units는 모델 표현력을 바꾸므로 너무 작거나 너무 크면 결과가 달라질 수 있다.
hidden_results = [
    train_once(hidden_units=4, learning_rate=0.01, batch_size=32, epochs=120),
    train_once(hidden_units=16, learning_rate=0.01, batch_size=32, epochs=120),
    train_once(hidden_units=32, learning_rate=0.01, batch_size=32, epochs=120),
]
print("\n[실습 4] hidden_units 비교")
for row in hidden_results:
    print(row)

print("\n[실습 5] 하이퍼파라미터 해석")
print('learning_rate, batch_size, hidden_units, epochs는 사람이 먼저 정하는 값이며, 같은 데이터라도 결과를 바꿀 수 있다.')
