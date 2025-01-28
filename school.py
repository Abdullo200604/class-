class Pupil:
    school_name="Abc"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, name):
        Pupil.school_name = name


    def __del__(self):
        print("obyekt o'chirildi")


joxa = Pupil("da")
Pupil.change_school("Abdulloh maktabi")
print(joxa.school_name)
