import schedule
import time
import functools

def scheduleJob(cron):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            schedule.every().day.at(cron).do(func, *args, **kwargs)
            while True:
                schedule.run_pending()
                time.sleep(1)
        return wrapper
    return decorator