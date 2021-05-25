from django import forms
from .models import UserProfile
from allauth.account.forms import SignupForm


class DargansCustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove
        auto-generated labels and set autofocus
        on first field.
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "Town or City",
            "default_county": "County State or Locality",
            "default_postcode": "Postal Code",
        }
        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]}*"
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "profile-form-input"
            self.fields[field].label = False
