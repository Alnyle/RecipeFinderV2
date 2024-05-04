from django import template

register = template.Library()


@register.filter(name='divisibleby')
def divisibleby(number, divisor):
    return number % divisor == 0
