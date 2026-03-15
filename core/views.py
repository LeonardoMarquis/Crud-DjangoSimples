from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto
from .forms import ProdutoModelForm

class IndexView(ListView):
    model = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
    paginate_by = 10
    ordering = 'nome'

class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')     # o reverse lazy ve qual é a view da nossa rota e nos redireciona para ela

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index') # tipo. * atualizou, manda para a tela do index

# é melhor deixar separado em coisas diferentes para nao desorganizar
# e assim fica mais legivel

class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
    




    