def avrage_student_gpa(num):
    if gpa >= 17:
        return "very good"
    elif 15 <= gpa < 17:
        return "good"
    elif 10 <= gpa < 15:
        return "bad"
    elif gpa < 10:
        return "fail"
a = int(input("enter your score: "))
b = int(input("enter your score: "))
c = int(input("enter your score: "))
gpa = (a + b + c) / 3
print(avrage_student_gpa(gpa))
    
    
def save_note():
    note = input("enter your name: ")
    with open("names.txt","a" , encoding="utf-8") as file:
        file.write( note + "\n")
    print("note saved successfully.")
    return note
def read_note(user_name):
    try:
        with open("names.txt", "r", encoding="utf-8") as file:
            print(f"hello {user_name}, your saved names is successfuly:")
            print(file.read())
    except FileNotFoundError:
        print("no names found.")
name_from_user = save_note() 
read_note(name_from_user)