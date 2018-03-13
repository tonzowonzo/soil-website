from django import forms

# Form for contact view.
class ContactForm(forms.Form):
    
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
    
    def cleaned_message(self):
        
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words <= 4:
            # Raise an error if there are less than 5 words in the message.
            raise forms.ValidationError('Please enter 5 or more words.')
        return message

    
    