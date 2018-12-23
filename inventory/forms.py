from django import forms
from inventory.models import Server


class ServerAddForm(forms.ModelForm):
    # Form fields go here with validators params
    class Meta:
        model = Server
        # fields = "__all__"
        # exclude = ["field1","fields2"]
        fields = ["server", "servertype"]
