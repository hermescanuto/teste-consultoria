from __future__ import absolute_import, unicode_literals
from celery import shared_task
import pandas as pd
from demand.models import Category, Demand, People
from upload.models import Document


@shared_task
def importfile(filename):
    sheet = 'demandas'
    print('Started task, processing...')
    print("Name", filename)
    print('Finished Task')
    df = pd.read_excel(r"." + filename, sheet_name=sheet)
    print("Go import")
    document = Document.objects.get(document=filename)
    for index, row in df.iterrows():
        category = Category.checkorcreate(row['Categoria'])
        people = People.checkorcreate(row)
        demand = Demand(category=category,
                        people=people,
                        demand=row['Demanda'],
                        date=row['Data'],
                        document=document)
        demand.save()
    document.imported = 1
    document.save()

    print("End import")
    return None
