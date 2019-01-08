from django.contrib import admin

# Register your models here.
from django.template.defaultfilters import capfirst
from collections import OrderedDict as SortedDict

from blackList.models import BlackList, FeedBack, LinksResources


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        template_response = func(*args, **kwargs)
        for app in template_response.context_data['available_apps']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return template_response

    return inner


registry = SortedDict()
registry.update(admin.site._registry)
admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
admin.site.site_header = '成都软件测试'
admin.site.siteTitle = '成都软件测试'

display = ()


class BlackListForm(admin.ModelAdmin):
    search_fields = ('CompanyName', )
    list_display = ('id', 'CompanyName', 'CompanyAddress', 'ComplainData', 'status')
    list_display_links = ('id', 'CompanyName', 'CompanyAddress', 'status')
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('-id',)
    fieldsets = ([
        '黑名单', {
            'fields': ('CompanyName', 'CompanyAddress', 'ComplainData', 'status')
        }],
    )


admin.site.register(BlackList, BlackListForm)


class FeedBackForm(admin.ModelAdmin):
    search_fields = ('CompanyName', )
    list_display = ('id', 'CompanyName', 'CompanyAddress', 'InterviewTime', 'status', 'createTime')
    list_display_links = ('id', 'CompanyName', 'CompanyAddress', 'status')
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('-id',)
    fieldsets = ([
        '面试反馈', {
            'fields': ('CompanyName', 'CompanyAddress', 'SalaryRange', 'InterviewTime', 'InterviewPost',
                       'InterviewNumb', 'CompanyImage', 'InterviewerImpression', 'InterviewerLong', 'outsourcing',
                       'outsourcingNature', 'WriteQuestion', 'CommunicationKey', 'InterviewSummaryToCompany',
                       'InterviewSummaryToPerson', 'status')
        }],
    )


admin.site.register(FeedBack, FeedBackForm)


class LinksResourcesForm(admin.ModelAdmin):
    search_fields = ('remarks', )
    list_display = ('id', 'links', 'password', 'remarks', 'createTime', 'status')
    list_display_links = ('id', 'links', 'password', 'remarks', 'createTime', 'status')
    list_filter = ('status', )
    list_per_page = 20
    ordering = ('-id',)
    fieldsets = ([
        '资源链接', {
            'fields': ('links', 'password', 'remarks', 'status')
        }],
    )


admin.site.register(LinksResources, LinksResourcesForm)