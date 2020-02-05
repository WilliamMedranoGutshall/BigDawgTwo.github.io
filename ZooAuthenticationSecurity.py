#************************************************
# BigDawg Zoo Authentication Application
#
# Author: William Medrano Gutshall
# IT 499
#************************************************

import hashlib #Needed to access the MD5 Hashing
# ATTENTION: Number of Staff must equal the number of user names and passwords
numberOfStaff = 5  
# ATTENTION: List of all the users
userNameList = ["Will", "Michelle", "Briana","Celina","Mike"]
# ATTENTION: All user passwords - must be in same position as corresponding user name
passWordList = ["e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f"]
# ATTENTION: Job Title - must be in same position as corresponding user name
jobTitleList = ["Administrator", "Zookeeper", "Veterinarian", "Human Resources", "Labor"]
jobMenuSelect = "Empty"

#************User Name and Password Handling*******************************
#User Name Storage
def userName(userNameChecker):
    try:
        userNameListCounter = 0     #This is a counter used in the for loop
        nameReturnBool = False
        while userNameListCounter < numberOfStaff:
            if userNameChecker == userNameList[userNameListCounter]:
                nameReturnBool = True
                break
            userNameListCounter = userNameListCounter + 1
        return nameReturnBool, userNameListCounter
    except:
        print("Error occured verifying user name.\nPlease restart program.")   

#Password Storage
def password(passWordChecker, userNamePosition):
    try:
        passWordCheckerBool = False  
        hashedPassWord = hashlib.md5(passWordChecker.encode())
        hashedPassWordHex = hashedPassWord.hexdigest()
        if hashedPassWordHex == passWordList[userNamePosition]:
            passWordCheckerBool = True
        return passWordCheckerBool
    except:
        print("Error occured verifying user name.\nPlease restart program.")
#****************************************************************************

#*************Staff Menus by job title****************************************
#Menu for Zookeeper
def staffZooKeeper(displayName):
    jobMenuSelect = "Empty"         
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Zookeeper", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nChecking on the animals.")
                print("Reporting abnormalities to veterinarian staff.\nFeeding the animals.")
                print("Cleaning the animal enclosures.\n")
    except:     #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")   
    return

#Menu for Veterinarian
def staffVet(displayName):
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Veterinarian", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nPerforming wellness checks.")
                print("Treating sick or injured animals.\nGuiding the zookeepers on nutritional needs of the animals.")
                print("Filling out all medical records for animals treated.\n")
    except:        #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for Staff Administrator
def staffAdmin(displayName):
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Administrator", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nCoordinating daily activities of all the staff.")
                print("Procurement of zoo supplies.\nProviding financial information to accounting.")
                print("Customer service issue resolutions.\n")
    except:   #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for HR Administrator
def staffAdminHR(displayName):
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Human Resource administrator", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nMonitor staffing requirements.")
                print("Discipline employees as needed.\nHire high quality staff to provide best guest experience.")
                print("Maintain employee records in zoo system.\n")
    except:
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for General Labor Staff
def staffWorker(displayName):
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Staff Memeber", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nEnsure that work area is clean and ready to be opened on time.")
                print("Assist guests as needed.\nProvide feedback to supervisor on improving customer experience.")
                print("Make sure area is cleaned up before clocking out for the day.\n")
    except:
        print("Error occured during menu selection.\nPlease restart program.")
    return
#*****************************************************************


#**********Main Program*******************************************
def main():
    #Variable definitions for main program
    userNameIn = "Empty"
    userNameInBool = False
    passWordIn = "Empty"
    passWordInBool = False
    authenticationCounter = 0
    userNameIndexPosition = 0
    userJob = "Empty"
    
    while authenticationCounter <= 3:
        print ("Welcome to the BigDawg Zoo of San Antonio\n")
               
        #User Entry Block
        userNameIn = input("Please Enter Your User Name to Continue\nOr type Exit to Shutdown Application")
        while len(userNameIn) > 10:                   #Used to prevent buffer overflow attacks 
            try:
                userNameIn = input("Sorry, usernames are 10 characters or less.\nPlease Enter Your User Name to Continue\nOr type Exit to Shutdown Application")
            except:
                print("Error occured during input collection.\nPlease restart program.")
        #Allows user to end program
        if userNameIn == "exit" or userNameIn == "Exit":
            break            
        passWordIn = input("Please provide your password")
        while (len(passWordIn) < 4) or (len(passWordIn) > 10): #Prevents too small of passwords and buffer overflow attacks from too long on input
            try:
                passWordIn = input("Sorry, passwords are between 4 and 10 characters.\nPlease Enter Your Password to Continue")
            except:
                print("Error occured during input collection.\nPlease restart program.")
        #Checks user name - if valid then checks password
        userNameInBool, userNameIndexPosition = userName(userNameIn)                                    
        if userNameInBool == True:
            passWordInBool = password(passWordIn, userNameIndexPosition)
            if passWordInBool == True:
                authenticationCounter = 0
                userJob = jobTitleList[userNameIndexPosition]
                if userJob == "Zookeeper":
                    staffZooKeeper(userNameIn)
                elif userJob == "Veterinarian":
                    staffVet(userNameIn)
                elif userJob == "Administrator":
                    staffAdmin(userNameIn)
                elif userJob == "Human Resources":
                    staffAdminHR(userNameIn)
                elif userJob == "Labor":
                    staffWorker(userNameIn)
                else:
                    print("\nI'm sorry. The system is unable to resolve your current position.")
                    print("\nPlease see your administrator to resolve this issue.")
            else:
                authenticationCounter = authenticationCounter + 1
                print("\nUser name and passwords do not match.")
                print("Attempt ", authenticationCounter, " of 3")
                if authenticationCounter == 3:
                    break
                print("\nPlease try again or contact your admin for assistance.\n\n")      
        #Failed verification
        else:
            authenticationCounter = authenticationCounter + 1
            print("\nUser name and passwords do not match.")
            print("Attempt ", authenticationCounter, " of 3")
            if authenticationCounter == 3:
                break
            print("\nPlease try again or contact your admin for assistance.\n\n")           
    print("\nHave a Great Day\n")
  
#**********************************************************************************          
        
    
    



main()