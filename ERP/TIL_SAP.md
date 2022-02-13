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
