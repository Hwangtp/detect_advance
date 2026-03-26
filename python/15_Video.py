# 15_Video.py
# 동영상 파일 불러오기 실습 파일
# 이 파일에서는 OpenCV 라이브러리를 사용하여 동영상 파일을 불러와 재생합니다.
# 초심자를 위해 단계별로 설명합니다.
# pip install opencv-python  # OpenCV 설치 필요
# 동영상 파일 (예: sample.mp4)을 같은 폴더에 준비하세요.

import cv2  # OpenCV 라이브러리를 임포트합니다. 비디오 처리에 사용됩니다.

# 동영상 파일 경로 지정
video_path = 'sample.mp4'  # 재생할 동영상 파일의 경로를 지정합니다.
# 파일이 같은 폴더에 있으면 파일명만, 다른 경로면 전체 경로를 입력하세요.

# 동영상 파일 열기
cap = cv2.VideoCapture(video_path)  # 동영상 파일을 엽니다.
# VideoCapture 객체로 파일로부터 프레임을 읽습니다.

# 파일이 제대로 열렸는지 확인
if not cap.isOpened():  # 파일을 열지 못했으면
    print(f"동영상 파일 '{video_path}'을 열 수 없습니다.")  # 오류 메시지를 출력합니다.
    exit()  # 프로그램을 종료합니다.

print("동영상 파일이 열렸습니다. 'q' 키를 눌러 종료하세요.")  # 사용자에게 안내 메시지를 출력합니다.

# 동영상 재생 루프
while True:  # 무한 루프를 시작합니다. 동영상을 계속 재생합니다.
    ret, frame = cap.read()  # 동영상으로부터 한 프레임을 읽습니다.
    # ret: 프레임 읽기 성공 여부 (True/False, 파일 끝이면 False)
    # frame: 읽은 이미지 데이터

    if not ret:  # 프레임을 읽지 못했으면 (동영상 끝)
        print("동영상 재생이 끝났습니다.")  # 메시지를 출력합니다.
        break  # 루프를 종료합니다.

    cv2.imshow('Video', frame)  # 읽은 프레임을 창에 표시합니다.
    # 'Video'는 창의 제목입니다.

    # 키 입력 대기 및 종료 조건
    if cv2.waitKey(25) & 0xFF == ord('q'):  # 약 25ms 동안 키 입력을 기다립니다. (FPS에 맞춤)
        # 'q' 키가 눌렸으면 루프를 종료합니다.
        break

# 리소스 정리
cap.release()  # 동영상 파일 연결을 해제합니다.
cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫습니다.

print("동영상 실습이 종료되었습니다.")  # 종료 메시지를 출력합니다.

# 미션: 동영상을 회색으로 변환하여 재생하세요. (힌트: cv2.cvtColor 사용)
# 정답:
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 프레임을 회색으로 변환
# cv2.imshow('Gray Video', gray)  # 회색 동영상을 표시