#!/usr/bin/env python3.6
from user import User
from credential import Credential
import sys

def create_user(fname,lname,password,confirmation_password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,password,confirmation_password)
    return new_user
    
def create_credential(account_name,password):
    '''
    Function to create a credential user
    '''
    new_credential = Credential(account_name,password)
    return new_credential

def save_names(user):
    '''
    Function to save user
    '''
    user.save_user()
def save_names(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()
def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)
def find_credential(name):
     '''
     Function that finds credential by password and return credential
     '''
     return Credential.find_by_name(name)
def check_existing_names(name):
    '''
    Function that check if a name exists with that name and return a boolean
    '''
    return User.user_exist(name)
def check_existing_names(name):
    '''
    Function that check if a name exists with that name and return a boolean
    '''
    return Credential.credential_exist(name)

def display_names1():
    '''
    Function that return all the saved names
    '''
    return User.display_names()
def display_names():
    '''
    Function that return all the saved password
    '''
    return Credential.display_credential()
def del_names(credential):
     '''
     Function that delete credential
     '''
     credential.delete_credential()

def main():
         print("Hello Welcome to password locker.What is your name?")
         user_name=input()
         print(f"Hello {user_name}. you have to full your information to create a password locker")
         print('\n')

         print("New Password")
         print("-"*10)

         print("First Name......")
         f_name= input()
     
         print("Lat Name......")
         l_name = input()

         print("Password.......")
         password = input()

         print("Confirmation Passord....")
         confirmation = input()
         if password == confirmation:
              print("account successfully created")
         else:
              print("password incorrect")
              sys.exit()
         print("now let procceed to login to our account")
         print('\n')
         print("enter your first name (the name must the same to the as the first name you entered previously ):")
         print('\n')
         print("enter first name")
         login_name=input()
         print("enter password")
         password=input()
    
         if password==password and f_name==login_name:
              print("successfully logged in")
              print('\n')
         else:
              print(f"password: {password} or name: {login_name} incorrect. Next time , Please confirm the password correctly.")  
              sys.exit()   

         while True:
              print("Use these short codes : np - create new password, dp - display password, fp -find a password, del - delete password, gp - generate password, ex -exit the password list")
               
              short_code = input().lower()

              if short_code == 'np':
                    print("New Account")
                    print("-"*20)

                    print("Account Name......")
                    account_name = input()

                    print("password.....")
                    password =input()

                    save_names(create_credential(account_name,password)) # create and save password
                    print('\n')
                    print(f"Credential Name..........{account_name}")
                    print(f"Password................. {password}")
                    print("New Account created")
                    print('\n')

              elif short_code == 'dp':
                   if display_names():
                        print("Here is a list of all password ")
                        print('\n')

                        for credential in display_names():
                             print(f"credential name.......{credential.account_name}")
                             print(f"password..............{credential.password}")
                        print('\n')
                   else:
                       print('\n')
                       print("You dont seem to have any password saved yet")
                       print('\n')

              elif short_code == 'fp':
                   print("Enter search  Credential Name")
                   search_name = input()
                   if check_existing_names(search_name):
                        search_credential =  find_credential(search_name)
                        print(f"{search_credential.account_name}{search_credential.password}")
                        print('-' * 20)
                        print(f"credential name.......{search_credential.account_name}")
                        print(f"password.........{search_credential.password}")

                   else:
                        print("that password does not exist")

              elif short_code == 'del':
                   print("enter name of the account you wish to delete")
                   search_name=input()
                   if check_existing_names(search_name):
                        Credential = find_credential(search_name) 
                        del_names(Credential)
                        print(f"{Credential.account_name} deleted")
                        print('\n')
                        print("credential and password deleted")
                   else:
                        print("account name does not exist")  
              elif short_code == "ex":
                   print("bye.........")
                   break
              else:
                   print("I really didn't get that.please use the short code")


if __name__=='__main__':
     main()