from django.urls import path
from .views import home_page,home_page_pi

app_name = 'dashboard'
urlpatterns = [
    path('', home_page, name='home'),## Now Not used
    path('chart/', home_page_pi, name='home_pi'),
]