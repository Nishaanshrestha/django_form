from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,required=True, error_messages={'required' : 'This field is required'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput,required=True, error_messages={'required' : 'This field is required'})

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,required=True, error_messages={'required' : 'This field is required'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput,required=True, error_messages={'required' : 'This field is required'})
    email = forms.EmailField(label = 'Email',required=True, error_messages={'required' : 'This field is required'})