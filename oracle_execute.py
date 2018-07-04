#!/usr/bin/python

import cx_Oracle
from sqlalchemy import *
from sqlalchemy.orm import *

#Host - Ip ou DNS do banco Oracle que vai se conectar para ativar o supplement logs nas tabelas
#user - usuario para conectar no banco (Também é o schema)
#password - necessário o user a password estarem sincronizados (na ordem)

host = ""
user = [""]
password = [""]

def get_tables(host, user, password):
    for u, p in zip(user, password):
        #Buscar tabelas relacionadas ao usuario na lista acima
        query= "SELECT table_name, owner FROM all_tables WHERE owner='"+str(str(u).upper())+"' ORDER BY owner, table_name"
        print query
        engine = create_engine("oracle://"+u+":"+p+"@"+host+"/ORCL")
        conn = engine.connect()
        result = conn.execute(query)
        for table in result:
            alter_tables(conn, u, p, str(table[0]))
        conn.close()

def alter_tables(conn, u, p, tabela):
    #executa a ativacao do supplent logging em todas as tabelas do schema informado
    try:
        conn.execute("alter table "+u+"."+tabela+" add supplemental log data (ALL) columns")
        print "Schema: "+u+"Ativando supplemental loggin em "+tabela
    except:
        print "Schema "+ u + ": Supplemental logging ja ativado na tabela "+tabela

get_tables(host, user, password)

