import os
from datetime import datetime

from gpustat.core import GPUStatCollection
from apscheduler.schedulers.blocking import BlockingScheduler


def gpu_listening_scheduler():
    gs = GPUStatCollection.new_query()
    for gpu in gs.gpus:
        if gpu.index == 0:
            if float(gpu.memory_used)/float(gpu.memory_total) < 0.5 \
                and gpu.utilization < 10:
                    print('Restrictions satisfied~')
                    os.system("python send_email.py") # run `send_email.py`
                    print('Email sent~')
                    break


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(gpu_listening_scheduler, 'cron', 
                      second=30, next_run_time=datetime.now())
    scheduler.start()


if __name__ == '__main__':
    main()
