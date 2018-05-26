import openpyxl
from bookingapp.models import Dealer


def get_order_page_context():
    context = {}
    context["Brand_id"] = 1
    context["Category_id"] = 1
    context["Brand_name"] = "OTTO"
    context["Category_name"] = "Formal Shirts"
    context["Dealer_id"] = 101
    context["Dealer_name"] = "Pothys, Chennai"
    return context


def excel_extraction(file: str):
    wb = openpyxl.load_workbook(file)
    header = []
    body = []
    first_row = 1
    sheet = wb.active
    for row in sheet:
        rows = []
        for ro in row:
            rows.append(ro.value)
        if first_row == 1:
            header.append(rows)
            first_row = 0
        else:
            body.append(rows)
    print(header)
    return body


def import_dealers(data: list):
    for row in data:
        name = row[0]
        place = row[1]
        gst = row[2]
        phone = row[3]
        email = row[4]
        site_code = row[5]
        temp = Dealer(Name=name, Place=place, GST=gst, Phone=phone, Email=email, Site_code=site_code)
        temp.save()
