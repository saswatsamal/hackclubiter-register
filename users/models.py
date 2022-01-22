from django.db import models

BRANCH = (
    ('cse','CSE'),
    ('csit', 'CSIT'),
    ('ee','EE'),
    ('eee','EEE'),
    ('ece','ECE'),
    ('me','ME'),
    ('ce','CE'),
    ('other','OTHER'),
)
YEAR = (
    ('1','1st'),
    ('2', '2nd'),
    ('3','3rd'),
    ('4','4th'),
)

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    registrationnumber = models.BigIntegerField()
    branch = models.CharField(max_length=8, choices=BRANCH, default='green')
    year = models.CharField(max_length=4, choices=YEAR, default='green')
    contactnumber = models.BigIntegerField()

    def __str__(self):
        return self.firstname+" "+self.lastname
