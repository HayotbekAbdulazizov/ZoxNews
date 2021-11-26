from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api

def start():
	scheduler = BackgroundScheduler()
<<<<<<< HEAD
<<<<<<< HEAD
	scheduler.add_job(schedule_api, 'interval', minutes=100)
	scheduler.start()
	# 
=======
=======
>>>>>>> parent of bbb2baf (problem soplved with timezone)
	scheduler.add_job(schedule_api, 'interval', minutes=2)
	scheduler.start()
>>>>>>> parent of bbb2baf (problem soplved with timezone)
