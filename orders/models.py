from django.db import models


class Order(models.Model):

    customer_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    product = models.CharField(
        max_length=100
    )

    amount = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.customer_name