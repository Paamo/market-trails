from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#Django comes with a pre-built register form called UserCreationForm that connects to the pre-built model User. 
# However, the UserCreationForm only requires a username and password (password1 is the initial password and password2 is the password confirmation).
# #To customize the pre-built form, first create a new file called forms.py in the app directory.
# Create your forms here.

class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

