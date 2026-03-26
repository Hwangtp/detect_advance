# 추가 설치 없음

"""Ollama 로컬 채팅 최소 테스트.

이 파일은 Ollama가 실행 중인지 확인하고,
로컬 API로 아주 간단한 질문을 보내 답변이 돌아오는지 확인하는 최소 예제이다.
현재 PC에서는 gemma3:4b 모델이 정상 응답하므로 기본 모델을 gemma3:4b로 둔다.
"""

# json은 Ollama API에 보낼 요청 본문을 JSON 문자열로 바꾸는 데 사용한다.
import json

# urllib.request는 별도 라이브러리 설치 없이 로컬 HTTP API를 호출하기 위해 사용한다.
from urllib import request

# API 주소와 사용할 모델 이름을 상수로 두면 나중에 다른 모델로 바꾸기 쉽다.
OLLAMA_API_URL = 'http://127.0.0.1:11434/api/chat'
MODEL_NAME = 'gemma3:4b'

# 실제 채팅 메시지를 한 군데에 모아 두면 질문을 바꿔 테스트하기 편하다.
messages = [
    {
        'role': 'user',
        'content': '안녕하세요. 한 문장으로 자기소개를 해주세요.',
    }
]

# Ollama chat API는 model, messages, stream 같은 값을 JSON으로 받는다.
payload = {
    'model': MODEL_NAME,
    'messages': messages,
    'stream': False,
}

# JSON 데이터를 UTF-8 바이트로 바꿔 HTTP 요청 본문으로 보낸다.
data = json.dumps(payload).encode('utf-8')
req = request.Request(
    OLLAMA_API_URL,
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST',
)

print('=== Ollama 간단 채팅 테스트 ===')
print('사용 모델:', MODEL_NAME)
print('질문:', messages[0]['content'])

# 응답 JSON 안에는 message -> content 경로로 실제 답변이 들어 있다.
with request.urlopen(req, timeout=300) as response:
    result = json.loads(response.read().decode('utf-8'))

answer = result['message']['content']
print('\n[모델 답변]')
print(answer)