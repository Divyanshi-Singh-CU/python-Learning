#Experiment_01

##program of student result processing system 
name=input("enter a student name:")
roll_number=input("enter a student roll number:")
maths=int(input("enter marks of maths:"))
science=int(input("enter marks of science:"))
physics=int(input("enter marks of physics:"))
biology=int(input("enter marks of biology:"))
chemistry=int(input("enter marks of chemistry:"))

total=maths+science+physics+biology+chemistry

percentage=(total/500)*100

print("Name:",name)
print("Roll_number:",roll_number)

print("Total:",total)
print("Percentage:",percentage)

if percentage>=40:
       print(" Result=pass")
       if percentage>=90:
           print("Grade=A")
       else:
           if (percentage>=80):
              print("Grade=B")
           else:
              if (percentage>=70):
                  print("Grade C")
              else:
                  if (percentage>=60):
                     print("Grade=D")
                  else:
                     if (percentage>=50):
                       print("Grade=E")
                     else:
                           print("Grade=F")
else:
    print("Result=fail")
