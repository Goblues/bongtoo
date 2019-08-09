import csv
import os
from services.models import Volunteer
from commons.models import Region


def input():
    # path = os.path.abspath('./')
    # print(path)
    # os.chdir(path)
    with open('/home/gtah2mint/Workspace/bongtoo/jinuo/services/test.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _, created = Region.objects.get_or_create(
                city=row['city'],
                town=row['town'],
            )
            p = Volunteer(title=row['title'], term=row['term'], starttime=row['starttime'], endtime=row['endtime'], field=row['field'], place=row['place'],
                          subject=row['subject'], value=row['value'], subjectclass=row['subjectclass'], activityclass=row['activityclass'], city=row['city'], town=row['town'])
            p.save()
