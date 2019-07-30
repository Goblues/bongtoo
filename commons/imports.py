from .models import Region, Activity, Subject


def set_region():
    region_list = [
        ['서울특별시', '성북구'],
        ['서울특별시', '동대문구'],
        ['서울특별시', '서대문구'],
    ]
    for item in region_list:
        Region.objects.create(city=item[0], town=item[1])


def set_activity():
    activity_list = [
        '노인',
        '장애인',
        '아동',
        '청소년',
        '취약 계층'
    ]
    for item in activity_list:
        Activity.objects.create(name=item)


def set_subject():
    subject_list = [
        '사무',
        '학습',
        '식당',
        '외부활동',
        '환경미화',
        '치료'
    ]
    for item in subject_list:
        Subject.objects.create(name=item)

def construct_data():
  set_region()
  set_activity()
  set_subject()

def delete_all_data():
  Region.objects.all().delete()
  Activity.objects.all().delete()
  Subject.objects.all().delete()