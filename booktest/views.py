from django.shortcuts import render
from django.views import View
from booktest.models import HeroInfo, BookInfo
from django.http import JsonResponse
import json


class HeroListView(View):
    """ 英雄列表 获取 新增 视图 """

    def get(self, request):
        """ 英雄列表获取"""
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
        """ 英雄新增"""
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
        """ 获取指定英雄人物数据"""
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

    def put(self, request):
        pass

    def delete(self, request):
        pass
