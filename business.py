from studenti import Student
from discipline import disciplina

def get_student_by_id(lista_studenti, stud_id):
    for student in lista_studenti:
        if student.get_id() == stud_id:
            return student
    return False


def get_disciplina_by_id(lista_discipline, disc_id):
    for disc in lista_discipline:
        if disc.get_id() == disc_id:
            return disc
    return False


def adauga_student(lista_studenti, nume):
    student = Student(nume)
    lista_studenti.append(student)


def sterge_student(lista_studenti, stud_id):
    for index, student in enumerate(lista_studenti):
        if student.get_id() == stud_id:
            lista_studenti.pop(index)
            return


def modifica_student(lista_studenti, stud_id, nume_nou):
    student = get_student_by_id(lista_studenti, stud_id)
    student.set_nume(nume_nou)


def adauga_disciplina(lista_discipline, nume_disciplina, nume_profesor):
    Disciplina = disciplina(nume_disciplina, nume_profesor)
    lista_discipline.append(Disciplina)


def sterge_disciplina(lista_discipline, disc_id):
    for index, disc in enumerate(lista_discipline):
        if disc.get_id() == disc_id:
            lista_discipline.pop(index)
            return


def modifica_nume_disiciplina(lista_discipline, id_disciplina, nume_nou):
    disciplina = get_disciplina_by_id(lista_discipline, id_disciplina)
    if disciplina:
        disciplina.set_name(nume_nou)
    else:
        print("Nu exista")


def modifica_profesor_disciplina(lista_discipline, id_disciplina, profesor_nou):
    disciplina = get_disciplina_by_id(lista_discipline, id_disciplina)
    if disciplina:
        disciplina.set_profesor(profesor_nou)
    else:
        print("Nu exista")


def cauta_student(lista_studenti, stud_id):
    student = get_student_by_id(lista_studenti, stud_id)
    if student:
        return student
    else:
        return "Nu exista"


def cauta_disciplina(lista_discipline, id_disciplina):
    disciplina = get_disciplina_by_id(lista_discipline, id_disciplina)
    if disciplina:
        return disciplina
    else:
        return "Nu exista"


def adauga_nota(catalog, lista_studenti, lista_discipline, stud_id, disc_id, nota):
    student = get_student_by_id(lista_studenti, stud_id)
    disciplina = get_disciplina_by_id(lista_discipline, disc_id)

    if student and disciplina:
        catalog.adauga_nota(disciplina, student, nota)
        return True
    else:
        return False