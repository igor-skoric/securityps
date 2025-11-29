from django import forms
from .models import JobApplication


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


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = ["name", "email", "phone", "birth_year", "message", "cv"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full p-3 rounded bg-gray-700 text-white",
                "placeholder": "Unesite ime i prezime"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full p-3 rounded bg-gray-700 text-white",
                "placeholder": "Unesite email"
            }),
            "phone": forms.TextInput(attrs={
                "class": "w-full p-3 rounded bg-gray-700 text-white",
                "placeholder": "Unesite broj telefona"
            }),
            "birth_year": forms.NumberInput(attrs={
                "class": "w-full p-3 rounded bg-gray-700 text-white",
                "placeholder": "Godina rođenja"
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full p-3 rounded bg-gray-700 text-white h-32",
                "placeholder": "Zašto želite da radite kod nas?"
            }),
            "cv": forms.ClearableFileInput(attrs={
                "class": "w-full p-3 rounded bg-gray-700 text-white cursor-pointer"
            }),
        }

    def clean_cv(self):
        file = self.cleaned_data.get('cv')

        if not file:
            raise forms.ValidationError("Molimo postavite CV fajl.")

        allowed_extensions = ['pdf', 'doc', 'docx']
        ext = file.name.split('.')[-1].lower()

        if ext not in allowed_extensions:
            raise forms.ValidationError("CV mora biti PDF ili Word dokument (PDF, DOC, DOCX).")

        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError("CV može biti maksimalno 5MB.")

        return file
