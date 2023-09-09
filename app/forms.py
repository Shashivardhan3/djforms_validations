from django import forms


def validation_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError("First letter should not be a")
def validation_for_length(value):
    if len(value)<=5:
        raise forms.ValidationError('length is less than 5')


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[validation_for_a,validation_for_length])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField()
    


