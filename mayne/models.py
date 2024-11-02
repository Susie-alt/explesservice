from django.db import models

# Create your models here.

class Delivery(models.Model):
    tracking_number = models.CharField(max_length=200)
    sender = models.CharField(max_length=300)
    receiver = models.CharField(max_length=300)

    origin = models.CharField(max_length=400)
    order_date = models.CharField(max_length=100)
    order_status = models.BooleanField(default=False)

    shipment_location = models.CharField(max_length=400)
    shipment_date = models.CharField(max_length=100)
    shipment_status = models.BooleanField(default=False)

    delivery_destination = models.CharField(max_length=400)
    delivery_date = models.CharField(max_length=100)
    delivery_status = models.BooleanField(default=False)


    def __str__(self):
        return self.tracking_number

    def __str__(self):
        return self.sender

    def __str__(self):
        return self.receiver

    def __str__(self):
        return self.origin

    def __str__(self):
        return self.order_date

    def __str__(self):
        return self.shipment_location

    def __str__(self):
        return self.shipment_date

    def __str__(self):
        return self.delivery_destination

    def __str__(self):
        return self.delivery_date


class PotCovers(models.Model):
    epot_cover = models.CharField(max_length=300)
    ppot_cover = models.CharField(max_length=300)

    def __str__(self):
        return self.epot_cover

    def __str__(self):
        return self.ppot_cover