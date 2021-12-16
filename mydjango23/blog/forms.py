from django import forms
from blog.models import Post, Tag


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

    class Meta:
        model = Post
        fields = ["category",
                  "title",
                  "content",
                  "photo",
                  "status"]
