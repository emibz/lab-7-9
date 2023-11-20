class Notare:
    def __init__(self, disciplina, student, nota):
        self.disciplina = disciplina
        self.student = student
        self.nota = nota
    
    def __str__(self):
        return f"Disciplina {self.get_disciplina()}: student={self.get_student()}, nota={self.get_nota()}"

    def __repr__(self):
        return str(self)

    def get_disciplina(self):
        return self.disciplina.get_name()

    def get_student(self):
        return self.student.get_nume()

    def get_nota(self):
        return self.nota


class Catalog:
    def __init__(self):
        self.note = []

    def get_note(self):
        return self.note
    
    def adauga_nota(self, disciplina, student, nota):
        self.note.append(Notare(disciplina, student, nota))

    def print_catalog(self):
        for notare in self.get_note():
            print(notare)
