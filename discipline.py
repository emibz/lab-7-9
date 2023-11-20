class disciplina:
    nr_discipline = 0
    def __init__(self, nume, profesor):
        disciplina.nr_discipline +=1
        self.nume = nume
        self.id = disciplina.nr_discipline
        self.profesor = profesor

    def get_name(self):
        return self.nume

    def set_name(self, nume):
        self.nume = nume

    def get_id(self):
        return self.id

    def get_profesor(self):
        return self.profesor

    def set_profesor(self, profesor):
        self.profesor = profesor
