from django.db import models
from datetime import timedelta, datetime as dt


def is_task_overdue(sch_date):
    sch_date = dt.strptime(sch_date, '%Y-%m-%d')
    days_overdue = (dt.today() - sch_date).days
    is_overdue = days_overdue > 0
    return is_overdue, days_overdue


class Task(models.Model):

    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    schedule_date = models.DateField(default=dt.today() + timedelta(days=1))
    is_done = models.BooleanField(default=False)
    is_overdue = models.BooleanField(default=False)
    days_overdue = models.IntegerField(default=0)

    def __str__(self):
        return self.title


