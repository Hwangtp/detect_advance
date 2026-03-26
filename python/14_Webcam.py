# 14_Webcam.py
# 웹캠 연동 실습 파일
# 이 파일에서는 OpenCV 라이브러리를 사용하여 웹캠을 연결하고 실시간 영상을 표시합니다.
# 초심자를 위해 단계별로 설명합니다.
# pip install opencv-python  # OpenCV 설치 필요

import cv2  # OpenCV 라이브러리를 임포트합니다. 컴퓨터 비전을 위한 라이브러리입니다.

# 웹캠 연결
cap = cv2.VideoCapture(0)  # 웹캠을 연결합니다. 0은 기본 웹캠을 의미합니다.
# VideoCapture 객체를 생성하여 웹캠으로부터 영상을 캡처합니다.

# 웹캠이 제대로 열렸는지 확인
if not cap.isOpened():  # 웹캠이 열리지 않았으면
    print("웹캠을 열 수 없습니다.")  # 오류 메시지를 출력합니다.
    exit()  # 프로그램을 종료합니다.

print("웹캠이 연결되었습니다. 'q' 키를 눌러 종료하세요.")  # 사용자에게 안내 메시지를 출력합니다.

# 실시간 영상 표시 루프
while True:  # 무한 루프를 시작합니다. 영상을 계속 표시합니다.
    ret, frame = cap.read()  # 웹캠으로부터 한 프레임을 읽습니다.
    # ret: 프레임 읽기 성공 여부 (True/False)
    # frame: 읽은 이미지 데이터 (NumPy 배열)

    if not ret:  # 프레임을 읽지 못했으면
        print("프레임을 읽을 수 없습니다.")  # 오류 메시지를 출력합니다.
        break  # 루프를 종료합니다.

    cv2.imshow('Webcam', frame)  # 읽은 프레임을 창에 표시합니다.
    # 'Webcam'은 창의 제목입니다.

    # 키 입력 대기 및 종료 조건
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 1ms 동안 키 입력을 기다립니다.
        # 'q' 키가 눌렸으면 루프를 종료합니다.
        break

# 리소스 정리
cap.release()  # 웹캠 연결을 해제합니다.
cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫습니다.

print("웹캠 실습이 종료되었습니다.")  # 종료 메시지를 출력합니다.

# 미션: 웹캠 영상을 회색으로 변환하여 표시하세요. (힌트: cv2.cvtColor 사용)
# 정답:
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 프레임을 회색으로 변환
# cv2.imshow('Gray Webcam', gray)  # 회색 영상을 표시