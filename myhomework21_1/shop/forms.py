from django import forms

from shop.models import Shop, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

#가지고 있던 태그값 호출

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#초기값 기억하기
        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            tags = ", ".join(tag.name for tag in tag_qs)
            self.fields["tags"].initial = tags

#폼내부에서 태그입력가능
    def save(self):
        saved_tag = super().save()
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_tag.tag_set.clear()
        saved_tag.tag_set.add(*tag_list)

        return saved_tag

    class Meta:
        model = Shop
        fields =["category",
                 "name",
                 "description",
                 "telephone"]
