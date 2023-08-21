# from rest_framework import serializers
from .models import Tickets


from rest_framework import serializers
from datetime import timedelta

class TicketsSerializer(serializers.ModelSerializer):
    created_at_ist = serializers.SerializerMethodField()
    updated_at_ist = serializers.SerializerMethodField()

    class Meta:
        model = Tickets
        fields = '__all__'

    def get_created_at_ist(self, instance):
        return self.convert_utc_to_ist(instance.created_at)

    def get_updated_at_ist(self, instance):
        return self.convert_utc_to_ist(instance.updated_at)

    def convert_utc_to_ist(self, utc_timestamp):
        ist_offset = timedelta(hours=5, minutes=30)
        ist_timestamp = utc_timestamp + ist_offset
        return ist_timestamp.strftime("%Y-%m-%d %H:%M:%S %Z")
