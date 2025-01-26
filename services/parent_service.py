
from parents.models import Parent


  

def register_parent(parent):
    # Salvando o pai no banco de dados
    Parent.objects.create(
    usuario=parent.usuario,  # O usuário associado
    first_name=parent.first_name,
    last_name=parent.last_name,
    phone_number=parent.phone_number,
    email=parent.email,
    relationship=parent.relationship,
    profile_img=parent.profile_img,
    )

def list_parents():
    return Parent.objects.all().order_by("first_name")






       