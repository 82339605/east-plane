from django.db import models

# Create your models here.
class getIn(models.Model):
    flight = models.CharField(max_length=30,verbose_name='航班')
    status = models.CharField(max_length=30,verbose_name='状态')
    beginPlace = models.CharField(max_length=30,verbose_name='始发地')
    planarrtime = models.TimeField(verbose_name='计划到达')
    arrtime = models.CharField(max_length=30,verbose_name='实际到达')
    arrplace = models.CharField(max_length=10,verbose_name='到达航站楼')
    bagplace = models.CharField(max_length=20,verbose_name='行李转盘')
    class Meta:
        db_table = 'getIn'
        verbose_name_plural = '进港'
    def __str__(self):
        return self.flight
class left(models.Model):
    flight = models.CharField(max_length=30, verbose_name='航班')
    status = models.CharField(max_length=30, verbose_name='状态')
    beginPlace = models.CharField(max_length=30, verbose_name='始发地')
    planarrtime = models.TimeField(verbose_name='计划到达')
    arrtime = models.CharField(max_length=30, verbose_name='实际到达')
    arrplace = models.CharField(max_length=10, verbose_name='到达航站楼')
    bagplace = models.CharField(max_length=20, verbose_name='行李转盘')
    class Meta:
        db_table = 'left'
        verbose_name_plural = '离港'
    def __str__(self):
        return self.flight
class tickets(models.Model):
    beginplace = models.CharField(max_length=100,verbose_name='始发地')
    endplace = models.CharField(max_length=100,verbose_name='终点')
    money = models.CharField(max_length=50,verbose_name='价格')
    time = models.TimeField()
    class Meta:
        db_table = 'planeticketes'
        verbose_name_plural = '失误'
    def __str__(self):
        return self.beginplace+'-'+self.endplace
class ticket(models.Model):
    place = models.CharField(max_length=100,verbose_name='位置')
    infor = models.CharField(max_length=100,verbose_name='日期',)
    prices = models.CharField(max_length=50,verbose_name='价格')
    class Meta:
        db_table = 'planetickete'
        verbose_name_plural = '机票'
    def __str__(self):
        return self.place
class user(models.Model):
    log_name = models.CharField(max_length=50,verbose_name='登录名')
    username = models.CharField(max_length=50,verbose_name='使用名')
    pwd = models.CharField(max_length=30,verbose_name='密码')
    tic = models.ForeignKey(ticket,null=True)
    class Meta:
        db_table = 'user'
        verbose_name_plural = '用户信息表'
    def __str__(self):
        return self.log_name


