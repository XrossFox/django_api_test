from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList3.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail3.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)