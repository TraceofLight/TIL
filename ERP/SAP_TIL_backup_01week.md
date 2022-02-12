```
REPORT zca12_00001.

WRITE 'Hello ABAP'.
NEW-LINE.

NEW-LINE.

WRITE 'KHJ'.

---

REPORT ZCA12_00002.

Write '2022-02-12'.
New-LINE.
Write '토요일'.

---

REPORT zca12_00005.

* 사용자로부터 년도를 입력받고 싶다.
PARAMETERS p_age TYPE i.
PARAMETERS p_later TYPE i.

DATA my_age TYPE i. "my final age"
my_age = p_age + p_later.

*WRITE : p_later.
*WRITE 'years later,'.
*WRITE 'My age is'.
*WRITE my_age.

WRITE : p_later, 'years later,', 'My age is', my_age, '.'.

---

REPORT zca12_00006.

DATA my_name TYPE c LENGTH 10.
DATA today TYPE d.
DATA score TYPE n LENGTH 3.
DATA my_score TYPE p LENGTH 3 DECIMALS 2.
my_name = 'ABCDEFGHIJKL'.
today = '20220212'. "8자리 값
score = '99'. " 100 미만도 첫 자리 0 출력
my_score = '13.87'. "전체 길이 length *2 -1, decimals 은 소수자릿수
WRITE: my_name, today, score, my_score.

---

REPORT zbc400_12_hello.
PARAMETERS pa_name length 25.

WRITE: 'Hello world!'.
NEW-LINE.
WRITE: 'Hello, ', pa_name.
```
