from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    # path('', views.home, name='ho'),
    path('blog/', include('blog.urls')),
    path('core/', include('core.urls')),
    path('todo/', include('todo.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
