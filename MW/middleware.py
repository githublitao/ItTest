from blackList.api_response import JsonResponse
from django.core.cache import cache


class AaccessRestrictionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META['REMOTE_ADDR']  # 获取访问用户的ip
        if cache.has_key(ip):
            num = cache.get(ip)
            if num == 5:
                return JsonResponse(code="999997", msg="添加太频繁，请稍后添加")  # 返回响应
            else:
                cache.set(ip, num+1)
        else:
            cache.set(ip, 1, 60 * 60 * 24)
        response = self.get_response(request)
        return response
