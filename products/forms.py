from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductTag


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    main_image = forms.ImageField(
        label="Main Image", required=False, widget=CustomClearableFileInput
    )

    # Override the init method to make a couple of changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # Create a list of tuples
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Update the category field on the form to use the friendly names
        # for choices instead of the id.
        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            # Add styling so it matches the Dargan Health Foods theme
            field.widget.attrs["class"] = "rounded-0"


class ProductAndTagsForm(forms.ModelForm):
    class Meta:
        model = ProductTag
        exclude = ()


ProductAndTagsInlineFormSet = forms.inlineformset_factory(
    Product, ProductTag, form=ProductAndTagsForm, extra=3, can_delete=True)
