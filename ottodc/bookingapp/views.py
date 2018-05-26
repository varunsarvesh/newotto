from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .functions import get_order_page_context, excel_extraction, import_dealers


class OrderPage(View):

    @staticmethod
    def express(request):
        context = get_order_page_context()
        return render(request=request, template_name="OrderForms/ExpressForm.html", context=context)

    @staticmethod
    def normal(request):
        context = get_order_page_context()
        return render(request=request, template_name="OrderForms/NormalForm.html", context=context)


class LoginPage(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="OrderForms/index.html")


class AdminPanel(View):

    @staticmethod
    def get(request):
        return render(request=request, template_name="AdminPanel/index.html")


class Master(View):

    @staticmethod
    def dealer_import_form(request):
        return render(request=request, template_name="Master/import_dealer.html")

    @staticmethod
    def dealer_import(request):
        if request.method == 'POST':
            field_name_in_form = 'excel'
            file = request.FILES[field_name_in_form]
            dealer_detail = excel_extraction(file)
            print(dealer_detail)
        return HttpResponse('uploaded')