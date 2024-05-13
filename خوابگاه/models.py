from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import MyUserManager
from core.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class User(AbstractUser):

    GENDER_CHOICES = (
        ('پسر', 'پسر'),
        ('دختر', 'دختر'),
    )

    gender = models.CharField(verbose_name='جنسیت', max_length=4, choices=GENDER_CHOICES, default='دختر', blank=True,null=True)
    phone = models.CharField(verbose_name='شماره تلفن',max_length=11, blank=True, null=True)

    objects = MyUserManager()
    student_number = models.CharField(max_length=13, unique=True, verbose_name='شماره دانشجویی')
    USERNAME_FIELD = 'student_number'

    def save(self, *args, **kwargs):
        self.username = self.student_number
        if User.objects.filter(id=self.id):
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Room(BaseModel):
    room_number = models.PositiveIntegerField(verbose_name='شماره ی اتاق', unique=True, blank=False,
                                              validators=[MinValueValidator(1), MaxValueValidator(300)],
                                              help_text='شماره ی اتاق')
    capacity = models.PositiveIntegerField(verbose_name='ظرفیت اتاق', blank=False, default=5,
                                           validators=[MinValueValidator(1), MaxValueValidator(8)],
                                           help_text='ظرفیت اتاق')
    corridor = models.CharField(verbose_name='نام راهرو', max_length=40,
                                help_text='نام راهرویی که اتاق در آن قرار دارد')
    floor = models.PositiveSmallIntegerField(verbose_name='طبقه',
                                             validators=[MinValueValidator(1), MaxValueValidator(4)],
                                             help_text='طبقه ای که اتاق در آن قرار دارد')
    DORM_CHOICES = (
        ('پسران', 'پسران'),
        ('دختران', 'دختران'),
    )
    dorm = models.CharField(verbose_name='خوابگاه', choices=DORM_CHOICES, max_length=7,
                            help_text='اتاق در خوابگاه دختران است یا پسران')
    is_full = models.BooleanField(verbose_name='تکمیل ظرفیت', default=False, blank=False,
                                  help_text='آیا ظرفیت اتاق تکمیل است؟(تیک سبز یعنی بله)')

    class Meta:
        verbose_name = 'اتاق'
        verbose_name_plural = 'اتاق ها'