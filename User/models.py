from django.db import models

# collect the register information
class Userinfo(models.Model):
    class Meta():
        db_table = "Userinfo"
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

    username = models.CharField(max_length=10)
    password = models.CharField(max_length=40)
    headpic = models.ImageField(upload_to="head_pic")
    birth = models.DateField(auto_now_add=True)   # to reckon user's age
    gender = models.CharField(max_length=1,)
    email = models.CharField(max_length=20,)
    level = models.IntegerField(default=0)
    desc = models.CharField(max_length=100,null=True,blank=True)
    isdeleted = models.BooleanField(default=False)
    def __str__(self):
        return self.username

