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
