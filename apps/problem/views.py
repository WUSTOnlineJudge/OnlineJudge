from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter
from problem.serializers import ProblemListCreateSerializer, ProblemRetrieveSerializer
from problem.models import Problem
from utils.pagination import StanderPageNumberPagination


class ProblemListCreateViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = ProblemListCreateSerializer
    queryset = Problem.objects.all().filter(is_public=True)
    pagination_class = StanderPageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('title',)


class ProblemRetrieveViewSet(RetrieveModelMixin, GenericViewSet):
    lookup_field = 'display_id'
    serializer_class = ProblemRetrieveSerializer
    queryset = Problem.objects.all().filter(is_public=True).order_by('create_time')
