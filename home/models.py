from django.db import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('None', 'None'),
    ('Other', 'Other'),
)


TIME_CHOICES = (
    ('1st Wave', '1st Wave'),
    ('2nd Wave', '2nd Wave'),
    ('Both', 'Both'),
)


SOURCE_CHOICES = (
    ('Quora', 'Quora'),
    ('Reddit', 'Reddit'),
    ('Survey', 'Survey'),
)


class Queries(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, verbose_name='Name')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    subject = models.CharField(max_length=200, blank=False, null=False, verbose_name='Subject')
    message = models.CharField(max_length=2000, blank=False, null=False, verbose_name='Message')

    def __str__(self):
        return self.subject

class CovidExperience(models.Model):
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name='Name')
    age = models.IntegerField(blank=True, null=True, verbose_name='Age')
    mobile = models.CharField(max_length=10, blank=True, null=True, verbose_name='Contact')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='Gender', default='None')
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, verbose_name='Source', default='Survey')
    time_of_infection = models.CharField(max_length=10, choices=TIME_CHOICES, verbose_name='The time of Infection', default='1st Wave')
    testing_date1 = models.DateField(verbose_name="Testing Date (positive result date only)", null=True, blank=True)
    testing_date2 = models.DateField(verbose_name="Testing Date(optional)", null=True, blank=True)
    experience = models.CharField(max_length=5000, blank=False, null=False, verbose_name='Experience')
    islongcovid = models.BooleanField(verbose_name='Is Long Covid', default=False, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


class QueryReply(models.Model):
    experience = models.ForeignKey(CovidExperience, on_delete=models.CASCADE, related_name='experience_obj')
    text = models.CharField(max_length=1000, blank=False, null=False, verbose_name='Reply')
    def __str__(self):
        return str(self.pk)


class Symptom(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, verbose_name='Name')
    count = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.name)
