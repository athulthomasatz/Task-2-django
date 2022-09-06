class Student :
    def __init__ (self,name,depart,yos,m1,m2,m3,m4,m5,m6):
        self.name=name
        self.depart=depart
        self.yos=yos
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.m6=m6
        
    #def subject(self,m1,m2,m3,m4,m5,m6):
        #self.m1=m1
        #self.m2=m2
        #self.m3=m3
        #self.m4=m4
        #self.m5=m5
        #self.m6=m6
    
        
    #def to_mark(self,subject):
     #   total=m1+m2+m3
      #  print(total)

    def grade_crd(self):
        print(f"Student    : {self.name}")
        print(f"Department : {self.depart}")
        print(f"Year       : {self.yos}rd year")
        percent=str((self.m1+self.m2+self.m3+self.m4+self.m5+self.m6)/6)
        print(f"Percantage :{percent}")
        print()
s1=Student("athul","cs",3,34,45,65,78,98,34)
s2=Student("nikhil","bio",2,26,37,28,24,35,46)


        
        
        

