from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    from django.db import models

class Cliente(models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome

class Login(models.Model):
    id_cpf = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True, null=True)
    senha = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nome
