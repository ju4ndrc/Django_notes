from django.shortcuts import render

from my_fisrt_app.models import Author

# Create your views here.

def my_view(request):
    car_list=[
        {"title":"BWM"},
        {"title":"FORD"},
        {"title":"MAZDA"}

    ]

    context = {

        "car_list":car_list
    }
    return render(request, "my_fisrt_app/car_list.html",context)


def author_view(request,*args,**kwargs):
    print(args)
    print(kwargs)

    get_author = Author.objects.get(name=kwargs['name'])
    context={
        "author":get_author
    }
    return render(request, "my_fisrt_app/authors.html",context)