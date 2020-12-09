from django import forms




class AnalyseForm(forms.Form):


    Fichier_AUDIO = forms.FileField()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     start = cleaned_data.get("Start_time_of_analysis")
    #     end = cleaned_data.get("End_time_of_analysis")
    #
    #     if start < datetime.datetime.strptime('9:30', '%H:%M').time() or end > datetime.datetime.strptime('15:55', '%H:%M').time():
    #         raise ValidationError( "Analysis time must be between 9:30 and 15:55" )
    #
    #     if start >= end:
    #         raise ValidationError( "Seems like times are switched." )


