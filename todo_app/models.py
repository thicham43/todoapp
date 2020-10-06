from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime as dt


def is_task_overdue(sch_date):
    days_overdue = (dt.today().date() - sch_date).days
    is_overdue = days_overdue > 0
    return is_overdue, days_overdue


class Tag(models.Model):

    COLORS = (('yellow', 'Yellow'), ('orange', 'Orange'),
              ('red', 'Red'), ('green', 'Green'),
              ('purple', 'Purple'), ('blue', 'Blue'))

    name = models.CharField(max_length=15)
    color = models.CharField(choices=COLORS, max_length=10, default='yellow')

    def __str__(self):
        return self.name


class Task(models.Model):

    IMP_CHOICES = (('normal', 'Normal'),
                   ('medium', 'Medium'),
                   ('critical', 'Critical'))

    title = models.CharField(max_length=50)
    comment = models.TextField(max_length=200, blank=True)
    schedule_date = models.DateField(default=dt.today().date() + timedelta(days=1))
    is_done = models.BooleanField(default=False)
    is_overdue = models.BooleanField(default=False)
    days_overdue = models.IntegerField(default=0)
    importance = models.CharField(choices=IMP_CHOICES, max_length=10, default='normal')
    managed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["is_done", "-schedule_date"]

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        res = is_task_overdue(self.schedule_date)
        self.is_overdue = res[0]
        self.days_overdue = res[1]
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
