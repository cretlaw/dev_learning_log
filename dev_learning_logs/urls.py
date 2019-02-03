'''Define URL patterns for dev_learning_logs'''

from django.urls import path
from . import views
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # Details page for a single topic
    path('topics/<topic_id>/', views.topic, name='topic')
]
