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
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    kids_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in kids_chastisements:
        chastisement.delete()


def get_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=pupil_name)
    except MultipleObjectsReturned:
        print('Please specify the name, several students are found')
        return
    except ObjectDoesNotExist:
        print('This student does not exist, please check the name')
        return


def create_commendation(pupil_name, subject):
    pupil = get_schoolkid(pupil_name)
    lessons = Lesson.objects.filter(year_of_study=pupil.year_of_study,
                                    group_letter=pupil.group_letter,
                                    subject__title=subject)
    great_lesson = choice(lessons)
    commendation = choice(COMMENDATIONS)
    Commendation.objects.create(text=commendation,
                                created=great_lesson.date,
                                schoolkid=pupil,
                                subject=great_lesson.subject,
                                teacher=great_lesson.teacher)
