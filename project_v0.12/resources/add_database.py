#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:32:02 2021

@author: meg
"""
import sqlite3
import json
from werkzeug.security import generate_password_hash
#insert new information to database
database = sqlite3.connect("userslist.sqlite")
cursor = database.cursor()
# create database
def create_datase():
    sql='''
    create table usersList (
        id MEDIUMINT NOT NULL,
        username CHAR(50) NOT NULL UNIQUE,
        password text NOT NULL,
        name text,
        PRIMARY KEY(id)
        )
    '''
    cursor.execute(sql)
    # cursor.close()
    
    
    
def insert_data():
    with open("users.json", "r") as json_data:
        dicte_users = json.loads(json_data.read())
    # dicte_users = json.loads(str"users.json")
        # print(type(dicte_users))
        for key in dicte_users.keys():
            id_user = int(key)
            username = dicte_users[key]["prenom"]+dicte_users[key]["nom"]
            username = username.lower()
            name = dicte_users[key]["prenom"]
            password = generate_password_hash(username+str(key),method='sha256')
            # print(f"username:{username},name:{name},password:{password}")
            # sql = '''insert into user
            # (username, name, password)
            # values
            # (username,name,password)
            # '''
            print(f"INSERT INTO user (id, username, name, password) values ({id_user} {username},{name},{password});")
            cursor.execute(f"INSERT INTO usersList (id, username, name, password) values ('{id_user}', '{username}','{name}','{password}');")
            database.commit()
    
    
    cursor.close()
    database.close()
    print("done!")
    
# create_datase()
insert_data()