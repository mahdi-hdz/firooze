from rest_framework import serializers
from . import models

class SendMessageSerializer(serializers.Serializer):
    senderName = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)
    senderEmail = serializers.EmailField(allow_null=False, allow_blank=False)
    message = serializers.CharField(max_length=400, allow_null=False, allow_blank=False)


class EditDebtSerializer(serializers.Serializer):
    debtList = serializers.ListField()



class SubmitPostSerializer(serializers.Serializer):
    title = serializers.CharField(allow_null=False, allow_blank=False)
    content = serializers.CharField(allow_null=False, allow_blank=False)


class DeletePostSerializer(serializers.Serializer):
    id = serializers.CharField(allow_null=False, allow_blank=False)


class EditPostAdminSerializer(serializers.Serializer):
    id = serializers.CharField(allow_null=False, allow_blank=False)
    title = serializers.CharField(allow_null=False, allow_blank=False)
    content = serializers.CharField(allow_null=False, allow_blank=False)


class GetDebtSerialiser(serializers.Serializer):
    block = serializers.CharField(max_length=3, allow_null=False, allow_blank=False)
    floor = serializers.IntegerField(allow_null=False, required=True)
    unit = serializers.IntegerField(allow_null=False, required=True)
