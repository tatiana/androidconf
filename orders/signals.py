from models import Customer, Order
from products.models import Product

def confirm_payment(sender, **kwargs):
    # it's important to check that the product exists
    try:
        product = Product.objects.get(slug=sender.item_number)
    except Product.DoesNotExist:
        return
    # And that someone didn't tamper with the price
    if int(product.price) != int(sender.mc_gross):
        return
    # Check to see if it's an existing customer
    try:
        customer = Customer.objects.get(email=sender.payer_email)
    except Customer.DoesNotExist:
        customer = Customer.objects.create(
            email=sender.payer_email,
            first_name=sender.first_name,
            last_name=sender.last_name
        )
    # Add a new order
    Order.objects.create(customer=customer, product=product)

