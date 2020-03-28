from rest_framework import serializers
from . models import members,active_periods

class member_ser(serializers.modelserializers):
    class Meta:
        model = members,active_periods
        fields=['user_id','real_name','location','start_time','end_time']

class activity_ser(serializers.ModelSerializer):
    member= member_ser(required=True)
    class Meta:
        model = active_periods
        fields=['start_time','end_time','member']

    def create(self, validated_data):
        user_data = validated_data.pop('member')
        member = member_ser.create(member_ser(), validated_data=user_data)
        employee, created = activity_ser.objects.update_or_create(member=member,
                                                                start_time=validated_data.pop('start_time'),
                                                                 end_time=validated_data.pop('end_time'))
        return employee