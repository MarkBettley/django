from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
    )

    password_confirmation = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get(
            "password_confirmation"
        )

        if password != password_confirmation:
            self.add_error(
                "password_confirmation",
                "Las contraseñas no coinciden.",
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user
