from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api

def start():
<<<<<<< HEAD
	scheduler.add_job(schedule_api, 'interval', minutes=100)
=======
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_api, 'interval', minutes=2)
>>>>>>> parent of bbb2baf (problem soplved with timezone)
	scheduler.start()