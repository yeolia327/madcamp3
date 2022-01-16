from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .on_game_data import ingameOPGG


class main(APIView):
    def get(self, request):
        return render(request, "csgg/index.html")


class login(APIView):
    def get(self, request):
        return render(request, "csgg/login.html")


class signup(APIView):
    def get(self, request):
        return render(request, "csgg/signup.html")


class on_game(APIView):
    def post(self, request):
        userId = request.data.get('userId')
        userOnGameData = ingameOPGG(userId)
        print(userOnGameData)
        idlist = []
        champlist = []

        if (len(userOnGameData['Names']) == 0):
            print("게임중이 아닙니다")
        else:
            idlist = userOnGameData['Names']
            champlist = userOnGameData['Champions']
            imgList = userOnGameData['Champion Images']
            print(idlist)
            print(champlist)

        return Response(status=200, data=[idlist, champlist, imgList])
