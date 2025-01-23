from django.db import models
from ckeditor.fields import RichTextField

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

class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='Заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'О нас'

class AboutMe(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='Ключ'
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )

    def __str__(self):
        return self.key

    class Meta:
        verbose_name_plural = "Об мне"

class Works(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='works',
        verbose_name='Фото'
    )
    image_2 = models.ImageField(
        upload_to='works',
        verbose_name='Фото'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description2 = RichTextField(
        verbose_name='Описание'
    )
    key = models.CharField(
        max_length=155,
        verbose_name='Ключ'
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Работы'

class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    phone = models.IntegerField(
        verbose_name='Номер телефона'
    )
    subject = models.CharField(
        max_length=155,
        verbose_name='Обект'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )

    def __str__(self):
        return self.name