from django import forms
class MuneForm(forms.Form):
   email = forms.CharField(required=True, max_length=18,error_messages={'required':'邮件不能为空','max_length':'不能超过18个字符'})
   password=forms.CharField(required=True, max_length=10,error_messages={'required':'密码不能为空','max_length':'不能超过10个字符'})
   def clean(self):
       email = self.cleaned_data.get('email')
       password = self.cleaned_data.get('password')
       return self.cleaned_data
class RegisterForm(forms.Form):
   email = forms.CharField(required=True, max_length=18,error_messages={'required':'邮件不能为空','max_length':'不能超过18个字符'})
   password=forms.CharField(required=True, max_length=10,error_messages={'required':'密码不能为空','max_length':'不能超过10个字符'})
   repassword = forms.CharField(required=True, max_length=10,error_messages={'required': '再次输入密码不能为空', 'max_length': '不能超过10个字符'})
   mail_code=forms.CharField(required=True, min_length=4,max_length=4,error_messages={'required': '验证码不能为空', 'max_length': '4个字符','min_length':'4个字符'})
   def clean(self):
       email = self.cleaned_data.get('email')
       password = self.cleaned_data.get('password')
       repassword=self.cleaned_data.get('repassword')
       mail_code=self.cleaned_data.get('mail_code')
       return self.cleaned_data
