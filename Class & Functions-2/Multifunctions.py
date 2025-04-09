class Calculation():
    def num():
        num=int(input("Enter a number to check:"))
        if(num/5==0):
            print("No is divisible by 5")
        else:
            print("No is not divisible by 5")

    def Lists():
        lists=[10, 20, 14, 55, 43, 87, 76]
        print(lists)
        print("Number of item in the List2:",len(lists))

    
    def addition():
        a=int(input("Enter the n1:"))
        b=int(input("Enter the n2:"))
        add=a+b
        return add

    def oddEven():
        num=int(input("Enter the number:"))
        if(num%2==0):
            print("EVEN")
            out="EVEN"
        else:
            print("ODD")
            out="ODD"
        return out
        
    def ageCategory(): 
        age=int(input("Enter the age:"))
        if(age<18):
            print("Child")
            cate="Child"
        elif(age<26):
            print("Adult")
            cate="Child"
        elif(age<45):
            print("Citizen")
            cate="Citizen"
        else:
            print("Senior Citizen")
            cate="Senior Citizen"
        return cate
        
    def BMI():
        BMI=int(input("Enter the BMI:"))
        if(BMI<19):
            print("Underweight")
            return "Underweight"
        elif(BMI<25):
            print("Normal Weight")
            return "Normal Weight"
        else:
            print("Very Overweight")
            return "Very Overweight"
    
    def marriageAge():
        if(Gender=="Female"):        
            if(age>=18):    
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
            
        elif(Gender=="male"):
            if(age>=21):
                print("ELIGIBLE")
            else:
               print("NOT ELIGIBLE")
        else:
            print("Invaild Gender")
            
        age=int(input("Your AGE:"))
        Gender=input("Your Gender:")
    
    
    def SubfieldsInAI_Subfields(self):
        print("Sub-fields in AI are:")
        Fildes=[
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        for SubFiled in Fildes:
            print(SubFiled)
          
    def Marks():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        total=Sub1+Sub2+Sub3+Sub4+Sub5
        percentage=(total/500)*100
        print("Total:",total)
        print("percentage:",percentage)

    def triangle():
        Heigth=int(input("Height:"))
        Breath=int(input("Breath:"))
        areaFormula=(Heigth*Breath)/2
        print("Area of Triangle:",areaFormula)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breath=int(input("Breath:"))
        Perimeterformula=(Height1+Height2+Breath)
        print("Perimeter of Triangle:",Perimeterformula)
        return 0
        

