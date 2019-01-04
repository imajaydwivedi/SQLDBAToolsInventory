from django import forms
from .models import Server


class ServerAddForm(forms.ModelForm):
    # Form fields go here with validators params
    class Meta:
        model = Server
        # fields = "__all__"
        # exclude = ["field1","fields2"]
        fields = ["server", "servertype"]


''' To Display result of Get-ServerInfo
'''
class GetServerInfoForm(forms.Form):
    ServerName = forms.CharField()
    FQDN = forms.CharField()
    IPAddress = forms.GenericIPAddressField()
    Domain = forms.CharField()
    IsStandaloneServer = forms.BooleanField(required=False)
    IsSqlClusterNode = forms.BooleanField(required=False)
    IsAgNode = forms.BooleanField(required=False)
    IsWSFC = forms.BooleanField(required=False)
    IsSqlCluster = forms.BooleanField(required=False)
    IsAG = forms.BooleanField(required=False)
    ParentServerName = forms.CharField(required=False)
    OS = forms.CharField(required=False)
    SPVersion = forms.CharField(required=False)
    LastBootTime = forms.DateTimeField(widget=forms.DateTimeInput,required=False)
    UpTime = forms.CharField(required=False)
    IsVM = forms.BooleanField(required=False)
    Manufacturer = forms.CharField(required=False)
    Model = forms.CharField(required=False)
    RAM = forms.IntegerField(required=False)
    CPU = forms.IntegerField(required=False)
    Powerplan = forms.CharField(required=False)
    OSArchitecture = forms.IntegerField(required=False)


''' To display 3 columns in UI -> ServerName, EnvironmentType, GeneralDescription
    Rest of the columns would be fetched through powershell
'''
class AddServerInfoForm(forms.Form):
    ServerName = forms.CharField()
    SERVERTYPE_CHOICES = (
        ('NA', 'Not Available'),
        ('Dev', 'Development'),
        ('QA', 'Quality Analysis'),
        ('Test', 'Testing'),
        ('Prod', 'Production'),
    )
    #EnvironmentType = forms.CharField(choices=SERVERTYPE_CHOICES, default='NA')
    EnvironmentType = forms.CharField(label='EnvironmentType',widget=forms.Select(choices=SERVERTYPE_CHOICES))
    GeneralDescription = forms.CharField(max_length=2000, widget=forms.Textarea(
    ), help_text='Write some other information about server here!', required=False)

    def clean(self):
        cleaned_data = super(AddServerInfoForm, self).clean()
        ServerName = cleaned_data.get('ServerName')
        EnvironmentType = cleaned_data.get('EnvironmentType')
        if not ServerName and not EnvironmentType:
            raise forms.ValidationError(
                'Kindly provide at least ServerName and EnvironmentType!')
