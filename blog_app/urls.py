from django.urls import path
from . import views
from django.conf.urls.static import static
from YamiFood import settings

app_name = 'blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name='blogList_page'),
    path('detail/<slug:slug>', views.BlogDetail.as_view(), name='blogDetail_page'),
    path('tag/<slug:tag>', views.blog_tag, name='blogTagList_page'),
    path('category/<slug:category>', views.blog_category, name='blogCategoryList_page'),
    path('search', views.blog_search, name='blogSearch_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
