subjects = ['Maths', 'English', 'History', 'Computing', 'Art', 'Economics']

del_subject = input("Which of these subjects do you dislike: {0}?\nRemove Subject: ".format(", ".join(subjects))).strip().capitalize()

if del_subject.capitalize() in subjects:
    subjects.remove(del_subject.capitalize())
    print(subjects)
else:
    print("Subject not identified.")

