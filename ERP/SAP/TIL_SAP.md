## ABAP은 대소문자 구분이 없다

일괄적으로 문자 크기의 강제적용이 필요할 경우
_TRANSLATE LV_TEMP to UPPER/LOWER CASE._ 를 사용한다

---

## ABAP 내 주석처리

Ctrl + <, > 을 통해 주석처리를 넣고 뺄 수 있다

---

## command field T.code 모음

**/n**

- 초기화면으로 이동

**/n xxxx**

- 초기화면으로 이동 후 해당 T.code에 맞는 프로그램 실행

**/o**

- 새창 열기

**/o xxxx**

- 새창을 열고 해당 T.code에 맞는 프로그램을 실행

**/i**

- delete current window

**/NEND, /NEX**

- 로그인 세션을 나가는 커맨드로 NEND는 확인창이 팝업되는 커맨드, NED는 팝업 없이 종료된다.

**SM04**

- 접속 중인 사용자 전체 조회

**SE11, SE12**

- ABAP Dictionary 로 11에서는 테이블 생성, 인덱스 생성, Database 관리 작업이 가능하나, 12에서는 오로지 조회만 가능하다.

**SE16**

- DATA Browser, 해당 툴을 활용하여 테이블값 확인

**SE24**

- Class builder

**SE37**

- Function builder

**SE38**

- ABAP Editor (ABAP 프로그램 개발 Tool)

**SE41**

- Menu painter

**SE51**

- Screen painter

**SE80**

- Build, Edit 관련 ABAP 종합툴

**SE84**

- RIS (Repository Information System)로 모든 repository에 담긴 object에 대하여 다양한 조건으로 검색할 수 있는 프로그램

**SE93**

- Create Transaction 으로 해당 프로그램을 통하여 User T.code를 만들어낼 수 있다. <br />
  (SE80에서 Create - Transaction 을 통해서도 접근이 가능하다)

**SEARCH_USER_MENU** <br />
**SEARCH_SAP_MENU**

- USER와 SAP에서 만들어놓은 프로그램을 조회하고 T.code를 확인할 수 있도록 해놓은 프로그램

---

## Syntax 구문

**PARAMETERS**

- 사용자의 입력값을 받을 수 있도록 하는 선언문

**DATA**

- 데이터를 입력해 둘 수 있는 변수 선언문

**MOVE**

- 데이터를 이동시키는 명령어

**ADD**

- 더하기 명령어

**WRITE**

- 출력 명령어

**NEW-LINE**

- 한 줄 간격을 주는 명령어

### _**관련 링크 http://sapjoy.co.kr/abappds/56293**_

---

## ABAP 프로그램명의 조건

1. 반드시 Y 혹은 Z로 시작
2. 반드시 unique 해야함 (중복불가)

---

## 프로그램의 종류

1. Executable Program (1) <br />

- 레포트 용도의 프로그램 구현 시 사용

2. Module Program (M)

---

## Test 용도의 프로그램 사용법

Local Object 로 저장 <br />
= $TMP (임시) package에 저장

- 운영 시스템에 사용되지 않는다

---

## 프로그램 제작 절차

1. 로직의 구현
2. 문법 체크 (Ctrl + F2)
3. Save (Ctrl + S)
4. Activate (Ctrl + F3) <br />

- 해당 과정에서 체크, 저장, 활성화 동시에 가능

5. Test (F8)

---

## SAP의 지원대상

Window, Java, HTML을 통한 GUI를 지원한다

---

## Reuse Unit의 종류

1. Subroutine
2. Function Module
3. Class

---

## Request number에 대하여

Transport Request Number를 말하며, 일종의 고유번호로 해당 번호를 통해 프로그램을 전달하는 것이 가능하다.

---

## Release 에 관하여

Change Request 가 Release가 가능하려면 하위 Task 들이 전부 release 되어야 한다. (전부 active)

---

## 테이블에 관하여

### **_TSTC_**

- T.code 담긴 테이블로 테이블 조회

_~~SCUSTOM - SCARR~~_

~~항공사 관련 베이스 테이블로 중요 테이블은 아닌 듯~~

---

## 프로그램 T.code 병기하는 법

(Interface personalization) <br />
extra - setting - Display technical name

---

## F1 과 F4 도움말

F1 도움말은 기술 정보에 대해서 조회가 가능하며 F4의 경우는 필드에 입력할 수 있는 전항목에 대해 조회할 수 있다.

---

## Dispatcher 의 역할

- W/P (work processor) 의 Load Balancing을 담당한다.

---

## Development Objects의 Trasport

Development System (개발장비 DEV...) -> Change Request (품질장비 QAS...)-> Production System (운영장비 PRD...) <br />

- 따라서 나머지 package와 달리 local package($TMP)는 change request와 관련성이 없다. <br />
- Request number 과 Task number 구분

---

## Repository 구성

Package를 기준에 따라 분류하여 묶어두며 package 내에 program과 table definition, function module이 포함된 형태이다. (SE84를 통해 조회가능)

---

## menu 의 종류

- SAP menu 와 User menu 2가지로 구성

---

## ABAP program processing 절차

![](/Photo/SAP_SystemOverview.jpg)

---

## Database 내 Client의 종류

1. Cross-client (범용적) <br />

- 프로그램들이 해당

2. Client-specific (특정 클라이언트) <br />

- 사용자 정보, Data가 해당

---

## active와 inactive

- inactive 프로그램은 단순 저장된 프로그램으로 active는 시스템의 사용될 수 있도록 전환된 것이다. 또한 Active 하지 않으면 Release가 불가능하다.

---

## Complete/Incomplete Data type

complete는 size가 자동으로 지정되며,
incomplete의 경우는 length와 decimals 등을 통해 길이의 지정이 필요하다

- complete : D (날짜), T (시간), I (정수)
- incomplete : C (문자), N (숫자), P (소수)

## 2주차 정리

incomplete type data
type p decimals
length는 전체 길이 length\*2 -1 , decimal은 소수자릿수만큼

data type 2 종류

local data type 특정 프로그램에서만 확인할 수 있는 데이터타입
global data type abap dictionary 에 정의된 데이터 타입

ABAP Dictionary

Data element
Structure  
Table type

like : 선언된 변수랑 동일한 변수를 만든다는 명령어

naming rule
DATA gv_xxxxx 글로벌 변수 시
DATA iv_xxxxx 로컬 변수 시

(-) 음수 기호가 출력 시에 뒤에 출력되지만 입력 시에는 앞에 정상입력하여야 한다.

상수 : 한번 값이 할당된다면 해당 변수의 값을 바꿀 수 없는 특별한 변수.

text symbol : 다국어를 처리할 때 사용하는 오브젝트

text-<xxx> 3자리 ID

clear NAME 변수의 초기상태로 만드는 명령어

strlen( gv_string ) 변수 길이 출력

system fields

sy-subrc : 바로 앞 문장에 종속적인 값을 가지는 system field임.

SQL (Standard Query Language)
사용 목적 : 회사의 모든 데이터를 가지고 있는 Database는 오직 해당 데이터만 알아들음.

\*우리 회사에 이름이 홍길동인 직원의 나이는 몇 살인가요? (Database에 질문)
SELECT age FROM employee WHERE name = '홍길동'

CALL function

IF.
"함수 호출을 잘 했다."
ELSE
"함수 호출하다가 에러가 발생했다."

ENDIF.
SCARR: 테이블( = 데이터를 담고 있는 곳) : 항공사 테이블

SE11 > SCARR

질문 : 우리 회사에서 관리하는 항공사 모두 몇 개 있나요? 18개

Database에게 물어봄

> SELECT COUNT( \* ) FROM SCARR. => 18
> SELECT CURRCODE FROM SCARR WHERE CARRID = 'SR' => CHF

Dialog Message
사용 목적 : Status Bar에 메세지를 출력하기 위해서
종류 : 6가지
S : Success
E : Error
I : Information (팝업으로 나타남)

ABAP Debugger

F5 ~ F8까지 사용

F5 : 모듈 안으로 이동
F6 : 다음 명령어로 이동
F7 : 해당 모듈 밖으로 나가기 ( = 모듈 호출한 다음 라인으로 이동 )
F8 : 프로그램 끝까지 실행

디버깅 : 프로그램을 구동하면서, 프로그램의 상태를 파악하는 툴이자 행위

1. 상단 Stop 버튼 클릭
2. command field에 /h 입력해서
3. Break_point 기입 in source

Module

- 정의 : 재사용이 가능한 프로그램 로직 블럭

1. Local Module
   해당 프로그램에서만 사용 가능

   > Subroutine, Local Class

2. Global Module
   모든 프로그램이 재사용 가능
   > Function Module, Global Class

프로그램이 모듈을 호출하기 위해서는 파라미터를 통해
데이터를 주고 받아야 한다.

sum값 호출 부분도 서브루틴으로 변경 후 호출
서브루틴 이름: write_sum으로 정의

using value(f1) type i > call by value
using f1 type i > call by ref
changing f1 type i > call by ref

펑션그룹 : ZMATH##
함수이름 : ZCALCULATE##
사칙연산을 수행하는 함수 생성
입력파라미터 3개
I_NUM1 : INT1
I_NUM2 : INT1
I_OPERATOR : CHAR01

출력 파라미터 1개
E_RESULT : INT4

RFC 함수 (Remote Function Call)
