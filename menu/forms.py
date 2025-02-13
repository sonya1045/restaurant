from django import forms

class DishFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'all'),
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),]
   
    status = forms.ChoiceField(choices = STATUS_CHOICES, required=False, label='status')