# print("Web DB 연동 프로그램")
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host="localhost", user="root", passwd="worldcup7!",
                     db="madang", charset="utf8")

cur = db.cursor()

@app.route('/')
def index():
    sqlString = 'select * from Book;'
    res = cur.execute(sqlString)
    print("res = ", res)
    book_list = cur.fetchall()
    return render_template('booklist.html', pbook_list=book_list)

if __name__ == "__main__":
    app.run('0.0.0.0')