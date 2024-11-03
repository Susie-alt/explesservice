from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Delivery, PotCovers
from .forms import CreateNewDelivery, EditDelivery
from django.contrib import messages
from django.contrib.messages.storage import default_storage
import time
from random import randint

# Create your views here.


def get_random_time():
    random_time = randint(5, 8)
    return random_time

def under_construction(request):
    messages.success(request, "Site maintenance ongoing... Limited functionality.", extra_tags='under_construction')
    return HttpResponseRedirect("/")


def check_delivery(response, id):
    de = Delivery.objects.get(id=id)

    context = {
        "de": de
    }

    return render(response, "mayne/delivery_flow.html", context)


def view(request):
    de = Delivery.objects.all()

    context = {
        "de": de
    }

    return render(request, "mayne/view.html", context)


def home(request):
    if request.method == "GET":
        user_tracking_number = request.GET.get('user_tracking_number')

        user_tracking_number = str(user_tracking_number)

        if user_tracking_number == 'None':
            print(user_tracking_number)
            return render(request, "mayne/home.html", {})
        else:
            try:
                delivery = Delivery.objects.get(tracking_number=user_tracking_number)
                return HttpResponseRedirect("/%i/check_delivery/" % delivery.id)
            except Delivery.DoesNotExist:
                messages.success(request, "No record found!", extra_tags='no_record')
                return HttpResponseRedirect("/")

    return render(request, "mayne/home.html", {})


def create(response):
    if response.method == "POST":

        delivery_form = CreateNewDelivery(response.POST)

        if delivery_form.is_valid():
            t = delivery_form.cleaned_data["tracking_number"]
            s = delivery_form.cleaned_data["sender"]
            r = delivery_form.cleaned_data["receiver"]

            o = delivery_form.cleaned_data["origin"]
            od = delivery_form.cleaned_data["order_date"]
            os = delivery_form.cleaned_data["order_status"]

            sl = delivery_form.cleaned_data["shipment_location"]
            sd = delivery_form.cleaned_data["shipment_date"]
            ss = delivery_form.cleaned_data["shipment_status"]

            dd = delivery_form.cleaned_data["delivery_destination"]
            dda = delivery_form.cleaned_data["delivery_date"]
            ds = delivery_form.cleaned_data["delivery_status"]

            delivery = Delivery(tracking_number=t, sender=s, receiver=r, origin=o, order_date=od, order_status=os,
                                shipment_location=sl, shipment_date=sd, shipment_status=ss, delivery_destination=dd,
                                delivery_date=dda, delivery_status=ds)

            if delivery.order_status is False:
                delivery.order_date = ""

                delivery.shipment_location = ""
                delivery.shipment_date = ""
                delivery.shipment_status = False

                delivery.delivery_destination = ""
                delivery.delivery_date = ""
                delivery.delivery_status = False

            elif delivery.order_status is True and delivery.shipment_status is False:

                delivery.shipment_location = ""
                delivery.shipment_date = ""

                delivery.delivery_destination = ""
                delivery.delivery_date = ""
                delivery.delivery_status = False

            elif delivery.order_status is True and delivery.shipment_status is True and delivery.delivery_status is False:
                delivery.delivery_destination = ""
                delivery.delivery_date = ""

            delivery.save()

            context = {"delivery_form": delivery_form
                       }

        return HttpResponseRedirect("/%i/check_delivery" %delivery.id, context)
    else:
        delivery_form = CreateNewDelivery()

        context = {"delivery_form": delivery_form,
                   }

    return render(response, "mayne/create.html", context)


def edit(request, id):
    delivery = Delivery.objects.get(id=id)

    if request.method == 'POST':
        edit_delivery_form = EditDelivery(request.POST, instance=delivery)

        if edit_delivery_form.is_valid():

            if delivery.order_status is False:
                delivery.order_date = ""

                delivery.shipment_location = ""
                delivery.shipment_date = ""
                delivery.shipment_status = False

                delivery.delivery_destination = ""
                delivery.delivery_date = ""
                delivery.delivery_status = False

            elif delivery.order_status is True and delivery.shipment_status is False:

                delivery.shipment_location = ""
                delivery.shipment_date = ""

                delivery.delivery_destination = ""
                delivery.delivery_date = ""
                delivery.delivery_status = False

            elif delivery.order_status is True and delivery.shipment_status is True and delivery.delivery_status is False:
                delivery.delivery_destination = ""
                delivery.delivery_date = ""

            edit_delivery_form.save()

            return redirect("view")

    else:
        edit_delivery_form = EditDelivery(instance=delivery)

    context = {'delivery': delivery,
               'edit_delivery_form': edit_delivery_form}

    return render(request, 'mayne/edit_delivery.html', context)


def delete_delivery(request, id):
    delivery = Delivery.objects.get(id=id)

    if request.method == 'POST':
        delivery.delete()
        return redirect("view")

    context = {
        "de": delivery
    }
    return render(request, "mayne/confirm_delete.html", context)


def get_updates(request, id):
    delivery = Delivery.objects.get(id=id)

    context = {
        "de": delivery
    }

    if request.method == "POST":
        e = request.POST.get('epot_cover')
        p = request.POST.get('ppot_cover')
        i = request.POST.get('ipot_cover')

        e = str(e)
        p = str(p)
        i = str(i)

        potcovers = PotCovers(epot_cover=e, ppot_cover=p, ipot_cover=i)

        potcovers.save()

        time.sleep(get_random_time())

        return render(request, "mayne/delivery_flow.html", context)

    return render(request, "mayne/get_status_update.html", context)


def pot_covers(request):
    pc = PotCovers.objects.all()

    context = {
        "pc": pc
    }
    return render(request, "mayne/pot_covers.html", context)
