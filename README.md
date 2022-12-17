# BaykarIHARent

Backend Endpoints
- API Documentation: http://localhost:8000/schema/redoc/
- UAV CRUD Endpoints: http://localhost:8000/api/uav/
- Model CRUD Endpoints: http://localhost:8000/api/model/
- Brand CRUD Endpoints: http://localhost:8000/api/brand/
- Login Endpoint: http://localhost:8000/api/token/


Frontend Endpoints
- All Endpoint Lists: http://localhost:3000


Usage

    Frontend
        cd client
        npm run start 

    Backend
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

For admin account you have to create superuser:

- python manage.py createsuperuser

However, If you are admin or superuser you can create UAV, Model or Brand otherwise you can only see lists
