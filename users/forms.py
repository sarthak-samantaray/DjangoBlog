from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

# Create a class that will inherit the UserCreationForm class.

class UserRegistrationForm(UserCreationForm):

    # adding an email field.

    email = forms.EmailField() # By default the parameter is required=True

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    # This is a complete form , 
    # and now we will import this in views.py/users, and we will no longer use the default form.


# create  a new form , that will update the user model

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


# Now we can create the profile form.

class ProfileUpdateForm(forms.ModelForm):
    # we don;t need any additional fields. so  we can jump to class meta:

    class Meta:
        model = Profile
        fields=['image']

# lets add these forms to profile view.