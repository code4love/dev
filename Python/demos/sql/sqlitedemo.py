'''SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说
没有独立的维护进程，所有的维护都来自于程序本身。
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候
连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建
数据库文件，而是直接打开该数据库文件。
    连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库
    执行完任何操作后，都不需要提交事务的(commit)

    创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
    创建在内存上面： conn = sqlite3.connect('"memory:')

    下面我们一硬盘上面创建数据库文件为例来具体说明：
    conn = sqlite3.connect('c:\\test\\hongten.db')
    其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：

        commit()            --事务提交
        rollback()          --事务回滚
        close()             --关闭一个数据库链接
        cursor()            --创建一个游标

    cu = conn.cursor()
    这样我们就创建了一个游标对象：cu
    在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
    对于游标对象cu，具有以下具体操作：

        execute()           --执行一条sql语句
        executemany()       --执行多条sql语句
        close()             --游标关闭
        fetchone()          --从结果中取出一条记录
        fetchmany()         --从结果中取出多条记录
        fetchall()          --从结果中取出所有记录
        scroll()            --游标滚动

'''

import sqlite3

#create test.db if it exists
db = sqlite3.connect("test.db")

cursor = db.cursor()

#create table
#gender:0 for male and 1 for female
sql = """create table student (
            id integer primary key,
            name varchar(20),
            age integer,
            gender integer)"""
cursor.execute(sql)

#insert
for row in[(0,'Jack',30, 0), (1,'Jason',28, 0), (2,'Mary',22, 1), (3,'Lucy',20, 1)]:
    cursor.execute("insert into student values (?,?,?,?)", row)
#take insert effect
db.commit()

#select
def selectall():
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    print(rows)

#select using loop
# cursor.execute("select * from student")
# row = cursor.fetchone()
# while row != None:  #same to while !row:
#     print(row)
#     row = cursor.fetchone()

selectall()

#update
cursor.execute("""update student set
                    name=?,
                    age=?
                 where id=?""",
               ('Alice', 18, 3))
#the update will not take effect if we don't call commit()
db.commit()

selectall()

#delete
cursor.execute("delete from student where id = 3")
db.commit()
selectall()