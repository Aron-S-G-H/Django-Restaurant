from django.db import models
from django.utils.text import slugify


class Food(models.Model):
    TYPES = [
        ('drinks', 'نوشیدنی'),
        ('lunch', 'ناهار'),
        ('dinner', 'شام'),
    ]

    food_type = models.CharField(max_length=20, choices=TYPES, verbose_name='نوع غذا')

    name = models.CharField(max_length=20, verbose_name='اسم غذا')

    price = models.PositiveIntegerField(verbose_name='قیمت غذا')

    descripion = models.TextField(verbose_name='توضیحات غذا')

    image = models.ImageField(upload_to='Foods', verbose_name='عکس غذا',
                              help_text='تصاویر باید در سایز 800x480 باشند')

    slug = models.SlugField(blank=True, unique=True, verbose_name='اسلاگ',
                            help_text='این فیلد به صورت خودکار تکمیل میشود')

    update_at = models.DateTimeField(verbose_name='تاریخ به روزرسانی', auto_now=True)
    date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    situation = models.BooleanField(default=True, verbose_name='موجود بودن غذا')
    status = models.BooleanField(default=False, verbose_name='وضعیت', help_text='وضعیت انتشار در سایت')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Food, self).save()

    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذاها'


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comments', verbose_name='غذا',
                             help_text='کامنت مدنظر برای کدوم غذاست')

    name = models.CharField(max_length=20, verbose_name='نام و نام خانوادگی')

    email = models.EmailField(verbose_name='ایمیل', null=True)

    text = models.TextField(verbose_name='متن کامنت')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', verbose_name='جواب کامنت',
                               help_text='اگر این کامنت درجواب کامنت دیگری باشد تکمیل میگردد', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
