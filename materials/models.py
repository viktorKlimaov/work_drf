from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(max_length=150, verbose_name='Описание курса', blank=True, null=True)
    image = models.ImageField(upload_to='materials/', verbose_name='Изображение', blank=True, null=True)


    class Meta:
        verbose_name = 'Курс '
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(max_length=150, verbose_name='Описание урока', blank=True, null=True)
    image = models.ImageField(upload_to='materials/', verbose_name='Изображение', blank=True, null=True)
    url_to_video = models.URLField(max_length=300, verbose_name='Ссылка на видео', blank=True, null=True)

    class Meta:
        verbose_name = 'Урок '
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.name}'
