from django.db import models

class Faq(models.Model):
    fruit = models.CharField(max_length=100)  # Fruit name
    question = models.CharField(max_length=300)  # FAQ question
    answer = models.TextField()  # FAQ answer

    def __str__(self):
        return f"{self.fruit} - {self.question}"
