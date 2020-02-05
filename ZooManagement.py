#************************************************
# BigDawg Zoo Management Application
#
# Author: William Medrano Gutshall
# IT 499
#************************************************
# MAKE SURE TO USE ../startMongod.sh BEFORE RUNNING

#Accessing MongoDB
import json
import sys
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
connection = MongoClient('localhost',27017)
db = connection['BigDawgZoo']
collection = db['ZooTasks']

import hashlib #Needed to access the MD5 Hashing
# ATTENTION: Number of Staff must equal the number of user names and passwords
numberOfStaff = 5  
# ATTENTION: List of all the users
userNameList = ["Will", "Michelle", "Briana","Celina","Mike"]
# ATTENTION: All user passwords - must be in same position as corresponding user name
passWordList = ["e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f", "e2fc714c4727ee9395f324cd2e7f331f"]
# ATTENTION: Job Title - must be in same position as corresponding user name
jobTitleList = ["Human Resources", "Zookeeper", "Veterinarian", "Administrator", "Labor"]
jobMenuSelect = "Empty"


#******************Database Management***************************************
#Read Job Tasks - All employees can read their tasks - Human Resources and Administrator can read any employees tasks
def read_document(userNameSub):
  returnStatement = "Please see your immediate manager with any questions."
  try:
    zooTask_doc = collection.find_one({'userName':userNameSub},{'_id':0, 'jobTaskOne':1})
    stringtoprint = json.dumps(zooTask_doc, indent=1, default=json_util.default)
    print(stringtoprint)
    zooTask_doc = collection.find_one({'userName':userNameSub},{'_id':0, 'jobTaskTwo':1})
    stringtoprint = json.dumps(zooTask_doc, indent=1, default=json_util.default)
    print(stringtoprint)   
    zooTask_doc = collection.find_one({'userName':userNameSub},{'_id':0, 'jobTaskThree':1})
    stringtoprint = json.dumps(zooTask_doc, indent=1, default=json_util.default)
    print(stringtoprint)
    zooTask_doc = collection.find_one({'userName':userNameSub},{'_id':0, 'jobTaskFour':1})
    stringtoprint = json.dumps(zooTask_doc, indent=1, default=json_util.default)
    print(stringtoprint)
    return(returnStatement)
  except Exception as ve:
    print "Error: Read Process was unsuccessful"
    return False
    sys.exit(str(ve))

#Insert new employee jobs - Only available to AdminHR 
def insert_document(docin):
  returnStatement = "Insertion was a success"
  try:
    collection.insert_one(docin)
    return(returnStatement)
  except Exception as ve:
    return False
    sys.exit(str(ve))
    
#Delete employee jobs - Only available to Human Resources
def delete_document(userNameSubD):
  returnStatement = "Removal of employee task list was a success."
  try:
    mydquery = {"userName":userNameSubD}
    collection.delete_one(mydquery)
    return(returnStatement)
  except Exception as ve:
    print "Error: Delete Process was unsuccessful"
    return False
    sys.exit(str(ve))
    
#Update employee jobs - Only available to Human Resources and Administrator
def update_document(userNameSubU, updatedData):
  returnStatement = "Update process was a success."
  try:
    myuquery = {"userName":userNameSubU}
    newvalues = {"$set" : updatedData}
    collection.update_one(myuquery, newvalues)
    return(returnStatement)
  except Exception as ve:
    print "Error: Update Process was unsuccessful"
    return False
    sys.exit(str(ve))
#******************************************************************************

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
            print("\n\n\n")
            print("Welcome Zookeeper", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print read_document(displayName)
    except:     #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")   
    return

#Menu for Veterinarian
def staffVet(displayName):
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\n\n\n")
            print("Welcome Veterinarian", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
              print read_document(displayName)
    except:        #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for Staff Administrator
def staffAdmin(displayName):
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\n\n\n")
            print("Welcome Administrator", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\nu - Update employee job tasks\nv - View Employee Tasks\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d") and (jobMenuSelect is not "u") and (jobMenuSelect is not "v"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print read_document(displayName)
            if jobMenuSelect is "u":
              print "Updating an employee job task record."
              updateName = input("Enter Employee Name to be updated")
              whichTask = input("Which task number do you wish to update (one, two, three, of four)?")
              while (whichTask is not "one") and (whichTask is not "two") and (whichTask is not "three") and (whichTask is not "four"):
                print("I am sorry. The choices are one, two, three, or four only.")
                whichTask = input("Please enter one, two, three, or four to update that task")
              if (whichTask is "one"):
                updateJob = input("Enter the first task\n")
                updateData = {"jobTaskOne":updateJob}
              elif (whichTask is "two"):
                updateJob = input("Enter the second task\n")
                updateData = {"jobTaskTwo":updateJob}
              elif (whichTask is "three"):
                updateJob = input("Enter the third task\n")
                updateData = {"jobTaskThree":updateJob}
              elif (whichTask is "four"):
                updateJob = input("Enter the fourth task\n")
                updateData = {"jobTaskFour":updateJob}
              else:
                print("Job update failed. Please try again or contact Help Desk for support")
              print update_document(updateName,updateData)
            if jobMenuSelect is "v":
              print("Viewing an employee task list.")
              viewName = input("Please enter the employee name to be viewed.")
              print read_document(viewName)
    except:   #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for HR Administrator
def staffAdminHR(displayName):
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\n\n\n")
            print("Welcome Human Resource administrator", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\ni - Insert new employee tasks\nr - Remove employee task list\nu - Update employee task list\nv - View an employee task list\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d") and (jobMenuSelect is not "i") and (jobMenuSelect is not "r") and (jobMenuSelect is not "u") and (jobMenuSelect is not "v"):
              jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
              print read_document(displayName)
            if jobMenuSelect is "i":
              print "Inserting a new employee job list.\n\n"
              insertName = input("Enter the Employee Name\n")
              insertJobOne = input("Enter the first task\n")
              insertJobTwo = input("Enter the second task\n")
              insertJobThree = input("Enter the third task\n")
              insertJobFour = input("Enter the fourth task\n")
              myDocument={"userName":insertName, "jobTaskOne": insertJobOne, "jobTaskTwo": insertJobTwo, "jobTaskThree": insertJobThree, "jobTaskFour": insertJobFour}
              print insert_document(myDocument)
            if jobMenuSelect is "r":
              print "Removing an employee job task record."
              removeName = input("Please enter the employee name to be removed.")
              print delete_document(removeName)
            if jobMenuSelect is "u":
              print "Updating an employee job task record."
              updateName = input("Enter Employee Name to be updated")
              whichTask = input("Which task number do you wish to update (one, two, three, of four)?")
              while (whichTask is not "one") and (whichTask is not "two") and (whichTask is not "three") and (whichTask is not "four"):
                print("I am sorry. The choices are one, two, three, or four only.")
                whichTask = input("Please enter one, two, three, or four to update that task")
              if (whichTask is "one"):
                updateJob = input("Enter the first task\n")
                updateData = {"jobTaskOne":updateJob}
              elif (whichTask is "two"):
                updateJob = input("Enter the second task\n")
                updateData = {"jobTaskTwo":updateJob}
              elif (whichTask is "three"):
                updateJob = input("Enter the third task\n")
                updateData = {"jobTaskThree":updateJob}
              elif (whichTask is "four"):
                updateJob = input("Enter the fourth task\n")
                updateData = {"jobTaskFour":updateJob}
              else:
                print("Job update failed. Please try again or contact Help Desk for support")
              print update_document(updateName,updateData)
            if jobMenuSelect is "v":
              print("Viewing an employee task list.")
              viewName = input("Please enter the employee name to be viewed.")
              print read_document(viewName)
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
                print read_document(displayName)
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
        
    
#****************Executes the Main***********************************************
main()
#********************************************************************************