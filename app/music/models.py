from django.db import models


class Performer(models.Model):
    name  = models.CharField(max_length=255, unique=True, verbose_name='Исполнитель')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Album(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Имя альбома')
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE, verbose_name='Автор')
    date_relize = models.IntegerField('Год релиза')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Song(models.Model):
    name = models.CharField(max_length=255, verbose_name='Песня')
    performer = models.ForeignKey(Performer, on_delete=models.SET_NULL, 
                                  null=True, verbose_name='Исполнитель')
    # album = models.ManyToManyField(Album,  related_name='songs', verbose_name='Альбом')
    album = models.ForeignKey(Album, verbose_name='Альбом', on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, null=True, verbose_name='Позиция')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'