from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('adicionar/', CreateProdutoView.as_view(), name='adicionar_produto'),
    path('<int:pk>/atualizar/', UpdateProdutoView.as_view(), name='atualizar_produto'),
    path('<int:pk>/deletar/', DeleteProdutoView.as_view(), name='deletar_produto')
]

# poderia ter o mesmo, se tiver id e adicionar vai virar update, e se for so adicionar é create
# poderia ser mas separado fica mais simples e menos complicadot