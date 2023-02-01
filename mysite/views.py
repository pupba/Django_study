from django.shortcuts import render
def hello(request): 
    contexts = {'name':'Pupbani','strings':['hello','good','bye']}
    return render(request,'index.html',contexts)

def inh(request):
    return render(request,'parent.html')

# make csv with Django

import csv
from django.http import HttpResponse as HR

def mkCSV1(request):
    response = HR(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=test.csv"

    wr = csv.writer(response)
    wr.writerow(['Frist Row','Foo','Bar','Cho'])
    wr.writerow(['Second Row','A','B','C','Testing'])
    
    return response

def mkCSV2(request):
    response = HR(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=test.csv"

    csv_data = (
        ('Frist Row','Foo','Bar','Cho'),
        ('Second Row','A','B','C','Testing')
    )
    return render(request,'csv2.html',{'data':csv_data})

def session1(request):
    # set session
    request.session['One'] = "hello1"
    request.session['Two'] = "hello2"
    request.session['Three'] = "hello3"
    
    # 5초뒤 만료
    request.session.set_expiry(5)
    html = f"""<h1>One : {request.session['One']}</h1>
    <h1>Two :{request.session['Two']}</h1>
    <h1>Three : {request.session['Three']}</h1>"""
    return HR(html)

def session2(request):
    # set session
    request.session['Two'] = "hello2"
    request.session['Three'] = {"ao":"hello","bo":"hello"}
    # 일반적인 변경
    request.session['Two'] = "bye..."
    # 명시적 변경
    request.session['Three']['ao'] = 'GoodBye~'
    request.session.modified = True

    two = request.session['Two'] 
    three = request.session['Three']
    return HR(f"<h1>Two : {two}</h1><h1>Three : {three}</h1>")