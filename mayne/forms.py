from django import forms
from .models import Delivery


class CreateNewDelivery(forms.Form):
    tracking_number = forms.CharField(label="Tracking Number", max_length=200)
    sender = forms.CharField(label="Sender", max_length=300)
    receiver = forms.CharField(label="Receiver", max_length=300)

    origin = forms.CharField(label="Order Origin",  max_length=400)
    order_date = forms.CharField(label="Order Date", max_length=100)
    order_status = forms.BooleanField(label="Ordered")

    shipment_location = forms.CharField(label="Shipment Location", max_length=400, required=False)
    shipment_date = forms.CharField(label="Shipment Date", max_length=100, required=False)
    shipment_status = forms.BooleanField(label="Shipped", required=False)

    delivery_destination = forms.CharField(label="Delivery Destination", max_length=400, required=False)
    delivery_date = forms.CharField(label="Delivery Date", max_length=100, required=False)
    delivery_status = forms.BooleanField(label="Delivered", required=False)


class EditDelivery(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'