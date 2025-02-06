from django import forms

class JobApplicationForm(forms.Form):
    JOB_TYPES = (
        (None, '--Please choose--'),
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('contract_work', 'Contract work')
    )

    days = (
        ('monday', 'MON'),
        ('tuesday', 'TUES'),
        ('wednesday', 'WED'),
        ('thursday', 'THU'),
        ('friday', 'FRI'),
        ('saturday', 'SAT'),
        ('sunday', 'SUN')
    )

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    employment_type = forms.ChoiceField(choices= JOB_TYPES)
    start_date = forms.DateField(
        help_text='The earliest date you can start working.'
    )
    available_days = forms.MultipleChoiceField(
        choices= days, 
        help_text='Select all days that you can work.'
    )
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )