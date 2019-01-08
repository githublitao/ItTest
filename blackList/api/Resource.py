import logging

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from blackList.api_response import JsonResponse
from blackList.models import LinksResources
from blackList.serializers import LinksResourcesSerializer, LinksResourcesDeserializer

logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


class Links(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        """
        获取资源链接列表
        :param request:
        :return:
        """
        try:
            page_size = int(request.GET.get("page_size", 20))
            page = int(request.GET.get("page", 1))
        except (TypeError, ValueError):
            return JsonResponse(code="999985", msg="page and page_size must be integer!")
        name = request.GET.get("name")
        if name:
            obi = LinksResources.objects.filter(status=True).filter(remarks__contains=name).order_by("-id")
        else:
            obi = LinksResources.objects.filter(status=True).order_by("-id")
        paginator = Paginator(obi, page_size)  # paginator对象
        total = paginator.num_pages  # 总页数
        try:
            obm = paginator.page(page)
        except PageNotAnInteger:
            obm = paginator.page(1)
        except EmptyPage:
            obm = paginator.page(paginator.num_pages)
        serialize = LinksResourcesSerializer(obm, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  "page": page,
                                  "total": total
                                  }, code="999999", msg="成功")

    def post(self, request):
        """
        添加资源链接
        :param request:
        :return:
        """
        data = JSONParser().parse(request)
        black_serializer = LinksResourcesDeserializer(data=data)
        if black_serializer.is_valid():
            # 保持新项目
            black_serializer.save()
            return JsonResponse(code="999999", msg="成功")
        return JsonResponse(code="999998", msg="参数有误")
