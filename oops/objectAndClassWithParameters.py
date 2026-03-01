class subramaniam:
    vishnu = "VIKASH"
    def __init__(self,a,b):
        self.firstname=a
        self.lastname=b
    def keerthana(self):
        return f"daughter in law and Keerthana is wife of {self.firstname} {self.lastname}"
    def vikash(self):
        return f"SON{__class__().vishnu}"
    def kavitha(self):
        return "wife"
c=subramaniam("vishnu","vikash")
print(c.keerthana())
