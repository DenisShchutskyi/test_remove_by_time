from celery import Celery
from db_w import remove
path_celery = 'redis://localhost:6379/2'
app = Celery('evenot', broker=path_celery)


@app.task
def remove_data(id):
    print(1)
    remove(id)


