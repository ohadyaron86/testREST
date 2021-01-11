from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        # read_only_fields = ('is_staff', 'is_active', 'is_superuser')
        # test feeature
        extra_kwargs = {'password': {'write_only': True}
                        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        return user


