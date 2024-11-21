from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def my_task(arg1):
    # Your task logic goes here
    print(f"Task executed with argument: {arg1}")