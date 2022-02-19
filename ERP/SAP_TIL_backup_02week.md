Report zca12_00007

PARAMETERS p_age TYPE i.

IF p_age >= '50'.
WRITE: 'Old'.
ELSEIF p_age >= '10'.
WRITE: 'Adult'.
ELSE.
WRITE: 'Young'.
ENDIF.

Report zca12_00008

DATA count TYPE i.
PARAMETERS p_age TYPE i.
PARAMETERS p_count TYPE i.
DATA age TYPE i.

age = p_age.
count = p_count.

\*IF age > '10' AND age < '20'.

- DO count TIMES.
- WRITE: 'hello'.
- NEW-LINE.
- ENDDO.
  \*ENDIF.

WRITE:/ sy-mandt, " 로그인한 클라이언트.
sy-uname, " 로그인한 유저 id.
sy-langu, " 로그인한 언어.
sy-datum, " 현재 날짜.
sy-uzeit. " 현재 시간.

Report zca12_00009

PARAMETERS p_001 TYPE i.
PARAMETERS p_002 TYPE i.
PARAMETERS p_opt TYPE c.
DATA a TYPE i.

- 더하기
  IF p_opt = '+'.
  a = p_001 + p_002.
  ELSEIF p_opt = '-'.
  a = p_001 - p_002.
  ELSEIF p_opt = '_'.
  a = p_001 _ p_002.
  ELSEIF p_opt = '/'.
  a = p_001 / p_002.
  ELSE.
  MESSAGE e003(zmessage).

ENDIF.

WRITE: 'The answer is', a.

PARAMETERS p_num1 TYPE i.
PARAMETERS p_num2 TYPE i.
PARAMETERS p_num3 TYPE i.
PARAMETERS p_num4 TYPE i.

DATA gv_sum1 TYPE i.
DATA gv_sum2 TYPE i.

- 비즈니스 로직 구현

- gv_sum1 = p_num1 + p_num2.
- gv_sum2 = p_num3 + p_num4.

PERFORM add USING p_num1 p_num2 changing gv_sum1.
PERFORM add USING p_num3 p_num4 changing gv_sum2.

- 결과 출력
  PERFORM write_star.
- WRITE:/ 'Sum: ', gv_sum1.
- WRITE:/ 'Sum: ', gv_sum2.
  PERFORM write_sum USING gv_sum1.
  PERFORM write_sum USING gv_sum2.
  PERFORM write_star.

- 파라미터가 필요없는 모듈에 대한 정의
  FORM write_star.
  WRITE:/ '******\*\*\*\*******'.
  ENDFORM.

FORM add USING value(p_1) TYPE i
value(p_2) TYPE i
changing p_sum TYPE i.

p_sum = p_1 + p_2.
ENDFORM.

FORM write_sum USING a TYPE i.

WRITE:/ 'Sum: ', a.
ENDFORM.

Report zca12_00010

PARAMETERS p_base TYPE bc400_compute_base.
PARAMETERS p_power TYPE bc400_compute_power.
DATA gv_result TYPE bc400_compute_result.

CALL FUNCTION 'bc400_compute_base'
EXPORTING
iv_base = p_base
iv_power = p_power
IMPORTING
ev_result = gv_result
EXCEPTIONS
power_value_too_high
result_value_too_high
OTHERS.

IF sy-subrc = 0.

WRITE:/ 'Result : ', gv_result.
ELSE.
CASE sy-subrc.
WHEN 1.
WRITE:/ 'Power value is too high'.
WHEN 2.
WRITE:/ 'Resule value is too high'.
WHEN OTHERS.
WRITE :/ 'Unknown Error'.
ENDCASE.
ENDIF.

PARAMETERS I_NUM1 TYPE i.
PARAMETERS I_NUM2 TYPE i.
PARAMETERS I_OPERATOR TYPE c.
DATA a TYPE i.

form

CASE I_OPERATOR.
when +.
write:/ I_NUM1 + I_NUM2.
when -.
write:/ I_NUM1 - I_NUM2.
when _.
write:/ I_NUM1 _ I_NUM2.
when /.
write:/ I_NUM1 / I_NUM2.

- 더하기
  IF p_opt = '+'.
  a = p_001 + p_002.
  ELSEIF p_opt = '-'.
  a = p_001 - p_002.
  ELSEIF p_opt = '_'.
  a = p_001 _ p_002.
  ELSEIF p_opt = '/'.
  a = p_001 / p_002.
  ELSE.
  MESSAGE e003(zmessage).

ENDIF.
