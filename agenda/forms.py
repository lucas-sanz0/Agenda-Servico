from datetime import date

from django import forms

from .models import Agendamento, Servico


class AgendamentoForm(forms.ModelForm):
    # data e hora travadas no formato ISO pro input HTML5; sem isso dava
    # erro porque o pt-br espera dd/mm/aaaa
    data = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d')
    )
    hora = forms.TimeField(
        input_formats=['%H:%M', '%H:%M:%S'],
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M')
    )

    class Meta:
        model = Agendamento
        fields = ['servico', 'data', 'hora', 'cep', 'logradouro', 'numero',
                  'complemento', 'bairro', 'cidade', 'uf', 'observacoes']
        widgets = {
            'servico': forms.Select(attrs={'class': 'form-select'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_cep'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servico'].queryset = Servico.objects.filter(ativo=True)  # só ativos

    def clean_data(self):
        d = self.cleaned_data['data']
        if d < date.today():
            raise forms.ValidationError('Não é possível agendar para uma data passada.')
        return d
