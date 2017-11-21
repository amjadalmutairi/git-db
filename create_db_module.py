# -*- coding:utf-8 -*-
import sqlite3
from enum import Enum

#id , title , description , command , toCopy , approved

class approved(Enum):
    YES=1
    NO=0

def get_db_connection():
     return sqlite3.connect("git-commands.db")

def create_db():
    db_connetion = get_db_connection()
    cursor = db_connetion.cursor()
    q = ""
    with open('schem.sql', 'r') as f:
        q = f.read()
    cursor.executescript(q)
    db_connetion.commit()
    db_connetion.close()
    print("Command table is created successfully >.<")

def insert_commands():
    db_connetion = get_db_connection()
    cursor = db_connetion.cursor()
    file_content = ""
    with open("git_commands.txt" , 'r',encoding="utf-8" ) as f:
        file_content = f.read();
        f.close()
    lines = file_content.split("\n")
    id_count = 1
    i = 0
    while i < len(lines):
        title = lines[i]
        if not lines[i+1] == "":
            description = lines[i+1]
        else:
            description = None
        command  = lines[i+2]
        toCopy  = lines[i+3]
        q = '''INSERT INTO COMMANDS (id,title,description,command,toCopy,approved) VALUES (?,?,?,?,?,?)'''
        cursor.execute(q,(id_count,title,description,command,toCopy,approved.YES.value))
        i = i + 5
        id_count = id_count + 1
    db_connetion.commit()
    db_connetion.close()
    print("Commands are is inserted successfully >.<")

def approve_command(id):
    db_connetion = get_db_connection()
    cursor = db_connetion.cursor()
    q = '''UPDATE Commands SET approved=1 WHERE id=?'''
    cursor.execute(q,(id,))
    db_connetion.commit()
    db_connetion.close()
    print("The command with id:", id , "has been approved successfully >.<")

def upadet_value_to_copy(id, value):
    value = value.replace("\n" , " ").strip().rstrip()
    db_connetion = get_db_connection()
    cursor = db_connetion.cursor()
    q = '''UPDATE Commands SET toCopy=? WHERE id=?'''
    cursor.execute(q,(value,id))
    db_connetion.commit()
    db_connetion.close()
    print("The command with id:", id , "has been updated successfully >.<")

def update_entire_row(id,new_title,new_des,new_command,new_toCopy,approved):
    db_connetion = get_db_connection()
    cursor = db_connetion.cursor()
    q = '''UPDATE Commands SET title=? , description=? , command=? , toCopy=? , approved=?   WHERE id=?'''
    cursor.execute(q,(new_title,new_des,new_command,new_toCopy,approved,id))
    db_connetion.commit()
    db_connetion.close()
    print("The command with id:", id , "has been updated successfully >.<")

def print_rwos():
    db_connetion = get_db_connection()
    cursor = db_connetion.cursor()
    q = '''SELECT * FROM Commands'''
    cursor.execute(q)
    rwos = cursor.fetchall()
    for row in rwos:
        print(row)
    db_connetion.close()
