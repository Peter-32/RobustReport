import sys
import pandas as pd
import pandasql as ps
from flask import Flask, render_template, redirect, request
sys.path.append("/Users/peterjmyers/Documents/Projects/GitHub/RobustReport/app")
from lib.SQL_df_util.SQL_df_util import *
from lib.connection.connection import *
from lib.file_util.file_util import *
from lib.connection.config import *
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Remove this line in production
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template("index.html",title="Home",user=user)

@app.route('/new', methods=['POST'])
def new_report():
    result = request.form
    local_cnx, local_cnx2  = open_db_connections([config_localhost, config_localhost])
    try:
        insert_sql_statement1 = "INSERT INTO report (name, doe, dlu) values ('{}', now(), now())".format(result.get("report_name"))
        save_to_db(insert_sql_statement1, local_cnx)
        max_report_id = _query_for_max_report_id()
        print("HI")
        print(max_report_id)
        insert_sql_statement2 = "INSERT INTO dataquery (report_id, name, sql, is_visible, connection, doe, dlu) VALUES ({},'{}', '{}', '{}', '{}', now(), now())".format(max_report_id, result.get("query1_name"), result.get("query1_sql"), result.get("query1_visible_checkbox"), result.get("query1_connection"))
        save_to_db(insert_sql_statement2, local_cnx)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        close_db_connections([local_cnx, local_cnx2])
        return redirect("/")

def _query_for_max_report_id():
    try:
        print("AAAAAAAA")
        select_statement1 = "SELECT MAX(id) AS report_id from report"
        print("AAAAAAAA1")
        df = pd.read_sql(select_statement1, local_cnx)
        print("AAAAAAAA2")
        report_id = get_fields_from_single_row_df(df, "report_id")
        return report_id
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        write_to_page( "<p>Error: %s</p>" % e )
