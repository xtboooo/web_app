from django.shortcuts import render
from django.views import View
from booktest.models import HeroInfo, BookInfo
from django.http import JsonResponse
import json


class HeroListView(View):
    """ 英雄列表 获取 新增 视图 """

    def get(self, request):
        """ 获取所有的英雄人物数据 """
        heros_list = []
        heros = HeroInfo.objects.all()
        for hero in heros:
            hero_dict = {
                "id": hero.id,
                "hname": hero.hname,
                "hgender": hero.hgender,
                "hcomment": hero.hcomment,
                "hbook": hero.hbook.btitle,
                "hbook_id": hero.hbook_id,
            }
            heros_list.append(hero_dict)
        response_dict = {"code": 0,
                         "message": "OK",
                         "heros": heros_list
                         }
        return JsonResponse(response_dict)

    def post(self, request):
        """ 新增一个英雄人物数据 """
        req_dict = json.loads(request.body)
        hname = req_dict.get("hname")
        hgender = req_dict.get("hgender")
        hcomment = req_dict.get("hcomment")
        hbook_id = req_dict.get("hbook_id")
        hero = HeroInfo.objects.create(hname=hname, hgender=hgender, hcomment=hcomment, hbook_id=hbook_id)
        print(f'hero:{hname}')
        response_dict = {
            "code": 0,
            "message": "OK",
            "hero": {
                "id": hero.id,
                "hname": hname,
                "hgender": hgender,
                "hcomment": hcomment,
                "hbook": hero.hbook.btitle,
                "hbook_id": hero.hbook_id,
            }
        }
        return JsonResponse(response_dict)


class HeroDetailView(View):
    """ 英雄详情 获取 修改 删除 视图"""

    def get(self, request, id):
        """ 获取指定的英雄人物数据(根据英雄ID) """
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            fail_response_dict = {
                "code": 1,
                "message": f"id为{id}的英雄不存在"
            }
            return JsonResponse(fail_response_dict)
        else:
            success_response_dict = {
                "code": 0,
                "message": "OK",
                "hero": {
                    "id": hero.id,
                    "hname": hero.hname,
                    "hgender": hero.hgender,
                    "hcomment": hero.hcomment,
                    "hbook": hero.hbook.btitle,
                    "hbook_id": hero.hbook_id,
                }
            }
            return JsonResponse(success_response_dict)

    def put(self, request, id):
        """ 修改指定的英雄人物数据(根据英雄ID) """
        try:
            hero = HeroInfo.objects.get(id=id)

        except HeroInfo.DoesNotExist:
            fail_response_dict = {
                "code": 1,
                "message": f"id为{id}的英雄不存在"
            }
            return JsonResponse(fail_response_dict)
        else:
            req_dict = json.loads(request.body)
            hero.hname = req_dict.get("hname")
            hero.hgender = req_dict.get("hgender")
            hero.hcomment = req_dict.get("hcomment")
            hero.hbook_id = req_dict.get("hbook_id")
            hero.save()
            success_response_dict = {
                "code": 0,
                "message": "OK",
                "hero": {
                    "id": hero.id,
                    "hname": hero.hname,
                    "hgender": hero.hgender,
                    "hcomment": hero.hcomment,
                    "hbook": hero.hbook.btitle,
                    "hbook_id": hero.hbook_id,
                }
            }
            return JsonResponse(success_response_dict)

    def delete(self, request, id):
        """ 删除指定的英雄人物数据(根据英雄ID) """
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            fail_response_dict = {
                "code": 1,
                "message": f"id为{id}的英雄不存在"
            }
            return JsonResponse(fail_response_dict)
        else:
            success_response_dict = {
                "code": 0,
                "message": "OK",
            }
            hero.delete()
            return JsonResponse(success_response_dict)
