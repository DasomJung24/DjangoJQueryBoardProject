from django import forms

from .models import Posting


class PostingForm(forms.ModelForm):

    class Meta:
        model = Posting
        fields = ('writer', 'title', 'content', )

    # push 전에 삭제하기
    def clean(self):
        cleaned_data = super(PostingForm, self).clean()
        if self.errors:
            return cleaned_data
        return cleaned_data
