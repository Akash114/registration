from rest_framework import serializers

from .models import Registration


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

