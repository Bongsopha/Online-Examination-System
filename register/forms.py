from django import forms

from .models import Image
from .models import Register
from .models import *
from django.contrib.auth.models import User

# # class RegisterForm(forms.ModelForm):
# # 	class Meta:
# # 		model = Register
# # 		fields = ['firstname','email','lastname','phonenumber','country']
# # 		#exclude =['email']
		
class UploadFileForm(forms.ModelForm):
   class Meta:
   	model = Image
   	fields = ['file']

# class UserForm(forms.ModelForm):
#    class Meta:
#         model = User
#         fields = ('email',)
#    def clean_email(self):
#         # Get the email
#         email = self.cleaned_data.get('email')

#         # Check to see if any users already exist with this email as a username.
#         try:
#             match = User.objects.get(email=email)
#         except User.DoesNotExist:
#             # Unable to find a user, this is fine
#             return email

#         # A user was found with this as a username, raise an error.
#         raise forms.ValidationError('This email address is already in use.')

class FileUpload(forms.ModelForm):
	class Meta:
   		model = Register
   		fields = ('email','lastname','phonenumber','country','image','file','sname','address','city','birthday')
