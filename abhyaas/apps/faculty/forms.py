from django import forms
from courses.models import CourseFacultyMap

class NotificationForm(forms.Form):
	iquery=CourseFacultyMap.objects.all().values_list('course__course_code',flat=True)
	iqueryname=CourseFacultyMap.objects.all().values_list('course__course_name',flat=True)
	i=0
	iquery_choices = []
	while (i<len(iquery)):
		iquery_choices=iquery_choices+[(str(iquery[i]),str(iquery[i])+" "+str(iqueryname[i]))]
		i=i+1
	send_to = forms.ChoiceField(choices=iquery_choices)

	def __init__(self ,*args, **kwargs):
		self.user=kwargs.pop('user', None)
		super(NotificationForm, self).__init__(*args, **kwargs)
		iquery=CourseFacultyMap.objects.filter(faculty=self.user).values_list('course__course_code',flat=True)
		iqueryname=CourseFacultyMap.objects.filter(faculty=self.user).values_list('course__course_name',flat=True)
		i=0
		iquery_choices = []
		while (i<len(iquery)):
			iquery_choices=iquery_choices+[(str(iquery[i]),str(iquery[i])+" "+str(iqueryname[i]))]
			i=i+1
		self.fields['send_to'] = forms.ChoiceField(choices=iquery_choices)
		#print CourseFacultyMap.objects.filter(faculty=fac_user).values_list('course__course_code',flat=True)
		#print [definition.encode("utf8") for definition in CourseFacultyMap.objects.filter(faculty=fac_user).values_list('course__course_code',flat=True)]
	message = forms.CharField(widget=forms.Textarea)        