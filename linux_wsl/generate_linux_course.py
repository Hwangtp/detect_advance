from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parent
INSTRUCTOR_DIR = ROOT / "instructor_files"
STUDENT_DIR = ROOT / "student_md"
EXAMPLES_DIR = ROOT / "examples" / "final_flask_docker_app"


LESSONS = [
    {
        "no": "01",
        "slug": "linux_and_wsl_first_steps",
        "title": "리눅스와 WSL 첫걸음",
        "goal": "리눅스가 무엇인지 이해하고 WSL Ubuntu 터미널에 익숙해진다.",
        "summary": "리눅스의 역할, WSL Ubuntu의 의미, 터미널 프롬프트, 현재 사용자와 운영체제 정보를 읽는 실습을 진행한다.",
        "concepts": [
            "리눅스는 서버, 개발, 배포 환경에서 많이 사용하는 운영체제이다.",
            "WSL은 Windows 안에서 Linux 환경을 사용할 수 있게 해주는 기능이다.",
            "터미널은 마우스보다 명령어로 시스템을 다루는 화면이다.",
            "루트 디렉터리 / 는 리눅스 전체의 시작점이고 홈 디렉터리 ~ 는 현재 계정의 개인 작업 공간이다.",
        ],
        "commands": [
            ("pwd", "pwd는 print working directory의 약자이며 현재 작업 위치를 출력한다. 옵션 없이 자주 사용한다."),
            ("whoami", "whoami는 현재 로그인한 사용자 이름을 확인한다. 권한 관련 실습에서 매우 중요하다."),
            ("echo $USER", "echo $USER 는 현재 로그인한 계정 이름을 변수로 확인하는 방법이다. whoami와 결과를 비교해 볼 수 있다."),
            ("uname -a", "uname은 시스템 정보를 보여준다. -a 옵션은 커널, 아키텍처 등 가능한 많은 정보를 함께 출력한다."),
            ("cat /etc/os-release", "cat은 파일 내용을 그대로 출력한다. /etc/os-release는 배포판 정보가 들어 있는 대표 파일이다."),
            ("hostname", "hostname은 현재 컴퓨터 이름을 확인한다. 서버 식별에 자주 사용한다."),
            ("date", "date는 현재 시스템 날짜와 시간을 출력한다. 로그 해석과 예약 작업에서 자주 쓴다."),
            ("ls /", "ls는 목록을 보는 명령어다. /는 루트 디렉터리이며 리눅스 최상위 위치다."),
            ("ls /home", "WSL Ubuntu에서는 일반 사용자 홈 폴더가 /home 아래에 생성된다."),
            ("echo $HOME", "echo는 문자열이나 변수 값을 출력한다. $HOME은 현재 사용자의 홈 디렉터리 경로다."),
            ("echo /home/$USER", "현재 계정 홈 경로를 직접 조합해 보는 실습이다. $USER와 $HOME의 관계를 눈으로 확인한다."),
            ("ls -ld / /home ~", "ls -ld 의 -d 옵션은 디렉터리 자체 정보를 보여준다. 루트, home, 현재 계정 홈을 한 번에 비교한다."),
            ("cd ~", "cd는 디렉터리를 이동한다. ~는 홈 디렉터리를 의미한다."),
            ("pwd", "홈 디렉터리로 이동한 뒤 현재 위치가 정말 홈인지 다시 확인한다."),
            ("cd /", "루트 디렉터리로 이동해 홈과 다른 출발점이라는 점을 직접 확인한다."),
            ("pwd", "루트 디렉터리에서는 / 가 출력되는지 확인한다."),
            ("mkdir -p ~/linux_lab/day01", "mkdir은 폴더를 만든다. -p 옵션은 중간 폴더가 없어도 한 번에 생성한다."),
            ("cd ~/linux_lab/day01", "실습 폴더로 이동해 이후 작업을 한곳에 모은다."),
            ("touch welcome.txt", "touch는 빈 파일을 만든다. 기존 파일이 있으면 수정 시간만 갱신한다."),
            ("echo 'Linux class starts here.' > welcome.txt", "리다이렉션 > 는 명령어 결과를 파일에 덮어쓴다. 첫 실습 파일 내용을 만든다."),
            ("cat welcome.txt", "방금 만든 파일의 내용을 다시 확인한다."),
        ],
        "practice": [
            "현재 사용자 이름, 운영체제 이름, 홈 디렉터리 경로를 각각 확인해 보고 세 값을 노트에 적어보자.",
            "~/linux_lab/day01 안에 intro.txt 파일을 만들고 자기소개 한 줄을 저장해 보자.",
            "루트 디렉터리와 홈 디렉터리의 차이를 직접 이동해 보며 설명해 보자.",
            "/, /home, ~ 세 위치를 ls -ld 로 비교하고 어떤 곳이 개인 작업 공간인지 말해 보자.",
        ],
        "answers": [
            "whoami, cat /etc/os-release, echo $HOME 순서로 확인할 수 있다.",
            "touch intro.txt 후 echo '안녕하세요 리눅스 수업을 시작합니다.' > intro.txt 를 입력하면 된다.",
            "cd / 는 시스템 최상위 위치로 이동하고 cd ~ 는 현재 사용자 홈으로 이동한다.",
            "ls -ld / /home ~ 를 보면 / 는 전체 시작점, /home 은 사용자 홈 모음, ~ 는 내 계정 전용 작업 공간임을 확인할 수 있다.",
        ],
    },
    {
        "no": "02",
        "slug": "terminal_navigation_and_paths",
        "title": "터미널 이동과 경로 이해",
        "goal": "절대경로와 상대경로를 구분하고 원하는 폴더로 정확히 이동한다.",
        "summary": "pwd, ls, cd를 반복해 쓰며 경로 감각을 익히고 탭 자동완성도 함께 연습한다.",
        "concepts": [
            "절대경로는 /로 시작하는 전체 주소다.",
            "상대경로는 현재 위치를 기준으로 계산하는 주소다.",
            ".. 는 상위 폴더, . 는 현재 폴더를 의미한다.",
            "WSL Ubuntu에서는 보통 /home/계정명 아래에서 개인 작업을 진행한다.",
        ],
        "commands": [
            ("pwd", "실습 시작 전 현재 위치를 먼저 확인한다. 경로 학습은 항상 현재 위치 인식부터 시작한다."),
            ("realpath .", "realpath 는 현재 위치의 실제 절대경로를 보여준다. . 은 현재 폴더를 의미한다."),
            ("echo $HOME", "현재 계정의 홈 디렉터리 절대경로를 다시 확인한다."),
            ("cd /home", "/home 은 일반 계정 폴더들이 모이는 위치다."),
            ("ls -l /home", "ls -l 로 /home 아래 계정 폴더 구조를 본다. -l 옵션은 상세 목록이다."),
            ("cd ~", "~ 로 다시 현재 계정 홈으로 돌아온다."),
            ("mkdir -p ~/linux_lab/day02/projects/app", "여러 단계 폴더를 한 번에 만들며 경로 구조를 연습한다. -p 옵션은 중복 생성에도 안전하다."),
            ("mkdir -p ~/linux_lab/day02/projects/data", "프로젝트 폴더와 데이터 폴더를 따로 만든다."),
            ("cd ~/linux_lab/day02", "홈 기준 절대경로 이동 예시다."),
            ("pwd", "현재 위치를 눈으로 확인해 경로 감각을 만든다."),
            ("ls", "현재 폴더의 기본 목록을 본다."),
            ("ls -l", "ls -l의 -l 옵션은 long format이며 권한, 소유자, 크기, 날짜를 자세히 보여준다."),
            ("ls -a", "ls -a의 -a 옵션은 숨김 파일까지 함께 보여준다."),
            ("cd projects", "현재 위치 기준 상대경로 이동 예시다."),
            ("cd app", "하위 폴더로 더 이동한다."),
            ("pwd", "현재 위치가 ~/linux_lab/day02/projects/app 인지 확인한다."),
            ("cd ..", "상위 폴더 한 단계로 이동한다. .. 는 parent directory를 뜻한다."),
            ("cd ../data", "상위 폴더로 이동한 뒤 다른 형제 폴더로 바로 들어가는 상대경로 예시다."),
            ("cd ~/linux_lab/day02/projects/app", "절대경로로 다시 특정 위치를 지정한다."),
            ("cd -", "cd - 는 직전에 있던 디렉터리로 되돌아간다. 작업 위치를 빠르게 오갈 때 유용하다."),
            ("ls -ld . .. ~ /", "현재 폴더, 상위 폴더, 홈, 루트의 차이를 한 화면에서 비교한다. -d 옵션은 폴더 자체를 보여준다."),
        ],
        "practice": [
            "day02 폴더 아래에 notes, images, backup 세 폴더를 만들고 각각 들어가 본다.",
            "절대경로로 app 폴더에 들어간 뒤 상대경로만 써서 data 폴더로 이동해 본다.",
            "cd -, .., ~ 를 각각 써 보며 어떤 이동이 일어나는지 설명해 보자.",
            "현재 위치가 /home/계정명/projects/app 일 때 ../data 와 ~/linux_lab/day02/projects/data 의 차이를 말로 설명해 보자.",
        ],
        "answers": [
            "mkdir -p ~/linux_lab/day02/notes ~/linux_lab/day02/images ~/linux_lab/day02/backup 처럼 만들 수 있다.",
            "cd ~/linux_lab/day02/projects/app 후 cd ../data 로 이동하면 된다.",
            "cd - 는 이전 폴더, cd .. 는 상위 폴더, cd ~ 는 홈 디렉터리다.",
            "../data 는 현재 위치 기준 상대경로이고 ~/linux_lab/day02/projects/data 는 홈 기준 절대경로다.",
        ],
    },
    {
        "no": "03",
        "slug": "files_and_directories_basics",
        "title": "파일과 디렉터리 기본 조작",
        "goal": "파일 생성, 폴더 생성, 복사 전 준비 작업을 익힌다.",
        "summary": "touch, mkdir, echo, tree 대체 명령을 활용해 폴더 구조를 직접 설계해 본다.",
        "concepts": [
            "리눅스에서는 파일과 폴더를 명령어 한 줄로 빠르게 만들 수 있다.",
            "실습 폴더 구조를 잘 만드는 습관이 나중에 배포에도 큰 도움이 된다.",
            "경로를 이해하지 못하면 파일이 어디에 생성됐는지 잃어버리기 쉽다.",
        ],
        "commands": [
            ("pwd", "실습 시작 위치를 먼저 확인한다. 어느 위치에서 만들었는지가 매우 중요하다."),
            ("cd ~", "현재 계정 홈으로 이동해 개인 작업 공간을 기준점으로 삼는다."),
            ("mkdir -p ~/linux_lab/day03/classroom/students", "수업용 디렉터리 구조를 만든다."),
            ("mkdir -p ~/linux_lab/day03/classroom/teachers", "교사용 폴더도 함께 만든다."),
            ("cd ~/linux_lab/day03/classroom", "실습 위치로 들어간다."),
            ("pwd", "현재 위치가 classroom 인지 다시 확인한다."),
            ("touch plan.txt", "수업 계획을 적을 빈 파일을 만든다."),
            ("touch students/student01.txt students/student02.txt", "한 번에 여러 파일을 만들 수 있다."),
            ("echo 'Linux practice list' > plan.txt", "> 는 파일 내용을 새로 쓴다."),
            ("echo 'student01' > students/student01.txt", "학생 정보 파일 예시를 만든다."),
            ("echo 'student02' > students/student02.txt", "두 번째 학생 파일 예시다."),
            ("ls -R", "ls -R의 -R 옵션은 recursive이며 하위 폴더까지 재귀적으로 목록을 보여준다."),
            ("find . -maxdepth 2", "find는 파일을 찾는다. -maxdepth 2는 두 단계까지만 내려가게 제한한다."),
            ("find . -maxdepth 2 -type d", "-type d 옵션은 디렉터리만 찾는다. 폴더 구조만 따로 읽고 싶을 때 쓴다."),
            ("find . -maxdepth 2 -type f", "-type f 옵션은 파일만 찾는다. 파일과 폴더를 구분해 이해하게 도와준다."),
            ("mkdir -p backup/2026/03", "연월 구조 폴더를 한 번에 만드는 예시다."),
            ("touch backup/2026/03/readme.txt", "깊은 경로에 파일을 생성한다."),
            ("realpath backup/2026/03/readme.txt", "상대경로로 만든 파일이 실제 어디에 있는지 절대경로로 확인한다."),
        ],
        "practice": [
            "강의실 폴더, 과제 폴더, 제출 폴더를 직접 원하는 구조로 만들어 보자.",
            "find 명령으로 현재 폴더 아래 파일만 찾고 폴더도 함께 찾는 결과를 비교해 보자.",
            "한 줄 명령으로 3명의 학생 파일을 만들어 내용을 각각 다르게 저장해 보자.",
            "realpath 로 students/student01.txt 의 절대경로를 확인하고 왜 이 위치에 생겼는지 설명해 보자.",
        ],
        "answers": [
            "mkdir -p classroom homework submit 처럼 기본 폴더를 만든 뒤 필요시 하위 폴더를 추가하면 된다.",
            "find . -maxdepth 2 와 find . -type f 의 결과 차이를 보면 파일만 찾는 옵션을 이해할 수 있다.",
            "touch students/student03.txt 후 echo 명령으로 내용을 넣거나 한 줄로 세 파일을 만들 수 있다.",
            "현재 위치가 ~/linux_lab/day03/classroom 이기 때문에 상대경로 students/student01.txt 는 그 하위 위치에 생성된다.",
        ],
    },
    {
        "no": "04",
        "slug": "copy_move_remove_and_search",
        "title": "복사 이동 삭제와 파일 찾기",
        "goal": "cp, mv, rm, find를 이해하고 안전하게 파일을 관리한다.",
        "summary": "복사와 이동, 이름 변경, 삭제, 검색 작업을 실습 폴더 안에서 반복적으로 수행한다.",
        "concepts": [
            "cp는 복사, mv는 이동 또는 이름 변경, rm은 삭제다.",
            "삭제는 되돌리기 어렵기 때문에 항상 대상 경로를 먼저 확인해야 한다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day04/source ~/linux_lab/day04/target", "원본과 결과 폴더를 분리해 안전하게 실습한다."),
            ("cd ~/linux_lab/day04", "실습 위치로 이동한다."),
            ("echo 'report v1' > source/report.txt", "원본 파일을 만든다."),
            ("cp source/report.txt target/report_copy.txt", "cp는 파일을 복사한다. 대상 이름을 바꿔 저장할 수도 있다."),
            ("cp -r source target/source_backup", "cp -r 의 -r 옵션은 디렉터리를 재귀적으로 복사한다."),
            ("mv target/report_copy.txt target/report_final.txt", "mv는 파일 위치를 바꾸거나 이름을 바꿀 수 있다."),
            ("mv source/report.txt source/report_old.txt", "같은 폴더 안에서 이름 변경 예시다."),
            ("find . -name '*.txt'", "-name 옵션은 파일 이름 패턴으로 검색한다. 작은따옴표로 패턴을 감싼다."),
            ("find . -type d", "-type d 는 디렉터리만 찾는다. -type f 는 파일만 찾는다."),
            ("rm target/report_final.txt", "rm은 파일을 삭제한다. 경로를 반드시 확인한 뒤 사용한다."),
            ("rm -r target/source_backup", "rm -r 의 -r 옵션은 디렉터리와 그 안 내용을 재귀적으로 삭제한다."),
            ("ls -R", "실습 후 남아 있는 파일 구조를 확인한다."),
        ],
        "practice": [
            "source 안에 notes.txt와 todo.txt를 만들고 target으로 각각 다른 이름으로 복사해 보자.",
            "find 명령으로 report가 포함된 파일만 찾아보자.",
            "삭제 전에 ls와 pwd를 먼저 실행하는 습관을 직접 실습해 보자.",
        ],
        "answers": [
            "cp source/notes.txt target/notes_copy.txt 와 cp source/todo.txt target/todo_copy.txt 를 사용할 수 있다.",
            "find . -name '*report*' 로 찾을 수 있다.",
            "pwd 로 현재 위치를 확인하고 ls 로 대상을 다시 본 뒤 rm 을 실행하는 흐름이 안전하다.",
        ],
    },
    {
        "no": "05",
        "slug": "viewing_and_editing_text",
        "title": "텍스트 읽기와 편집",
        "goal": "cat, less, head, tail, nano로 텍스트 파일을 읽고 수정한다.",
        "summary": "긴 로그 파일과 설정 파일을 읽는 기본 패턴을 익히고 nano 편집을 처음 경험한다.",
        "concepts": [
            "서버 운영에서 텍스트 파일을 읽는 능력은 매우 중요하다.",
            "설정 파일, 로그 파일, 코드 파일을 모두 텍스트로 다룬다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day05", "day05 실습 폴더를 만든다."),
            ("cd ~/linux_lab/day05", "실습 폴더로 이동한다."),
            ("printf 'line1\\nline2\\nline3\\nline4\\nline5\\nline6\\n' > log.txt", "printf는 줄바꿈이 포함된 여러 줄 문자열을 만들기 좋다."),
            ("cat log.txt", "cat은 짧은 파일을 한 번에 볼 때 좋다."),
            ("head log.txt", "head는 기본적으로 앞 10줄을 보여준다. 짧은 파일에서도 확인용으로 쓴다."),
            ("head -n 3 log.txt", "head -n 3 의 -n 옵션은 줄 수를 지정한다."),
            ("tail log.txt", "tail은 뒤 10줄을 보여준다."),
            ("tail -n 2 log.txt", "tail -n 2 는 마지막 두 줄만 확인한다."),
            ("less log.txt", "less는 긴 파일을 페이지 단위로 읽는다. q 키로 종료한다."),
            ("nano notes.txt", "nano는 초보자가 쓰기 쉬운 텍스트 편집기다. 수정 후 Ctrl+O 저장, Ctrl+X 종료를 사용한다."),
            ("cat notes.txt", "편집 내용을 다시 확인한다."),
            ("nl log.txt", "nl은 line number를 붙여 출력한다. 줄 번호로 설명할 때 유용하다."),
        ],
        "practice": [
            "10줄 이상의 practice.txt 파일을 만든 뒤 head와 tail로 앞뒤를 각각 확인해 보자.",
            "nano로 자기소개 파일을 만들고 두 줄 이상 입력해 보자.",
            "less에서 /line4 검색을 해 보고 q로 종료해 보자.",
        ],
        "answers": [
            "printf를 활용해 여러 줄을 쉽게 만들 수 있고 head -n, tail -n 으로 앞뒤를 잘라 볼 수 있다.",
            "nano intro.txt 로 열고 저장 후 cat intro.txt 로 확인하면 된다.",
            "less 안에서 /line4 입력 후 Enter 로 검색하고 q 로 종료한다.",
        ],
    },
    {
        "no": "06",
        "slug": "redirection_and_pipes",
        "title": "리다이렉션과 파이프",
        "goal": "출력 방향을 바꾸고 여러 명령어를 연결하는 법을 익힌다.",
        "summary": ">, >>, | 를 중심으로 텍스트를 가공하고 결과를 파일로 저장하는 패턴을 연습한다.",
        "concepts": [
            "리눅스의 강점은 작은 명령어를 파이프로 연결해 큰 작업을 만드는 데 있다.",
            "리다이렉션은 출력을 화면이 아니라 파일로 보내는 기술이다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day06", "실습 폴더를 만든다."),
            ("cd ~/linux_lab/day06", "실습 위치로 이동한다."),
            ("printf 'apple\\nbanana\\napple\\norange\\nbanana\\nbanana\\n' > fruits.txt", "중복 데이터가 있는 예시 파일을 만든다."),
            ("cat fruits.txt", "원본 데이터를 확인한다."),
            ("sort fruits.txt", "sort는 줄 단위 정렬을 한다. 기본은 오름차순이다."),
            ("sort fruits.txt > fruits_sorted.txt", "> 로 정렬 결과를 새 파일에 저장한다."),
            ("sort fruits.txt | uniq", "uniq는 연속 중복 줄을 하나로 줄인다. 보통 sort와 함께 쓴다."),
            ("sort fruits.txt | uniq -c", "uniq -c 의 -c 옵션은 중복 횟수를 함께 보여준다."),
            ("sort fruits.txt | uniq -c > count.txt", "파이프 결과도 파일에 저장할 수 있다."),
            ("echo 'grape' >> fruits.txt", ">> 는 append이며 기존 파일 끝에 내용을 추가한다."),
            ("cat fruits.txt | wc -l", "wc -l 의 -l 옵션은 줄 수를 센다."),
            ("grep 'banana' fruits.txt | wc -l", "grep 결과를 바로 다음 명령어에 넘겨 특정 단어 개수를 센다."),
        ],
        "practice": [
            "student 목록 파일을 만들어 정렬 후 count.txt 같은 결과 파일을 직접 만들어 보자.",
            "중복된 과일 파일에서 가장 많이 나온 단어를 눈으로 찾아보자.",
            "원본 파일을 덮어쓸 때와 이어 쓸 때의 차이를 > 와 >> 로 실험해 보자.",
        ],
        "answers": [
            "sort students.txt | uniq -c > students_count.txt 패턴을 그대로 응용하면 된다.",
            "sort 후 uniq -c 결과를 보면 banana가 가장 많다는 것을 확인할 수 있다.",
            "> 는 덮어쓰기, >> 는 이어쓰기다.",
        ],
    },
    {
        "no": "07",
        "slug": "permissions_and_ownership",
        "title": "권한과 소유자",
        "goal": "ls -l 결과를 읽고 chmod로 권한을 바꿀 수 있다.",
        "summary": "권한 표기, 읽기 쓰기 실행 권한, chmod 숫자 표기와 문자 표기를 함께 익힌다.",
        "concepts": [
            "리눅스에서는 파일마다 권한과 소유자가 존재한다.",
            "권한 문제를 이해해야 서버 실행 오류를 해결할 수 있다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day07", "실습 폴더를 만든다."),
            ("cd ~/linux_lab/day07", "실습 위치로 이동한다."),
            ("echo '#!/bin/bash\necho hello linux' > hello.sh", "실행 스크립트 예시 파일을 만든다."),
            ("ls -l hello.sh", "ls -l 은 권한과 소유자를 자세히 보여준다."),
            ("chmod u+x hello.sh", "chmod는 권한을 변경한다. u+x 는 user에게 execute 권한을 추가한다."),
            ("ls -l hello.sh", "변경된 권한을 다시 확인한다."),
            ("./hello.sh", "./ 는 현재 폴더를 의미한다. 실행 권한이 있는 스크립트를 직접 실행한다."),
            ("chmod 644 hello.sh", "숫자 권한 표기 예시다. 6은 rw, 4는 r, 4는 r 을 의미한다."),
            ("ls -l hello.sh", "숫자 권한 변경 결과를 확인한다."),
            ("chmod 755 hello.sh", "755는 소유자 rwx, 그룹 r-x, 기타 r-x 를 의미한다."),
            ("ls -l hello.sh", "실행 가능한 일반 스크립트 권한 형태를 확인한다."),
            ("id", "id는 현재 사용자의 uid, gid, 그룹 정보를 보여준다."),
        ],
        "practice": [
            "readme.txt 파일을 만들고 600, 644, 666 권한으로 각각 바꿔보자.",
            "hello.sh의 실행 권한을 뺀 뒤 다시 주는 과정을 반복해 보자.",
            "숫자 권한 700, 744, 755의 차이를 말로 설명해 보자.",
        ],
        "answers": [
            "chmod 600 readme.txt, chmod 644 readme.txt, chmod 666 readme.txt 순으로 실습할 수 있다.",
            "chmod u-x hello.sh 로 제거하고 chmod u+x hello.sh 로 다시 추가할 수 있다.",
            "700은 소유자만 모두 가능, 744는 소유자만 쓰기 가능, 755는 소유자 전체와 타인 읽기 실행 가능이다.",
        ],
    },
    {
        "no": "08",
        "slug": "users_groups_and_sudo",
        "title": "사용자 그룹 sudo 이해",
        "goal": "사용자와 그룹, sudo의 의미를 이해하고 안전하게 시스템 명령을 실행한다.",
        "summary": "whoami, id, groups, sudo를 중심으로 시스템 권한 구조를 이해한다.",
        "concepts": [
            "사용자와 그룹은 권한 관리의 기본 단위다.",
            "sudo는 관리자 권한이 필요한 명령을 일시적으로 실행하게 해준다.",
            "WSL Ubuntu에서도 계정 구조와 시스템 계정 파일은 일반 리눅스와 거의 같은 방식으로 보인다.",
        ],
        "commands": [
            ("whoami", "현재 로그인한 사용자 이름을 다시 확인한다."),
            ("id", "id는 uid, gid, 소속 그룹을 보여준다."),
            ("groups", "groups는 현재 사용자가 속한 그룹 목록을 간단히 보여준다."),
            ("echo $HOME", "현재 계정 홈 디렉터리를 확인해 계정과 홈의 연결을 다시 확인한다."),
            ("grep \"^$USER:\" /etc/passwd", "/etc/passwd 는 계정 정보 파일이다. 현재 계정 한 줄을 찾아 홈 경로와 기본 셸을 읽어 본다."),
            ("grep '^sudo' /etc/group", "/etc/group 은 그룹 정보 파일이다. sudo 그룹 줄을 직접 읽으며 그룹 구조를 이해한다."),
            ("sudo -l", "sudo -l 은 현재 사용자가 어떤 sudo 권한을 갖는지 조회한다."),
            ("sudo apt update", "apt update 는 패키지 목록을 갱신한다. sudo가 필요한 대표 명령이다."),
            ("sudo apt install -y tree", "apt install 은 패키지를 설치한다. -y 옵션은 yes를 자동 승인한다."),
            ("tree ~/linux_lab", "설치한 tree 명령으로 실습 폴더 구조를 보기 좋게 출력한다."),
            ("sudo adduser linuxstudent", "adduser는 새 사용자를 만든다. 실습 환경에서는 필요시만 사용한다."),
            ("sudo usermod -aG sudo linuxstudent", "usermod -aG 는 기존 그룹을 유지한 채 새 그룹을 추가한다. sudo 그룹에 넣는 예시다."),
            ("grep '^linuxstudent:' /etc/passwd", "실습용 새 계정이 만들어졌는지 passwd 파일에서 확인한다."),
            ("sudo deluser linuxstudent", "생성한 실습용 사용자를 삭제하는 예시다."),
        ],
        "practice": [
            "현재 사용자가 어떤 그룹에 속해 있는지 확인하고 그 의미를 설명해 보자.",
            "tree가 없다면 sudo apt install로 설치한 뒤 다시 실행해 보자.",
            "sudo가 왜 필요한지 apt update 예시를 기준으로 설명해 보자.",
            "/etc/passwd 에서 현재 계정 줄을 찾아 홈 디렉터리와 기본 셸이 어디인지 읽어 보자.",
        ],
        "answers": [
            "groups 또는 id로 확인할 수 있으며 그룹은 권한 묶음 단위다.",
            "sudo apt install -y tree 후 tree ~/linux_lab 를 실행하면 된다.",
            "시스템 전역 패키지 정보와 설정은 일반 사용자 권한으로 바꾸기 어려워서 sudo가 필요하다.",
            "grep \"^$USER:\" /etc/passwd 결과에서 보통 /home/계정명 과 /bin/bash 또는 /bin/sh 같은 셸 정보를 볼 수 있다.",
        ],
    },
    {
        "no": "09",
        "slug": "process_jobs_and_monitoring",
        "title": "프로세스 작업 제어 모니터링",
        "goal": "실행 중인 프로그램을 확인하고 종료하거나 백그라운드로 보낸다.",
        "summary": "ps, top, kill, jobs를 사용해 프로세스 관리 감각을 익힌다.",
        "concepts": [
            "프로세스는 실행 중인 프로그램이다.",
            "서버 운영에서는 실행 상태 확인과 종료가 매우 중요하다.",
        ],
        "commands": [
            ("ps", "ps는 현재 셸 기준 프로세스를 본다."),
            ("ps -ef | head", "ps -ef 는 전체 프로세스를 자세히 본다. -e는 all, -f는 full format이다."),
            ("top", "top은 실시간 프로세스 모니터링 도구다. q로 종료한다."),
            ("sleep 300 &", "& 는 명령을 백그라운드에서 실행한다. sleep은 대기 프로세스 예시로 좋다."),
            ("jobs", "jobs는 현재 셸에서 백그라운드로 돌고 있는 작업을 보여준다."),
            ("ps -ef | grep sleep", "grep으로 특정 프로세스를 찾아본다."),
            ("kill %1", "kill은 프로세스를 종료한다. %1 은 jobs 목록의 첫 번째 작업 번호다."),
            ("sleep 300 &", "다시 백그라운드 작업을 하나 띄운다."),
            ("jobs -l", "jobs -l 의 -l 옵션은 PID까지 함께 보여준다."),
            ("kill -9 $(jobs -p)", "kill -9 는 강제 종료 신호다. jobs -p 는 PID만 출력한다. 강제 종료는 마지막 수단으로 쓴다."),
            ("free -h", "free는 메모리 사용량을 보여준다. -h 옵션은 human readable 형식이다."),
            ("df -h", "df는 디스크 사용량을 파일시스템별로 본다. -h 옵션은 보기 쉬운 단위다."),
        ],
        "practice": [
            "sleep 120 백그라운드 작업을 2개 띄우고 jobs로 확인해 보자.",
            "ps -ef | grep sleep 으로 PID를 찾은 뒤 kill로 종료해 보자.",
            "top, free -h, df -h 세 명령의 역할 차이를 설명해 보자.",
        ],
        "answers": [
            "sleep 120 & 를 두 번 실행하면 된다.",
            "grep으로 PID를 확인한 뒤 kill PID 형식으로 종료하면 된다.",
            "top은 실시간 프로세스, free는 메모리, df는 디스크 사용량을 확인한다.",
        ],
    },
    {
        "no": "10",
        "slug": "package_management_and_environment",
        "title": "패키지 관리와 환경 정보",
        "goal": "apt로 프로그램을 설치하고 환경 관련 명령을 이해한다.",
        "summary": "업데이트, 설치, 제거, 환경변수, which, whereis를 통해 개발 환경을 준비한다.",
        "concepts": [
            "패키지 관리자는 리눅스에서 프로그램을 설치하는 표준 방법이다.",
            "어떤 명령이 어디에 설치됐는지 아는 습관이 중요하다.",
        ],
        "commands": [
            ("sudo apt update", "패키지 목록을 최신 상태로 갱신한다."),
            ("sudo apt upgrade -y", "upgrade는 설치된 패키지를 최신 버전으로 업데이트한다. -y는 자동 승인이다."),
            ("which python3", "which는 명령어 실행 파일 경로를 찾는다."),
            ("whereis python3", "whereis는 바이너리, 소스, 매뉴얼 위치를 함께 보여준다."),
            ("python3 --version", "--version 옵션은 설치된 버전을 확인할 때 자주 사용한다."),
            ("echo $PATH", "$PATH는 명령어를 찾는 경로 목록이다. 콜론으로 구분된다."),
            ("sudo apt install -y curl", "curl은 HTTP 요청 테스트에 자주 쓰이는 도구다."),
            ("curl --version", "설치가 잘 됐는지 버전으로 확인한다."),
            ("sudo apt remove -y tree", "remove는 패키지를 삭제한다. 설정 일부는 남을 수 있다."),
            ("sudo apt install -y tree", "수업용 도구를 다시 설치한다."),
            ("tree -L 2 ~/linux_lab", "-L 2 는 tree 깊이를 2단계로 제한한다."),
        ],
        "practice": [
            "which, whereis, --version 세 가지로 python3 정보를 각각 확인해 보자.",
            "curl과 tree를 설치하거나 재설치해 보고 버전을 확인해 보자.",
            "$PATH를 보고 왜 명령어를 폴더명 없이 실행할 수 있는지 설명해 보자.",
        ],
        "answers": [
            "which python3, whereis python3, python3 --version 을 순서대로 실행하면 된다.",
            "sudo apt install -y curl tree 후 curl --version, tree --version 또는 tree 실행으로 확인한다.",
            "PATH에 등록된 폴더를 셸이 탐색해 실행 파일을 찾기 때문이다.",
        ],
    },
    {
        "no": "11",
        "slug": "network_basics_and_downloads",
        "title": "네트워크 기초와 다운로드",
        "goal": "IP, 포트, localhost를 이해하고 curl과 wget을 사용한다.",
        "summary": "네트워크 기초 개념을 배우고 웹 요청 및 포트 확인 명령을 실습한다.",
        "concepts": [
            "localhost는 현재 내 컴퓨터 자신을 의미한다.",
            "포트는 하나의 컴퓨터 안에서 서비스를 구분하는 번호다.",
        ],
        "commands": [
            ("hostname -I", "-I 옵션은 네트워크 인터페이스의 IP 주소를 간단히 출력한다."),
            ("ping -c 4 8.8.8.8", "ping은 네트워크 연결을 확인한다. -c 4 는 4번만 보내고 종료한다."),
            ("ping -c 2 google.com", "도메인 이름이 IP로 해석되는지 함께 확인한다."),
            ("curl https://example.com", "curl은 URL에 요청을 보내고 응답을 받아온다."),
            ("curl -I https://example.com", "-I 옵션은 본문 없이 헤더만 가져온다."),
            ("wget -O sample.html https://example.com", "wget은 파일 다운로드에 특화돼 있다. -O 옵션은 저장 파일명을 지정한다."),
            ("head sample.html", "다운로드한 파일 앞부분을 확인한다."),
            ("ss -tulnp | head", "ss는 소켓 상태를 본다. -t TCP, -u UDP, -l listening, -n 숫자형, -p 프로세스 정보다."),
            ("python3 -m http.server 8000", "간단한 웹서버를 8000번 포트에서 실행한다. 브라우저 테스트용이다."),
            ("curl http://localhost:8000", "로컬 웹서버에 직접 접속해 응답을 확인한다."),
        ],
        "practice": [
            "python3 -m http.server 9000 을 띄운 뒤 curl http://localhost:9000 으로 확인해 보자.",
            "curl -I 와 curl 본문의 차이를 직접 비교해 보자.",
            "ss -tulnp 결과에서 LISTEN 상태의 의미를 설명해 보자.",
        ],
        "answers": [
            "다른 터미널에서 서버를 띄우거나 실행 후 curl로 확인하면 된다.",
            "-I 는 헤더만, 일반 curl 은 본문까지 가져온다.",
            "LISTEN은 외부 연결을 기다리는 서버 포트 상태다.",
        ],
    },
    {
        "no": "12",
        "slug": "archives_logs_and_disk_usage",
        "title": "압축 로그 디스크 사용량",
        "goal": "tar, zip, du, df, tail을 이용해 로그와 파일 묶음을 다룬다.",
        "summary": "백업과 로그 관리의 핵심 명령어를 배우고 운영 습관을 만든다.",
        "concepts": [
            "배포와 운영에서는 압축과 로그 확인이 자주 등장한다.",
            "디스크 사용량을 읽는 능력은 서버 관리의 기본이다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day12/project", "압축 대상 폴더를 만든다."),
            ("cd ~/linux_lab/day12/project", "프로젝트 폴더로 이동한다."),
            ("printf 'log1\\nlog2\\nlog3\\n' > app.log", "로그 파일 예시를 만든다."),
            ("printf 'config=true\\nport=5000\\n' > config.ini", "설정 파일 예시를 만든다."),
            ("cd ..", "상위 폴더에서 압축 실습을 진행한다."),
            ("tar -cvf project.tar project", "tar -cvf 는 create, verbose, file 옵션이다. 폴더를 tar 묶음으로 만든다."),
            ("tar -tvf project.tar", "-t 옵션은 압축 내부 목록을 본다."),
            ("mkdir -p extracted", "압축 해제 대상 폴더를 미리 만든다."),
            ("tar -xvf project.tar -C extracted", "-x 는 extract, -C 는 특정 폴더에 푸는 옵션이다."),
            ("du -sh project", "du는 디스크 사용량을 본다. -s 요약, -h 보기 쉬운 단위다."),
            ("df -h", "df는 파일시스템 전체 용량과 사용량을 본다."),
            ("tail -f project/app.log", "-f 옵션은 파일 끝을 계속 따라가며 본다. 실시간 로그 확인용이다."),
        ],
        "practice": [
            "practice 폴더를 만들고 tar로 묶었다가 다른 폴더에 풀어보자.",
            "du -sh 와 df -h 의 차이를 설명해 보자.",
            "tail -f 로 로그를 보는 이유를 말해 보자.",
        ],
        "answers": [
            "tar -cvf practice.tar practice 후 mkdir extracted && tar -xvf practice.tar -C extracted 로 실습할 수 있다.",
            "du는 특정 폴더 사용량, df는 파일시스템 전체 용량을 본다.",
            "실시간으로 새로운 로그 줄을 확인하며 서버 상태를 보기 위해 쓴다.",
        ],
    },
    {
        "no": "13",
        "slug": "bash_script_basics",
        "title": "배시 스크립트 기초",
        "goal": "셸 스크립트 구조와 변수, 입력, 조건문의 기본을 익힌다.",
        "summary": "처음으로 .sh 파일을 직접 만들고 실행하며 자동화 감각을 잡는다.",
        "concepts": [
            "반복 작업을 줄이기 위해 스크립트를 만든다.",
            "스크립트는 명령어를 순서대로 묶은 자동화 문서다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day13", "스크립트 실습 폴더를 만든다."),
            ("cd ~/linux_lab/day13", "실습 폴더로 이동한다."),
            ("nano hello_script.sh", "nano로 새 스크립트 파일을 만든다."),
            ("chmod +x hello_script.sh", "+x 는 실행 권한을 추가한다."),
            ("./hello_script.sh", "현재 폴더의 스크립트를 직접 실행한다."),
            ("nano input_script.sh", "입력을 받는 스크립트도 만든다."),
            ("chmod +x input_script.sh", "실행 권한을 부여한다."),
            ("./input_script.sh", "사용자 입력을 받아 결과를 출력해 본다."),
        ],
        "script_examples": [
            ("hello_script.sh", "#!/bin/bash\necho \"안녕하세요 리눅스 스크립트 수업입니다.\"\necho \"현재 사용자는 $(whoami) 입니다.\"\necho \"현재 위치는 $(pwd) 입니다.\""),
            ("input_script.sh", "#!/bin/bash\nread -p \"이름을 입력하세요: \" USER_NAME\nif [ -z \"$USER_NAME\" ]; then\n  echo \"이름이 비어 있습니다.\"\nelse\n  echo \"반갑습니다, $USER_NAME 님.\"\nfi"),
        ],
        "practice": [
            "오늘 날짜와 사용자 이름을 출력하는 스크립트를 직접 만들어 보자.",
            "read -p 를 사용해 좋아하는 과일을 입력받고 출력해 보자.",
            "입력이 비어 있으면 경고 문장을 출력하는 if 문을 다시 작성해 보자.",
        ],
        "answers": [
            "date 와 whoami 명령을 echo와 함께 조합하면 된다.",
            "read -p '좋아하는 과일: ' FRUIT 후 echo \"$FRUIT\" 를 사용하면 된다.",
            "if [ -z \"$VALUE\" ]; then ... fi 형태를 그대로 응용하면 된다.",
        ],
    },
    {
        "no": "14",
        "slug": "bash_script_practice",
        "title": "배시 스크립트 실전 자동화",
        "goal": "반복문과 파일 작업을 활용해 작은 자동화 도구를 만든다.",
        "summary": "백업 스크립트, 반복 출력, 조건 검사, 로그 남기기 예제를 통해 실전 감각을 익힌다.",
        "concepts": [
            "스크립트는 여러 리눅스 명령어를 묶어 자동화하는 도구다.",
            "운영자는 반복적인 작업을 스크립트로 줄여 시간을 절약한다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day14/source", "백업 대상 폴더를 만든다."),
            ("cd ~/linux_lab/day14", "실습 위치로 이동한다."),
            ("printf 'alpha\\nbeta\\n' > source/list.txt", "백업 대상 파일을 만든다."),
            ("nano backup_script.sh", "백업 스크립트를 만든다."),
            ("chmod +x backup_script.sh", "실행 권한을 부여한다."),
            ("./backup_script.sh", "백업 스크립트를 실행한다."),
            ("ls -R", "생성된 backup 폴더를 확인한다."),
            ("cat backup.log", "실행 기록 파일을 읽는다."),
        ],
        "script_examples": [
            ("backup_script.sh", "#!/bin/bash\nDATE=$(date +%Y%m%d_%H%M%S)\nBACKUP_DIR=\"backup_$DATE\"\nmkdir -p \"$BACKUP_DIR\"\ncp -r source \"$BACKUP_DIR\"\necho \"[$DATE] backup completed\" >> backup.log\necho \"백업이 완료되었습니다: $BACKUP_DIR\""),
        ],
        "practice": [
            "for 문을 사용해 student1, student2, student3 폴더를 자동 생성해 보자.",
            "백업 스크립트에 백업 후 tree 출력 줄을 추가해 보자.",
            "if 문을 사용해 source 폴더가 없으면 경고 후 종료하는 기능을 넣어 보자.",
        ],
        "answers": [
            "for i in 1 2 3; do mkdir -p student$i; done 형태를 사용할 수 있다.",
            "tree \"$BACKUP_DIR\" 또는 find \"$BACKUP_DIR\" 를 추가하면 된다.",
            "if [ ! -d source ]; then echo 'source 폴더 없음'; exit 1; fi 를 넣으면 된다.",
        ],
    },
    {
        "no": "15",
        "slug": "python_and_venv_on_wsl",
        "title": "WSL에서 파이썬과 가상환경",
        "goal": "python3, pip, venv를 이용해 개발 환경을 분리한다.",
        "summary": "WSL Ubuntu에서 파이썬 개발 준비를 하고 가상환경을 사용해 본다.",
        "concepts": [
            "가상환경은 프로젝트별 패키지 충돌을 막아 준다.",
            "배포 전 개발 환경을 분리하는 습관이 중요하다.",
        ],
        "commands": [
            ("python3 --version", "설치된 파이썬 버전을 확인한다."),
            ("pip3 --version", "pip는 파이썬 패키지 관리자다."),
            ("mkdir -p ~/linux_lab/day15/flask_project", "프로젝트 폴더를 만든다."),
            ("cd ~/linux_lab/day15/flask_project", "프로젝트 폴더로 이동한다."),
            ("python3 -m venv .venv", "-m venv 는 venv 모듈을 실행해 가상환경 폴더를 만든다."),
            ("source .venv/bin/activate", "source는 현재 셸에서 스크립트를 실행한다. activate로 가상환경을 활성화한다."),
            ("which python", "가상환경 활성화 후 python 경로가 .venv 안으로 바뀌는지 확인한다."),
            ("python --version", "가상환경 안에서도 버전을 확인한다."),
            ("pip install flask", "pip install은 파이썬 패키지를 설치한다."),
            ("pip freeze", "현재 설치된 패키지 목록을 requirements 형태로 출력한다."),
            ("pip freeze > requirements.txt", "패키지 목록을 파일로 저장한다."),
            ("deactivate", "가상환경을 종료하고 시스템 기본 셸 상태로 돌아간다."),
        ],
        "practice": [
            "새 가상환경을 만들고 requests 패키지를 설치한 뒤 pip freeze 결과를 확인해 보자.",
            "가상환경 활성화 전후 which python 결과가 왜 다른지 설명해 보자.",
            "requirements.txt를 만드는 이유를 말해 보자.",
        ],
        "answers": [
            "python3 -m venv .venv 후 source .venv/bin/activate, pip install requests 순서로 진행하면 된다.",
            "활성화 후에는 셸이 .venv/bin/python 을 우선 사용하기 때문이다.",
            "다른 환경에서도 동일한 패키지 버전을 다시 설치하기 위해서다.",
        ],
    },
    {
        "no": "16",
        "slug": "flask_run_and_port_check",
        "title": "Flask 실행과 포트 확인",
        "goal": "간단한 Flask 앱을 실행하고 localhost와 포트 개념을 확인한다.",
        "summary": "WSL Ubuntu에서 Flask 앱을 만들고 브라우저와 curl로 접속 확인까지 해 본다.",
        "concepts": [
            "웹 앱은 특정 포트에서 요청을 기다리는 프로세스다.",
            "localhost와 127.0.0.1은 현재 내 컴퓨터 자신을 가리킨다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day16/flask_app", "Flask 앱 폴더를 만든다."),
            ("cd ~/linux_lab/day16/flask_app", "앱 폴더로 이동한다."),
            ("python3 -m venv .venv", "가상환경을 만든다."),
            ("source .venv/bin/activate", "가상환경을 활성화한다."),
            ("pip install flask", "Flask 패키지를 설치한다."),
            ("nano app.py", "Flask 앱 파일을 작성한다."),
            ("python app.py", "파이썬으로 앱을 직접 실행한다."),
            ("curl http://127.0.0.1:5000", "curl로 로컬 서버 응답을 확인한다."),
            ("ss -tulnp | grep 5000", "5000번 포트에서 어떤 프로세스가 대기 중인지 확인한다."),
        ],
        "script_examples": [
            ("app.py", "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello from WSL Flask'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000, debug=True)"),
        ],
        "practice": [
            "/hello 경로를 추가해 다른 문장을 반환하도록 만들어 보자.",
            "port 값을 5001로 바꾸고 curl 주소도 맞춰 다시 접속해 보자.",
            "ss 명령에서 LISTEN 상태가 왜 보이는지 설명해 보자.",
        ],
        "answers": [
            "@app.route('/hello') 함수를 하나 더 만들면 된다.",
            "app.run(..., port=5001) 로 바꾸고 curl http://127.0.0.1:5001 로 테스트하면 된다.",
            "Flask 서버가 외부 요청을 기다리며 포트를 열고 있기 때문이다.",
        ],
    },
    {
        "no": "17",
        "slug": "gunicorn_and_background_service_mindset",
        "title": "Gunicorn과 백그라운드 실행",
        "goal": "개발 서버와 운영 서버의 차이를 알고 Gunicorn으로 앱을 실행한다.",
        "summary": "Flask 개발 서버와 Gunicorn의 차이, nohup, 백그라운드 실행, 로그 확인을 경험한다.",
        "concepts": [
            "개발 서버는 학습용, 운영 서버는 실제 서비스용에 가깝다.",
            "Gunicorn은 Python 웹 앱을 더 안정적으로 실행하는 WSGI 서버다.",
        ],
        "commands": [
            ("cd ~/linux_lab/day16/flask_app", "앞에서 만든 Flask 앱 폴더로 이동한다."),
            ("source .venv/bin/activate", "가상환경을 활성화한다."),
            ("pip install gunicorn", "운영형 실행 예시를 위해 gunicorn을 설치한다."),
            ("gunicorn --bind 0.0.0.0:8000 app:app", "--bind 는 주소와 포트를 지정한다. app:app 은 app.py 안의 Flask 객체 app을 뜻한다."),
            ("curl http://127.0.0.1:8000", "Gunicorn 서버 응답을 확인한다."),
            ("nohup gunicorn --bind 0.0.0.0:8000 app:app > gunicorn.log 2>&1 &", "nohup은 터미널 종료 후에도 프로세스를 유지한다. > 와 2>&1 은 표준출력과 에러를 로그 파일에 모은다. & 는 백그라운드 실행이다."),
            ("jobs", "현재 셸의 백그라운드 작업을 확인한다."),
            ("ps -ef | grep gunicorn", "실제 실행 중인 gunicorn 프로세스를 찾는다."),
            ("tail -n 20 gunicorn.log", "로그 파일 마지막 20줄을 확인한다."),
            ("pkill -f gunicorn", "pkill -f 는 명령행 패턴으로 프로세스를 종료한다."),
        ],
        "practice": [
            "Flask 개발 서버와 Gunicorn의 차이를 말로 정리해 보자.",
            "nohup으로 실행 후 로그 파일이 생기는지 확인해 보자.",
            "8000 대신 9000 포트로 Gunicorn을 띄우고 curl로 테스트해 보자.",
        ],
        "answers": [
            "Flask 개발 서버는 개발용, Gunicorn은 더 운영 환경에 가까운 WSGI 서버다.",
            "nohup 명령 뒤에 > gunicorn.log 2>&1 & 를 붙이면 된다.",
            "gunicorn --bind 0.0.0.0:9000 app:app 후 curl http://127.0.0.1:9000 로 확인한다.",
        ],
    },
    {
        "no": "18",
        "slug": "docker_intro_and_basic_commands",
        "title": "도커 입문과 기본 명령어",
        "goal": "Docker가 무엇인지 이해하고 이미지와 컨테이너를 직접 실행한다.",
        "summary": "리눅스 위에서 Docker가 어떤 역할을 하는지 배우고 hello-world와 nginx 컨테이너를 실습한다.",
        "concepts": [
            "이미지는 실행 준비가 끝난 프로그램 묶음이고 컨테이너는 실제 실행 중인 인스턴스다.",
            "Docker는 환경 차이를 줄여 배포를 쉽게 만드는 도구다.",
        ],
        "commands": [
            ("docker --version", "도커가 설치됐는지 버전을 확인한다."),
            ("docker pull hello-world", "pull은 이미지를 다운로드한다."),
            ("docker images", "images는 로컬에 저장된 이미지 목록을 보여준다."),
            ("docker run hello-world", "run은 이미지를 기반으로 컨테이너를 생성하고 실행한다."),
            ("docker pull nginx", "웹서버 예시 이미지인 nginx를 내려받는다."),
            ("docker run -d -p 8080:80 --name mynginx nginx", "-d 는 detached 백그라운드 실행, -p 8080:80 은 호스트 포트와 컨테이너 포트를 연결, --name 은 이름 지정이다."),
            ("docker ps", "현재 실행 중인 컨테이너 목록을 본다."),
            ("curl http://127.0.0.1:8080", "nginx 컨테이너가 잘 응답하는지 확인한다."),
            ("docker logs mynginx", "logs는 컨테이너 로그를 출력한다."),
            ("docker stop mynginx", "stop은 실행 중인 컨테이너를 정상 종료한다."),
            ("docker rm mynginx", "rm은 종료된 컨테이너를 삭제한다."),
        ],
        "practice": [
            "hello-world와 nginx 이미지의 차이를 설명해 보자.",
            "8081:80 포트 매핑으로 nginx를 다시 실행해 보자.",
            "docker ps 와 docker images 의 차이를 설명해 보자.",
        ],
        "answers": [
            "hello-world는 테스트용, nginx는 실제 웹서버 예시 이미지다.",
            "docker run -d -p 8081:80 --name mynginx2 nginx 로 실습할 수 있다.",
            "ps는 실행 중인 컨테이너, images는 저장된 이미지 목록을 보여준다.",
        ],
    },
    {
        "no": "19",
        "slug": "dockerfile_and_compose_for_flask",
        "title": "Dockerfile과 Compose로 Flask 묶기",
        "goal": "Flask 앱을 Docker 이미지로 만들고 compose로 실행한다.",
        "summary": "직접 만든 앱을 컨테이너화하면서 Docker의 진짜 가치를 체감한다.",
        "concepts": [
            "Dockerfile은 이미지를 만드는 조리법이다.",
            "compose는 여러 설정을 파일로 적어 실행을 단순하게 만든다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day19/flask_docker", "Docker 예제 폴더를 만든다."),
            ("cd ~/linux_lab/day19/flask_docker", "예제 폴더로 이동한다."),
            ("nano app.py", "Flask 앱 파일을 작성한다."),
            ("nano requirements.txt", "필요 패키지 목록 파일을 작성한다."),
            ("nano Dockerfile", "이미지 빌드용 Dockerfile을 작성한다."),
            ("docker build -t flask-demo:1.0 .", "build는 Dockerfile을 읽어 이미지를 만든다. -t 는 태그 이름 지정이다."),
            ("docker images", "방금 만든 이미지가 목록에 생겼는지 확인한다."),
            ("docker run -d -p 5050:5000 --name flask-demo-app flask-demo:1.0", "호스트 5050 포트를 컨테이너 5000 포트와 연결해 실행한다."),
            ("curl http://127.0.0.1:5050", "컨테이너로 실행된 Flask 앱 응답을 확인한다."),
            ("docker stop flask-demo-app", "실행 중인 컨테이너를 종료한다."),
            ("docker rm flask-demo-app", "컨테이너를 제거한다."),
        ],
        "script_examples": [
            ("app.py", "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Dockerized Flask on Linux'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000)"),
            ("requirements.txt", "flask==3.1.0\ngunicorn==23.0.0"),
            ("Dockerfile", "FROM python:3.11-slim\n\nWORKDIR /app\n\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\nCOPY app.py .\n\nEXPOSE 5000\n\nCMD [\"gunicorn\", \"--bind\", \"0.0.0.0:5000\", \"app:app\"]"),
        ],
        "practice": [
            "/health 경로를 추가하고 다시 이미지를 빌드해 보자.",
            "컨테이너 이름과 포트를 바꿔 두 번째 실행을 해 보자.",
            "Dockerfile의 EXPOSE와 docker run -p 의 차이를 설명해 보자.",
        ],
        "answers": [
            "app.py 수정 후 docker build -t flask-demo:1.1 . 로 새 이미지를 만들면 된다.",
            "docker run -d -p 5051:5000 --name flask-demo-app2 flask-demo:1.1 형태로 실행할 수 있다.",
            "EXPOSE는 문서적 선언이고 실제 포트 연결은 -p 옵션이 수행한다.",
        ],
    },
    {
        "no": "20",
        "slug": "final_deployment_project",
        "title": "최종 배포 프로젝트",
        "goal": "WSL Ubuntu에서 Flask 앱을 Docker Compose로 실행하고 배포 흐름을 정리한다.",
        "summary": "리눅스 명령어, 네트워크, Python, Flask, Docker를 하나로 묶어 실제 배포형 예제를 완성한다.",
        "concepts": [
            "배포는 앱을 다른 사람도 접속 가능한 상태로 만드는 과정이다.",
            "개발과 운영 사이의 핵심 차이는 실행 방식, 로그, 포트, 재현 가능성이다.",
        ],
        "commands": [
            ("mkdir -p ~/linux_lab/day20/final_project", "최종 프로젝트 폴더를 만든다."),
            ("cd ~/linux_lab/day20/final_project", "최종 프로젝트 폴더로 이동한다."),
            ("cp -r ~/linux_lab/day19/flask_docker/* .", "이전 차시 예제를 복사해 출발점을 만든다."),
            ("nano docker-compose.yml", "compose 설정 파일을 작성한다."),
            ("docker compose up -d", "compose up은 정의된 서비스를 실행한다. -d 는 백그라운드 실행이다."),
            ("docker compose ps", "compose ps는 서비스 컨테이너 상태를 확인한다."),
            ("curl http://127.0.0.1:5050", "최종 배포 앱 응답을 다시 확인한다."),
            ("docker compose logs", "전체 서비스 로그를 본다."),
            ("docker compose down", "compose down은 관련 컨테이너와 네트워크를 정리한다."),
        ],
        "script_examples": [
            ("docker-compose.yml", "services:\n  web:\n    build: .\n    container_name: linux_final_web\n    ports:\n      - \"5050:5000\""),
        ],
        "practice": [
            "서비스 이름을 webapp으로 바꾸고 compose up이 어떻게 반영되는지 확인해 보자.",
            "docker compose logs 로 앱 로그를 읽고 어떤 서버가 실행 중인지 말해 보자.",
            "최종적으로 리눅스와 Docker가 왜 배포에 연결되는지 설명해 보자.",
        ],
        "answers": [
            "docker-compose.yml 의 service 키 이름을 webapp으로 바꾸고 다시 up 하면 된다.",
            "Gunicorn 또는 Flask 앱 로그가 보이며 포트 바인딩 정보도 확인할 수 있다.",
            "리눅스는 실행 환경, Docker는 동일한 환경을 재현해 배포를 쉽게 만드는 도구이기 때문이다.",
        ],
    },
]


def lesson_prefix(lesson):
    return f"lesson{lesson['no']}_{lesson['slug']}"


def render_instructor(lesson):
    lines = [
        "#!/bin/bash",
        "# WSL Ubuntu 기준 강사용 실습 파일",
        "# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.",
        "# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.",
        "# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.",
        "",
        f"# 수업 제목: {lesson['title']}",
        f"# 수업 목표: {lesson['goal']}",
        f"# 수업 개요: {lesson['summary']}",
        "",
        "# 핵심 개념",
    ]
    for concept in lesson["concepts"]:
        lines.append(f"# - {concept}")
    lines.extend(["", "# 핵심 실습 명령어", ""])

    for command, comment in lesson["commands"]:
        lines.append(f"# {comment}")
        lines.append(command)
        lines.append("")

    if lesson.get("script_examples"):
        lines.extend(["# 보충 코드 예시", ""])
        for filename, content in lesson["script_examples"]:
            lines.append(f"# 파일 예시: {filename}")
            for row in content.strip().splitlines():
                lines.append(f"# {row}")
            lines.append("")

    lines.extend(["# 개인 실습 문제", ""])
    for idx, item in enumerate(lesson["practice"], start=1):
        lines.append(f"# 문제 {idx}. {item}")
    lines.extend(["", "# 정답 예시", ""])
    for idx, item in enumerate(lesson["answers"], start=1):
        lines.append(f"# 정답 {idx}. {item}")

    return "\n".join(lines).strip() + "\n"


def render_student(lesson):
    command_block = "\n".join(command for command, _ in lesson["commands"])
    option_notes = []
    for command, comment in lesson["commands"]:
        if "옵션" in comment or "의미" in comment:
            option_notes.append(f"- `{command}` : {comment}")
    md = [
        '<div align="center">',
        "",
        f"# {lesson['title']}",
        "",
        "**WSL Ubuntu 리눅스 실습 자료**",
        "",
        "</div>",
        "",
        "---",
        "",
        f"> **오늘의 목표**  \n> {lesson['goal']}",
        "",
        f"> **오늘 배우는 내용**  \n> {lesson['summary']}",
        "",
        "## 핵심 개념",
        "",
    ]
    for concept in lesson["concepts"]:
        md.append(f"- {concept}")
    md.extend([
        "",
        "## 복붙 실습 코드",
        "",
        "> **실습 환경 안내**  ",
        "> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.",
        "",
        "```bash",
        command_block,
        "```",
        "",
    ])

    if option_notes:
        md.extend(["## 옵션 포인트", ""])
        md.extend(option_notes)
        md.append("")

    for filename, content in lesson.get("script_examples", []):
        md.extend([f"### 실습 파일 예시: `{filename}`", "", "```bash", content.strip(), "```", ""])

    md.extend(["## 개인 실습 문제", ""])
    for idx, item in enumerate(lesson["practice"], start=1):
        md.append(f"{idx}. {item}")
    md.extend(["", "## 정답 예시", ""])
    for idx, item in enumerate(lesson["answers"], start=1):
        md.append(f"{idx}. {item}")
    md.extend([
        "",
        "---",
        "",
        "<table>",
        "  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>",
        "  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>",
        "</table>",
    ])
    return "\n".join(md).strip() + "\n"


def render_overview():
    intro_lessons = LESSONS[:4]
    system_lessons = LESSONS[4:10]
    network_lessons = LESSONS[10:14]
    app_lessons = LESSONS[14:17]
    docker_lessons = LESSONS[17:20]

    def card(title, bg, border, color, lessons):
        items = []
        for lesson in lessons:
            items.append(
                f'<li style="margin:8px 0;"><code>{lesson["no"]}</code> {lesson["title"]}: {lesson["goal"]}</li>'
            )
        items_html = "\n".join(items)
        return textwrap.dedent(
            f"""\
            <div style="background-color:{bg}; border:1px solid {border}; border-radius:16px; padding:16px 18px; margin:14px 0;">
              <h3 style="margin:0 0 10px 0; color:{color};">{title}</h3>
              <ul style="margin:0; padding-left:20px; line-height:1.8;">
                {items_html}
              </ul>
            </div>
            """
        ).strip()

    sections = [
        "# linux_wsl Overview",
        "",
        '<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">',
        '  <h2 style="margin:0 0 10px 0;">학습 로드맵</h2>',
        '  <p style="margin:0; line-height:1.8;">',
        "    이 폴더는 WSL Ubuntu를 기준으로 리눅스를 거의 처음 배우는 학습자를 위한 20차시 수업 자료입니다.",
        "    리눅스와 터미널의 기초부터 파일, 경로, 계정, 권한, 프로세스, 네트워크, 배시 스크립트, Flask 실행,",
        "    Gunicorn, Docker, Docker Compose 기반 배포 예시까지 단계적으로 이어집니다.",
        "  </p>",
        "</div>",
        "",
        "## 파일 구성",
        "",
        card("기초 구조와 경로", "#eff6ff", "#93c5fd", "#1d4ed8", intro_lessons),
        "",
        card("파일, 권한, 시스템 기초", "#f0fdf4", "#86efac", "#15803d", system_lessons),
        "",
        card("네트워크와 스크립트", "#fefce8", "#fde047", "#a16207", network_lessons),
        "",
        card("개발 환경과 Flask 실행", "#ecfeff", "#67e8f9", "#0f766e", app_lessons),
        "",
        card("Docker와 최종 배포", "#faf5ff", "#d8b4fe", "#7e22ce", docker_lessons),
        "",
        "## 학습 순서 추천",
        "",
        '<div style="background-color:#f8fafc; border-left:8px solid #334155; padding:16px 18px; border-radius:12px; margin:12px 0;">',
        '  <ol style="margin:0; padding-left:20px; line-height:1.9;">',
        '    <li><code>01</code> ~ <code>04</code>로 리눅스와 경로 구조 감각 익히기</li>',
        '    <li><code>05</code> ~ <code>10</code>으로 파일, 권한, 프로세스, 패키지 관리 다루기</li>',
        '    <li><code>11</code> ~ <code>14</code>로 네트워크와 배시 스크립트 자동화 익히기</li>',
        '    <li><code>15</code> ~ <code>17</code>로 Python, Flask, Gunicorn 흐름 연결하기</li>',
        '    <li><code>18</code> ~ <code>20</code>으로 Docker와 최종 배포 예제 완성하기</li>',
        "  </ol>",
        "</div>",
        "",
        "## 사용 목적",
        "",
        '<div style="background-color:#fffbeb; border:1px solid #fcd34d; border-radius:14px; padding:16px; margin:12px 0;">',
        '  <ul style="margin:0; padding-left:20px; line-height:1.8;">',
        '    <li>WSL Ubuntu 기반 리눅스 입문 수업 자료</li>',
        '    <li>서버 기초와 터미널 실습 중심 강의 자료</li>',
        '    <li>Flask와 Docker를 활용한 배포 입문 자료</li>',
        "  </ul>",
        "</div>",
        "",
        "## 권장 환경",
        "",
        '<div style="background-color:#eef2ff; border:1px solid #a5b4fc; border-radius:14px; padding:16px; margin:12px 0;">',
        '  <ul style="margin:0; padding-left:20px; line-height:1.8;">',
        '    <li>Windows + WSL Ubuntu</li>',
        '    <li>터미널: Windows Terminal 또는 VS Code Terminal</li>',
        '    <li>추가 도구: Python 3, Flask, Gunicorn, Docker</li>',
        "  </ul>",
        "</div>",
    ]
    return "\n".join(sections).strip() + "\n"


def render_example_files():
    return {
        "app.py": textwrap.dedent(
            """\
            from flask import Flask

            app = Flask(__name__)


            @app.route("/")
            def home():
                return "Linux WSL Docker deployment example"


            @app.route("/health")
            def health():
                return {"status": "ok"}


            if __name__ == "__main__":
                app.run(host="0.0.0.0", port=5000)
            """
        ),
        "requirements.txt": "flask==3.1.0\ngunicorn==23.0.0\n",
        "Dockerfile": textwrap.dedent(
            """\
            FROM python:3.11-slim

            WORKDIR /app

            COPY requirements.txt .
            RUN pip install --no-cache-dir -r requirements.txt

            COPY app.py .

            EXPOSE 5000

            CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
            """
        ),
        "docker-compose.yml": textwrap.dedent(
            """\
            services:
              web:
                build: .
                container_name: linux_wsl_web
                ports:
                  - "5050:5000"
            """
        ),
        "README.md": textwrap.dedent(
            """\
            # Final Flask Docker App

            ```bash
            docker compose up -d
            docker compose ps
            curl http://127.0.0.1:5050
            docker compose logs
            docker compose down
            ```
            """
        ),
    }


def write_all():
    INSTRUCTOR_DIR.mkdir(parents=True, exist_ok=True)
    STUDENT_DIR.mkdir(parents=True, exist_ok=True)
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    for lesson in LESSONS:
        prefix = lesson_prefix(lesson)
        (INSTRUCTOR_DIR / f"{prefix}.sh").write_text(render_instructor(lesson), encoding="utf-8")
        (STUDENT_DIR / f"{prefix}.md").write_text(render_student(lesson), encoding="utf-8")
    (ROOT / "Overview.md").write_text(render_overview(), encoding="utf-8")
    for name, content in render_example_files().items():
        (EXAMPLES_DIR / name).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    write_all()

