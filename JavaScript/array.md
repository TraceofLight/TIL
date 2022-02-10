### length

숫자로 길이를 반환

### toString

string의 표현을 반환

### join

배열에 존재하는 모든 item을 연결하여 하나의 string으로 만들며, toString과 다르게 콤마가 아닌 다른 seperator 사용이 가능하다

### toLocaleString

string의 표현을 반환, 사용언어를 반영한다

### pop

끝에서부터부터 item 삭제

### push

끝에 item 추가

### unshift

처음에 item 추가

### shift

처음에 아이템 제거

## shift 계열이 pop, push 보다 느리다!

### concat

array 2개를 결합한다.
기존에 array 2개에는 변화가 발생하지 않는다

### reverse

item들 배치의 앞과 뒤를 전환한다

### slice

array를 시작점과 종료점을 기준으로 잘라낸다

### sort

array를 유니코드 코드 포인트에 따라서 정렬
a-b 는 a부터 작은 순서대로 정렬

#### (유니코드 코드 포인트)

https://miaow-miaow.tistory.com/37
관련링크

### splice

지정, 제거요소수, 새로운 요소의 형태의 구문을 가졌으며 배열의 기존요소를 삭제 혹은 교체할 수 있다

### indexOf

해당 item 의 array 내의 최초 위치를 알려준다

### lastIndexOf

해당 item 의 array 내의 마지막 위치를 알려준다

### every

array 내의 item이 판별함수를 "모두" 만족하는지 테스트

### some

array 내의 item이 판별함수를 "어떤 하나라도" 만족하는지 테스트

### forEach

array 내의 item을 각각 나열

### map

각 item에 주어진 함수를 호출한 결과로 새로운 array를 반환

### filter

주어진 함수의 테스트를 통과한 요소들을 모아 새로운 배열로 반환

### reduce

배열의 각 요소에 대하여 reducer 함수를 실행하고 결과값 하나를 반환, 일종의 결과값 누적이 가능하다

### reduceRight

누적기에 대하여 reducer 함수를 실행하고 단일값으로 item을 반환
