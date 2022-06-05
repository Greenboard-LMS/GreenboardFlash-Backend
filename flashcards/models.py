from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


Topics = (
    'Math',
    'Science',
    'English',
    'History',
    'Geography',
    'Biology',
    'Chemistry',
    'Physics',
    'Music',
    'Art',
    'Literature',
    'Business',
    'Economics',
    'Computer Science',
    'Programming',
    'Other',
)


class Cardset(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default="Untitled")

    def __str__(self):
        return self.title

    @property
    def flashcard_count(self):
        return self.flashcard_set.all().count()


class Flashcard(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    cardset = models.ForeignKey(Cardset, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Studyplan(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateField()
    cardsets_to_study = models.ManyToManyField(
        Cardset, related_name="study_plans")

    def __str__(self):
        return self.title
