import csv
import os
from services.models import Volunteer
from commons.models import Region

os.chdir('./')


def input():
    with open('test.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _, created = Region.objects.get_or_create(
                city=row['city'],
                town=row['town'],
            )
            p = Volunteer(title=row['title'], term=row['term'], starttime=row['starttime'], endtime=row['endtime'], field=row['field'], place=row['place'],
                          subject=row['subject'], value=row['value'], subjectclass=row['subjectclass'], activityclass=row['activityclass'], city=row['city'], town=row['town'])
            p.save()
