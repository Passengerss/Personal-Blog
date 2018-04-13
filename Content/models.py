from django.db import models
from tinymce.models import HTMLField


class Contentinfo(models.Model):
    class Meta():
        db_table="Contentinfo"
        verbose_name = "文章信息"
        verbose_name_plural = "文章信息"

    title = models.CharField(max_length=20,verbose_name="标题")
    content = HTMLField(max_length=5000,verbose_name="内容",blank=True)
    author = models.ForeignKey("User.Userinfo",verbose_name="作者")
    ttype = models.ForeignKey("Contenttype",verbose_name="文章分类")
    def __str__(self):
        return self.title

class Contenttype(models.Model):
    class Meta():
        db_table = "Contenttype"
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"


    type = models.CharField(max_length=20,verbose_name="文章分类")

    def __str__(self):
        return self.type