from django import forms
from .models import Profile,state_choices


gender_choices=[
    ('Male','Male'),
    ('female','female'),
    ('Other','Other')  ]


job_city_choices=[

    ('Bangalore','Bangalore'),  
    ('Chennai','Chennai'),
    ('Hyderabad','Hyderabad'),
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Pune','Pune'),
    ('Kolkata','Kolkata'),
    ('Other','Other')]

class ProfileForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        choices=job_city_choices,
        widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'})
    )
    class Meta:
        model = Profile
        fields = '__all__'
        labels={
            'dob':'Date of Birth',
            'pin':'Pin Code',
            'name':'Full Name',
            'mobile':'Mobile Number'}
        
        help_texts={
            'profile_image':'Optional:Upload your profile picture',
            'file':'Optional:Upload any supporting document(pdf,docx,txt)'}
        widgets={
            'dob':forms.DateInput(attrs={ 'class':'form-control','id':'datepicker','type':'date'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your full name'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your locality'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your city'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
                   
        }