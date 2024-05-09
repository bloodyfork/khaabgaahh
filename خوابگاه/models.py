from django.db import models
from django.contrib.auth.models import AbstractUser
from  core.models import MyUserManager
# Create your models here.
class User(AbstractUser):
    objects = MyUserManager()
    student_number = models.CharField(max_length=13, unique=True, verbose_name='شماره دانشجویی')
    USERNAME_FIELD = 'student_number'

    def save(self, *args, **kwargs):
        self.username = self.student_number
        if User.objects.filter(id=self.id):
            self.set_password(self.password)
        super().save(*args, **kwargs)