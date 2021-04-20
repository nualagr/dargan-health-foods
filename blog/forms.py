from django import forms

from .models import BlogPost
from products.widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):
    """
    Create a form for Super Users to add Blog Posts
    """
    class Meta:
        model = BlogPost
        exclude = ('slug', 'created_on', 'updated_on', 'author')

    main_image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    # Override the init method to make a couple of changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Add styling so it matches the Dargan Health Foods theme
            field.widget.attrs["class"] = "rounded-0"