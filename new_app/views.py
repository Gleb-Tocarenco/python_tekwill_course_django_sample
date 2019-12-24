from django.shortcuts import render
from time import sleep
from django.http import HttpResponse, FileResponse, JsonResponse, StreamingHttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_first_view(request):
    print(request.GET)
    print(request.path)
    return HttpResponse("Hello")

def date_view(request):
    now = datetime.now().strftime('%m-%d-%Y')
    return HttpResponse(now)

def days_until_new_year(request):
    days = (
        datetime.date(2019, 12, 31) - 
        datetime.date.today()
    ).days
    return HttpResponse(days)


def special_case_2003(request):
    print('--- 2003 ----')
    return HttpResponse('---- Year is 2003 ----')

def year_view(request, year):
    print(year)
    return HttpResponse(f'Year is {year}')

def month_view(request, year, month):
    return HttpResponse(f'Hello')

def article_detail(request, year, month, title):
    type_month = str(type(month))
    print(str(type_month))
    return HttpResponse(
        f"""Year is {year}, month is {month} type is {type_month},
            title is {title} type is {type(title)}"""
    )

def cat_image_view(request):
    return FileResponse(open('cat.jpg', 'rb'))

def cvs_file_view(request):
    return FileResponse(open('data.csv', 'rb'))

def json_view(request):
    return HttpResponse({'data': 'value'})


    
def streaming_writer(rows):
    yield 'Name, Age, Hobby\n'
    for row in range(rows):
        yield f'Name_{row}, Age_{row}, Hobby_{row}\n'

def streaming_view(request):
    response = StreamingHttpResponse(streaming_writer(1000000), content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    return response