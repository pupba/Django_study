from django.shortcuts import render
def hello(request): 
    contexts = {'name':'Pupbani','strings':['hello','good','bye']}
    return render(request,'index.html',contexts)

def inh(request):
    return render(request,'parent.html')
