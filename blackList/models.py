from django.db import models

# Create your models here.


class BlackList(models.Model):
    """
    公司黑名单
    """
    id = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=128, verbose_name="公司名称")
    CompanyAddress = models.CharField(max_length=1024, verbose_name="公司地址")
    ComplainData = models.TextField(verbose_name="投诉内容")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    status = models.BooleanField(default=True, verbose_name="审核状态")

    def __unicode__(self):
        return self.CompanyName

    def __str__(self):
        return self.CompanyName

    class Meta:
        verbose_name = '公司黑名单'
        verbose_name_plural = '公司黑名单'


class FeedBack(models.Model):
    """
    面试反馈
    """
    id = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=128, verbose_name="公司名称")
    CompanyAddress = models.CharField(max_length=1024, verbose_name="公司地址")
    SalaryRange = models.CharField(max_length=1024, blank=True, null=True, verbose_name="薪资范围")
    InterviewTime = models.DateTimeField(max_length=50, verbose_name='面试时间')
    InterviewPost = models.CharField(max_length=50, verbose_name="面试岗位")
    InterviewNumb = models.CharField(max_length=50, blank=True, null=True, verbose_name="面试次数")
    CompanyImage = models.TextField(blank=True, null=True, verbose_name="公司印象")
    InterviewerImpression = models.TextField(blank=True, null=True, verbose_name="面试官印象")
    InterviewerLong = models.CharField(max_length=50, verbose_name="面试时长")
    outsourcing = models.BooleanField(default=False, verbose_name="是否外包")
    outsourcingNature = models.CharField(max_length=50, blank=True, null=True, verbose_name="外包性质",
                                         choices=(('人力外包', '人力外包'), ('项目外包', '项目外包')))
    WriteQuestion = models.FileField(upload_to='../data/', blank=True, null=True, verbose_name="笔试题")
    CommunicationKey = models.TextField(blank=True, null=True, verbose_name="沟通重点")
    InterviewSummaryToCompany = models.TextField(blank=True, null=True, verbose_name="总结/公司")
    InterviewSummaryToPerson = models.TextField(blank=True, null=True, verbose_name="总结/个人")
    welfare = models.CharField(max_length=1024, blank=True, null=True, verbose_name="公司福利")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    status = models.BooleanField(default=True, verbose_name="审核状态")

    def __unicode__(self):
        return self.CompanyName

    def __str__(self):
        return self.CompanyName

    class Meta:
        verbose_name = '面试总结'
        verbose_name_plural = '面试总结'


class LinksResources(models.Model):
    """
    资源链接
    """
    id = models.AutoField(primary_key=True)
    links = models.URLField(verbose_name="链接")
    password = models.CharField(blank=True, null=True, verbose_name="密码", max_length=50)
    remarks = models.CharField(max_length=50, verbose_name="内容")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    status = models.BooleanField(default=True, verbose_name="审核状态")

    def __unicode__(self):
        return self.remarks

    def __str__(self):
        return self.remarks

    class Meta:
        verbose_name = '资源链接'
        verbose_name_plural = '资源链接'
