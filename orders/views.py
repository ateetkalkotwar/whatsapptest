from django.shortcuts import render



from .forms import OrderForm

from .whatsapp import (
    send_whatsapp_message
)


def place_order(request):

    if request.method == "POST":

        form = OrderForm(
            request.POST
        )

        if form.is_valid():

            order = form.save()

            message = f"""
🛒 NEW ORDER

Customer:
{order.customer_name}

Phone:
{order.phone}

Product:
{order.product}

Amount:
₹{order.amount}
"""

            # send_whatsapp_message(
            #     message
            # )

            return render(
                request,
                "success.html"
            )

    else:

        form = OrderForm()

    return render(
        request,
        "order_form.html",
        {
            "form": form
        }
    )
