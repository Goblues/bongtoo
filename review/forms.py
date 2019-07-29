from django import forms
from .models import Review, Image


class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'body', 'region', 'activity', )


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )

    def clean_image(self):
        image = self.cleaned_data['image']
        return image
