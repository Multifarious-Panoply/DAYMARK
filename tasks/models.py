from datetime import datetime, timedelta

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    scheduled_date = models.DateField(null=True, blank=True)
    scheduled_time = models.TimeField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["is_completed", "-created_at"]

    def __str__(self):
        return self.title

    @property
    def scheduled_end_time(self):
        if self.scheduled_time is None or self.duration_minutes is None:
            return None

        base_date = self.scheduled_date or self.created_at.date()
        start = datetime.combine(base_date, self.scheduled_time)
        end = start + timedelta(minutes=self.duration_minutes)
        return end.time()
