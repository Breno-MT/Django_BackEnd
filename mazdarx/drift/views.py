from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
# Shortcut
from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    latest_car_list = Car.objects.order_by("-created_date")[:5]
    # template = loader.get_template("drift/index.html")
    # context = {
    #     "latest_car_list": latest_car_list
    # }
    # return HttpResponse(template.render(context, request))
    # Shortcut method
    context = {"latest_car_list": latest_car_list}
    return render(request, "drift/index.html", context)

def detail(request, car_id):
    return HttpResponse("You're looking at car %s." % car_id)


def results(request, car_id):
    response = "You're looking at the results of car %s."
    return HttpResponse(response % car_id)
