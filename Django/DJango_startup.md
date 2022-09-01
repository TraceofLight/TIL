# DJango 초반 설정

```bash
# 가상머신 설정
$ python -m venv venv

# 가상머신 activation
$ source venv/Scripts/activate

# 가상환경 내 Django 설치
$ pip install django==3.2.13

# requirement에 관한 명령어
$ pip freeze > requirements.txt # 백업
$ pip install -r requirements.txt # 복원

# 프로젝트 생성
$ django-admin startproject {projectname}

# 서버 실행
$ python manage.py runserver

# 어플리케이션 생성
$ python manage.py startapp {appname}

# 모델 생성 후 migration
$ python manage.py makemigrations
$ python manage.py migrate
```



