""" from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from classes.models import Class """

# from students.models import Student


""" 
@receiver(post_save, sender=Student)
def update_student_count_on_save(sender, instance, **kwargs):
    """
# Atualiza o campo student_count ao adicionar ou atualizar um aluno.
"""
    if instance.classroom:
        instance.classroom.student_count = instance.classroom.student_set.count()
        instance.classroom.save()


@receiver(post_delete, sender=Student)
def update_student_count_on_delete(sender, instance, **kwargs):
    """
# Atualiza o campo student_count ao remover um aluno.
"""
    if instance.classroom:
        instance.classroom.student_count = instance.classroom.student_set.count()
        instance.classroom.save()
 """
