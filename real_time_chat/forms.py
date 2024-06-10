from django import forms
from .models import GroupMessage, ChatGroup
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple
from account.models import Account

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

class NewGroupForm(forms.ModelForm):
    
    class Meta:
        model = ChatGroup
        fields = ['group_name', 'group_photo']

        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group_photo': forms.FileInput(attrs={'class': 'form-control'})
        }
        

class EditGroupForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Account.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Remove Members"
    )

    class Meta:
        model = ChatGroup
        fields = ['group_name', 'group_photo', 'members']
        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditGroupForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['members'].queryset = self.instance.members.all()
            self.fields['members'].initial = self.instance.members.all()
            
            # Set the admin user ID to be used in the template
            self.admin_user_id = self.instance.admin.id if self.instance.admin else None
            self.initial_members_ids = [user.id for user in self.instance.members.all()]

    def clean_members(self):
        members = self.cleaned_data.get('members')
        if self.instance and self.instance.admin:
            admin_user = self.instance.admin
            members = list(members)
            if admin_user not in members:
                members.append(admin_user)
        return members