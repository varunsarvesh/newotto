from django.shortcuts import render
from django.views.generic.base import View


class ExpressOrderPage(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="expressform.html")


class NormalOrderPage(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="normalform.html")
