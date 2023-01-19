import datetime as dt
from django.http import HttpResponse as HR
def currentTime(request,offset):
    now = dt.datetime.now()
    html = """<html><body>
    <h1>It is now {0}</h1>
    <h1>Offset --> {1}</h1>
    </body></html>""".format(now,int(offset))
    return HR(html)

from django.template import Template, Context
from django.template.loader import get_template
def temp(request):
    t = get_template('include.html')
    contexts = {}
    return HR(t.render(contexts))

def condi1(request):
    html = """{% ifequal num1 num2 %} 
    <h1>참!</h1> 
    {% endifequal %}"""
    t = Template(html)
    c = Context({'num1':30,'num2':30})
    return HR(t.render(c))
def condi2(request):
    html = """{% if num < 10 %} 
    <h1>{{ num }}은 한자리 숫자{# 주석이용 #}</h1> 
    {% elif num >= 10 %}
    <h1>{{ num }}은 두자리 숫자{# 주석이용 #}</h1>
    {% endif %}"""
    t = Template(html)
    c = Context({'num':30})
    return HR(t.render(c))
def forloop(request):
    html = """{% for name in names%}
    <table border = 1>
    <tr><td>{{ forloop.counter }}</td>
    <td>{{ name }}</td></tr>
    </table>
    {% endfor %}"""
    t = Template(html)
    c = Context({'names':['Pupbani','Redbani','Yellbani']})
    return HR(t.render(c))
def filter1(request):
    html = '<h1>{{ name|upper }}</h1>'
    t = Template(html)
    return HR(t.render(Context({'name':'pupbani'})))
def allRequest(request):
    req = sorted(request.META.items())
    tmp = '\n'.join([f'<tr><td>{k}</td><td>{v}</td></tr>' for k,v in req])
    html = f'<table>{tmp}</table>'
    return HR(html)