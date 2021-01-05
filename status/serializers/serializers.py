from rest_framework import serializers
from ..models import Status


# serializer = SnippetSerializer(data=data)
# serializer.is_valid()
# # True
# serializer.validated_data
# # OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
# serializer.save()
# # <Snippet: Snippet object


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
