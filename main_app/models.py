from django.db import models


class HomeSlider(models.Model):
    image = models.ImageField(upload_to='Slider', verbose_name='عکس اسلایدر',
                              help_text='اندازه عکس ها باید 1920x1280 پیکسل باشند')

    update_at = models.DateTimeField(verbose_name='تاریخ به روزرسانی', auto_now=True)
    date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name = 'عکس اسلایدر'
        verbose_name_plural = 'عکس های اسلایدر'

    def __str__(self):
        return 'عکس اسلایدر ' + str(self.id)


class Gallery(models.Model):
    image = models.ImageField(upload_to='Gallery', verbose_name='عکس گالری',
                              help_text='اندازه عکس ها باید 1200x800 پیکسل باشند')

    update_at = models.DateTimeField(verbose_name='تاریخ به روزرسانی', auto_now=True)
    date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name = 'عکس گالری'
        verbose_name_plural = 'عکس های گالری'

    def __str__(self):
        return 'عکس گالری ' + str(self.id)


class ContactUs(models.Model):
    name = models.CharField(max_length=30, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره همراه')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
