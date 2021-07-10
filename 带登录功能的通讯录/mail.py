import sqlite3 as sql
import tkinter as tk
from tkinter.constants import NONE
import tkinter.messagebox
def get_table():
    db_mail = sql.connect('mail_list.db')
    return db_mail

def set_frame():    
    win=tk.Tk()
    win.title('Mail List')
    win.geometry('512x512')
    #建立窗口   
    menu_1=tk.Menu(win)
    win.config(menu=menu_1)
    #建立菜单
    menu_1.add_command(label='增加', command=func_add)

    menu_1.add_command(label='删除', command=func_delete)

    menu_1.add_command(label='查询', command=func_inquire)

    menu_1.add_command(label='修改', command=func_change)

    menu_1.add_command(label='查看', command=func_examine)
    win.mainloop()

def func_add():
    global win1,member_name,member_gender,member_age,member_phone
    win1=tk.Toplevel()
    #提供一个对话框进行输入
    win1.title('增加')   
    win1.geometry('400x300')

    L1= tk.Label(win1, text="姓名",bg='white',width=6, height=1).grid(row=1,column=0,padx=20, pady=10)
    L2= tk.Label(win1, text="性别",bg='white',width=6, height=1).grid(row=2,column=0,padx=20, pady=10)
    L3= tk.Label(win1, text="年龄",bg='white',width=6, height=1).grid(row=3,column=0,padx=20, pady=10)
    L4= tk.Label(win1, text="电话",bg='white',width=6, height=1).grid(row=4,column=0,padx=20, pady=10)

    member_name=tk.StringVar()
    member_name.set('')
    member_gender=tk.StringVar()
    member_gender.set('')
    member_age=tk.StringVar()
    member_age.set('')
    member_phone=tk.StringVar()
    member_phone.set('')

    entry_name=tk.Entry(win1,textvariable=member_name).grid(row=1,column=1,padx=20, pady=10)
    entry_gender=tk.Entry(win1,textvariable=member_gender).grid(row=2,column=1,padx=20, pady=10)
    entry_age=tk.Entry(win1,textvariable=member_age).grid(row=3,column=1,padx=20, pady=10)
    entry_phone=tk.Entry(win1,textvariable=member_phone).grid(row=4,column=1,padx=40, pady=10)

    button_add=tk.Button(win1,text='增加',width=20,height=2,command=insert_data)
    button_add.grid(row=5,column=1,padx=20, pady=10)
    win1.mainloop()

def insert_data():
    args=(member_name.get(),member_gender.get(),member_age.get(),member_phone.get())
    try:
        table = get_table()
        c = table.cursor()
        c.execute("SELECT * FROM mail WHERE phone =(?)",(member_phone.get(),))
        result=c.fetchone()
        #判断电话是否存在
        if result == None:
            c.execute("INSERT INTO mail VALUES (?,?,?,?)",args)    
            tkinter.messagebox.showinfo(title='恭喜', message='增加成功' )
            win1.destroy()
            #不存在即插入信息
        else:
            tkinter.messagebox.showinfo(title='警告',message='该电话已存在')               
            member_name.set('')   
            member_gender.set('')
            member_age.set('')
            member_phone.set('')
            #若存在则清空输入的信息，并提示该电话已存在
    except Exception as ex:
        tkinter.messagebox.showinfo(title='警告', message=ex )
        win1.destroy()
    table.commit()
    c.close()
    table.close()
    #保存修改并关闭连接

def func_delete():
    global win2,member_name,member_phone
    win2=tk.Toplevel()
    win2.title('删除')   
    win2.geometry('400x300')
     
    L1= tk.Label(win2, text="姓名",bg='white',width=6, height=1).grid(row=1,column=0,padx=20, pady=10)
    L4= tk.Label(win2, text="电话",bg='white',width=6, height=1).grid(row=2,column=0,padx=20, pady=10)

    member_name=tk.StringVar()
    member_name.set('')
    member_phone=tk.StringVar()
    member_phone.set('')

    entry_name=tk.Entry(win2,textvariable=member_name).grid(row=1,column=1,padx=20, pady=10)
    entry_phone=tk.Entry(win2,textvariable=member_phone).grid(row=2,column=1,padx=40, pady=10)

    button_inquire=tk.Button(win2,text='删除',width=20,height=2,command=delete_data)
    button_inquire.grid(row=5,column=1,padx=20, pady=10)
    win2.mainloop()

def delete_data():
    try:
        table = get_table()
        c = table.cursor()
        c.execute("SELECT * FROM mail WHERE phone =(?)",(member_phone.get(),))
        result=c.fetchone()
        if result == None:
            tkinter.messagebox.showinfo(title='警告',message='该电话不存在')
            member_name.set('')   
            member_phone.set('')
        else:
            c.execute("DELETE FROM mail WHERE NAME =(?) AND PHONE =(?)",(member_name.get(),member_phone.get()))    
            tkinter.messagebox.showinfo(title='恭喜', message='删除成功' )
            win2.destroy()
    except Exception as ex:
        tkinter.messagebox.showinfo(title='警告', message=ex )
        win2.destroy()
    table.commit()
    c.close()
    table.close()
   
def func_inquire():
    global win3,member_name
    win3=tk.Toplevel()
    win3.title('查询')   
    win3.geometry('400x300')
    
    L1= tk.Label(win3, text="姓名",bg='white',width=6, height=1).grid(row=1,column=0,padx=20, pady=10)

    member_name=tk.StringVar()
    member_name.set('')

    entry_name=tk.Entry(win3,textvariable=member_name).grid(row=1,column=1,padx=20, pady=10)

    button_inquire=tk.Button(win3,text='查询',width=20,height=2,command=inquire_data)
    button_inquire.grid(row=5,column=1,padx=20, pady=10)
    win3.mainloop()

def inquire_data():
    try:
        table=get_table()
        c=table.cursor()
        c.execute("SELECT * FROM mail WHERE NAME =(?)",(member_name.get(),))
        #参数后面带有一个逗号，当不带有这个逗号时会报错
        results = c.fetchone()
        if results == None:
            tkinter.messagebox.showinfo(title='警告', message='未查询到该信息')
            member_name.set('')   
        else:
            win_inquire=tk.Toplevel()
            win_inquire.title('查询结果')
            win_inquire.geometry('400x300')
            L1= tk.Label(win_inquire, text="姓名",bg='white',width=6, height=1).grid(row=1,column=0,padx=20, pady=10)
            L2= tk.Label(win_inquire, text="性别",bg='white',width=6, height=1).grid(row=2,column=0,padx=20, pady=10)
            L3= tk.Label(win_inquire, text="年龄",bg='white',width=6, height=1).grid(row=3,column=0,padx=20, pady=10)
            L4= tk.Label(win_inquire, text="电话",bg='white',width=6, height=1).grid(row=4,column=0,padx=20, pady=10)

            L5= tk.Label(win_inquire, text=results[0],bg='white',width=6, height=1).grid(row=1,column=1,padx=20, pady=10)
            L6= tk.Label(win_inquire, text=results[1],bg='white',width=6, height=1).grid(row=2,column=1,padx=20, pady=10)
            L7= tk.Label(win_inquire, text=results[2],bg='white',width=6, height=1).grid(row=3,column=1,padx=20, pady=10)
            L8= tk.Label(win_inquire, text=results[3],bg='white',width=6, height=1).grid(row=4,column=1,padx=20, pady=10)

            def close_win_inquire():
                c.close()            
                win_inquire.destroy()
        
            button_close=tk.Button(win_inquire,text='关闭',width=20,height=2,command=close_win_inquire)
            button_close.grid(row=5,column=1)
            win_inquire.mainloop()
    except Exception as ex:
        tkinter.messagebox.showinfo(title='警告', message=ex)
        win3.destroy()

def func_change():
    global win4
    win4=tk.Toplevel()
    win4.title('修改')
    win4.geometry('400x300')

    L1= tk.Label(win4, text="姓名",bg='white',width=6, height=1).grid(row=1,column=0,padx=20, pady=10)
    L4= tk.Label(win4, text="电话",bg='white',width=6, height=1).grid(row=2,column=0,padx=20, pady=10)

    global member_name,member_phone

    member_name=tk.StringVar()
    member_name.set('')
    member_phone=tk.StringVar()
    member_phone.set('') 

    entry_name=tk.Entry(win4,textvariable=member_name).grid(row=1,column=1,padx=20, pady=10)
    entry_phone=tk.Entry(win4,textvariable=member_phone).grid(row=2,column=1,padx=40, pady=10)

    button_change=tk.Button(win4,text='修改',width=20,height=2,command=change_data)
    button_change.grid(row=5,column=1,padx=20, pady=10)
    win4.mainloop()

def change_data():
    try:
        table = get_table()
        c = table.cursor()
        c.execute("SELECT * FROM mail WHERE NAME =(?)",(member_name.get(),))
        result=c.fetchone()
        if result ==None:
            tkinter.messagebox.showinfo(title='警告',message='该信息不存在')
            member_name.set('')
            member_phone.set('')
        else:
            c.execute("UPDATE mail set PHONE = (?) where NAME=(?)",(member_phone.get(),member_name.get()))    
            tkinter.messagebox.showinfo(title='恭喜', message='修改成功' )
            win4.destroy()
    except Exception as ex:
        tkinter.messagebox.showinfo(title='警告', message=ex)
        win4.destroy()
    table.commit()
    c.close()
    table.close()

def func_examine():
    win5= tk.Toplevel()
    win5.title('查看')
    win5.geometry('400x800')

    try:
        table=get_table()
        c=table.cursor()
        c.execute("SELECT * FROM mail ")
        results = c.fetchall()
        L1= tk.Label(win5, text="姓名",bg='white',width=18, height=1).grid(row=0,column=0)
        L2= tk.Label(win5, text="性别",bg='white',width=6, height=1).grid(row=0,column=1)
        L3= tk.Label(win5, text="年龄",bg='white',width=6, height=1).grid(row=0,column=2)
        L4= tk.Label(win5, text="电话",bg='white',width=6, height=1).grid(row=0,column=3)
        for x in range (0,len(results)):
            L5= tk.Label(win5, text=results[x][0],bg='white',width=18, height=1).grid(row=x+1,column=0)
            L6= tk.Label(win5, text=results[x][1],bg='white',width=6, height=1).grid(row=x+1,column=1)
            L7= tk.Label(win5, text=results[x][2],bg='white',width=6, height=1).grid(row=x+1,column=2)
            L8= tk.Label(win5, text=results[x][3],bg='white',width=6, height=1).grid(row=x+1,column=3)
        c.close()
        win5.mainloop()
    except Exception as ex:
        tkinter.messagebox.showinfo(title='警告', message=ex )

def register_frame():
    global user,password,win_login
    win_login = tk.Tk()
    win_login.title('通讯录')
 
    # 禁止拉伸窗口
    win_login.resizable(width = False, height = False)
    win_login.geometry('400x300')
 
    tk.Label(win_login,text='用户名',width=8).grid(row=1,column=1,padx=25,pady=20)
    tk.Label(win_login,text='密码',width=8).grid(row=2,column=1,padx=25,pady=20)
 
    user = tk.StringVar(win_login,value='')
    entry_user = tk.Entry(win_login,width=8,textvariable=user)
    entry_user.grid(row=1,column=2,padx=25,pady=20)
 
    password = tk.StringVar(win_login,value='')
    entry_passwd = tk.Entry(win_login,width=8,textvariable=password)
    entry_passwd.grid(row=2,column=2,padx=25,pady=20)
 
    tk.Button(win_login,text='登录',width=8,command=logon).grid(row=3,column=1,padx=25,pady=20)
    tk.Button(win_login,text='注册',width=8,command=register).grid(row=3,column=2,padx=25,pady=20)
    tk.Button(win_login,text='取消',width=8,command=cancel).grid(row=3,column=3,padx=25,pady=20)
 
    win_login.mainloop()

def register():
    try:
        table_user = sql.connect('user_restore.db')
        c = table_user.cursor()
        #连接到储存账号信息的库
        user_name = user.get()
        user_password = password.get()
        # 判断用户名是否存在
        c.execute('SELECT * FROM users WHERE user_name=(?)',(user_name,))
        result = c.fetchone()
        if result is None:
            try:
                c.execute('INSERT INTO users VALUES (?,?)',(user_name,user_password))
                table_user.commit()
            except:
                tkinter.messagebox.showinfo(title='警告', message='注册失败')
        else:
            tkinter.messagebox.showinfo(title='警告', message='用户名已经存在，请重新注册')  

    except Exception as ex:
        tkinter.messagebox.showinfo(title='警告', message='注册失败，原因是：%s' % ex)

    c.close()
    table_user.close()

def logon():
    try:
        table_user = sql.connect('user_restore.db')
        c = table_user.cursor()
        #连接数据库
        user_name = user.get()
        user_password = password.get()
        c.execute('SELECT user_password FROM users WHERE user_name = (?)',(user_name,) )
        result=c.fetchone()
        if result==None:
            tkinter.messagebox.showinfo(title='警告', message='用户名错误，登录失败')
        elif result[0] == user_password:
            tkinter.messagebox.showinfo(title='恭喜', message='登录成功')
            win_login.destroy()
            set_frame()
        else:
            tkinter.messagebox.showinfo(title='警告', message='密码错误，登录失败')

    except Exception as ex:
        print("登录失败，失败原因为：%s"% ex)
    c.close()
    table_user.close()

def cancel():
	user.set('')
	password.set('')
    # 清空用户输入的用户名和密码

def main():
    register_frame()

if __name__ == '__main__':
    main()
