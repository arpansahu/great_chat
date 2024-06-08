from django import forms
from .models import GroupMessage

class ChatMessageCreateForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add a message ...',
                'class': "form-control",
                'name': "message",
                'style': "border-radius: 0 0 12px 12px;",
                'maxlength': '300',
                'autofocus': 'True',
            }),
        }
        labels = {
            'body': '',  # This will remove the label text
        }