from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import SubmissionModel
from utils.pagination import StanderPageNumberPagination
from .serializers import SubmissionCreateSerializer, SubmissionListSerializers


class SubmissionViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    queryset = SubmissionModel.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = StanderPageNumberPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return SubmissionCreateSerializer
        return SubmissionListSerializers
