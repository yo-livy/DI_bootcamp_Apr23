from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateField(null=True, blank=True)
    deadline_date = models.DateTimeField()
    category =  models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.details} | {self.date_creation} | {self.deadline_date} | {self.category}"
    

