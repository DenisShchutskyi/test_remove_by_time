from celery_test import remove_data
from datetime import datetime, timedelta

tomorrow = datetime.utcnow() + timedelta(minutes=1)


def rm():
    print(-1)
    remove_data.apply_async((20,), eta=tomorrow)
    remove_data.delay(20)
    print(-2)


rm()