from django import forms


class CommentForm(forms.Form):
    com_name = forms.CharField(widget=forms.TextInput(attrs={"id": "author","class":"form-control","required": "required","size": "25"}),
                               max_length=50,error_messages={"required":"username不能为空"})
    com_email = forms.EmailField(widget=forms.TextInput(attrs={"id": "email","type": "email", "class":"form-control","required": "required","size": "25"}),
                               max_length=50,error_messages={"required": "email不能为空"})
    com_content = forms.CharField(widget=forms.Textarea(attrs={"id": "comment", "class":"form-control","required": "required"}),
                              error_messages={"required": "评论不能为空"})
    article_id = forms.CharField(widget=forms.HiddenInput())