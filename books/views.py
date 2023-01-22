from django.shortcuts import render
from django.http import HttpResponse as HR
from mysite.forms import LoginForm as LF

# Create your views here.
def search_form(request):
    return render(request,'search_form.html')

def search(request):
    if 'txt1' in request.GET:
        message = f'<h1>GET Data => {request.GET["txt1"]}</h1>'
    else :
        message = 'You submitted an empty form'
    return HR(message)

def current_page(request):
    inputD = ''
    if request.method == 'POST':
        inputD = request.POST['txt']
    else :
        inputD = None
    contexts = {'inputData':None}
    contexts['inputData'] = inputD
    return render(request,'cur_page.html',contexts)

def login(request):
    inputD = []
    if request.method == 'POST':
        form = LF(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            inputD.append(request.POST['iD'])
            inputD.append(request.POST['pW'])
    else :
        form = LF(initial={'iD':'','pW':''})
        inputD = None
    contexts = {'inputData':None,'form':form}
    contexts['inputData'] = inputD
    return render(request,'login.html',contexts)

def debug(request):
    return HR('<h1>추가된 페이지</h1>')

from django.db import connection
def custom_sql():
    try:
        cur = connection.cursor()
        cur.execute("SELECT * FROM books_publisher WHERE country = %s",['Korea'])
        connection.commit()

        rows = cur.fetchall()

        connection.close()
        return rows
    except:
        connection.rollback()
        print('Query is Failed')