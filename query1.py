#Find the employee_id of employee whose is working in Finance Department in Investment firm from Employee SQLite Database.

employee_id=[101,102,103,104,105,106,107,108,109,110,111,112]
name=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
age=[25,27,25,24,30,26,23,26,25,26,29,24]
department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]
import sqlite3
import sqlite3
db=sqlite3.connect('Employee.sqlite')
cur=db.cursor()
cur.execute('create table employee_detail (employee_id int primary key,name text,age integer,Department text,salary int)')
l=[]
for i in range(12):
    t = (employee_id[i],name[i],age[i],department[i],salary[i]) #list of tupples
    l.append(t)
#above is insertion 
cur.executemany('Insert into Employee_detail values(?,?,?,?,?)',l) # to insert many elm as paparemter passing 
db.commit()
#exex query , cursor points to result 
cur.execute('Select employee_id,department from employee_detail where department="Finance"')
#
ans=cur.fetchall()
s=len(ans)
for i in range(s):
    print(ans[i][0])
