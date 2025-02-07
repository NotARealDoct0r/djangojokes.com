from datetime import datetime
from django import forms

class JobApplicationForm(forms.Form):
    JOB_TYPES = (
        (None, '--Please choose--'),
        ('ft', 'Full-Time'),
        ('pt', 'Part-Time'),
        ('contract', 'Contract work')
    )

    DAYS = (
        ('1', 'MON'),
        ('2', 'TUES'),
        ('3', 'WED'),
        ('4', 'THU'),
        ('5', 'FRI'),
        ('6', 'SAT'),
        ('7', 'SUN')
    )

    YEARS = range(datetime.now().year, datetime.now().year+2)

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={'placeholder': 'https://www.example.com', 'size': '50'}
        )
    )
    employment_type = forms.ChoiceField(choices= JOB_TYPES)
    start_date = forms.DateField(
        help_text='The earliest date you can start working.',
        widget=forms.SelectDateWidget(
            years=YEARS
        )
    )
    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text='Check all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked':True}
        )
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'min':'10.00', 'max':'100.00', 'step':'.25'}
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'})
    )
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )