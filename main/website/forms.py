from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Vaše ime",
            "class": "bg-gray-100 text-gray-800 w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Vaš email",
            "class": "bg-gray-100 text-gray-800 w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Vaša poruka...",
            "rows": 4,
            "class": "bg-gray-100 text-gray-800 w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none"
        })
    )
