from django import forms

class CourseForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name of Course'
        self.fields['description'].label = 'Short Description'