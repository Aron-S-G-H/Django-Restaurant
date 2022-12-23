from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=30, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره همراه')
    date = models.DateField(verbose_name='تاریخ رزرو', auto_now=False, auto_now_add=False)
    time = models.TimeField(verbose_name='زمان رزرو', auto_now=False, auto_now_add=False)
    number = models.PositiveSmallIntegerField(verbose_name='تعداد نفرات رزروی')

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو ها'
