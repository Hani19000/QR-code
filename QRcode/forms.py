from django import forms


class QRCodeForm(forms.Form):
    QR_code_name = forms.CharField(
        max_length=50,
        label='QR name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter QR name'
        })
        )
    url = forms.URLField(
        max_length=200, 
        label='Website URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL of your online website'
        })
        )