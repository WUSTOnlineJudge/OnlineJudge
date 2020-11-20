from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter
from problem.serializers import ProblemCreateSerializer, ProblemListSerializer, ProblemRetrieveSerializer
from problem.models import Problem
from utils.pagination import StanderPageNumberPagination


class ProblemListCreateViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ProblemCreateSerializerMo


class ProblemReadOnlyViewSet(ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = Problem.objects.all().filter(is_public=True).order_by('create_time')
    pagination_class = StanderPageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('title',)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProblemListSerializer
        return ProblemRetrieveSerializer
