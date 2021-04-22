from django import forms
from profiles.models import UserProfile
from products.widgets import CustomClearableFileInput
from .models import BlogPost, BlogPostTag, BlogPostComment


class BlogPostForm(forms.ModelForm):
    """
    Create a form for Super Users to add Blog Posts
    """
    class Meta:
        model = BlogPost
        exclude = ("slug", "created_on", "updated_on", "author")

    main_image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    # Override the init method to make a couple of changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Add styling so it matches the Dargan Health Foods theme
            field.widget.attrs["class"] = "rounded-0"


class BlogPostAndTagsForm(forms.ModelForm):
    class Meta:
        model = BlogPostTag
        exclude = ()


BlogPostAndTagsInlineFormSet = forms.inlineformset_factory(
    BlogPost, BlogPostTag, form=BlogPostAndTagsForm, extra=3, can_delete=True)


class BlogPostCommentForm(forms.ModelForm):
    """
    Create a form for Dargan site members to add comments to Blog Posts.
    Add a placeholder and a css class and remove the auto-generated label.
    """
    class Meta:
        model = BlogPostComment
        exclude = ("blogpost", "user", "created_on")

    # Override the init method to make a couple of changes to the
    # 'content' field, the only field being displayed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].label = ""

        for field_name, field in self.fields.items():
            if field_name == "content":
                field.widget = forms.Textarea(
                    attrs={
                        "placeholder": "Share your thoughts here...",
                        "class": "rounded-0"}
                )
