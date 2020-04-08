print ('''*******************************************************************************
                    Python User Data Validation
                    AYO OMOLADE
                    Slack username : Ayodee
                    Email Address : omoladee11@gmail.com
******************************************************************************''')

#Random String
import random
import string

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Main Program
New = True
Database = []

while New:
    
    #Get User Details
    Fname = str(input("Enter Firstname : "))
    Lname = str(input("Enter Lastname : "))
    Email = str(input("Enter Email address : "))

    info_user = {}

    info_user["FirstName"] = Fname
    info_user["LastName"] = Lname
    info_user["Email Address"] = Email

    #Generate Password
    Password = Fname[0:2].lower() + Lname[-2:] + randomString()

    print ("Are you satisfied with the suggested password: %s" %(Password))
    Reply = str(input("Enter Y/N: "))

    #User Password
    if Reply.lower() == "n":
        New_Pwd = str(input("Enter a Password 7 characters or more: "))
        info_user["Password"] = New_Pwd
        Database.append(info_user)
        #Check Length of User Password
        while len(New_Pwd) < 7:
            New_Pwd = str(input("Password must be at least 7 characters long: "))
            info_user["Password"] = New_Pwd

    else:
        info_user["Password"] = Password
        Database.append(info_user)
    
    
    User = str(input("Registration Sucessful.\n \nWould you like to register a new user, Y/N: "))
    if User.lower() == "n":
        New = False
        print ("Thank you for registering.\n \nUser data will be displayed below.")
        for i in Database:
            print('-------------------------------------')
            for key, value in i.items():
                print(key, ':', value)
    else:
        New = True
