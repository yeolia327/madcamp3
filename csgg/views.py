from django.shortcuts import render
from rest_framework.views import APIView


class main(APIView):
    def get(self, request):
        return render(request, "csgg/index.html")
