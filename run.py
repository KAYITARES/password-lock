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
