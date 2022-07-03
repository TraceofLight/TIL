## 문제 개념정리

\
String이 포함할 수 있는 element :

- String process statements, Literals

SAP enhancements for customer exits는 어떤 Transaction에 의해 관리? :

- Transaction SMOD

Text mode에 있는 파일을 열 때 Unicode system을 반드시 특정해야 하는 것 :

- The ENCODING addition

Session break point 추가하는 법 :

- /h 커맨드 실행
- ABAP Editor에서 breakpoint 설정

Selections screen 위 \<Field> 를 위한 Help request에 관하여 옳은 것?  
"해당 이벤트는 event block에서 프로그래밍된 input field 에 대한 self defined help를 보여주고 필드를 위한 가능한 ABAP 사전의 도움을 덮어쓸 수 있다" :

- 덮어쓸 수는 없다.
- input field를 위한 도움을 selection screen 내에서 줄 수 있다.

프로그램이 종료를 권할 때 어떻게 찾아낼 것인가 :

- App Area 내부 SAP 레퍼런스 이미지에서 Customer Exit를 찾음
- Repository Information System을 사용
- Application Hierarchy(계급) 사용
- Character string CUSTOMER-FUNCTION을 찾는다

메인스크린 안으로 서브스크린을 넣는 법 :

- 메인 스크린의 Flow Logic 에서 Call Subscreen을 사용한다

input/output 필드에서 foreign key check가 작동하는 때? :

- 필드가 check table을 정의한 사전 필드를 나타낼 때

classical screen에서 FIELD_NAME 필드에 있는 user 입력값을 확인하고 싶다.
만약 부정확한 값이 입력되어 있을 때, 값을 정정해야 한다. PAI 내 CHECK_MODULE을 어떻게 불러낼 것인가? :

- FIELD field_name MODULE check_module

어떤 데이터 타입이 ABAP data type으로 미리 정의되는가 :

- DECFLOAT34
- STRING
- XSTRING

필드를 위한 Online Documentation(F1 help)을 어디에 만드는가? :  
Data Element

동료가 시작 화면에서 버튼을 눌렀을 때 제대로 작동하지 않는 ABAP 프로그램 분석을 요청했다. 시작 버튼을 눌렀을 때 디버거가 실행되어 분석을 시행할 수 있도록 하고 싶다. 명령 필드에 어떤 커맨드를 입력해야 하는가? :

- /h

주어진 날짜에 대하여 (variable lv_date), 프랑크프루트에서 시드니까지 중간에 단 1번만 환승하는 모든 연결을 찾으려고 한다. 또한 당일에 환승하고 싶다. 비행과 관련한 테이블 ZFLIGHTS이 이하와 같을 때, 당일 환승이 가능한 모든 도시를 찾기 위해 사용할 수 있는 SQL Queries? :

```{
- flightid : primary key
- cityfrom : departure city
- datefrom : departure date
- timefrom : departure time
- cityto : destination city
- dateto : destination date
- timeto : destination time
```

- SELECT DISTINCT cityfrom INTO TABLE lt_cities FROM zflights AS destination  
  WHERE city from IN(SELECT cityto FROM zflights WHERE dateto =  
  destination~datefrom AND timeto < destination~timefrom AND cityfrom =  
  'FRANKFURT' AND datefrom = lv_date) AND destination~cityto = 'Sydney'

이하 transaction 중 ABAP workbench tools에 포함된 것? :

- Class builder(SE24), ABAP editor(SE38)

character type으로 취급되는 elementary field types? :

- T, D, STRING, N, C

hashed internal table의 성질? :

- Unique key를 반드시 보유한다.
- Key를 사용하여 접근이 가능하다.

테이블 타입을 그것의 components를 정의하는 데에 사용할 경우 어떤 structure가 만들어지나? :

- Deep Structure

Object Navigator에 대한 사실? :

- object navigator 내 스크린을 표시하고 편집할 수 있다.
- object navigator 내 ABAP Dictionary 유지가 가능하다.
- object navigator 내 메뉴 표시 및 편집이 가능하다.
- object navigator 내 ABAP 프로그램 표시 및 편집이 가능하다.

transport 가능한 function module을 만들기 전 반드시 존재해야 하는 것? :  
Function Group, Package, Change Request

CALL BADI와 GET BADI는 어떤 타입의 BAdls에 사용되는가? :

- New BAdl

SAP 프로그램의 Function 확장을 위해 BAdl을 사용하고 싶다. 어떤 과정이 필수인가? :

- BAdl 인터페이스를 보충하는 class를 보충해야 한다.

local data objects로 정의할 수 있는 source code blocks? :

- Subroutine, Function Module, Static Method

SAP 표준 어플리케이션 내 new (kernel) Business Add-in(BAdl) 에 위치하고 있는가? BAdl을 보충하기 위해서 어떤 것을 만들어야만 하며, 어떤 순서로 생성해야 하는가? :

- Enhancement Spot implementation
- Badl implementation

web dynpro component에 노출될 수 있는 것은? :

- Custom methods of the component controller

개발시스템으로부터 그 다음 시스템으로 transport request를 옮기고 싶다. 이하에서 그를 위해 필요한 전제조건? :

- transport request 내 모든 object는 activated 되어있어야 한다.
- transport request는 반드시 released 되어있어야 한다.

시스템 로그가 필드의 컨텐츠를 변경할 수 있도록 어떤 data element property를 세팅해야하나?

- documents를 변경한다.

BAdl을 사용할 수 있도록 하기 위해 반드시 해야하는 것? :

- BAdl implemnetatio의 생성
- method를 위한 코드 writing

deep 한 elementary data types? :

- XSTRING

lock object를 release하는 행동? :

- Commit Work
- 커맨드 필드에 /n 입력
- DEQUEUE\_
- The display of a dialog message type A
- ROLLBACK WORK

view A의 database를 정의하고 view B를 ABAP Dictionary에서 유지 중일 때, 어떤 제약사항이 해당 view에 존재하는가? :

- A만 select statement의 FROM 절을 사용 가능
- B에 join된 table들은 반드시 foreign key 관게를 가져야 한다.

multiple inheritance를 시뮬레이팅할 때 어떤 것을 사용하는가? :

- 인터페이스

ABAP에서 local class를 정의할 때, 반드시 따라야 하는 구문의 순서? :

- PUBLIC SECTION, PROTECTED SECTION, PRIVATE SECTION

selection 필드의 파라미터 필드의 기본값을 덮어 쓸 수 있는 건 어떤 event block에서 가능한가? :

- INITIALIZATION

input field 의 documentation을 스크린에 유지할 수 있는 방법? :

- underlying data element에 documentation을 추가한다.

ABAP Dictionary 에서 테이블 타입을 정의할 때 어떠한 properties가 세팅되는가? :

- Line type, Primary key, Access mode

ABAP Dictionary를 사용할 목적? :

- To activate logging for transparent tables
- To create lock objects

2개의 테이블에서 데이터를 선택하고 결과를 structure에 저장하고자 한다. TABLE PARTNER는 필드 PART_ID, KIND를 포함하고 있으며, CONTACT는 CONT_ID, CONT_TYPE, DIVISION의 필드를 포함하고 있다. structure는 이하와 같이 정의되어 있다.

```{
DATA : BEGIN OF wa_result,
Part_id type partner-part_id,
cont_id type contract-cont_id,
Cont_type TYPE contract-cont_type,
END of wa_result,
Lt_result type table of wa_result
```

어떻게 외부 참여가 있는 이하의 SELECT statement 를 대체할 수 있을까?

```{
SELECT part_id from partner INTO wa_result WHERE kind = 'Residential'.
SELECT cont_id form CONTRACT into wa_result-cont_id WHERE part EQ wa_partner-part_id and DIVISION eq 'Water'.
Append wa_result to lt_result.
ENDSELECT.
If sy-subrc<>0. CLEAR wa_result-cont_id APPEND wa_result TO lt_result.
ENDIF.
ENDSELECT.
```

- SELECT part_idcont_id from partner AS A LEFT JOIN contract AS b ON a~part_id = b~part_id INTO CORRESPONDING FIELDS OF TABLE lt_result WHERE kind = 'Residential' and AND division EQ 'Water'.

SAP 표준 어플리케이션에서 GUI 상태를 증진시킬 것을 요청 받았다. 어떤 메뉴 나가기 함수가 코드를 사용할 수 있는지 어떻게 알아낼 것인가? :

- (+) 기호로 시작하는 것을 찾는다.

C data type의 표준 길이는 무엇인가? :

- 1

z1 데이터 참조를 일반적으로 정의했습니다. 참조된 변수의 내용에 접근하기 위해 어떤 statement를 사용하겠습니까? :

- Assign z1 -> \* to \<fs>

여러가지 프로그램에 사용될 수 있는 코드를 짜야 한다. SAP에서 추천하는 기술은 다음 중 어느 것인가? :

- function group의 function module을 사용한다
- global 클래스의 method를 사용한다.

transparent table을 만들고 싶다. table을 활성화하기 위해 어떤 것을 반드시 정의해야 하는가? :

- 간단한 설명
- delivery 클래스
- primary key

static constructor 를 만들 때 반드시 따라야 하는 법칙 2가지? :

- public으로 method를 반드시 정의해야 한다.
- parameters를 정의할 수 없다.

시스템의 업그레이드 이후 수정 조정을 수행하는 데 사용할 수 있는 transaction은 무엇입니까? :

- SPAU, SPDD

container에 있는 것과 full screen으로 보여주는 것의 차이는 무엇입니까? :

- 어떤 타입의 ALV라도 event handling의 사용이 허가된다.
- 컨테이너는 추가 오브젝트의 사용이 요구된다. (a container control)

transparent table에 CURR 타입의 필드를 추가하고 싶다. 어떤 행동을 더 해야 하는가? :

- CUKY 타입 필드에 대한 참조레퍼런스를 만든다.

SAP 어플리케이션 레이어에 속한 구성요소? :

- ABAP dispatcher
- Database interface

ABAP declaration 을 data elements S_CARR_ID를 사용하여 작성 중이다. data object를 맞게 정의하고 있는 statemnets는 어느 것인가? :

- CONSTANTS gc_qf TYPE s_carr_id VALUE 'QF'
- DATA gv_id TYPE s_carr_id

클래스가 이하와 같이 정의되어 있다. 해당 클래스의 어떤 구성요소가 static method 'static1' 이 직접 주소를 지정이 가능합니까? :

```{
CLASS my_class DEFINITION.
PUBLIC SECTION.
METHODS do_something.
EVENTS state_changed.
CLASS-METHODS static1.
PRIVATE SECTION.
TYPES t table TYPE STANDARD TABLE OF t001 WITH NON-UNIQUE DEFAULT KEY.
CONSTANTS gc_const TYPE IVALUE 1.
ENDCLASS.
```

- gc_const constant
- t_table type

SAP 시스템에서 가능한 인터페이스 기술? :

- RFC
- HTTP
- OLE

고객 패키지를 위한 소프트웨어의 구성요소로는? :

- HOME

database view A 를 정의하고 ABAP Dictionary 내 view B를 점검하고 있다. 이렇게 볼 때 어떤 제한사항이 적용됩니까? :

- A만 SELECT statement의 FROM 절에서 사용될 수 있다.
- B에 join된 테이블은 반드시 foreign key 관계를 가지고 있어야 한다.

SELECT에 ENDSELECT가 필요치 않을 때? :

- 테이블 확장을 지정했을 때
- SELECT SINGLE 했을 때
- 테이블에 지정했을 때

function module이 제공하는 매개변수 타입? :

- Input
- Output
- Input/Output(changing)
- Exceptions

pre-defined된 ABAP 데이터 타입 중 deep한 것? :

- STRING

Code Inspector를 구동할 때 어떤 매개변수를 세팅할 수 있는가? :

- Inspection name
- Object set name
- Check varient name

remote function call을 통해 외부 시스템에서 call 될 function module을 작성중이다. 어떻게 외부 발신자에게 에러 리포트를 발송할 수 있는가? :

- Error Data를 레퍼런스 참조를 통해 패스될 테이블 파라미터에 에러데이터를 작성한다.

많으면 몇 개까지 화면에 메뉴를 가지고 있을 수 있는지? :

- 15개

이하의 표현을 ABAP 프로그램이 처리중이다. 다음 중 어떤 데이터 선언이 런타임 환경에 고정 소수점 산술을 사용하도록 초래하는가? :

```{
  r = a / b + c
```

- DATA : r TYPE p DECIMALS 2, a TYPE iVALUE 201, b TYPE iVALUE 200, c TYPE p.

다음 중 유저 인터페이스로 데이터베이스 데이터를 이동시키기 위해 웹 동적 프로그래밍 어플리케이션에서 사용되는 것? :

- Interface controller
- Context node

해당 클래스의 static method의 보충에 접근이 가능한 구성요소의 클래스? :

- Constants
- Types

초기화면으로부터 스크린 시퀸스를 끝내고 시작하는 명령문? :

- SET SCREEN 0

데이터베이스로 옮겨졌을 때 VB\* 테이블로 변경되는 때? :

- update works process 가 실행되었을 때

내부 테이블로의 접속 시간의 향상을 가져오는 boundary 조건? :

- Fully qualified key for sorted tables
- Index access for standard tables
- Left justified part of key for sorted tables

SAP 시스템에서 글로벌 데이터 타입은 어떻게 정의되는가? :

- ABAP Dictionary types

문자열의 공백을 문자A로 덮어써야 할 때 이하 명령문 중 어떤 것을 사용할 수 있는가? :

- OVERLAY
- TRANSLATE
- REPLACE

ABAP 프로그램에서 이하와 같은 코드 시퀸스를 가지고 있다. 할당된 메모리 영역을 캐스팅하는 데에 사용하는 유형은 어떤 것인가?

```{
DATA var TYPE n LENGTH 1.
FIELD -SYMBOLS <fs> TYPE c
ASSIGN var TO <fs> CASTING
```

- The type of var
