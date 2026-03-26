# 11_날개달기_1.py
# 수업 설명: 이 파일에서는 클래스와 모듈의 기본 개념을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 실습 예제 1: 클래스 정의
class Person:  # Person 클래스를 정의합니다.
    def __init__(self, name):  # __init__ 생성자 메서드를 정의합니다. 객체 생성 시 호출됩니다.
        self.name = name  # self.name 속성을 설정합니다.

    def greet(self):  # greet 인스턴스 메서드를 정의합니다.
        print(f"Hello, {self.name}!")  # 이름을 포함한 인사말을 출력합니다.

p = Person("Alice")  # Person 클래스의 인스턴스를 생성합니다.
p.greet()  # greet 메서드를 호출합니다.

# 실습 예제 2: 클래스에 더 많은 속성과 메서드
class Car:  # Car 클래스를 정의합니다.
    def __init__(self, brand, model, year):  # 생성자: 브랜드, 모델, 연식을 매개변수로 받습니다.
        self.brand = brand  # 브랜드 속성 설정
        self.model = model  # 모델 속성 설정
        self.year = year  # 연식 속성 설정
        self.mileage = 0  # 주행거리 초기화

    def drive(self, distance):  # drive 메서드: 주행 거리를 증가시킵니다.
        self.mileage += distance  # mileage에 distance를 더합니다.
        print(f"{self.brand} {self.model} drove {distance} km. Total: {self.mileage} km")  # 주행 정보 출력

    def get_info(self):  # get_info 메서드: 차량 정보를 반환합니다.
        return f"{self.year} {self.brand} {self.model}, Mileage: {self.mileage} km"  # 정보 문자열 반환

my_car = Car("Toyota", "Corolla", 2020)  # Car 인스턴스 생성
my_car.drive(50)  # 50km 주행
print(my_car.get_info())  # 차량 정보 출력

# 실습 예제 3: 상속
class Student(Person):  # Person 클래스를 상속받는 Student 클래스 정의
    def __init__(self, name, student_id):  # 생성자: 이름과 학번을 받습니다.
        super().__init__(name)  # 부모 클래스의 생성자를 호출합니다.
        self.student_id = student_id  # 학번 속성 설정

    def study(self):  # study 메서드 정의
        print(f"{self.name} (ID: {self.student_id}) is studying.")  # 공부 중 메시지 출력

s = Student("Bob", "12345")  # Student 인스턴스 생성
s.greet()  # 상속된 greet 메서드 호출
s.study()  # 자신의 study 메서드 호출

# 실습 예제 4: 메서드 오버라이딩
class Teacher(Person):  # Person을 상속받는 Teacher 클래스
    def __init__(self, name, subject):  # 생성자: 이름과 과목을 받습니다.
        super().__init__(name)  # 부모 생성자 호출
        self.subject = subject  # 과목 속성 설정

    def greet(self):  # greet 메서드를 오버라이딩합니다.
        print(f"Hello, I am {self.name}, teaching {self.subject}.")  # 교사용 인사말 출력

t = Teacher("Dr. Smith", "Math")  # Teacher 인스턴스 생성
t.greet()  # 오버라이딩된 greet 호출

# 실습 예제 5: 클래스 변수
class Dog:  # Dog 클래스 정의
    species = "Canis familiaris"  # 클래스 변수: 모든 인스턴스가 공유합니다.

    def __init__(self, name, breed):  # 생성자: 이름과 품종을 받습니다.
        self.name = name  # 인스턴스 변수
        self.breed = breed  # 인스턴스 변수

    def bark(self):  # bark 메서드
        print(f"{self.name} says woof!")  # 짖는 소리 출력

dog1 = Dog("Buddy", "Golden Retriever")  # Dog 인스턴스 생성
dog2 = Dog("Max", "Bulldog")  # 또 다른 인스턴스
print(dog1.species)  # 클래스 변수 출력: Canis familiaris
print(dog2.species)  # 클래스 변수 출력: Canis familiaris
Dog.species = "Domestic Dog"  # 클래스 변수 변경
print(dog1.species)  # 변경된 값 출력: Domestic Dog

# 실습 예제 6: 모듈 만들기 (주석으로 설명)
# 별도 파일 my_module.py에:
# def hello():
#     print("Hi from module!")
# 작성 후 import

# 실습 예제 7: 모듈 임포트
# import my_module  # my_module 모듈을 임포트합니다.
# my_module.hello()  # 모듈의 hello 함수 호출

# 실습 예제 8: from import
# from my_module import hello  # my_module에서 hello 함수만 임포트
# hello()  # hello 함수 직접 호출

# 실습 예제 9: if __name__ == "__main__"
# 모듈 파일에:
# def main():
#     print("This is main function")
# if __name__ == "__main__":  # 스크립트가 직접 실행될 때만 main 호출
#     main()

# 실습 예제 10: 클래스나 변수 등을 포함한 모듈
# 모듈에 클래스 정의 후 import하여 사용

# 미션: 자동차 클래스를 만들고, 주행 거리를 증가시키는 메서드를 추가하세요. (힌트: 클래스 변수와 메서드)
# 정답:
# class Vehicle:  # Vehicle 클래스 정의
#     def __init__(self, make, model):  # 생성자
#         self.make = make  # 제조사
#         self.model = model  # 모델
#         self.distance = 0  # 주행 거리 초기화
#     
#     def drive(self, km):  # 주행 메서드
#         self.distance += km  # 거리 증가
#         print(f"주행 거리: {self.distance} km")  # 출력
#     
#     def get_distance(self):  # 거리 반환 메서드
#         return self.distance
# 
# car = Vehicle("Honda", "Civic")  # 인스턴스 생성
# car.drive(100)  # 100km 주행