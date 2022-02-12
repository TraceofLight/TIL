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

- ABAP Editor (ABAP 프로그램 개발툴)

**SE41**

- Menu painter

**SE51**

- Screen painter

**SE80**

- Build, Edit 관련 ABAP 종합툴

**SE84**

- RIS (Repository Information System)로 모든 repository에 담긴 object에 대하여 다양한 조건으로 검색할 수 있는 프로그램

---

## 정리해야 할 내용

request number, code syntax <br />
T.code 연결하기, 이관하기 TO QA system

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

## menu 의 종류

- SAP menu 와 User menu 2가지로 구성

---

## ABAP program processing 절차

- 정리 필요

---

## Database 내 Client의 종류

- 정리 필요

---

## active와 inactive

- 정리 필요

---

## Complete/Incomplete Data type

complete는 size가 자동으로 지정되며,
incomplete의 경우는 length와 decimals 등을 통해 길이의 지정이 필요하다

- complete : D (날짜), T (시간), I (정수)
- incomplete : C (문자), N (숫자), P (소수)
