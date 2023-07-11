from django import forms
def validate_for_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError("First letter should not be a")

def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('len is less than 5')

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    Sage=forms.IntegerField()