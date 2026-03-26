# linux_wsl Overview

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">학습 로드맵</h2>
  <p style="margin:0; line-height:1.8;">
    이 폴더는 WSL Ubuntu를 기준으로 리눅스를 거의 처음 배우는 학습자를 위한 20차시 수업 자료입니다.
    리눅스와 터미널의 기초부터 파일, 경로, 계정, 권한, 프로세스, 네트워크, 배시 스크립트, Flask 실행,
    Gunicorn, Docker, Docker Compose 기반 배포 예시까지 단계적으로 이어집니다.
  </p>
</div>

## 파일 구성

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
              <h3 style="margin:0 0 10px 0; color:#1d4ed8;">기초 구조와 경로</h3>
              <ul style="margin:0; padding-left:20px; line-height:1.8;">
                <li style="margin:8px 0;"><code>01</code> 리눅스와 WSL 첫걸음: 리눅스가 무엇인지 이해하고 WSL Ubuntu 터미널에 익숙해진다.</li>
<li style="margin:8px 0;"><code>02</code> 터미널 이동과 경로 이해: 절대경로와 상대경로를 구분하고 원하는 폴더로 정확히 이동한다.</li>
<li style="margin:8px 0;"><code>03</code> 파일과 디렉터리 기본 조작: 파일 생성, 폴더 생성, 복사 전 준비 작업을 익힌다.</li>
<li style="margin:8px 0;"><code>04</code> 복사 이동 삭제와 파일 찾기: cp, mv, rm, find를 이해하고 안전하게 파일을 관리한다.</li>
              </ul>
            </div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
              <h3 style="margin:0 0 10px 0; color:#15803d;">파일, 권한, 시스템 기초</h3>
              <ul style="margin:0; padding-left:20px; line-height:1.8;">
                <li style="margin:8px 0;"><code>05</code> 텍스트 읽기와 편집: cat, less, head, tail, nano로 텍스트 파일을 읽고 수정한다.</li>
<li style="margin:8px 0;"><code>06</code> 리다이렉션과 파이프: 출력 방향을 바꾸고 여러 명령어를 연결하는 법을 익힌다.</li>
<li style="margin:8px 0;"><code>07</code> 권한과 소유자: ls -l 결과를 읽고 chmod로 권한을 바꿀 수 있다.</li>
<li style="margin:8px 0;"><code>08</code> 사용자 그룹 sudo 이해: 사용자와 그룹, sudo의 의미를 이해하고 안전하게 시스템 명령을 실행한다.</li>
<li style="margin:8px 0;"><code>09</code> 프로세스 작업 제어 모니터링: 실행 중인 프로그램을 확인하고 종료하거나 백그라운드로 보낸다.</li>
<li style="margin:8px 0;"><code>10</code> 패키지 관리와 환경 정보: apt로 프로그램을 설치하고 환경 관련 명령을 이해한다.</li>
              </ul>
            </div>

<div style="background-color:#fefce8; border:1px solid #fde047; border-radius:16px; padding:16px 18px; margin:14px 0;">
              <h3 style="margin:0 0 10px 0; color:#a16207;">네트워크와 스크립트</h3>
              <ul style="margin:0; padding-left:20px; line-height:1.8;">
                <li style="margin:8px 0;"><code>11</code> 네트워크 기초와 다운로드: IP, 포트, localhost를 이해하고 curl과 wget을 사용한다.</li>
<li style="margin:8px 0;"><code>12</code> 압축 로그 디스크 사용량: tar, zip, du, df, tail을 이용해 로그와 파일 묶음을 다룬다.</li>
<li style="margin:8px 0;"><code>13</code> 배시 스크립트 기초: 셸 스크립트 구조와 변수, 입력, 조건문의 기본을 익힌다.</li>
<li style="margin:8px 0;"><code>14</code> 배시 스크립트 실전 자동화: 반복문과 파일 작업을 활용해 작은 자동화 도구를 만든다.</li>
              </ul>
            </div>

<div style="background-color:#ecfeff; border:1px solid #67e8f9; border-radius:16px; padding:16px 18px; margin:14px 0;">
              <h3 style="margin:0 0 10px 0; color:#0f766e;">개발 환경과 Flask 실행</h3>
              <ul style="margin:0; padding-left:20px; line-height:1.8;">
                <li style="margin:8px 0;"><code>15</code> WSL에서 파이썬과 가상환경: python3, pip, venv를 이용해 개발 환경을 분리한다.</li>
<li style="margin:8px 0;"><code>16</code> Flask 실행과 포트 확인: 간단한 Flask 앱을 실행하고 localhost와 포트 개념을 확인한다.</li>
<li style="margin:8px 0;"><code>17</code> Gunicorn과 백그라운드 실행: 개발 서버와 운영 서버의 차이를 알고 Gunicorn으로 앱을 실행한다.</li>
              </ul>
            </div>

<div style="background-color:#faf5ff; border:1px solid #d8b4fe; border-radius:16px; padding:16px 18px; margin:14px 0;">
              <h3 style="margin:0 0 10px 0; color:#7e22ce;">Docker와 최종 배포</h3>
              <ul style="margin:0; padding-left:20px; line-height:1.8;">
                <li style="margin:8px 0;"><code>18</code> 도커 입문과 기본 명령어: Docker가 무엇인지 이해하고 이미지와 컨테이너를 직접 실행한다.</li>
<li style="margin:8px 0;"><code>19</code> Dockerfile과 Compose로 Flask 묶기: Flask 앱을 Docker 이미지로 만들고 compose로 실행한다.</li>
<li style="margin:8px 0;"><code>20</code> 최종 배포 프로젝트: WSL Ubuntu에서 Flask 앱을 Docker Compose로 실행하고 배포 흐름을 정리한다.</li>
              </ul>
            </div>

## 학습 순서 추천

<div style="background-color:#f8fafc; border-left:8px solid #334155; padding:16px 18px; border-radius:12px; margin:12px 0;">
  <ol style="margin:0; padding-left:20px; line-height:1.9;">
    <li><code>01</code> ~ <code>04</code>로 리눅스와 경로 구조 감각 익히기</li>
    <li><code>05</code> ~ <code>10</code>으로 파일, 권한, 프로세스, 패키지 관리 다루기</li>
    <li><code>11</code> ~ <code>14</code>로 네트워크와 배시 스크립트 자동화 익히기</li>
    <li><code>15</code> ~ <code>17</code>로 Python, Flask, Gunicorn 흐름 연결하기</li>
    <li><code>18</code> ~ <code>20</code>으로 Docker와 최종 배포 예제 완성하기</li>
  </ol>
</div>

## 사용 목적

<div style="background-color:#fffbeb; border:1px solid #fcd34d; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>WSL Ubuntu 기반 리눅스 입문 수업 자료</li>
    <li>서버 기초와 터미널 실습 중심 강의 자료</li>
    <li>Flask와 Docker를 활용한 배포 입문 자료</li>
  </ul>
</div>

## 권장 환경

<div style="background-color:#eef2ff; border:1px solid #a5b4fc; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>Windows + WSL Ubuntu</li>
    <li>터미널: Windows Terminal 또는 VS Code Terminal</li>
    <li>추가 도구: Python 3, Flask, Gunicorn, Docker</li>
  </ul>
</div>
