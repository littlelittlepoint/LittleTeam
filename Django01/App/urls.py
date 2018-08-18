from django.conf.urls import url

from App import views
from App.views import hello_django

urlpatterns = [
    url(r'^students/', views.StudentsView.as_view(), name='students'),
    url(r'^hellodjango/', hello_django, name='hello_django'),
    url(r'^studenttemplate/', views.StudentTemplateView.as_view(template_name='StudentTemplate.html'))
]
