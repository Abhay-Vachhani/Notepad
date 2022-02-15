from django.urls import path
from notepad_app.views import home, homeWithNote

urlpatterns = [
    path('', home, name='home'),
    path('<slug:noteId>', homeWithNote, name='home'),
    path('index.php', home, name='home'),
    path('index.php/<slug:noteId>', homeWithNote, name='load'),
]
