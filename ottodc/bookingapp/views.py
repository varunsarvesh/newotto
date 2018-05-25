from django.shortcuts import render
from django.views.generic.base import View


class ExpressOrderPage(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="OrderForms/ExpressForm.html")


class NormalOrderPage(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="OrderForms/NormalForm.html")


class LoginPage(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="OrderForms/index.html")


class AdminPanel(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="AdminPanel/index.html")
