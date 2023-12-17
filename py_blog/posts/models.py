from django.db import models
from django import forms

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        related_name="comments",
        on_delete=models.CASCADE,        
    )
    content = models.TextField("내용", default='')
    created = models.DateField("생성일시", auto_now_add=True)
    
class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("사진", upload_to="post")
    
class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
        
    )
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateField("생성일시", auto_now_add=True)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"placeholder": "댓글 달기. . ."}),
        }

    def __init__(self, *args, **kwargs):
        post_id = kwargs.pop("post_id", None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if post_id:
            # 수정된 부분: post_id를 사용하여 post 필드 초기값 설정
            self.fields["post"].initial = post_id
            self.fields["post"].widget = forms.HiddenInput()