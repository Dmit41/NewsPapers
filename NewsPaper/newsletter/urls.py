from django.urls import path
from .views import (
   NewsletterView
)


urlpatterns = [
   path('make_newsletter/', NewsletterView.as_view(), name='newsletters'),
]