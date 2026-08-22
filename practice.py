
class student:
  def __init__(self,name):
    print("creating profile",self.name)
  def __init__(self,name,marks):
    student.name=name
    student.marks=marks


s=[]

s.append(student('karim',10))
print(s[0].name)