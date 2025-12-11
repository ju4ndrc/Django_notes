from django.shortcuts import render

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