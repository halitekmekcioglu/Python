import pandas as pd
import glob
import psycopg2
import numpy
from psycopg2.extensions import register_adapter, AsIs


def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)
def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)
register_adapter(numpy.float64, addapt_numpy_float64)
register_adapter(numpy.int64, addapt_numpy_int64)


def connect_db(frame,numberoffile):
    conn = psycopg2.connect(database="postgresq", user="yourusername", password="yourpwd",
                            host="yourhost", port="5432")  # database connection

    print("DB opened successfully")
    sqlpart(conn, frame,numberoffile)


def sqlpart(conn, frame,numberoffile):
    cur = conn.cursor()

    sql = """INSERT INTO actuals (timeslot,unit_id,actual) 
            VALUES(%s,%s,%s) 
            ON CONFLICT (timeslot,unit_id)
            DO UPDATE SET actual = EXCLUDED.actual"""   #This part is depends on your table infos

    for x in range(len(frame)):
        val = frame[0][x], frame[1][x], frame[2][x]

        cur.execute(sql, val)
    conn.commit()
    print(numberoffile, "different Excel File and", len(frame), " row data are inserted to DB")
    print("note: in case of same value, sql was overwriten")

def patika():

    path = r'C:\Users\...../Desktop\FolderExcel'  #path of the folder that we keep excel files
    all_files = glob.glob(path + "/*.xlsx")

    templist = []

    for filename in all_files:
        df = pd.read_excel(filename, index_col=None,header=None)
        templist.append(df)

    frame = pd.concat(templist, axis=0, ignore_index=True)

    connect_db(frame,len(all_files))


patika()

