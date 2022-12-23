from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان', unique=True)

    body = models.TextField(verbose_name='متن')

    image = models.ImageField(verbose_name='تصویر بلاگ', upload_to='Blog',
                              help_text='اندازه تصاویر 470x570 پیکسل باشد')

    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='blog')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')

    tag = models.ManyToManyField('Tag', verbose_name='تگ ها', related_name='tag')

    situation = models.BooleanField(verbose_name='وضعیت انتشار', default=False)

    created_at = models.DateField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    update = models.DateTimeField(verbose_name='تاریخ به روزرسانی', auto_now=True)

    slug = models.SlugField(blank=True, verbose_name='اسلاگ',
                            help_text='این فیلد به صورت خودکار تکمیل میشود')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Blog, self).save()

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'


class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='عنوان دسته بندی', unique=True)

    slug = models.SlugField(blank=True, verbose_name='اسلاگ',
                            help_text='این فیلد به صورت خودکار تکمیل میشود')

    date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Tag(models.Model):
    title = models.CharField(max_length=25, verbose_name='عنوان تگ', unique=True)

    slug = models.SlugField(blank=True, unique=True, verbose_name='اسلاگ',
                            help_text='این فیلد به صورت خودکار تکمیل میشود')

    date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Tag, self).save()

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله',
                             help_text='کامنت مدنظر برای چه مقاله ای هست')

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
