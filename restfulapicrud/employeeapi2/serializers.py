from rest_framework import serializers
from employeeapi2.models import Employee,PunchInOut

class employeeapi2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class PunchInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = PunchInOut
        fields = '__all__'
class displaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee,PunchInOut
        fields="__all__"
