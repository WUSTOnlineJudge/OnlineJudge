from rest_framework import serializers
from .models import Problem
from account.models import User
from json import loads


class ProblemListCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=User.objects.all())

    class Meta:
        model = Problem
        fields = ('display_id', 'author', 'title', 'is_public', 'description', 'hint', 'samples', 'test_case',
                  'create_time', 'last_update_time', 'time_limit', 'memory_limit', 'submission_number', 'ac_number')

        extra_kwargs = {
            'is_public': {'write_only': True},
            'test_case': {'write_only': True},
            'description': {'write_only': True},
            'hint': {'write_only': True},
            'time_limit': {'write_only': True},
            'memory_limit': {'write_only': True},
            'samples': {'write_only': True},
            'create_time': {"read_only": True},
            'last_update_time': {"read_only": True},
        }

    @staticmethod
    def test_case(input_case):
        try:
            json_parse = loads(input_case)
            if type(json_parse) != list:
                raise serializers.ValidationError(f"测试用例要求list, 但是给了{type(json_parse)}")
            if len(json_parse) == 0:
                raise serializers.ValidationError(f"测试用例长度不能为0")
            for i in json_parse:
                if "input" not in i or "output" not in i:
                    raise serializers.ValidationError(f"测试用例必须包括input和output")
            return input_case
        except serializers.ValidationError:
            raise
        except Exception:
            raise serializers.ValidationError("样例格式错误!")

    def validate_samples(self, samples):
        return self.test_case(samples)

    def validate_test_case(self, test_case):
        return self.test_case(test_case)

    def save(self, **kwargs):
        attr = self.validated_data
        Problem.objects.create(
            display_id=attr['display_id'],
            is_public=attr['is_public'],
            title=attr['title'],
            author=User.objects.all()[0],
            description=attr['description'],
            hint=attr['hint'],
            samples=attr['samples'],
            test_case=attr['test_case'],
            time_limit=attr['time_limit'],
            memory_limit=attr['memory_limit']
        )


class ProblemRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('display_id', 'title', 'description', 'hint', 'description_input', 'description_output', 'source',
                  'create_time', 'last_update_time', 'time_limit', 'memory_limit', 'samples',
                  'submission_number', 'ac_number', 'wa_number', 'tle_number', 'mle_number', 're_number', 'ce_number')
