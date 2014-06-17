from django import forms
from models import Entry
from epiceditor.widgets import AdminEpicEditorWidget


class EntryForm(forms.ModelForm):
    content = forms.CharField(widget=AdminEpicEditorWidget())

    class Meta:
        model = Entry
