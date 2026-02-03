from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from datetime import date
from decimal import Decimal


class Utilizadores(AbstractUser):

    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )

    FUNCAO_CHOICES = (
        ('Inativo','Inativo'),
        ('Ativo','Ativo'),
    )

    PRETENDE_RECIBO = (
        ('Sim', 'Sim'),
        ('Nao', 'Não')
    )

    CLASSIFICACAO_ESFORCO = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    FUMADOR = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
    )

    PROBLEMAS_SAUDE = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
    )

    LIMITACOES = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
    )

    CONHECIMENTO_FITCLUB = (
        ('atraves_familiares', 'Através de Familiares'),
        ('atraves_amigos', 'Através de Amigos'),
        ('atraves_redes_sociais', 'Através das Redes Sociais'),
        ('atraves_outdoors_flyers', 'Através de Outdoors/Flyers'),
        ('recomendacao_medica', 'Recomendação Médica')
    )

    REGIME_CHOICES = (
        ('regime_livre', 'Regime Livre - 35€'),
        ('regime_livre+plano_alimentar', 'Regime Livre + Plano Alimentar – 40€ (fidelização de 3 meses)'),
        ('regime_basico', 'Regime Básico - 30€ (2 sessões semanais)'),
        ('regime_basico+plano_alimentar', 'Regime Básico + Plano Alimentar – 37,5€ - (fidelização de 3 meses)'),
        ('so_treinos_online', 'Só Treinos Online – 10€'),
        ('regime_kids', 'Regime Kids - 20€'),

        ('pack_6_aulas', 'Pack 6 Aulas – 25€ (sem desconto familiar)'),
        ('pack_4_aulas', 'Pack 4 Aulas - 20€ (sem desconto familiar)'),
    )


    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contacto = models.IntegerField()
    data_nascimento = models.DateField(null=False, blank=False)
    genero = models.CharField(max_length=12, choices=GENERO_CHOICES, null=False, blank=False)
    morada = models.CharField(max_length=255, null=True, blank=True)
    codigo_postal = models.CharField(max_length=8, null=True, blank=True)
    localidade = models.CharField(max_length=100, null=True, blank=True)
    funcao = models.CharField(max_length=20, choices=FUNCAO_CHOICES, default='Ativo')
    regime = models.CharField(max_length=30, choices=REGIME_CHOICES, null=True, blank=True)
    regime_data = models.DateField(blank=True, null=True)
    altura = models.IntegerField(null=True)

    # OUTRAS INFORMAÇÕES
    nif = models.IntegerField()
    pretende_recibo = models.CharField(max_length=3, choices=PRETENDE_RECIBO)
    profissao = models.CharField(max_length=255)
    classificacao_esforco_na_profissao = models.CharField(max_length=1, choices=CLASSIFICACAO_ESFORCO)
    fumador = models.CharField(max_length=3, choices=FUMADOR)
    problemas_saude = models.CharField(max_length=3, choices=PROBLEMAS_SAUDE)
    limitacoes_para_pratica_exercicio_fisico = models.CharField(max_length=3, choices=LIMITACOES)
    como_teve_conhecimento_existencia_fitclub = models.CharField(max_length=100, choices=CONHECIMENTO_FITCLUB, default='Por Definir')

    taxa_respondida = models.BooleanField(default=False)



    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utilizadores_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='utilizadores',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utilizadores_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='utilizadores',
    )

    def clean(self):
        super().clean()
        email = self.email
        if '@' not in email:
            raise ValidationError({'email': "O e-mail deve conter um '@'."})
        
        domain = email.split('@')[-1]
        if '.' not in domain:
            raise ValidationError({'email': "O domínio do e-mail parece inválido."})
        
        allowed_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
        if domain not in allowed_domains:
            raise ValidationError({'email': f"Domínio '{domain}' não é permitido."})
        
    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    


# ========== ========== ========== ========== ========== ========== ========== ========== ========== ========== ========== #



class Dados_biometricos(models.Model):
    idade = models.IntegerField(null=True, blank=True)  # Inteiro para idade
    # altura = models.IntegerField(null=True, blank=True)  # Decimal para manter precisão
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    imc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, editable=False)
    massa_gorda = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    massa_muscular = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    agua = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gordura_visceral = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    idade_biologica = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nivel_fisico = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    data_registo = models.DateField(auto_now_add=True)
    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)

    def calcular_idade(self):
        if self.utilizador.data_nascimento:
            hoje = date.today()
            nascimento = self.utilizador.data_nascimento
            return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return None

    def save(self, *args, **kwargs):
        # CALCULAR O IMC
        if self.peso and self.utilizador.altura:
            altura_metros = Decimal(self.utilizador.altura) / Decimal(100)
            if altura_metros > 0:
                self.imc = round(self.peso / (altura_metros ** 2), 2)  # CONVERTE ALTURA PARA METROS
        super().save(*args, **kwargs)


class NomeTipoTreino(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Treino(models.Model):
    DIAS_DA_SEMANA_CHOICES = [
        ('segunda-feira', 'Segunda-feira'),
        ('terça-feira', 'Terça-feira'),
        ('quarta-feira', 'Quarta-feira'),
        ('quinta-feira', 'Quinta-feira'),
        ('sexta-feira', 'Sexta-feira'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    TIPO_TREINO_CHOICES = [
        ('treino_funcional', 'Treino Funcional'),
        ('mobilidade', 'Mobilidade'),
        ('força', 'Força'),
        ('total_fit', 'Total FIT'),
    ]

    RESERVAS_HORAS_ANTES_CHOICES = [
        (1, '1 hora antes'),
        (6, '6 horas antes'),
        (12, '12 horas antes'),
        (24, '24 horas antes'),
        (48, '48 horas antes')
    ]

    RESERVAS_HORAS_FECHO_CHOICES = [
        (0, 'No início do treino'),
        (1, '1 hora antes'),
        (2, '2 horas antes'),
        (6, '6 horas antes'),
        (12, '12 horas antes'),
    ]

    tipo_treino = models.CharField(max_length=50, choices=TIPO_TREINO_CHOICES, null=True, blank=True)
    tipo_treino_nome = models.ForeignKey(NomeTipoTreino, on_delete=models.CASCADE, null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    dia_da_semana = models.CharField(max_length=20, choices=DIAS_DA_SEMANA_CHOICES)
    max_participantes = models.PositiveIntegerField(null=False, blank=False, default=0)
    max_lista_espera = models.PositiveIntegerField(null=False, blank=False, default=0)
    reservas_horas_antes = models.PositiveIntegerField(default=24, choices=RESERVAS_HORAS_ANTES_CHOICES)
    reservas_horas_fecho = models.IntegerField(default=1, choices=RESERVAS_HORAS_FECHO_CHOICES)
    participantes = models.ManyToManyField(Utilizadores, related_name='treinos_participados', blank=True)

    def reservas_abertas(self):
        now = timezone.now()
        inicio_treino = timezone.make_aware(
            timezone.datetime.combine(self.data_inicio, self.hora_inicio)
        )
        abertura_reservas = inicio_treino - timedelta(hours=self.reservas_horas_antes)
        fechamento_reservas = inicio_treino - timedelta(hours=self.reservas_horas_fecho)
        
        # Retorna True se o horário atual estiver no intervalo de abertura e fechamento
        return abertura_reservas <= now <= fechamento_reservas
    
    def total_reservas(self):
        return Reservas.objects.filter(treino=self).count()
    
    def reservado_por_usuario(self, usuario):
        return self.participantes.filter(id=usuario.id).exists()

    def __str__(self):
        return f"{self.get_tipo_treino_display()} - {self.dia_da_semana}"







# ========== ========== ========== ========== ========== ========== ========== ========== ========== ========== ========== #



class Reservas(models.Model):
    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='reservas')
    confirmado = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = ('utilizador', 'treino')

    def __str__(self):
        return f"{self.utilizador.username} - {self.treino.hora_inicio} - {self.treino.hora_fim} - {self.treino.tipo}"

class ListaEspera(models.Model):
    utilizador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    treino = models.ForeignKey('Treino', on_delete=models.CASCADE)
    data_entrada = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilizador', 'treino')

    def __str__(self):
        return f"{self.utilizador.username} na lista de espera para o treino {self.treino.tipo_treino}"
    

class Ausencias(models.Model):
    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reservas, on_delete=models.CASCADE)
    taxa_respondida = models.CharField(max_length=10, choices=[('sim', 'Sim'), ('nao', 'Não')], null=True, blank=True)



# ========== ========== ========== ========== ========== ========== ========== ========== ========== ========== ========== #



class RecordesNomes(models.Model):
    nome = models.CharField(max_length=100)
    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Recordes(models.Model):
    EXERCICIOS_PREDEFINIDOS_CHOICES = [
        ('vazio', 'Escolhe uma opção'),
        ('peso_morto', 'Peso Morto'),
        ('agachamento_com_barra', 'Agachamento c/barra'),
        ('remada', 'Remada'),
        ('press_ombro', 'Press de Ombro'),
        ('flexoes', 'Flexões'),
        ('burpees', 'Burpees'),
        ('elevacao', 'Elevação'),
        ('agachamento_livre', 'Agachamento livre'),
    ]

    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    nome = models.ForeignKey(RecordesNomes, on_delete=models.CASCADE, null=True, blank=True)
    predefinidos = models.CharField(max_length=100, choices=EXERCICIOS_PREDEFINIDOS_CHOICES, null=True, blank=True)
    valor = models.FloatField()
    data_do_recorde = models.DateField()
    data_criacao_recorde = models.DateField(auto_now_add=True)



class AvaliacaoMensal(models.Model):
    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    ano = models.IntegerField()
    mes = models.IntegerField()
    mes_ausente = models.BooleanField(default=False)
    nivel_satisfacao = models.IntegerField(null=True)
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('utilizador', 'ano', 'mes')


class AvaliacaoTrimestral(models.Model):
    utilizador = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)
    ano = models.IntegerField()
    mes = models.IntegerField()
    nivel_satisfacao = models.IntegerField(default=None)
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('utilizador', 'ano', 'mes')

#TESTES

class FormData(models.Model):
    # Suponhamos que você tenha um campo de texto e um campo de data
    campo1 = models.CharField(max_length=200, verbose_name="Campo 1")
    campo2 = models.CharField(max_length=200, verbose_name="Campo 2")
    campo3 = models.CharField(max_length=200, verbose_name="Campo 3")

    # Campo adicional para armazenar a data de criação do registro
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return f"FormData {self.id} - {self.campo1}"


class TreinosOnline(models.Model):
    TIPO_TREINOS_ONLINE_CHOICE = (
        ('mobilidade', 'Mobilidade'),
        ('força', 'Força'),
        ('funcional', 'Funcional'),
        ('metabólico', 'Metabólico'),
        ('aeróbica', 'Aeróbica'),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='aulas_online', default='aulas_online/default.png', null=True)
    tipo_treino = models.CharField(max_length=20, choices=TIPO_TREINOS_ONLINE_CHOICE)
    link_yt = models.CharField(max_length=255)


