from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s balance: {self.amount}"



