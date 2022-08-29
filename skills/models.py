from django.db import models


# для *Навыки*

class Skills(models.Model):
    description = models.CharField(max_length=150, verbose_name='Сфера деятельности')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ['id']


class Element(models.Model):
    description_element = models.CharField(max_length=150, verbose_name='Описание элемента')
    logotypes = models.ImageField(upload_to='photos/', blank=True, verbose_name='Логотип')
    description = models.ForeignKey(Skills, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.description_element

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
        ordering = ['id']


# для *Обо мне*

class Aboutme(models.Model):
    info = models.TextField(max_length=200, verbose_name='Информация')
    icons = models.ImageField(upload_to='photos/', blank=True, verbose_name='Иконки')

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Инфа'
        verbose_name_plural = 'Инфушечки'
        ordering = ['id']


# для *Портфолио*

class Examples(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название проекта')
    pict = models.ImageField(upload_to='photos/', blank=False, verbose_name='Картинги примеров работ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'
        ordering = ['id']

class Contact(models.Model):
    hr = models.CharField(max_length=200, verbose_name='Ссылка на соцсеть')
    media = models.ImageField(upload_to='photos/', blank=False, verbose_name='Иконка соцсети')

    def __str__(self):
        return self.hr

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['id']