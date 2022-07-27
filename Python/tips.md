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
