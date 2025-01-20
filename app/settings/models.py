from django.db import models

class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    image = models.ImageField(
        upload_to="settings/",
        verbose_name='Фото'
    )
    image2 = models.ImageField(
        upload_to="settings/",
        verbose_name='Фото 2'
    )
    job = models.CharField(
        max_length=155,
        verbose_name='Где работает'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Info(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Информация'