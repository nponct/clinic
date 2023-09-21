from rest_framework import serializers
from .import models


class DoctorSpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.DoctorSpecialty
        fields=('name')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Doctor
        fields=('lastname','spec')

class ClaimSerializer(serializers.ModelSerializer):
    total_count=serializers.IntegerField(default=0)
    class Meta:
        model=models.Claim
        fields=('nickname','doc','problem_description','visittime','otherdocs','total_count')

