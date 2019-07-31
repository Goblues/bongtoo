from django import forms
from .models import Review, Image, Comment


class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'body', 'target', 'activity', )


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )

    def clean_image(self):
        image = self.cleaned_data['image']
        return image


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
