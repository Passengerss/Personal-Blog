from django.db import models

class Movie_info(models.Model):
    class Meta():
        db_table="Movie_info"
        verbose_name = "电影信息"
        verbose_name_plural = "电影信息"

    name_ch = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)   # English name
    magnet_link = models.CharField(max_length=500,default="暂无")
    thunder_link = models.CharField(max_length=300,default="暂无")
    publist_date = models.CharField(max_length=20,default="不详")
    movie_length = models.CharField(max_length=10,default="--:--")
    download_count = models.IntegerField()