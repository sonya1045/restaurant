from django import forms

class DishFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', "Усі страви"),
        ('first-dish', "Перші страви"),
        ('salad', "Салати"),
        ('dessert', "Десерти"),
        ('drinks', "Напої"),
    ]
   
    category = forms.ChoiceField(choices = STATUS_CHOICES, required=False, label='category')

