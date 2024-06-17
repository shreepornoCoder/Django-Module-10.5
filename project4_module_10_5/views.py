from django.shortcuts import render
import datetime

def home(request):
    d = {"text":"", "lst":['Monday', 'Tuesday', 'Wednesday'], "date":datetime.datetime.now(), 'value':'20', 
        'name':'python', 'name_lst':"python is best", 'stu':[
        {'name': 'Josh', 'age': 19},
        {'name': 'Dave', 'age': 22},
        {'name': 'Joe', 'age': 31},
        ],
        'new_name':"SHREE"
    }

    return render(request, 'index.html', context=d)
