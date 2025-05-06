from django.db import models

class StudentInfo(models.Model):
    GENDER_CHOICES = [
        ('Male', 'male'),
        ('Female', 'female'),
    ]

    INTEREST_CHOICES = [
        ('accounting', 'Accounting'),
        ('bookkeeping', 'Bookkeeping'),
        ('business', 'Business'),
        ('child education', 'Child Education'),
        ('coding', 'Coding'),
        ('community service', 'Community Service'),
        ('conflict resolution', 'Conflict Resolution'),
        ('cybersecurity', 'Cybersecurity'),
        ('data science', 'Data Science'),
        ('debate', 'Debate'),
        ('finance', 'Finance'),
        ('forensics', 'Forensics'),
        ('gaming', 'Gaming'),
        ('history', 'History'),
        ('investigation', 'Investigation'),
        ('investment', 'Investment'),
        ('law enforcement', 'Law Enforcement'),
        ('lesson planning', 'Lesson Planning'),
        ('networking', 'Networking'),
        ('numbers', 'Numbers'),
        ('philosophy', 'Philosophy'),
        ('politics', 'Politics'),
        ('psychology', 'Psychology'),
        ('public speaking', 'Public Speaking'),
        ('recruitment', 'Recruitment'),
        ('social issues', 'Social Issues'),
        ('teaching', 'Teaching'),
        ('tech', 'Tech'),
        ('training', 'Training'),
        ('volunteering', 'Volunteering'),
    ]

    COURSE_CHOICES = [
        ('accountancy', 'Accountancy'),
        ('BSIT', 'BSIT'),
        ('criminology', 'Criminology'),
        ('education', 'Education'),
        ('financial_mgmt', 'Financial Management'),
        ('hrm', 'Human Resource Management'),
        ('polsci', 'Political Science'),
        ('social_work', 'Social Work'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    interest = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
