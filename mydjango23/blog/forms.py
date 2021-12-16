import re

from django import forms
from blog.models import Post, Tag, Subscriber


class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=200)

    # 초기값지정
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            inital = ", ".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = inital

       #DB로 저장
        # 아래의 함수가 호출되기 전에, instance.save()가 호출되었음을 보장받는다
    def _save_m2m(self):
        super()._save_m2m()
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        self.instance.tag_set.clear()
        self.instance.tag_set.add(*tag_list)

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if content:
            # script 태그를 제거한다.
            content = re.sub(r'<script.*?>.*?</script>', '', content, flags= re.I | re.S)
        return content

    class Meta:
        model = Post
        fields = ["category",
                  "title",
                  "content",
                  "photo",
                  "status"]


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"

    # Form 만의 유효성 검사 방법
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            if not phone.startswith("010"):
                raise forms.ValidationError("010으로 시작하는 전화번호를 입력해주세요.")
        return phone
    
    