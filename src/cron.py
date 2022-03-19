from crontab import CronTab

cron = CronTab(user='PeeterLiik')
job = cron.new(command='python app.py')


def cron_job():
    job.hour.every(1)
    cron.write()
