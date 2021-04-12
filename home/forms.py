from django import forms


class ContactForm(forms.Form):
    """
    Form for Contact Us Page
    Sent with EmailJS
    """

    your_name = forms.CharField(
        label="Your name",
        max_length=100,
        required=True,
        )
    your_email = forms.EmailField(label="Your email", required=True)
    your_message = forms.CharField(
        label="Your message",
        widget=forms.Textarea(
            attrs={
                "rows": 8,
            },
        ),
        required=True,
        )

    class Meta:
        fields = [
            'your_name',
            'your_email',
            'your_message',
        ]

    # Override the init method to make a couple of changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields[field_name].widget.attrs.update({
                "placeholder": field.label,
                'class': "input-control"
            })
