import sys
#import pandas as pd
#import pandasql as ps
from flask import Flask, render_template, redirect, request
import mysql.connector
sys.path.append("/Users/peterjmyers/Documents/Projects/GitHub/RobustReport/app")
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # TODO: Remove this line in production
@app.route('/')
@app.route('/index')
def index():
    rows = []
    local_cnx = mysql.connector.connect(user= "root", password= "", database="robust_report", host= "localhost", port= 3306)
    try:
        cur = local_cnx.cursor()
        cur.execute("SELECT name from report")
        rows = cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        local_cnx.close()
        return render_template("index.html",rows=rows)

@app.route('/new', methods=['POST'])
def new_report():
    result = request.form
    checkbox_values = [0]
    for i in range(1,int(result.get("query_count"))+1):
        if "query"+str(i)+"_visible_checkbox" in result:
            checkbox_values.append(1)
        else:
            checkbox_values.append(0)
    local_cnx  = mysql.connector.connect(user= "root", password= "", database="robust_report", host= "localhost", port= 3306)
    try:
        cur = local_cnx.cursor()
        cur.execute("""INSERT INTO report (name, doe, dlu) values ('{}', now(), now())""".format(result.get("report_name")))
        local_cnx.commit()

        for i in range(1,int(result.get("query_count"))+1):
            cur.execute("""INSERT INTO dataquery (report_id, name, sql_, is_visible, connection, doe, dlu) SELECT max(id),'{}', '{}', '{}', '{}', now(), now() from report""".format(result.get("query"+str(i)+"_name"), result.get("query"+str(i)+"_sql"), checkbox_values[i], result.get("query"+str(i)+"_connection")))
            local_cnx.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except Exception as e:
        print(e)
    finally:
        local_cnx.close()
        return redirect("/")
