from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class HTMLField(forms.Field):
    def __init__(self, attrs=None, *args, **kwargs):
        self.error_messages = {}
        self.label_suffix = None
        self.help_text = None
        self.name = None
        self.label = None
        self.initial = None
        self.required = False
        self.attrs = {"id": None}
        self.show_hidden_initial = False
        self.localize = False
        self.disabled = False
        self.is_hidden = False
        self.validators = [validators.ProhibitNullCharactersValidator()]

    def validate(self, value):
        if value in self.empty_values and self.required:
            raise ValidationError(self.error_messages["required"], code="required")
