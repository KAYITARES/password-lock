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