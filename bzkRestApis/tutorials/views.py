import django_filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer


class TutorialsView(ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    pagination_class = PageNumberPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['level', 'title', 'published']

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Tutorial.objects.all()
    #     # title = self.request.query_params.get('title', None)
    #     # if title is not None:
    #     #     queryset = queryset.filter(title__startswith=title)
    #     return queryset


class TutorialDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TutorialSerializer

    def get_queryset(self):
        return Tutorial.objects.filter(id=self.kwargs.get('pk'))
