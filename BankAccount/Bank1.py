#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:13:32 2021
@author: jarrett
This is the login screen 
"""
from os import read
import Bank2

#Username Info
userName='Username'
passWord='Password'

uN=input("Enter username: ")
pW=input("Enter password: ")

attempts=1

while userName != uN or passWord != pW and attempts <4:
     print("Invalid username or password")
     uN=input("Enter user name: ")
     pW=input("Enter password: ")
     attempts+=1
     
    execfile("MacintoshHD/Users/jarrett/Documents/GitHub/BankAccount-Python/BankAccount/Bank2.py")


    
   
else:
    print("Your account is disabled")
