import pymysql

con = pymysql.connect(
    host='rm-2zeo25h474310yk6tjo.mysql.rds.aliyuncs.com',
    user='RoOt',
    password='_root235476',
    db='assistant',
    charset='utf8',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)

def query_user_exist(usr)->bool:
    cursor = con.cursor()
    cursor.execute('select * from sys_user where username = %s', (usr,))
    result = cursor.fetchone()
    if result == None:
        return False
    else:
        return True

def query_user_by_username(username):
    cursor = con.cursor()
    cursor.execute('select * from sys_user where username = %s', (username,))
    result = cursor.fetchone()
    #usr = result["username"]
    #pwd = result["password"]
    return result

def add_user(username,password):
    sql = "insert into sys_user (username,password) values (%s,%s)"
    cur = con.cursor()
    cur.execute(sql, [username,password])
    con.commit()

def query_userchat_by_username(username):
    cursor = con.cursor()
    cursor.execute("""
select * from chat_message where user_id = (select user_id from sys_user where username = %s)
""",(username,))
    con.commit()
    return cursor.fetchall()