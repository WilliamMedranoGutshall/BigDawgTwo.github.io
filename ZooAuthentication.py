#************************************************
# BigDawg Zoo Authentication Application
#
# Author: William Medrano Gutshall
# IT 499
#************************************************




import hashlib #Needed to access the MD5 Hashing
# ATTENTION: Number of Staff must equal the number of user names and passwords
numberOfStaff = 3  
# ATTENTION: List of all the users
userNameList = ["Will", "Michelle", "Briana"]
# ATTENTION: All user passwords - must be in same position as corresponding user name
passWordList = ["e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f"]
# ATTENTION: Job Title - must be in same position as corresponding user name
jobTitleList = ["Administrator", "Zookeeper", "Veterinarian"]
jobMenuSelect = "Empty"

#************User Name and Password Handling*******************************
#User Name Storage
def userName(userNameChecker):
    userNameListCounter = 0     #This is a counter used in the for loop
    nameReturnBool = False
    while userNameListCounter < numberOfStaff:
        if userNameChecker == userNameList[userNameListCounter]:
            nameReturnBool = True
            break
        userNameListCounter = userNameListCounter + 1
    return nameReturnBool, userNameListCounter   

#Password Storage
def password(passWordChecker, userNamePosition):
    passWordCheckerBool = False  
    hashedPassWord = hashlib.md5(passWordChecker.encode())
    hashedPassWordHex = hashedPassWord.hexdigest()
    if hashedPassWordHex == passWordList[userNamePosition]:
        passWordCheckerBool = True
    return passWordCheckerBool
#****************************************************************************

#*************Staff Menus by job title****************************************
#Menu for Zookeeper
def staffZooKeeper(displayName):
    jobMenuSelect = "Empty"
    while jobMenuSelect is not "l":
            print("\nWelcome Zookeeper", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nChecking on the animals.")
                print("Reporting abnormalities to veterinarian staff.\nFeeding the animals.")
                print("Cleaning the animal enclosures.\n")
    
    return

#Menu for Veterinarian
def staffVet(displayName):
    jobMenuSelect = "Empty"
    while jobMenuSelect is not "l":
        print("\nWelcome Veterinarian", displayName)
        jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
        while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
            jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
        if jobMenuSelect is "d":
            print(displayName, "your daily duties include:\nPerforming wellness checks.")
            print("Treating sick of injured animals.\nGuiding the zookeepers on nutritional needs of the animals.")
            print("Filling out all medical records for animals treated.\n")
    return

#Menu for Staff Administrator
def staffAdmin(displayName):
    jobMenuSelect = "Empty"
    while jobMenuSelect is not "l":
        print("\nWelcome Administrator", displayName)
        jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
        while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
            jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
        if jobMenuSelect is "d":
            print(displayName, "your daily duties include:\nCoordinating daily activities of all the staff.")
            print("Procurement of zoo supplies.\nProviding financial information to accounting.")
            print("Customer service issue resolutions.\n")
    return

#Menu for HR Administrator
def staffAdminHR(displayName):
    jobMenuSelect = "Empty"
    while jobMenuSelect is not "l":
        print("\nWelcome Human Resource administrator", displayName)
        jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
        while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
            jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
        if jobMenuSelect is "d":
            print(displayName, "your daily duties include:\nFutureJob1.")
            print("FutureJob2.\nFutureJob3.")
            print("FutureJob4.\n")
    return

#Menu for General Labor Staff
def staffWorker(displayName):
    jobMenuSelect = "Empty"
    while jobMenuSelect is not "l":
        print("\nWelcome Staff Memeber", displayName)
        jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
        while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
            jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
        if jobMenuSelect is "d":
            print(displayName, "your daily duties include:\nFutureJob1.")
            print("FutureJob2.\nFutureJob3.")
            print("FutureJob4.\n")
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
        #Allows user to end program
        if userNameIn == "exit" or userNameIn == "Exit":
            break            
        passWordIn = input("Please provide your password")

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