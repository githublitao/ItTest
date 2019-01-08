# -*- coding: utf-8 -*-

# @Time    : 2018/12/29 15:46

# @Author  : litao

# @Project : ItTest

# @FileName: TestApi.py

# @Software: PyCharm
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from blackList.api_response import JsonResponse

_dict = {"DogAdmin": "阿杰", "Speciality": "女装", "GayFriend": "老学委"}


class TestApi(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        value = request.GET.get("test", "GayFriend")
        try:
            _dict.pop(value)
        except KeyError:
            pass
        return JsonResponse(data=_dict, code="999999", msg="虽然我是get，但只要我想也可以删除数据, 传递test=key试试")

    def post(self, request):
        data = JSONParser().parse(request)
        try:
            _dict["GayFriend"] = data["GayFriend"]
        except KeyError:
            pass
        return JsonResponse(data=_dict, code="999999", msg="虽然我是post，但只要我想也可以修改数据，试试修改基友")

    def put(self, request):
        JSONParser().parse(request)
        return JsonResponse(data=_dict, code="999999", msg="虽然我是put，但我也可以获取数据")

    def delete(self, request):
        value = request.GET.get("attribute", "成都测试群")
        _dict["attribute"] = value
        return JsonResponse(data=_dict, code="999999", msg="虽然我是delete，但我也可以添加数据，试试添加属性")
