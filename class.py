class Girl:
    name=""
    age=0
    def rupa(self):
        if (self.age<=20):
            return "you are not eligible to get a job"
        else:
            return (self.name, self.age)

girl = Girl()
girl.name ="rupa"
girl.age = 20

girl1 = Girl()
girl1.name ="rupa"
girl1.age = 21
print (girl.rupa())
print (girl1.rupa())
