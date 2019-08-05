from django.contrib import admin
from django.urls import path, include

"""
4. Implement a password protected healthcheck endpoint covering:
    1.	Django app is up and running and not in dev mode
    2.	Database is accessible and can be queried
    3.	App server has disk space left
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls', namespace='polls')),
    path('ht/', include('health_check.urls')),
    path('watchman/', include('watchman.urls'))

]
