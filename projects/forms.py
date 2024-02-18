from django import forms
from django.forms import widgets
from .models import Project, Review, Tag

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

    # Override the __init__ method to add css classes
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        # Loop over all the fields
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})   # 'input' is a css class (static -> css) 
        
        # For the single field
        # self.fields['title'].widget.attrs.update(({'placeholder': 'Add a title'}))
        # self.fields['description'].widget.attrs.update(({'placeholder': 'Write your Description'}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})