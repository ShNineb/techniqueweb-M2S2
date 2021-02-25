#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:32:02 2021

@author: meg
"""
import sqlite3
import json
import re
from werkzeug.security import generate_password_hash
#insert new information to database
database = sqlite3.connect("db_copy.sqlite")
cursor = database.cursor()
# create database
def create_datase():
    sql="""
    create table geonames (
        geonameid INT NOT NULL UNIQUE,
        name text NOT NULL,
        asciiname text ,
        alternatenames text,
        latitude Float,
        longitude Float,
        feature_class text,
        feature_code text,
        country_code text,
        cc2 char(2),
        admin1_code INT,
        admin2_code INT,
        admin3_code INT,
        admin4_code INT,
        population INT,
        elevation INT,
        dem INT,
        timezone text,
        modification date,
        modified_by text,
        PRIMARY KEY(geonameid)
        )
    """
    cursor.execute(sql)
    # cursor.close()
    
    
    
def insert_data():
    with open("FR.txt", "r") as data:
        for l in data:
            l = re.sub(r" +", " ", l)
            if "," in l:
                l=l.replace(","," " )
            line = l.split("\t")
            sql = f'INSERT INTO geonames (geonameid, name, asciiname, alternatenames,latitude,longitude,feature_class,feature_code,country_code,cc2,admin1_code,admin2_code,admin3_code,admin4_code,population,elevation,dem,timezone,modification) values ("{line[0]}","{line[1]}","{line[2]}","{line[3]}","{line[4]}","{line[5]}","{line[6]}","{line[7]}","{line[8]}","{line[9]}", "{line[10]}","{line[11]}","{line[12]}","{line[13]}","{line[14]}","{line[15]}", "{line[16]}","{line[17]}","{line[18]}");'
            print(sql)
            # break
            cursor.execute(sql)
            database.commit()
    
    
    cursor.close()
    database.close()
    print("done!")
    
create_datase()
insert_data()
