from django import forms
from .models import Order

# OrderForm class taken from the Code Institute
# Boutique Ado walkthrough project:
# https://github.com/nualagr/boutique-ado-v1 - and then modified


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "street_address1",
            "street_address2",
            "town_or_city",
            "county",
            "postcode",
            "country",
            "phone_number",
        )

    # Override the init method of the form to enable customization
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # Call the default init method to set the default form up
        super().__init__(*args, **kwargs)
        # Create a dict of placeholders to populate the form fields
        # rather than using labels and empty boxes
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "town_or_city": "Town or City",
            "county": "County, State or Locality",
            "postcode": "Postal Code",
            "phone_number": "Phone Number",
        }
        # Set the cursor to the 'full_name' field when the page loads
        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                # Add an asterisk to the fields that are required
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                # Set the placeholder attributes to their respective values
                # in the dict above
                self.fields[field].widget.attrs["placeholder"] = placeholder
            # Add a CSS class we can use to style the inputs
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            # Remove the default labels
            self.fields[field].label = False
