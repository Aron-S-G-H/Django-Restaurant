from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Blog, Category, Tag, Comment


class BlogList(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'blog_app/blog.html', {'blogs': blogs})


class BlogDetail(View):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        categorys = Category.objects.all()
        tags = Tag.objects.all().filter(tag=blog)
        recent_blog = Blog.objects.all().order_by('-created_at')[:5]

        return render(request, 'blog_app/blog-details.html',
                      {'blog': blog, 'categorys': categorys, 'tags': tags, 'recent_blog': recent_blog})

    def post(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        categorys = Category.objects.all()
        tags = Tag.objects.all().filter(tag=blog)
        recent_blog = Blog.objects.all().order_by('-created_at')[:5]

        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        parent_id = request.POST.get('parent_id')

        Comment.objects.create(blog=blog, name=name, email=email, text=text, parent_id=parent_id)

        return render(request, 'blog_app/blog-details.html',
                      {'blog': blog, 'categorys': categorys, 'tags': tags, 'recent_blog': recent_blog})


def blog_tag(request, tag):
    blogs = Blog.objects.filter(tag__slug=tag)
    return render(request, 'blog_app/blog.html', {'blogs': blogs})


def blog_category(request, category):
    blogs = Blog.objects.filter(category__slug=category)
    return render(request, 'blog_app/blog.html', {'blogs': blogs})


def blog_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        blogs = Blog.objects.filter(title__icontains=query)
        return render(request, 'blog_app/blog.html', {'blogs': blogs})
