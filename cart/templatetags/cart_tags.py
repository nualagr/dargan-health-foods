from django import template

# Create a variable which is an instance
# of the template Library
register = template.Library()


# Use the register filter decorator to register
# the function as a template filter
@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity
