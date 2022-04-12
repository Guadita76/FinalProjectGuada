from django import forms


class StudentsForms (forms.Form):
    
    
    name= forms.CharField (max_length=40)

    last_name= forms.CharField(max_length=40)

    address= forms.CharField (max_length=50)
    
    
class PersonalDataForms (forms.Form):
    
    age= forms.CharField()

    height= forms.CharField()

    weight= forms.CharField()

    preexisting_condition= forms.CharField (max_length=50)
    
    

class AdditionalDataForms (forms.Form):
    
    extra_activities= forms.CharField (max_length=50)

    training_style= forms.CharField (max_length=50)

    proposed_objectives= forms.CharField (max_length=50)