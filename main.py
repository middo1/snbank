import json
import random
import time
import os


def getpass(usrn, pw):
    with open("staff.txt", 'r') as file:
        res = json.load(file)
        if usrn == "Middo":
            if pw == res["Middo"]["Password"]:
                return True
            else:
                return False
        elif usrn == "Shenah":
            if pw == res["Shenah"]["Password"]:
                return True
            else:
                return False
        else:
            return None
            
            
def addcont(acctmail, acctname, startbal, accttype):
    with open("customer.txt" , "r") as file:
        try :
            customers = json.load(file)
        except:
            customers = dict()   
        file.close
    acctno = "" 
    customer = dict()
    while len(acctno) < 10:
        x = random.randint(0,9)
        acctno += str(x)    
        if len(acctno) == 10:
            customer["Account number"] = acctno                  
    customer["Account Name"] = acctname
    customer["Account Email"] = acctmail 
    customer["Starting Balance"] = startbal 
    customer["Account Type"] = accttype
    customers[acctno] = customer
    with open("customer.txt", "w") as file:
        json.dump(customers, file, indent=2)
    return acctno

def sessions(things):
    FILE = ".session"
    with open(FILE, "a") as file:
        file.write("\n" +things+ " " +str(time.asctime())) 
    return FILE
  
    
    
print("##### WELCOME TO THE STAFF LOGIN CONSOLE APP #####") 
while True:
    fcond = input("Please select these options by entering the number before the option \n [1] Staff login \n [2] Close app ") 
    try:
        fcond = int(fcond) 
    except:
        print("Invalid input please try again ") 
        fcond = input("Press enter key to try again ") 
    if fcond == 1:
        print("WELCOME") 
        name = input("Enter your username : ") 
        password = input("Enter your password : ")
        scond = None
        while scond != 3:
            if getpass(name, password) == True:
                print("Welcome back", name) 
                sessions(name + " logged in at") 
                while scond != 3:
                    scond = input("Please select these options by entering the number before the option \n [1] Create new account \n [2] Check account details \n [3] Log out ") 
                    try:                        
                        scond = int(scond)
                    except:
                        print("invalid input please try again") 
                        scond = input("Press enter key to try again ") 
                    if scond == 1:
                        aname = input("Enter customer's full name : ")
                        amail = input("Enter customer's Email : ")
                        sbal = input("Enter customer's starting balance : ")
                        atype = input("Enter customer's Account type: ")
                        res = addcont(amail, aname, sbal, atype) 
                        print("The new account number is", res) 
                        continue
                    elif scond == 2:
                            try:                                                                                          
                                with open("customer.txt","r") as file:
                                    chk = json.load(file) 
                                acno = input("Enter account number of the required details: ") 
                                while True:
                                    if chk.__contains__(acno) == True:
                                        print("Account Name :", chk[acno]["Account Name"]) 
                                        print("Account Email :", chk[acno]["Account Email"]) 
                                        print("Account Number:", chk[acno]["Account number"]) 
                                        print("Account Type :", chk[acno]["Account Type"]) 
                                        print("Starting Balance :", chk[acno]["Starting Balance"]) 
                                        break
                                    else:
                                        acno = input("Please enter required account number of the required details or enter cancel to go back : ")
                                        if acno == "cancel":
                                            break
                            except :
                                print("There is no customer registered yet, Please try adding a customer ")                                                               
                    elif scond == 3:
                        
                        os.remove(sessions(name + "user logged out" )) 
                        print("Thank you for using  our services", name) 
                        continue
                    elif scond != str():
                        print("Wrong option please try again") 
                    
            elif getpass(name, password) == False:
                print("Invalid username or password, try again") 
                name = input("Enter your username : ") 
                password = input("Enter your password : ") 
                
            elif getpass(name, password) == None:
                print("We don't have your details with us, Check your details and try again thank you" ) 
                break 
    elif fcond == 2:
        print("Closing app.... ") 
        break
    elif fcond != str():
        print("Wrong option number try again") 
        continue
    
    
    
    
    
    
    
    
            

