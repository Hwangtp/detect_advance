# 11_Classes.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">클래스</h2>
  <p style="margin: 0; line-height: 1.7;">객체지향 프로그래밍의 기본인 클래스와 객체를 설명하는 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      큰 프로그램을 구조적으로 만드는 데 필요한 사고방식을 배울 수 있습니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> 클래스 정의</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> 객체 생성</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 속성</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 메서드</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">5.</strong> 객체지향 기초</li>
  </ul>
</div>

## 추천 학습 방법

<div style="background-color:#ecfeff; border-left:8px solid #06b6d4; padding:16px 18px; border-radius:12px; margin:12px 0;">
  <ol style="margin:0; padding-left:20px; line-height:1.9;">
    <li><code>.py</code> 파일을 직접 실행해 예제 결과를 확인합니다.</li>
    <li>주석과 출력 결과를 함께 보며 코드 흐름을 따라갑니다.</li>
    <li>예제 값을 조금씩 바꿔 보며 어떤 점이 달라지는지 관찰합니다.</li>
    <li>마지막에는 비슷한 문제를 스스로 다시 작성해 봅니다.</li>
  </ol>
</div>

## 같이 보면 좋은 파일

<div style="background-color:#f5f3ff; border:1px solid #c4b5fd; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li><code>Overview.md</code></li>
    <li>이전 번호 파일과 다음 번호 파일</li>
    <li>같은 주제가 이어지는 후속 실습 파일</li>
  </ul>
</div>

## 코드

```python
class Person:

    def __init__(self, name):

        self.name = name

    def greet(self):

        print(f"Hello, {self.name}!")

p = Person("Alice")

p.greet()

class Car:

    def __init__(self, brand, model, year):

        self.brand = brand

        self.model = model

        self.year = year

        self.mileage = 0

    def drive(self, distance):

        self.mileage += distance

        print(f"{self.brand} {self.model} drove {distance} km. Total: {self.mileage} km")

    def get_info(self):

        return f"{self.year} {self.brand} {self.model}, Mileage: {self.mileage} km"

my_car = Car("Toyota", "Corolla", 2020)

my_car.drive(50)

print(my_car.get_info())

class Student(Person):

    def __init__(self, name, student_id):

        super().__init__(name)

        self.student_id = student_id

    def study(self):

        print(f"{self.name} (ID: {self.student_id}) is studying.")

s = Student("Bob", "12345")

s.greet()

s.study()

class Teacher(Person):

    def __init__(self, name, subject):

        super().__init__(name)

        self.subject = subject

    def greet(self):

        print(f"Hello, I am {self.name}, teaching {self.subject}.")

t = Teacher("Dr. Smith", "Math")

t.greet()

class Dog:

    species = "Canis familiaris"

    def __init__(self, name, breed):

        self.name = name

        self.breed = breed

    def bark(self):

        print(f"{self.name} says woof!")

dog1 = Dog("Buddy", "Golden Retriever")

dog2 = Dog("Max", "Bulldog")

print(dog1.species)

print(dog2.species)

Dog.species = "Domestic Dog"

print(dog1.species)
```
