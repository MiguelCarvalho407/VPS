from django.urls import path
from . import views

urlpatterns = [
    path('', views.dologin, name='login'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.dologin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('acessonegado/', views.acesso_negado, name='acesso_negado'),
    path('fitclub/', views.fcBase, name='fcBase'),
    path('fitclub/calendario/', views.calendario, name='calendario'),
    path('fitclub/criar_treino/', views.criar_treinos, name='criar_treino'),

    path('fitclub/membros/', views.membros, name='membros'),
    path('fitclub/utilizador/<int:user_id>/', views.detalhe_utilizador, name='detalhe_utilizador'),
    path('fitclub/apagarconta/<int:user_id>/', views.apagarconta, name='apagarconta'),

    path('fitclub/definicoes/', views.definicoes, name='definicoes'),
    path('fitclub/recordes/', views.recordes, name='recordes'),
    path('fitclub/recordes/apagar/<int:recorde_id>/', views.apagar_recorde, name='apagar_recorde'),
    path('fitclub/criarnomerecordes/', views.criarnomerecordes, name='criarnomerecordes'),
    path('fitclub/apagarecorde/<int:recorde_id>/', views.apagar_nome_recorde, name='apagar_nome_recorde'),
    path('fitclub/dadosbiometricos/', views.dadosbiometricos, name='dadosbiometricos'),
    path('fitclub/utilizador/<int:user_id>/editar/', views.editar_utilizador, name='editar_utilizador'),
    path('fitclub/assiduidade/', views.assiduidade, name='assiduidade'),
    path('fitclub/cartao/', views.cartao, name='cartao'),

    path('fitclub/reservas_detalhes/<int:treino_id>/', views.reservas_detalhes, name='reservas_detalhes'),
    path('reservas/<int:treino_id>/', views.reservas, name='reservas'),


    path('treino/<int:treino_id>/adicionar_utilizador/', views.adicionar_utilizador_treino, name='adicionar_utilizador_treino'),

    #CRUD
    path('fitclub/editar_treino/<int:treino_id>/', views.editar_treino, name='editar_treino'),
    path('fitclub/apagartreino/<int:pk>/', views.apagartreino, name='apagartarefa'),
    
    path('fitclub/criartipotreino/', views.criar_tipo_treino, name='criar_tipo_treino'),

    path('sairlistaespera/<int:treino_id>/', views.cancelar_lista_espera, name='cancelar_lista_espera'),

    path('fitclub/utilizador/<int:user_id>/dadosbiometricos', views.editardadosbiometricos, name='editardadosbiometricos'),
    path('fitclub/utilizador/<int:user_id>/assiduidade/', views.ver_assiduidade, name='verassiduidade'),

    path('fitclub/apagartreinos/', views.apagar_treinos_em_massa, name='apagar_treinos_em_massa'),

    path('fitclub/utilizador/<int:user_id>/recordes/', views.ver_recordes_utilizador, name='ver_recordes_utilizador'),

    path('fitclub/listaespera/<int:treino_id>/', views.lista_espera_view, name='listaespera'),


    # EXPORTA OS DADOS DE TODOS OS UTILIZADORES
    path('exportar_excel/', views.export_to_excel, name='exportar_excel'),
    # EXPORTA OS DADOS DE UM UTILIZADOR ESPECIFICO
    path('exportar_utilizador/<int:user_id>/', views.export_user_data_to_excel, name='exportar_utilizador'),
    path('exportar-avaliacoes-mensais/', views.baixar_avaliacoes_mensais, name='baixar_avaliacoes_mensais'),
    path('exportar-treinos/', views.exportar_treinos, name='exportar_treinos'),

    path('assiduidade/exportar-estatisticas/',views.exportar_assiduidade_estatisticas_excel,name='exportar_assiduidade_estatisticas'),


    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('alterar_senha_concluido/', views.alterar_senha_concluido, name='alterar_senha_concluido'),




    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("reset/<uidb64>/<token>/", views.password_reset_confirm, name="password_reset_confirm"),


    path('criar-aula-online/', views.criar_treino_online, name='criar_treino_online'),

    path('fitclub/treinos-funcionais/', views.treinos_funcionais, name='funcionais'),
    path('fitclub/<int:treino_id>/apagar-funcional/', views.apagar_funcionais_online, name='apagar_funcionais_online'),

    path('fitclub/treinos-mobilidade/', views.treinos_mobilidade, name='mobilidade'),
    path('fitclub/<int:treino_id>/apagar-mobilidade/', views.apagar_mobilidade_online, name='apagar_mobilidade_online'),

    path('fitclub/treinos-forca/', views.treinos_forca, name='força'),
    path('fitclub/<int:treino_id>/apagar-forca/', views.apagar_forca_online, name='apagar_forca_online'),

    path('fitclub/treinos-metabolico/', views.treinos_metabolico, name='metabolico'),
    path('fitclub/<int:treino_id>/apagar-metabolico/', views.apagar_metabolico_online, name='apagar_metabolico_online'),

    path('fitclub/treinos-aerobica/', views.treinos_aerobica, name='aerobica'),
    path('fitclub/<int:treino_id>/apagar-aerobica/', views.apagar_aerobica_online, name='apagar_aerobica_online'),
    
    path('escolher-regime/', views.escolher_regime, name='escolher_regime'),

    path('contactos-direitos-imagem/', views.contactos_direitos_imagem, name='contactos_direitos_imagem'),
    path('marcacoes-cancelamentos/', views.marcacoes_cancelamentos, name='marcacoes_cancelamentos'),
    path('mensalidades/', views.mensalidades, name='mensalidades'),
    path('regras-treino/', views.regras_treino, name='regras_treino'),
    path('suspensao-cancelamento-inscricao/', views.suspensao_cancelamento_inscricao, name='suspensao_cancelamento_inscricao'),

    path('teste/', views.descarregar_dados, name='descarregar_dados')

]

