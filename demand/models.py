from django.db import models
from upload.models import Document


# Create your models here.

class Category(models.Model):
    category = models.CharField(verbose_name="Categoria", max_length=20)

    def checkorcreate(category):
        try:
            category = Category.objects.get(category=category.lower())
            return category
        except Category.DoesNotExist:
            category = Category(category=category.lower())
            category.save()
            return category


class People(models.Model):
    identificator = models.CharField(verbose_name="identificador", max_length=50)
    name = models.CharField(verbose_name="Nome", max_length=100)
    phone = models.CharField(verbose_name="Telefone", max_length=30, null=True, blank=True)
    gender = models.CharField(verbose_name="Sexo", max_length=1)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def checkorcreate(row):
        try:
            people = People.objects.get(identificator=row['Identificador da pessoa'])
            return people
        except People.DoesNotExist:
            male = ['m', "masc", 'masculino']
            female = ['f', 'feminino']
            gender = "0"
            if row['Sexo'].lower() in male:
                gender = "M"
            elif row['Sexo'].lower() in female:
                gender = "F"
            print(gender, row['Sexo'].lower())
            if row['Telefone']  != row['Telefone']:
                row['Telefone'] = ""

            poeple = People(identificator=row['Identificador da pessoa'],
                            name=row['Nome Pessoa'],
                            phone=row['Telefone'],
                            gender=gender
                            )
            poeple.save()
            return poeple


class Demand(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Arquivo', default=1,
                                 db_column="document_id")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria', default=1,
                                 db_column="category_id")
    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='Usuario', default=1,
                               db_column="people_id")
    demand = models.CharField(verbose_name="Demanda", max_length=100)
    date = models.DateField(verbose_name="Data")
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
