import re
class check_register:       #class define
    

    def __init__(self, name,lastname,username,password,email,mobile,code):

        self._name = name
        self._lastname = lastname
        self._username = username
        self._password = password
        self._email = email
        self._mobile = mobile
        self._code = code
        
        

    def check_name(self,name):     #get name and check it
        
        name=input("Please Enter your name: ")


        if (re.findall(r'\b[a-zA-Z\s]{2,21}\b',name)):
            print("name is correct...\n")
            list.append(name)
            
        else:
            print("name is incorrect!\n")

            

    def check_lastname(self,lastname):     #get lastname and check it
        
        lastname=input("Please Enter your LastName: ")


        if (re.findall(r'\b[a-zA-Z\s]{2,30}\b', lastname)):
            print("LastName is correct...\n")
            list.append(lastname)
            
        else:
            print("LastName is incorrect!\n")

            
            
    def check_username(self,username):      #get username as input and check it
        
        username=input("Please Enter username: ")

        if( username=="username" or username=="admin"):      #if input 'username' and 'admin' raise error  
          print("the word is invalid!\n")
        else:

            if (re.findall(r'\b[a-zA-Z0-9_@]{6,50}\b', username)):
                print("username is correct...\n")
                list.append(username)
                
            
            else:
                print("username is incorrect!\n")
            

    def check_password(self,password):          # get password and check it
        
        pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        password =input("Enter your password: ")
        result = re.findall(pattern, password)
        if (result):
            print( "password is correct...\n")
            list.append(password)
            
        else:
            print( "Password is incorrect!\n")
            


    def check_email(self,email):       #get email and check it
        
        email =input("Enter your e-mail address: ")
        if (re.findall(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', email)):
            if (re.search('.com',email)):
                
                print( "email address is correct...\n")
                list.append(email)
            else:
                print("email has not '.com'\n")
            
        else:
            print( "email address is incorrect!\n")
        


    def check_mobile(self,mobile):         #get mobile number and check it
        
        mobile=input("Enter mobile number: ")
        if (re.findall(r'^09[0|1|2|3][0-9]{8}$', mobile)):
            print( "mobile number is correct...\n")
            list.append(mobile)
            
            
        else:
            print( "mobile number is incorrect!\n")



    def check_code(self,code):      #get code and check it

        
        code=input("enter code:")
        i=0
        m=0
        j=0
        sum=0
        if (len(code))==10:      #check code length and be numeric
            for i in range(0,10):
                if '0'<=code[i]<='9':
                    m=m+1
                else:
                    print("there are some word in code...")
                    j=j+1
        elif ('a'<=code[i]<='z' or 'A'<=code[i]<='Z'):
            print("your code must be completely numeric!")


        else:
            print("your code length must be 10!")

        if(m>0):        #check code 
            if (j==0):
                C=int(code)
                o=C
                for i in range (1,11):
                    b=C % 10
                    C=C//10
                    sum=sum+(b*i)
                    r=sum-(o%10)
                    r=r%11
                if (r>=2):
                    r=11-r
                    if r==(o%10):
                        print("your code is correct..")
                        list.append(code)
                    else:
                        print("your code is incorrect!")
                elif (r==0):      #if the last digit code was 0
                    print("your code is correct..")
                    list.append(code)
        
    
        else:
            print("your code is not correct!")
            

        
if __name__ == '__main__':

    list=[]

    check_register.check_name('self','name')
    check_register.check_lastname('self','lastname')
    check_register.check_username('self','username')
    check_register.check_password('self','password')
    check_register.check_email('self','email')
    check_register.check_mobile('self','mobile')
    check_register.check_code('self','code')

    print()
    print()
    print()

    if (len(list)==7):      #if length of list equal to identifiers register is ok...
        print("Congratulations,you have registered...:)")
    else:
        print("sorry... there was a problem!")
        print("Registration was not successful!")
    
    
        
    
    
    
    
    

    
        
