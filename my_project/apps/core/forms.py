from django import forms


class TextForm(forms.Form):
    text_field = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your text here"}
        ),
    )
