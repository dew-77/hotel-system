from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Поле email не может быть пустым')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('date_joined', timezone.now())

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперюзер должен иметь is_staff=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Суперюзер должен иметь is_active=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя."""

    email = models.EmailField('Почта', unique=True)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=150)
    patronymic = models.CharField(
        'Отчество', max_length=50, blank=True, null=True)
    phone_number = models.CharField(
        'Номер телефона', max_length=15, blank=True, null=True)
    photo = models.ImageField(
        upload_to='user_photos/', default='default_user.png',
        blank=True, null=True
    )
    is_superuser = models.IntegerField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name}'
        if self.patronymic:
            full_name += f' {self.patronymic}'
        return full_name

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
