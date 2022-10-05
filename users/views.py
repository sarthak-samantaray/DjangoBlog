from django.shortcuts import render,redirect
from django.contrib import messages
#importing predined calsses that can turn into html files. FORMS
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# Creating a user registration route
def register(request):
    if request.method == 'POST':
        # Create a form with POST data.
        # The form will save the data as POST method so that it can be saved and used.
        form = UserRegistrationForm(request.POST)
        # If the data in the form is valid,
        if form.is_valid():
            # saving the user.
            form.save()
            # we will grab the valid username from the form.
            username = form.cleaned_data.get('username')
            # And then we will flash a message  by importing messages.
            messages.success(request,f'Account Created for { username }! You are now able to Log In')
            # And redirect the user to home page!.
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

# For adding the new forms we need to import those  forms.
# Profile route
# The user must be logged in to see this profile page.
# We use login required decorator
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account Has Been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form': u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)