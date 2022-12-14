from django.forms import ModelForm, Form, Textarea, TextInput
from network.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'text',
        ]
        labels = {
            'text': '',
        }
        error_messages = {
            'name': {
                'max_length': ("140 symbols MAX"),
            },
        }
        widgets = {
            'text': Textarea(attrs={'rows':3, 'cols':50}),
        }
