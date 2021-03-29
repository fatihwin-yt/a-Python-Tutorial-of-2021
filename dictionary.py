math_Value = {'joni':5,
              'edward' : 8,
              'edi' : 7,
              'hendrik' : 9}

name = input("Enter the student's name: ")

if name in math_Value:

    print("math value" , name , "is",
     math_Value [name] )

else:

    print("student data not found.")
    print("the following is the name of the student:")

    for i in math_Value.keys():

        print(i)