import csv


def write_in_to_csv(info_list):
    with open("student_info.csv", "a", newline='') as csv_file: #Note: usin in 'w+' mode means it writes again and again. So use 'a' append mode
        w=csv.writer(csv_file)
        if csv_file.tell()==0:
            w.writerow(["Name",'age',"Contact",'Email_id'])
        w.writerow(info_list)


if __name__=='__main__':
    cond = True
    i = 0
    while (cond):
        info = input('Enter the information of student#{} in the following format(Name age Contact_Number Email_id):\n'.format(i))
        #split
        student_info_list=info.split(' ')
        print('\nThe entered information for student#{} is:\nName: {}\nAge: {}\nContact:{}\nEmailID:{}'.format(i,student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        check1=input("Is the information entered correct?(yes/no):\n" )
        if check1 == "yes":
            check=input('do you want to enter more info:yes/no:\n')
            write_in_to_csv(student_info_list)
            if check == 'yes':
                    i=i+1
            elif check == 'no':
                cond=False
        elif check1=='no':
            print("Please re-enter the correct details!\n ")