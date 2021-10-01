
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Department(models.Model):
    dept_name = models.CharField(max_length=1000)
    dept_desc = models.CharField(max_length=1000)
    
    # difine string representation for this model class, will be used when display model class data in dajango admin web site. 
    def __str__(self):
        ret = self.dept_name + ',' + self.dept_desc
        return ret
    class Meta:
        unique_together = ['dept_name']