import requests
import schedule
import time
from datetime import datetime


def fetch_schedules():
    url = "https://smart-farm-server.vercel.app/schedules"
    response = requests.get(url)
    return response.json()


def job_start(schedule_name):
    print(f"Starting {schedule_name} at {datetime.now()}")


def job_stop(schedule_name):
    print(f"Stopping {schedule_name} at {datetime.now()}")


def setup_scheduler(schedules):
    for sched in schedules:
        start_time = sched['startTime']
        stop_time = sched['stopTime']
        scheduler_name = sched['schedulerName']
        is_active = sched['isActive']

        if is_active:
            # Schedule the start job
            schedule.every().day.at(start_time).do(job_start, scheduler_name)
            # Schedule the stop job
            schedule.every().day.at(stop_time).do(job_stop, scheduler_name)


if __name__ == '__main__':
    schedules = fetch_schedules()
    setup_scheduler(schedules)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)
