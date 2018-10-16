from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 120, null=True, blank=True)
    done = models.BooleanField(default = False)
    duedate = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.done:
            return f'{self.name} (done)'
            # f'{self.name} (done)' is the python 3.6+ alternative for '{} (done)'.format(self.name)
        else:
            return f'{self.name}'
