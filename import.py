import sys
import mysql.connector
import datetime
import pandas as pd


def get_argument_from_console(args, arg_name):
    try:
        index = args.index(arg_name)
        return args[index + 1]
    except:
        raise Exception(arg_name + ' not specified')


arg_len = len(sys.argv)

if arg_len < 5:
    raise Exception('Invalid argument number supplied')

database_selected = mysql.connector.connect(
    host=get_argument_from_console(sys.argv, '-h'),
    user=get_argument_from_console(sys.argv, '-u'),
    passwd=get_argument_from_console(sys.argv, '-p'),
    database=get_argument_from_console(sys.argv, '-d'),
    port=3306
)

query_headers = ("DESCRIBE " + sys.argv[arg_len - 1]);
cursor_headers = database_selected.cursor(dictionary=True)
cursor_headers.execute(query_headers)
columns = []

for row in cursor_headers:
    columns.append(row['Field'])

query = ("SELECT * FROM " + sys.argv[arg_len - 1])
cursor = database_selected.cursor(dictionary=True)
cursor.execute(query)

df = pd.DataFrame(cursor, columns=columns)
'''
    Adding column mapings and reordering to match and generate your entire csv
    like you need it
'''
# print(df.columns)
# new_order = [4, 3, 2, 5, 9, 8, 6, 7, 1, 0]
# df = df[df.columns[new_order]]
# print(df.columns)
df.to_csv('exported_data.' + datetime.datetime.now().time().strftime('%f') + '.csv')
