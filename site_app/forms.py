from django import forms
from site_app.models import Guest

class GuestForm(forms.ModelForm):

    class Meta():
        model = Guest
        fields = {'first_name','last_name', 'attending', 'meal_selection'}