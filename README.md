# poster
This application is a scheduler to post anything to facebook on a specific time.

### Instruction to run the application locally.
* docker-compose up poster-db redis
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

### To run celery beat and worker
* celery -A poster worker -l info
* celery -A poster beat -l info
