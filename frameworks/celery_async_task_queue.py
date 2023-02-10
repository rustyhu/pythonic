# https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#running-the-celery-worker-server

from celery import Celery

# specifying the URL of the message broker you want to use
app = Celery('name_tasks', broker='redis://localhost')

# Simple start:
# 1. start a worker using cmd "celery -A celery_async_task_queue worker"
# 2. Use a python REPL as a client to import this `app.task` and send message
# 3. This `app.task` will be completed asynchronously


@app.task
def add(x, y):
    return x + y
