from django.urls import path
from .views import FaqListCreate, FaqRetrieveUpdateDestroy

urlpatterns = [
    path('faqs/', FaqListCreate.as_view(), name='faq-list-create'),  # List and create FAQs
    path('faqs/<int:pk>/', FaqRetrieveUpdateDestroy.as_view(), name='faq-retrieve-update-destroy'),  # Retrieve, update, delete
]
