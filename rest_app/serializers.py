from rest_framework import serializers
from rest_app.models import FancyCat


class FancyCatListSerilizer(serializers.ModelSerializer):

    class Meta:
        model = FancyCat
        fields = ('id', 'name')

class FancyCatSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = FancyCat
        fields = ('__all__')

