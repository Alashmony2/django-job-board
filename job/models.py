from django.db import models

JOB_TYBE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_tybe = models.CharField(max_length=50,choices=JOB_TYBE)
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title