from rest_framework import serializers


class TaskResultSerializer(serializers.Serializer):
    task_id = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()
    date_done = serializers.SerializerMethodField()
    traceback = serializers.SerializerMethodField()

    def get_task_id(self, obj):
        return obj.task_id

    def get_status(self, obj):
        return obj.status

    def get_result(self, obj):
        return obj.result

    def get_date_done(self, obj):
        return obj.date_done

    def get_traceback(self, obj):
        return obj.traceback
