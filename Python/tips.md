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



### - 함수에서 따로 반환값을 만들지 않을 경우 Void Function으로 반환값은 None이 기본값이다. (print와 다름에 주의)



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


