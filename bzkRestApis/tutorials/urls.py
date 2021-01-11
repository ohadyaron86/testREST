from django.conf.urls import url
from rest_framework import routers

from .views import TutorialsView, TutorialDetailView

router = routers.SimpleRouter(trailing_slash=True)

urlpatterns = [
    url(r'^api/tutorials$', TutorialsView.as_view(), name='tutorials'),
    # url(r'^api/tutorials/$', TutorialsView.as_view(), name='tutorials'),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', TutorialDetailView.as_view(), name='tutorial_detail'),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
