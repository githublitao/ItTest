import logging
import os
import time
from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import StreamingHttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from blackList.api_response import JsonResponse
from blackList.models import FeedBack
from blackList.serializers import FeedBackSerializer, FeedBackDeserializer
logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


class InterView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        """
        获取面试反馈列表
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
            obi = FeedBack.objects.filter(status=True).filter(CompanyName__contains=name).order_by("-id")
        else:
            obi = FeedBack.objects.filter(status=True).order_by("-id")
        paginator = Paginator(obi, page_size)  # paginator对象
        total = paginator.num_pages  # 总页数
        try:
            obm = paginator.page(page)
        except PageNotAnInteger:
            obm = paginator.page(1)
        except EmptyPage:
            obm = paginator.page(paginator.num_pages)
        serialize = FeedBackSerializer(obm, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  "page": page,
                                  "total": total
                                  }, code="999999", msg="成功")

    def post(self, request):
        """
        添加面试反馈信息
        :param request:
        :return:
        """
        data = JSONParser().parse(request)
        data["InterviewTime"] = datetime.strptime(data["InterviewTime"], "%Y-%m-%d %H:%M:%S")
        feed_serializer = FeedBackDeserializer(data=data)
        if feed_serializer.is_valid():
            # 保持新项目
            feed_serializer.save()
            return JsonResponse(code="999999", msg="成功")
        return JsonResponse(code="999998", msg="参数有误")


class FilePost(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        _file = request.FILES.get("file")
        if not _file:
            return JsonResponse(code="999998", msg="参数有误")
        file_to_save = open(os.path.join("../data", str(int(time.time()))+_file.name), "wb+")
        for chunk in _file.chunks():
            file_to_save.write(chunk)
        file_to_save.close()
        return JsonResponse(code="999999", msg="成功", data="../data/"+str(int(time.time()))+_file.name)


def download_doc(request):
    url = request.GET.get("url")
    if not url:
        return JsonResponse(code="999999", msg="参数有误")

    def file_iterator(_file, chunk_size=512):
        while True:
            c = _file.read(chunk_size)
            if c:
                yield c
            else:
                break
    layout = url.split(".")[-1]
    file_name = str(int(time.time())) + "." + layout
    _file = open(url, "rb")
    response = StreamingHttpResponse(file_iterator(_file))
    response["Content-Type"] = "application/octet-stream"
    response["Content-Disposition"] = "attachment;filename=\"{0}\"".format(file_name)
    return response
