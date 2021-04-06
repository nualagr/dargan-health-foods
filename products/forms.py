from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductTag, Tag


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


class ProductTagForm(forms.ModelForm):
    class Meta:
        model = ProductTag
        fields = "__all__"

    # Override the init method to change the tag field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tags = Tag.objects.all()
        # Create a list of tuples
        friendly_names = [(t.id, t.get_friendly_name()) for t in tags]
        # Add a blank option at the start of the list
        friendly_names.insert(0, ('', '---------'))
        full_choice_list = friendly_names

        # Update the tag field on the form to use the friendly names
        # for tags instead of the id.
        self.fields["tag"].choices = full_choice_list
        for field_name, field in self.fields.items():
            if field_name == "product":
                field.widget.attrs["class"] = "d-none"
            else:
                # Add styling so it matches the Dargan Health Foods theme
                field.widget.attrs["class"] = "product-tag-field"
