Python 3.12.3

pip install celery[redis] django-celery-beat django-celery-results

pip install celery redis
pip install django-celery-results




Start the Celery worker process for your project:
bash
celery -A main worker --loglevel=info

#

If you're using periodic tasks, start the scheduler:
bash
celery -A main beat --loglevel=info


pip install flower
celery -A main flower


<!-- 
 -->


python manage.py shell
from myapcheckp.tasks import add
result = add.delay(2, 3)  # Call the task asynchronously
print(result.get())


<!-- if u dont want to store result of task in redis or db -->

CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"  # Redis as the broker
CELERY_RESULT_BACKEND = None  # Disable result storage
CELERY_IGNORE_RESULT = True  # Instruct Celery to skip result storage