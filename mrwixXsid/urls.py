# from django.urls import include, path
# import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


from post.views import index, blog, post
# from portfolio.views import Portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('', Portfolio.as_view(), name='portfolio-list'),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
    path('tinymce/', include('tinymce.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
