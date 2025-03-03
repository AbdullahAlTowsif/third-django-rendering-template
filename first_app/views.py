from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html', {'courses': [
        {
            'id': 1,
            'course': 'C',
            'teacher': 'Abdullah'
        },
        {
            'id': 2,
            'course': 'C++',
            'teacher': 'Al'
        },
        {
            'id': 3,
            'course': 'Python',
            'teacher': 'Towsif'
        }
    ]})
