from rest_framework import serializers
from .models import SubmissionModel
from problem.serializers import ProblemShortSerializer


class SubmissionCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, _):
        return self.context['request'].user

    @staticmethod
    def validate_lang(value):
        for lang in SubmissionModel.lang_choice:
            if lang[0] == value:
                return value
        raise serializers.ValidationError("Language not supported")

    class Meta:
        model = SubmissionModel
        fields = (
            'id',
            'user',
            'problem',
            'verdict',
            'language',
            'create_time',
            'time_spend',
            'memory_spend'
        )
        read_only_fields = (
            'create_time',
        )


class SubmissionListSerializers(serializers.ModelSerializer):
    problem = ProblemShortSerializer()

    class Meta:
        model = SubmissionModel
        fields = (
            'id',
            'problem',
            'verdict',
            'language',
            'create_time',
            'time_spend',
            'memory_spend'
        )
