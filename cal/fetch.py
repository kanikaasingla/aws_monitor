import json
import os
import pymysql
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
user = os.getenv("MYSQL_USER")
passwd = os.getenv("MYSQL_PASSWORD")
db = os.getenv("MYSQL_DB")

file = os.path.abspath('../staticfiles') + "/data.json"
json_data = open(file).read()
json_obj = json.loads(json_data)


def validate_string(val):
    if val is not None:
        if type(val) is int:
            # for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


con = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
cursor = con.cursor()

# parse json data to SQL insert
for i, item in enumerate(json_obj):
    date = validate_string(item.get("date", None))
    EC2 = validate_string(item.get("EC2", None))
    RDS = validate_string(item.get("RDS", None))

    cursor.execute("INSERT INTO cal_data (date,	EC2, RDS) VALUES (%s,	%s,	%s)", (date, EC2, RDS))
con.commit()
con.close()
