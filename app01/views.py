from django.shortcuts import render, HttpResponse
from app01 import models


# Create your views here.


def test(request):
    obj = models.DegreeCourse.objects.filter(title='python').first()
    # print(obj)
    models.PricePolicy.objects.create(price=9.9, period=30, content_object=obj)
    obj = models.Course.objects.filter(title='restful').first()
    # print(obj)
    models.PricePolicy.objects.create(price=1.9, period=10, content_object=obj)

    course = models.Course.objects.filter(id=1).first()
    price_policys = course.price_policy_list.all()
    print(price_policys)
    return HttpResponse('ok')


def service(request):
    if request.method == 'OPTIONS':
        print('ok')
        obj = HttpResponse()
        obj['Access-Control-Allow-Headers'] = 'k1'
        obj['Access-Control-Allow-Methods'] = 'PUT'
    else:
        v1 = request.GET.get('v1')
        v2 = request.GET.get('v2')
        result = v1 + v2
        obj = HttpResponse(result)
        obj['Access-Control-Allow-Origin'] = 'http://localhost:63342,http://localhost:63343'
    obj['Access-Control-Allow-Origin'] = '*,'
    return obj
