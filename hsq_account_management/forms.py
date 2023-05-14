from django import forms
class MuneForm(forms.Form):
   email = forms.CharField(required=True, max_length=10,error_messages={'required':'邮件不能为空','max_length':'不能超过10个字符'})
   password=forms.CharField(required=True, max_length=10,error_messages={'required':'密码不能为空','max_length':'不能超过10个字符'})
   def clean(self):
       email = self.cleaned_data.get('email')
       password = self.cleaned_data.get('password')
       return self.cleaned_data
