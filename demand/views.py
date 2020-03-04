from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Demand
from .serializers import DemandSerializer
import os
import requests


class DemandViewSet(APIView):
    def get(self, request):
        page_size = 10
        if self.request.query_params.get('page_size'):
            page_size = self.request.query_params.get('page_size')
        demands = Demand.objects.all()
        serializer = DemandSerializer(demands, many=True)
        p = Paginator(serializer.data, page_size)
        try:
            response = p.page(self.request.query_params.get('page')).object_list
        except PageNotAnInteger:
            response = p.page(1).object_list
        except EmptyPage:
            response = p.page(1).object_list
        return Response(response, status=status.HTTP_200_OK)


def userlogin(request):
    template = 'login.html'
    data = {"title": "Login"}

    if request.method == 'POST':
        payload = {
            "username": request.POST['user'],
            "password": request.POST['pass']
        }

        re = requests.post('http://localhost:8000/dologin/', json=payload)
        dados = re.json()
        if re.status_code == 200:
            data = {"title": "Demandas", "token": dados['token']}
            template = 'lista-damandas.html'
        else:
            data['erro'] = 1

    try:
        user = User.objects.create_user(
            username=os.environ.get("USER_NAME", ""),
            password=os.environ.get("USER_PASS", ""),
            email=os.environ.get("USER_EMAIL", "")
        )
        user.save()
    except:
        print("usuario já criado")

    return render(request, template, data)
