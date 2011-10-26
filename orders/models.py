from django.db import models
from products.models import Product
from paypal.standard.ipn.signals import payment_was_successful

class Customer(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.email

    class Admin:
        list_display   = ('first_name', 'last_name', 'email')
        list_filter    = ('first_name', 'last_name')
        ordering       = ('-first_name',)
        search_fields  = ('first_name','last_name','email')

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    time_of_purchase = models.DateTimeField(auto_now_add=True)

    class Admin:
        list_display   = ('customer', 'product', 'time_of_purchase')
        list_filter    = ('customer', 'product')
        ordering       = ('-time_of_purchase',)
        search_fields  = ('customer','product')

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

payment_was_successful.connect(confirm_payment)
