from django import forms
from .models import DiscountCode


class DiscountCodeForm(forms.ModelForm):
    class Meta:
        model = DiscountCode
        fields = ['discount_code', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'discount_code': 'Promo Code',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add a CSS class we can use to style the inputs
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].label = False
