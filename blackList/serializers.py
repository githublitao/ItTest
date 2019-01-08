from rest_framework import serializers

from blackList.models import BlackList, FeedBack, LinksResources


class BlackListSerializer(serializers.ModelSerializer):
    """
    黑名单序列化
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = BlackList
        fields = ('id', 'CompanyName', 'CompanyAddress', 'ComplainData', 'createTime')


class BlackListDeserializer(serializers.ModelSerializer):
    """
    黑名单反序列化
    """
    class Meta:
        model = BlackList
        fields = ('CompanyName', 'CompanyAddress', 'ComplainData', 'createTime')


class FeedBackSerializer(serializers.ModelSerializer):
    """
    面试反馈序列化
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)
    InterviewTime = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = FeedBack
        fields = ('id', 'CompanyName', 'CompanyAddress', 'SalaryRange', 'InterviewTime', 'InterviewPost',
                  'InterviewNumb', 'CompanyImage', 'InterviewerImpression', 'InterviewerLong', 'outsourcing',
                  'outsourcingNature', 'WriteQuestion', 'CommunicationKey', 'InterviewSummaryToCompany', 'welfare',
                  'InterviewSummaryToPerson', 'createTime')


class FeedBackDeserializer(serializers.ModelSerializer):
    """
    面试反馈反序列化
    """
    WriteQuestion = serializers.CharField(allow_blank=True, allow_null=True, label='文件路径', max_length=1024, required=False)

    class Meta:
        model = FeedBack
        fields = ('CompanyName', 'CompanyAddress', 'SalaryRange', 'InterviewTime', 'InterviewPost',
                  'InterviewNumb', 'CompanyImage', 'InterviewerImpression', 'InterviewerLong', 'outsourcing',
                  'outsourcingNature', 'WriteQuestion', 'CommunicationKey', 'InterviewSummaryToCompany',
                  'InterviewSummaryToPerson', 'welfare')


class LinksResourcesSerializer(serializers.ModelSerializer):
    """
    资源链接序列化
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = LinksResources
        fields = ('id', 'links', 'password', 'remarks', 'createTime', 'status')


class LinksResourcesDeserializer(serializers.ModelSerializer):
    """
    资源链接反序列化
    """
    class Meta:
        model = LinksResources
        fields = ('links', 'password', 'remarks')
