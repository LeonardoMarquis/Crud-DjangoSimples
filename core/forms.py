from django import forms

from .models import Produto

class ProdutoModelForm(forms.ModelForm):    # esse parametro é a classe mae dessa aqui que estou criando
    
    class Meta:
        model = Produto
        fields = '__all__'