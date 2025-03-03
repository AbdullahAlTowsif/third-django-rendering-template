from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html', {"name": "Abdullah Al Towsif", "marks": 98, "lst": [24, 4, 10, 5], "blog": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos rerum aliquid dolore laboriosam. Nam non voluptatibus reprehenderit fugiat, iusto magni!"})


# def contact(request):
#     return render(request, './first_app/index.html', {'courses': [
#         {
#             'id': 1,
#             'course': 'C',
#             'teacher': 'Abdullah'
#         },
#         {
#             'id': 2,
#             'course': 'C++',
#             'teacher': 'Al'
#         },
#         {
#             'id': 3,
#             'course': 'Python',
#             'teacher': 'Towsif'
#         }
#     ]})
