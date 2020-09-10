from rest_framework import serializers
from .models import ParliamentMember


class ParliamentMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParliamentMember
        fields = "__all__"
