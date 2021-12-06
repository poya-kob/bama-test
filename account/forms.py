from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
                               min_length=8)
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}), min_length=8)

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه عبور یکسان نیست')
        return password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
