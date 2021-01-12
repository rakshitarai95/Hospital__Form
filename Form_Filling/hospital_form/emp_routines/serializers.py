from rest_framework import serializers
from .models import EmpRoutines
from rest_framework import status

# WEEKDAYS_DICT = {
#     0: "Sunday",
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
# }
# WEEKDAYS_DICT = {
#     "sunday",
#     "monday",
#     "tuesday",
#     "wednesday",
#     "thursday",
#     "friday",
#     "saturday",
# }

class EmpRoutinesListSerializer(serializers.ModelSerializer):
    # week_days = serializers.CharField(max_length=200, write_only= True)
    user_email = serializers.CharField(source='client.email', read_only = True)
    # weekdays = serializers.SerializerMethodField()
    weekdays_only = serializers.SerializerMethodField()

    # def get_weekdays(self, obj):
    #     days = None
    #     weekdays = []
    #     if obj.weekdays:
    #         days = obj.weekdays.split(",")
    #         for day in days:
    #             weekdays.append(WEEKDAYS_DICT[int(day)])
    #         days = ','.join(weekdays)
    #     return days

    def get_weekdays_only(self, obj):
        status = False
        if not ('sunday' in obj.weekdays.lower() or 'saturday' in obj.weekdays.lower()):
            status =True
        return status

    class Meta:
        model = EmpRoutines
        fields = ['start_date', 'arrival_time', 'departure_time', 'repeat', 'shift_availablity', 'weekdays',
                  'user_email', 'weekdays_only']


    def create(self, validated_data):
        validated_data['client'] = self.context['request'].user
        validated_data['weekdays'] = validated_data['weekdays'].title()
        emp_rout_obj = EmpRoutines(**validated_data)
        emp_rout_obj.save()
        return emp_rout_obj