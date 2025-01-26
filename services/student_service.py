from datetime import datetime
from students.models import Student



def register_student(student):


    def generate_student_number():
        current_year = datetime.now().year
        count = Student.objects.count() + 1
        return f"STU{current_year}{count:05}"

    return Student.objects.create(
        usuario=student.usuario,
        first_name=student.first_name,
        last_name=student.last_name,
        date_of_birth=student.date_of_birth,
        gender=student.gender,
        nationality=student.nationality,
        phone_number=student.phone_number,
        email=student.email,
        address=student.address,
        city=student.city,
        neighborhood=student.neighborhood,
        postal_code=student.postal_code,
        student_number=generate_student_number(),
        profile_img=student.profile_img,
        is_active=student.is_active,
        parent = student.parent,
    )


def get_all_students():
    """
    Retorna todos os estudantes cadastrados.
    """
    return Student.objects.all()


def get_student_by_id(id):
    """
    Busca um estudante pelo ID.
    """
    return Student.objects.get(id=id)




def update_student(student_id, updated_data):
    """
    Atualiza os dados de um estudante existente.
    """
    student = get_student_by_id(student_id)
    if student:
        for key, value in updated_data.items():
            setattr(student, key, value)
        student.save()
        return student
    return None


def delete_student(student_id):
    """
    Remove um estudante do banco de dados.
    """
    student = get_student_by_id(student_id)
    if student:
        student.delete()
        return True
    return False





def editar_cliente(cliente_antigo, cliente_novo):
    cliente_antigo.nome = cliente_novo.nome
    cliente_antigo.apelido = cliente_novo.apelido
    cliente_antigo.email = cliente_novo.email
    cliente_antigo.nif = cliente_novo.nif
    cliente_antigo.data_nascimento = cliente_novo.data_nascimento
    cliente_antigo.telefone = cliente_novo.telefone
    cliente_antigo.endereco = cliente_novo.endereco
    cliente_antigo.profissao = cliente_novo.profissao
    cliente_antigo.estado_civil = cliente_novo.estado_civil
    cliente_antigo.ativo = cliente_novo.ativo
    cliente_antigo.save(force_update=True)


def remover_cliente(cliente):
    cliente.delete()
