# About Git

## Git이란?

버전 관리 도구의 일종으로 버전 관리를 통해 파일의 변화를 기록했다가 특정 시점의 기록을 다시 사용할 수 있도록 하는 시스템

### 로컬 버전 관리

1. 디렉토리의 복사
   - 가장 Naive 한 방법
   - 실수로 파일을 잘못 고칠 수도 있고, 잘못 복사할 수도 있다.
2. VCS (Version Control System)
   - DB를 활용하여 파일의 변경 정보를 관리
   - Revision Control System이 대표적
   - Patch Set(파일에서 변경되는 부분)을 관리
   - 일련의 Patch Set을 활용하여 모든 파일을 특정 시점으로 되돌릴 수 있음

### 중앙집중식 버전 관리

- 프로젝트를 진행할 경우 다른 개발자와의 협업이 잦음

- 이럴 경우 파일을 관리하는 서버가 별도로 존재하고 클라이언트가 중앙 서버에서 파일을 받아서 사용하는 방식이 유리
- 중앙 서버에 문제가 발생할 경우 시스템의 백업이 존재하지 않는다면 모든 히스토리를 잃을 수 있고 이는 로컬에서도 존재하고 있었던 문제

### 분산 버전 관리 시스템

- 단순하게 스냅샷만 보관하는 것이 아닌 저장소와 히스토리를 동시에 복제한다. 
- 서버에 문제가 발생했을 경우, 해당 복제물을 통해 작업의 재개가 가능
- 클라이언트 중에서 아무거나 골라 서버를 복원하는 것도 가능
- 리모트 저장소의 존재로 다양한 방식의 협업이 가능

## General Usage

### 설정 및 파일 접근 명령어

```bash
# 전역 사용자 설정
git config --global user.name {name} # 이름
git config --global user.email {email_address} # 이메일

# 로컬 사용자 설정 (해당 디렉토리에서 실행)
git config user.name {name} # 이름
git config user.email {email_address} # 이메일

# 설정 조회
git config --list

# 생성
git mkdir {path}/{folder_name} # 폴더
git touch {file_name} # 파일
git init # 파일 관리 시스템

# 저장소 및 히스토리 복제
git clone {repository_url}

# 원격 저장소
git remote add {remote_repo_name} {remote_repo_url} # 추가
git remote -v # 정보 확인

# commit history
git log
git log --oneline # 정보 표시 간략화
git log --all # 현재 head 이후의 최신 기록들을 포함한 전체 정보를 표시
git log --graph # 브랜치를 시각화하여 분기를 표현한 그래프 형태로 정보를 표시
```

### 저장소 관리에 사용하는 명령어

```bash
git status # 변경사항을 확인하는 명령어
git commit -m {message} # 현재 스테이지에 존재하는 변경 사항을 커밋

git add {file_name} # 특정한 파일을 스테이지에 추가하는 경우
git add . # 해당 레포지토리의 변경사항을 전부 스테이지에 추가하는 경우
```

## Git Undoing

### 스테이지 비우기

```bash
git rm --cached # root commit이 존재하지 않을 때
git restore --staged # root commit이 존재할 때
```

### commit의 수정

```bash
git commit --amend 
# 스테이지에 파일이 없는 경우: 직전 커밋의 메시지를 수정
# 스테이지에 파일이 있는 경우: 기존 커밋에 현재 스테이지를 더하여 덮어쓰기 진행
```

### commit 특정 시점까지 전부 되돌리기

```bash
git reset --soft {commit_id} # 미래 파일들 전부 stage에 돌려놓음
git reset --mixed {commit_id} # default, 미래 파일들을 전부 working directory에 유지 (add 필요)
git reset --hard {commit_id} # 미래 파일 전부 제거
```

### 과거 commit을 제거

```bash
git revert {commit_id} # 과거 commit을 제거 후, 제거했음을 commit으로 추가
```

reset은 commit 갯수가 줄어들기 때문에 협업에 부적합, 따라서 협업 시 reset 대신 revert 사용을 권장

## Git Branch

Branch: 작업 공간을 분할, 독립적으로 작업할 수 있도록 돕는 장치

- 원본 상태를 계속 유지할 수 있어 안전함
- 하나의 브랜치에서 하나의 작업을 진행하여 협업의 효율이 증가
- Git의 경우 Branch의 생성 속도도 빠르고 파일 용량도 크지 않음

### 관련 명령어

```bash
# 조회
git branch # 로컬 저장소의 브랜치 대상
git branch -r # 원격 저장소의 브랜치 대상

# 생성
git branch {branch_name}
git branch {branch_name} {commit_id} # 특정 커밋 지점을 기준점으로 생성

# 제거
git branch -d {branch_name} # 병합 완료된 경우
git branch -D {branch_name} # 병합하지 못한 브랜치 강제 삭제


# 브랜치 이동
# 이동 전 반드시 현재 브랜치의 변경사항을 기록할 것
git switch {branch_name} # 이미 있는 브랜치로 이동
git switch -c {branch_name} # 해당 이름의 브랜치를 생성 후 이동
git switch -c {branch_name} {commit_id} # 특정 커밋 지점을 기준점으로 하는 해당 이름의 브랜치를 생성 후 이동
```

## Git Merge

분기된 브랜치를 병합하는 과정

### 병합의 종류

- Fast - Forward: 브랜치가 가리키는 커밋을 맨 앞으로 이동
- 3 - Way Merge: 각 브랜치의 제일 최신 커밋 2개 + 두 브랜치의 공통 조상을 사용한 병합
- Merge Confilict: 같은 파일을 수정했을 경우 충돌 발생 => 충돌을 해결한 뒤 3 - Way Merge를 진행

```bash
# 해당 브랜치를 현재 위치한 브랜치에 병합
git merge {merged_branch}
```

## Git Fork

소유권이 없는 원격 저장소를 복제하는 것, 주로 오픈 소스와 같은 협업 대상이 다수일 때 사용

### Fork 된 소스에 내 커밋이 반영되는 과정

```bash
#
#    원본 원격 저장소 (upstream) <----------- 복제본 원격 저장소 (origin)
#                \           merge request      /|
#                 \                              |
#                  \                 push branch | pull master
#                   \                            |
#                    \     ( pull upstream )     |/
#                     ------------------> 로컬 저장소 (user)
#
```

1. 원본 저장소를 내 원격 저장소에 복제
2. 해당 원격 저장소에서 로컬로 저장
3. 로컬에서 브랜치를 생성해서 작업 후 해당 작업들을 커밋
4. 원본 원격 저장소에 변경 사항에 대한 merge 요청을 push
5. 원본 원격 저장소에서 해당 변경 사항을 merge
6. 해당 원본 저장소에서 변경된 내용을 pull 
   - pull upstream
   - sync origin & pull origin
7. 로컬에서 merge된 내 브랜치를 제거