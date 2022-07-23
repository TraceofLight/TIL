### 줄 가운데에 정렬하는 방법

Line-height를 사이즈와 같게 정리할 것

### 투명도

기본적으로 opacity를 활용할 수 있으나 투명도를 0으로 만들어도 결과적으로 클릭 등의 상호작용은 일어나기 때문에 display: none; 을 활용하여 상호작용을 배제하는 것이 유용할 때가 있다.

##### 0에 가까울수록 안 보이며 1은 그대로 출력

### @media 활용하는 법

##### https://developer.mozilla.org/ko/docs/Web/CSS/@media

screen and (max-width: 000px) {} 와 같은 방식으로 사용하는데 화면 너비에 따른 새 규칙이 적용됨

### nth-child()

##### https://developer.mozilla.org/ko/docs/Web/CSS/:nth-child

지정한 구문 내에서의 인덱스 순서를 따라간다
따라서 지정한 클래스 다수 내부에서 각각의 룰을 따르며 외부의 영향을 받지 않는다.

### flex-grow

#####https://developer.mozilla.org/ko/docs/Web/CSS/flex-grow
요소 내에서 할당 가능한 갯수를 나타낸다. 즉 1을 입력할 시에 해당 라인에서 1개 항목을 제외하면 다른 것들은 밀려나게 됨

### transform

#####https://developer.mozilla.org/ko/docs/Web/CSS/transform

Rotate 회전 Translate 좌표이동

### transition

##### https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions

간단한 애니메이션 사용 300ms 가 자연스럽게 체감하는 효과로 좋음
{transition: 항목 시간 효과;} 순으로 보통 활용

### flexbox의 justify-content/align-items 정리

가로축이 중심축 세로축이 교차축
justify-content는 중심축 선에서 배열 정리
align-items는 교차축 선에서 배열 정리

ex) default 상태 row 중심축 기준
가로로 나열된 물건을 간격 정리 : justify-content
난잡하게 위아래로 뒤틀린 물건을 축을 들고 쭉 밀어내듯 정리 : align-items
