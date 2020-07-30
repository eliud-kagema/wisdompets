from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]



# Applications URLS
urlpatterns += [
    path('adoptions/', include('adoptions.urls')),
]


#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/adoptions/', permanent=True)),
]
