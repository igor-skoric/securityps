from django.db import models


class JobApplication(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    birth_year = models.PositiveIntegerField()
    message = models.TextField()
    cv = models.FileField(upload_to='cv_uploads/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
