from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from classes.models import Class

# from students.models import Student


def register_classes(classes):

    Class.objects.create(
        name=classes.name,
        year=classes.year,
        room=classes.room,
        period=classes.period,
        student_count=classes.student_count,
    )


""" @receiver(post_save, sender=Student)
def update_student_count_on_add(sender, instance, created, **kwargs):
    if created and instance.class_:
        instance.class_.student_count += 1
        instance.class_.save()

@receiver(post_delete, sender=Student)
def update_student_count_on_delete(sender, instance, **kwargs):
    if instance.class_:
        instance.class_.student_count -= 1
        instance.class_.save() """
