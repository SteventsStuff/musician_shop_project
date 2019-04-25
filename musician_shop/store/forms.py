from django.forms import ModelForm

from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('content', 'comment_to')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('cust_first_name', 'cust_last_name', 'cust_address', 'cust_phone', 'cust_email', 'product')
