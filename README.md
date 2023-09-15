# Platform-for-photographers-
Welcome to the Photographer Platform! The goal of this project is to provide a powerful API for photographers and photography studios that will help manage your photos, orders. Our platform will provide you with all the necessary tools to create, organize and sell photos.

## Technologies used

- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) Django: Powerful Python web framework.
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) Django REST Framework: A library for building APIs based on Django.
- ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) Swagger: A tool for creating interactive API documentation.

---


## How to start
1) Clone the repository: 
```
git clone https://github.com/daler1313/Platform-for-photographers-API
```
2) Create a virtual environment: 
```
python -m venv .venv
```
3) Activate the virtual environment: 
```
source .venv/bin/activate
```
4) Install dependencies: 
```
pip install -r requirements.txt
```
5) Run make migrations: 
```
python manage.py makemigrations
```
6) Run migrate: 
```
python manage.py migrate
```
6) Run super user:
```
python manage.py createsuperuser
```
7) Run the development server: 
```
python manage.py runserver
```

Open Swagger API documentation [localhost:8000/api/v1/swagger-ui/](http://localhost:8000/api/v1/swagger-ui/)


