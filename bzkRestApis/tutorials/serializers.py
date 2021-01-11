from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'level',
                  'published')
        validators = [
            UniqueTogetherValidator(
                queryset=Tutorial.objects.all(),
                fields=['title', 'description']
            )
        ]
