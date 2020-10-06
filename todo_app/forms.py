from django.forms import ModelForm, Textarea, DateInput
from .models import Task
from datetime import timedelta, datetime as dt


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'schedule_date', 'importance', 'managed_by', 'tags', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 20, 'rows': 2, 'placeholder': 'Add details'}),
            'schedule_date': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        help_texts = {
            'schedule_date': "When you are planning to achieve this task",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for vf in self.visible_fields():
            vf.field.widget.attrs['class'] = 'rounded px-2 py-1 w-2/3'
            f = vf.field
            x = 1
            if vf.field.label == 'Comment':
                vf.field.widget.attrs['class'] += ' placeholder-gray-800'


