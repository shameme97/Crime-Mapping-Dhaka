from django import forms


report_stat_choices= [
    ('Reported', 'Reported'),
    ('Not Reported', 'Not Reported'),
    ]


class CreatePost(forms.Form):
	email = forms.CharField(label="Email:", max_length=50)
	date = forms.DateField(label="Date of crime:")
	time = forms.TimeField(label="Time of crime:")
	nature = forms.CharField(label="Nature of crime:", max_length=50)
	area_name = forms.CharField(label="Area", max_length=150)
	location = forms.CharField(label="Location of crime:", max_length=100)
	# report_status = forms.BooleanField(label="Report Status:", required=False)
	report_status = forms.CharField(label="Report Status:", widget=forms.Select(choices=report_stat_choices))
	report_id = forms.CharField(label="Report ID:", required=False)
	description = forms.CharField(label="Description of crime:", max_length=200)
