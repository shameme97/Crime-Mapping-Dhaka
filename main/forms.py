from django import forms


report_stat_choices= [
    ('Reported', 'Reported'),
    ('Not Reported', 'Not Reported'),
    ]

crime_choices= [
	('Choose', 'Choose'),
    ('Assault', 'Assault'),
    ('Pick-pocketing', 'Pick-pocketing'),
    ('Vandalism', 'Vandalism'),
    ('Sexual-Harassment', 'Sexual-Harassment'),
    ('Mugging', 'Mugging'),
    ('Stalking', 'Stalking'),
    ('Kidnapping', 'Kidnapping'),
    ('Snatching', 'Snatching'),
    ('Household-Abuse', 'Household-Abuse'),
    ]


class CreatePost(forms.Form):
	email = forms.CharField(label="Email:", max_length=50)
	date = forms.DateField(label="Date of crime:")
	time = forms.TimeField(label="Time of crime:")
	nature = forms.CharField(label="Nature of crime:", max_length=50, widget=forms.Select(choices=crime_choices))
	area_name = forms.CharField(label="Area", max_length=150)
	location = forms.CharField(label="Location of crime:", max_length=100)
	report_status = forms.CharField(label="Report Status:", widget=forms.Select(choices=report_stat_choices))
	report_id = forms.CharField(label="Report ID:", required=False)
	description = forms.CharField(label="Description of crime:", widget=forms.Textarea(attrs={"rows":5, "cols":50}))

class PostComment(forms.Form):
	email = forms.CharField(label="Email:", max_length=50)
	post_id = forms.CharField(label="Post ID:", max_length=10)
	comment = forms.CharField(label="Comment:", widget=forms.Textarea(attrs={"rows":5, "cols":50}))
