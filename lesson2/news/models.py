from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Название',max_length=100)
    short_description = models.CharField('Короткое описание',max_length=200)
    content = models.TextField('Новость')
    source = models.CharField('Источник',max_length=50,default='Пользователь')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'