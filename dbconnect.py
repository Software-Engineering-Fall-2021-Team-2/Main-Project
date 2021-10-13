import psycopg2
from psycopg2 import Error

def checkdb(id):
    try:
        #Connect to database
        conn = psycopg2.connect(user="fyvfgbrmzsdxqv",
                                password="f9bd96ad063a4183904cc463789f189038c4a5fdab483a05001908ee40a36a30",
                                host="ec2-18-214-214-252.compute-1.amazonaws.com",
                                port="5432",
                                database="d2shnh1e69v774")
        print("Connection Open")
        cur = conn.cursor()
        cur.execute("select * from player;")
        table = cur.fetchall()
        id_numbers = [f_tuple[0] for f_tuple in table]
        #print(id_numbers)
        if isinstance(id, int):
            if id in id_numbers:
                id_exists = True
            else:
                id_exists = False
    except (Exception, Error) as error:
        print("Error while connecting to DB", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Connection to DB is closed")
            #return(id_exists)

def retrieveCode(id):
    try:
        #Connect to database
        conn = psycopg2.connect(user="fyvfgbrmzsdxqv",
                                password="f9bd96ad063a4183904cc463789f189038c4a5fdab483a05001908ee40a36a30",
                                host="ec2-18-214-214-252.compute-1.amazonaws.com",
                                port="5432",
                                database="d2shnh1e69v774")
        print("Connection Open")
        cur = conn.cursor()
        cur.execute("select * from player;")
        for record in cur:
            if record[0] == id:
                result = record[3]
                break
    except (Exception, Error) as error:
        print("Error while connecting to DB", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Connection to DB is closed")
            #return(result)

def addRecord(record):
    try:
        #Connect to database
        conn = psycopg2.connect(user="fyvfgbrmzsdxqv",
                                password="f9bd96ad063a4183904cc463789f189038c4a5fdab483a05001908ee40a36a30",
                                host="ec2-18-214-214-252.compute-1.amazonaws.com",
                                port="5432",
                                database="d2shnh1e69v774")
        print("Connection Open")
        cur = conn.cursor()
        insert_query = """ Insert into player (id,first_name, last_name, codename) values (%s,'None','None',%s)"""
        cur.execute(insert_query, record)
        conn.commit()
        #print("Record Successfully Added")
    except (Exception, Error) as error:
        print("Error while connecting to DB", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Connection to DB is closed")
