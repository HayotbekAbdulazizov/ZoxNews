from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api
from pytz import utc
scheduler = BackgroundScheduler({'apscheduler.timezone': 'UTC'})

def start():
	scheduler.add_job(schedule_api, 'interval', minutes=100)
	scheduler.start()