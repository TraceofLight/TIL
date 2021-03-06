### Console API 관련 내용 링크

https://developer.mozilla.org/ko/docs/Web/API

### string object 관련 링크

https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/Useful_string_methods

문자열 내용 ' ' 안에 표기

### JS 공식 사이트

https://ecma-international.org

보통은 모질라 사이트를 활용

https://developer.mozilla.org

### async defer

- async : 병렬로 js와 html의 데이터를 다운로드
- defer : 병렬로 다운로드한 이후 실행은 html 로드 이후에 발생

#### defer 을 사용하지 않을 경우

body 요소 가장 밑부분에 자바스크릡트를 위치
HTML 요소들의 스크립트 로딩지연으로 인한 렌더링 문제가 없어 페이지 로딩 시간이 단축되며, DOM이 완성된 상태가 아닐 때 자바스크립트가 DOM을 조작할 경우 에러가 발생하기 때문

### Console log 출력이 안될 때

https://ooz.co.kr/438

콘솔창에 있는 필터 영역의 문제
필터링 레벨을 낮춰보도록 하자

### ${} 변환 해결하는 방법 (JSP의 경우)

https://copycoding.tistory.com/245

> 해당 방식으로 해결하지 못하여 이후 하단 해결책 확인

### upperstrophy와 grave accent의 차이

둘은 비슷하게 생겼는데 JS 작성 시 upperstrophy를 사용하면 string 인식이 안된다!!! 따라서 Quotation mark를 사용할 때는 주의가 필요함

### break 와 continue 정리

break는 조건 만족하는 시점에 바로 loop out
continue는 조건을 만족하지 못하면 거기서 바로 끊고 loop의 다음을 반복

### 이름 설정

변수는 명사로, 함수는 동사나 커맨드 형태로

### arguments 객체

args
https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/arguments

### JS에서 function은 object

함수 뒤에 .을 붙이면 속성값을 확인할 수 있음

### Local, Global Scope

밖에서는 안이 보이지 않고 안에서만 밖을 볼 수 있다

### 세미콜론의 필요성

JS 에서 굳이 필요하진 않다
ASI 라는 인터프리터의 세미콜론 자동 삽입을 거치기 때문이다
세미콜론을 붙이면 안되는 위치도 존재함

https://bakyeono.net/post/2018-01-19-javascript-use-semicolon-or-not.html

### key = value

key 값에 value 값의 이름이 동일한 오브젝트를 받아오게 될 경우 둘 다 쓰지 않고 1개를 생략해도 인식한다.

- ex)

  function makePerson(name, age) {
  return {
  name,
  age
  }
  }

### cloning

기본적으로 .. = .. 의 방식을 사용하면
reference 값만 다르고 내부에 있는 object는 동일함

빈 object를 먼저 생성한 이후 키 자체 value를 하나하나 복사하는 방법

### type

type 이 있는 자료구조에서는 동일한 type 끼리만 data를 담을 수 있음 그러나 JS는 동적으로 타입이 정의가 가능하기 때문에 일단 다른 type 도 같은 class에 담는 것이 가능하다

### @param

매개변수에 대한 설명을 표시할 때 사용되는 태그
작성위치는 메소드, 중복작성 가능, 출력 형식은 매개변수명 및 설명을 작성한다.

HTML 로 출력되기 때문에 줄바꿈 \<br /> 에 대한 내용이 요구된다.
