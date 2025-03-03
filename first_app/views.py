from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html', context={'author': 'Phitron', 'age' : 22, 'marks' : 88})
