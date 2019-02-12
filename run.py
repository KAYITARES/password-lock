#!/usr/bin/env python3.6
from user import User
from credential import Credential

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
def find_credential(name)
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

def display_names():
    '''
    Function that return all the saved names
    '''
    return User.display_names()
def display_names():
    '''
    Function that return all the saved password
    '''
    return Credential.display_names()

    def main():
         print("Hello Welcome to password locker.What is your name?")
         user_name=input()
         print(f"Hello {user_name}. you have to full your information to create a password locker")
         print('\n')