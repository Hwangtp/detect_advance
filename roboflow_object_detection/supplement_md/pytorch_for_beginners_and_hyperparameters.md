# PyTorch 부록. 초심자용 입문과 하이퍼파라미터

<div style="background: linear-gradient(135deg, #b91c1c, #ea580c); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">PyTorch가 무엇인지, 텐서와 모델 학습이 어떤 흐름으로 진행되는지, 그리고 하이퍼파라미터가 결과에 어떤 영향을 주는지 초심자 눈높이에서 설명하는 보충 자료입니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">핵심 학습 내용</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>PyTorch와 tensor의 기본 개념</li>
    <li>nn.Module, forward, loss, backward, step의 역할</li>
    <li>DataLoader와 batch 학습 흐름</li>
    <li>hidden_units, learning_rate, batch_size, epochs 비교</li>
  </ul>
</div>

<div style="background-color:#fefce8; border:1px solid #fde047; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#a16207;">하이퍼파라미터 메모</h3>
  <p style="margin:0; line-height:1.9;">하이퍼파라미터는 모델이 학습을 시작하기 전에 사람이 정하는 값입니다. learning_rate는 한 번에 얼마나 크게 움직일지, batch_size는 몇 개씩 묶어 학습할지, hidden_units는 은닉층 너비를 얼마나 줄지, epochs는 전체 데이터를 몇 번 반복할지를 뜻합니다.</p>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">학습 가이드</h3>
  <p style="margin:0; line-height:1.9;">이 부록 파일은 한 번에 실행되도록 구성되어 있으므로 처음에는 전체를 그대로 돌려 보고, 그다음 learning_rate나 batch_size만 하나씩 바꿔 보면서 결과 차이를 관찰하면 이해가 빠릅니다.</p>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd


import torch


from torch import nn


from torch.utils.data import DataLoader, TensorDataset


from sklearn.model_selection import train_test_split


from sklearn.preprocessing import StandardScaler


torch.manual_seed(42)
print("=== PyTorch 보충: 초심자용 입문과 하이퍼파라미터 ===")


df = pd.read_csv("data/student_learning_extended.csv")
X = df[['study_hours', 'practice_hours', 'sleep_hours']]
y = df['passed']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.to_numpy(), dtype=torch.int64)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.to_numpy(), dtype=torch.int64)


train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)


class SimpleClassifier(nn.Module):
    def __init__(self, hidden_units: int = 16):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(3, hidden_units),
            nn.ReLU(),
            nn.Linear(hidden_units, 2),
        )

    def forward(self, x):

        return self.network(x)

def train_once(hidden_units: int, learning_rate: float, batch_size: int, epochs: int) -> dict:

    torch.manual_seed(42)
    loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    model = SimpleClassifier(hidden_units=hidden_units)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for _ in range(epochs):
        model.train()
        for batch_X, batch_y in loader:

            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)

            loss.backward()

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


base_result = train_once(hidden_units=16, learning_rate=0.01, batch_size=32, epochs=120)
print("\n[실습 1] 기본 설정 결과")
print(base_result)


lr_results = [
    train_once(hidden_units=16, learning_rate=0.001, batch_size=32, epochs=120),
    train_once(hidden_units=16, learning_rate=0.01, batch_size=32, epochs=120),
    train_once(hidden_units=16, learning_rate=0.05, batch_size=32, epochs=120),
]
print("\n[실습 2] learning_rate 비교")
for row in lr_results:
    print(row)


batch_results = [
    train_once(hidden_units=16, learning_rate=0.01, batch_size=16, epochs=120),
    train_once(hidden_units=16, learning_rate=0.01, batch_size=64, epochs=120),
    train_once(hidden_units=16, learning_rate=0.01, batch_size=256, epochs=120),
]
print("\n[실습 3] batch_size 비교")
for row in batch_results:
    print(row)


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
```
