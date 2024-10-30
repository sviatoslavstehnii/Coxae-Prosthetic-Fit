from django.urls import path
from prothesizer.views import ProsthesisProcessAPIView



urlpatterns = [
    path('process/', ProsthesisProcessAPIView.as_view(), name='prosthesis-process'),
]