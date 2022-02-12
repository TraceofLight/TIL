### 마크다운 미리보기

vscode 우상단에 있는 옵션 중 돋보기 걸린 창문 선택하면 마크다운이 어떤 식으로 보이게 될지 확인할 수 있음

### 일괄 변경

변수나 문자 클릭하고 Ctrl + Shift + L 키를 동시에 누르면 해당하는 중복값이 전체 선택된다.

### 'const' can only be used in a .ts file

const 형은 typescript에서만 사용이 가능하다는 에러가 뜰경우
javascript.validate.enable = true로 되어있을 가능성이 높다.
javascript.validate.enable = false로 바꿔주자.
vs code인 경우엔 Ctrl + ,로 javascript.validate.enable를 검색하면 바로 나온다.

출처: https://zereight.tistory.com/132

### prettier 적용 불가능한 오류

VSCode > Preference (cmd+,) 들어가서 'Default Formatter'를 검색
아래 설정이 null로 되어있을 텐데, 이를 'enbenp.prettier-vscode'로 고쳐준다.
출처: https://nuggy875.tistory.com/110
