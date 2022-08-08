# Python 팁

---

## 해당 md는 Python을 공부하면서 새로 알게 되거나 정리가 부족했던 부분을 따로 모아둔 것

### - 함수 설정 시 기본 인자가 있는 항목이 기본 인자가 없는 항목 뒤에 나타날 수 없음

```python
def greeting(name='peter', age):
    return f'{name}은 {age}살이다.
```

해당 코드 실행 시 SynntaxError가 발생한다.

### - 키워드 인자를 활용할 경우, 키워드 인자 활용 이후 위치 인자의 활용은 불가능하다.

```python
def greeting(age, name):
    return f'{name}은 {age}살이다.'

greeting(age=24, '민수')
```

반대로 위치 인자를 활용하다가 키워드 인자를 활용하는 것은 상관 없고 이 경우도 마찬가지로 키워드 인자 사용 이후의 위치 인자 사용은 불가능하다.

### - Void Function 에 관하여

함수에서 따로 반환값을 만들지 않을 경우를 말하며 반환값은 None이 기본값이다. 

(print와 다름에 주의)

### - 가변 인자 리스트 (*args)

arguments는 전부 하나의 tuple 자료형으로 사용됨

## - 가변 키워드 인자 (**kwargs)

argument 가 dictionary로 처리됨

```python
def keyword_arguments(**kwargs):
    return kwargs

print(keyword_arguments(인사='안녕', 이름='민수', 강아지= '멍멍'))
```

## - Function vs Method

메서드는 클래스 "내부에 작성된 함수"

## - dict.items()

딕셔너리를 튜플로 구성된 리스트로 변환해주는 함수

## - namespace

## - 얕은 복사란?

깊은 복사 : 실제 값을 새로운 메모리 공간에 복사하는 것

얕은 복사 : 주소 값을 복사하는 것 (참조하는 실제값은 동일)

따라서 얕은 복사로 복사된 array의 경우, 하나를 변경하면 다른 것들도 전부 변경된다.

## - 복소수 실수부 허수부 쪼개는 법

real.x : 복소수 x 의 실수부를 리턴한다.

imag.x : 복소수 x 의 허수부를 리턴한다.

## - iterable 의 종류

list, tuple, set, dictionary, string

## - all() ,any()

all : iterable 내 하나라도 True 가 아니라면 False 출력

any : iterable 내 하나라도 True 라면 True 출력

## - slice 에 관하여

[start : end : step]

start 지점부터 end까지 (end는 미포함) step만큼의 간격을 두고 (기본값 1)

필요에 따라 스타트나 end를 생략할 수 있고 처음이나 끝부터 시작 

## - x.isnumeric()

숫자형 + 숫자값 표현에 해당하는 문자열까지 숫자인지 체크해서 숫자인 경우 True 

isdigit의 경우 단일 글자가 숫자 형태일 경우 True

isdecimal은 해당 문자열이 int로 변환이 가능한지 check 해서 가능하면 True

## - 함수의 메인 역할

기능을 분해하고 재사용할 수 있도록 하는 것

Decompostion > Abstraction

## - OOP (object oriented program)

객체지향 프로그램

모든 파이썬의 행동, 변수 등은 전부 객체(object)

객체는 특정 타입의 인스턴스

객체이면서 어떤 것의 인스턴스라고 할 수 있음

```python
class Human() :    
    hello = 'hello' # 클래스 변수
    def __init__(self,name) :
        Human.name = name # 셀프 인스턴스, 인스턴스 변수

print(Human.hello) # 'hello'
a1 = Human('사람이름') # 사람이름
```

클래스(설계도) > 인스턴스(객체) 형성

메서드는 인스턴스, 클래스, 정적 메서드 총 3종류 존재

- 인스턴스 메서드 : 인스턴스 변수 값 설정 메서드이며 자기 자신을 첫 인자로 전달, 내부 정의되는 메서드 중 기본 (self)
  
  - 생성자 메서드 : 인스턴스 객체 생성 시 자동 호출
    
    > 생성자 함수라는 것은 파이썬에 존재하지 않음. 인스턴스를 만들어 주는 것은 new, 초기화를 해주는 것이 init, new와 init이 협력하여 객체를 생성하는 것 (파이썬의 생성자에 대한 논란이 있는 이유)
  
  - 매직 메서드 : 특수 동작을 위해 만들어진 메서드, 특정 상황에 자동으로 불림
  
  - 소멸자 메서드 : 인스턴스 객체 소멸 직전에 호출되는 메서드

- 클래스 메서드 : @classmethod  데코레이터를 사용하여 정의, 첫 인자로 클래스 전달

## - 데코레이터

함수를 다른 함수로 꾸며서 새로운 기능을 부여

@데코레이터(함수명) 형태로 함수 위에 작성

순서대로 적용, 작성 순서가 중요함

## - 클래스 메서드와 인스턴스 메서드

인스턴스 메서드는 클래스 변수와 인스턴스 변수 둘 다 사용이 가능

클래스는 인스턴스 변수의 사용이 불가능함

## - 스태틱 메서드

인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드

속성을 다루지 않고 기능만을 하는 메서드를 정의할 때 사용

@staticmethod 데코레이터를 사용하여 정의

일반함수처럼 동작하지만 클래스 이름 공간에 귀속됨

해당 클래스로 한정하는 용도로 사용

## - 상속

class ChildClass(ParentClass) 의 형태로 사용

하위 클래스는 상위 클래스에 지정된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음

다중 상속도 가능

super() : 자식 클래스에서 부모 클래스를 사용하고 싶은 경우

mro() : 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드

## - enumerate()

인덱스와 리스트를 같이 반환하는 파이썬의 내장함수

```python
for idx, element in enumerate(['가', '나', '다']) :
    print(idx, element)
(0, '가')
(1, '나')
(2, '다')
```

## - lambda 함수

익명 함수, 함수명을 지정하지 않고 사용할 때 사용하며 sort 조건에도 많이 활용된다.

## - 매개변수탐색

조건을 만족하는 최대 최소값을 구하는 방법
이진탐색 등으로 큰 범위의 탐색을 진행한 이후 매개변수값을 조여서 다시 탐색 진행

