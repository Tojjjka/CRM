from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField("Название компании", max_length=255)
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Client(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name='clients',
        verbose_name="Компания"
    )
    name = models.CharField("Имя клиента", max_length=255)
    email = models.EmailField("Email", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    responsible = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Ответственный менеджер"
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

