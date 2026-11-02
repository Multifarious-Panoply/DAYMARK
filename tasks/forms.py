from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    scheduled_time = forms.TimeField(
        required=False,
        input_formats=["%I:%M %p", "%H:%M"],
        widget=forms.TimeInput(
            format="%I:%M %p",
            attrs={
                "class": "form-input",
                "type": "text",
                "placeholder": "09:00 AM or 09:00 PM",
            },
        ),
    )

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "scheduled_date",
            "scheduled_time",
            "duration_minutes",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "e.g. Finish my assignment",
                "maxlength": "200",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-input form-textarea",
                "placeholder": "Add a few details (optional)...",
                "rows": 3,
            }),
            "scheduled_date": forms.DateInput(attrs={
                "class": "form-input",
                "type": "date",
            }),
            "duration_minutes": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "e.g. 60",
                "min": "1",
                "step": "1",
            }),
        }

        labels = {
            "title": "Task title",
            "description": "Description",
            "scheduled_date": "Scheduled date",
            "scheduled_time": "Scheduled time",
            "duration_minutes": "Duration in minutes",
        }
