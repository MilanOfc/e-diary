from datacenter.models import Mark, Commendation, Chastisement, Schoolkid, Lesson
from random import choice

COMMENDATIONS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    kids_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    kids_chastisements.delete()


def get_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print('Please specify the name, several students are found')
        return
    except Schoolkid.DoesNotExist:
        print('This student does not exist, please check the name')
        return


def create_commendation(pupil, subject):
    great_lesson = Lesson.objects.filter(year_of_study=pupil.year_of_study,
                                         group_letter=pupil.group_letter,
                                         subject__title=subject).order_by('?').first()
    commendation = choice(COMMENDATIONS)
    Commendation.objects.create(text=commendation,
                                created=great_lesson.date,
                                schoolkid=pupil,
                                subject=great_lesson.subject,
                                teacher=great_lesson.teacher)
