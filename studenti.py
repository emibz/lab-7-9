class Student:
    nr_studenti = 0
    def __init__(self,nume):
        Student.nr_studenti += 1
        self.id = Student.nr_studenti
        self.nume = nume

    def get_nume(self):
        return self.nume
    def set_nume(self, nume_nou):
        self.nume = nume_nou

    def get_id(self):
        return self.id