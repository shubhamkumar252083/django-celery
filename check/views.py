from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .models import One

def list_view(request):
    objects = One.objects.all().values("name", "timestamp", "created_at", "updated_at")
    return JsonResponse({"data": list(objects)}, safe=False)


from django.http import JsonResponse
from check.tasks import add

def add_view(request):
    # Call the Celery task
    task = add.delay(3, 58888)  # This runs asynchronously in the Celery worker
    # Optionally, return the task ID to track the status
    return JsonResponse({"task_id": task.id, "status": "Task Submitted"})


from celery.result import AsyncResult

def task_status(request, task_id):
    result = AsyncResult(task_id)  # Fetch the task using the task_id
    return JsonResponse({
        "task_id": task_id,
        "status": result.status,  # Status could be PENDING, STARTED, SUCCESS, FAILURE
        "result": result.result if result.ready() else None,
    })
