


from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import mysql.connector
from PIL import Image, ImageTk
import datetime
import time



mydb=mysql.connector.connect(
host="localhost",
user="root",
password="abc123",
port="3308",
auth_plugin='mysql_native_password'
)
nowd= datetime.datetime.now().date()
nowt= datetime.datetime.now().time()
print(mydb)

mycursor=mydb.cursor()
'''mycursor.execute("drop database if exists bmi")'''
mycursor.execute("create database if not exists bmi")
mycursor.execute("use bmi")
mycursor.execute("show databases")

for db in mycursor:
	print(db)
'''mycursor.execute("drop table if exists person_info")'''
mycursor.execute("Create table if not exists person_info(name varchar(20) not null,age int(10) not null,phone varchar(10) not null,gender varchar(10) not null,height float(5,2) not null,weight float(5,2) not null,bmi float(5,2) not null,created_date datetime)")


mycursor.execute("show tables")
for db in mycursor:
	print(db)



if(mydb):
	print('connected')
else:
	print('not connected')

'''*********************************************************************'''
def f1():
	bmi.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	bmi.withdraw()


def f3():
	data.deiconify()
	bmi.withdraw()


def f4():
	bmi.deiconify()
	data.withdraw()




def f5():
	con=None
	try:
		sql="select * from person_info"
		mycursor.execute(sql)
		data=mycursor.fetchall()
		print(data)
		msg= ""
		for d in data:
			msg=msg+"Name:  "+str(d[0])+"\n"+"Age  :  "+str(d[1])+"\n"+"phone_No  :  "+str(d[2])+"\n"+"gender  :  "+str(d[3])+"\n"+"Height  :  "+str(d[4])+"\n"+"Weight  :  "+str(d[5])+"\n"+"BMI   :  "+str(d[6])+"\n"+"Date & Time  :  "+str(d[7])+"\n"+"******************************************************"
		vist_stdata.delete(1.0,END)
		vist_stdata.insert(INSERT,msg)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
	vist.deiconify()
	bmi.withdraw()

def f6():
	bmi.deiconify()
	vist.withdraw()
		


def f7():
	try:
		now = datetime.datetime.now()
		age=int(data_entage.get())
		sql="insert into person_info values('%s','%d','%s','%s','%f','%f','%s','%s')"
		age=int(data_entage.get())
		name=data_entname.get()
		print(age)
		
		name=data_entname.get()
		print(name)
				
		phone=data_entmno.get()
		print(phone)
		
		gender=radio.get()
		print(gender)
		height=float(data_enthgt.get())
		weight=float(data_entwgt.get())
		print(height)
		print(weight)
		if(name.isdigit()):
			showerror("Error","Enter Correct name:Enter only alphabets")
			data_entname.delete(0,END)
			data_entname.focus()
		elif(not name.isalpha()):
			showerror("Error","Enter Correct name:Enter only alphabets")
			data_entname.delete(0,END)
			data_entname.focus()
		elif(age<0 or age>100):
			showerror("Error","Enter Correct Age")
			data_entage.delete(0,END)
			data_entage.focus()
		elif(len(name)<2):
			showerror("Error","Enter valid name: length should be more than 2 ")
			data_entname.delete(0,END)
			data_entname.focus()
		
		elif(len(phone)<10 or len(phone)>10):
			showerror("Error","Enter valid phone no.")
			data_entmno.delete(0,END)
			data_entmno.focus()
		elif(height<0.0):
			showerror("Error","Enter valid height")
			data_enthgt.delete(0,END)
			data_enthgt.focus()
		elif(weight<0.0):
			showerror("Error","Enter valid weight")
			data_entwgt.delete(0,END)
			data_entwgt.focus()
		else:
			bmi=round(weight/(height*height),2)
			print(bmi)
			if(bmi<=18.5):
				showinfo("BMI","BMI = "+str(bmi)+" => Underweight")
			elif(bmi<=24.9):
				showinfo("BMI","BMI = "+str(bmi)+" => Normal weight")
			elif(bmi<=29.9):
				showinfo("BMI","BMI = "+str(bmi)+" => Overweight")
			else:
				showinfo("BMI","BMI = "+str(bmi)+" => Obesity")

			mycursor.execute(sql % (name,age,phone,gender,height,weight,bmi,now.strftime("%Y-%m-%d %H:%M:%S")))
			showinfo("Success","Record Added")
			mycursor.execute("select * from person_info")
			data=mycursor.fetchall()
			print(data)
			mydb.commit()
			data_entwgt.delete(0,END)
			data_entage.delete(0,END)
			data_entname.delete(0,END)
			data_enthgt.delete(0,END)
			data_entmno.delete(0,END)

	except Exception as e:
		showerror("Failure","Record not added  ==> " + str(e))
		mydb.rollback()
	


def f8():
	conv.deiconify()
	data.withdraw()


def f9():
	data.deiconify()
	conv.withdraw()


def f10():
	try:
		feet=float(conv_entfeet.get())
		inch=float(conv_entinc.get())
		print(feet)
		print(inch)
		if(feet>0 and inch<12 and inch>0 ):
			print('yes')
			inch += feet * 12
			h_cm = round(inch * 2.54, 1)
			print("Your height is : %d cm." % h_cm)
			h_m = h_cm/100.0
			print("Your height is : %d m." % h_m)
			showinfo("Height","Height In Meter = "+str(h_m))
			conv_entfeet.delete(0,END)				
			conv_entinc.delete(0,END)
		else:
			if(feet<0):
				showerror("Error","Enter Correct height in Feet")
				conv_entfeet.delete(0,END)
				conv_entfeet.focus()
			if(inch>12 or inch<0):
				showerror("Error","Enter Correct height in Inches")
				conv_entinc.delete(0,END)
				conv_entinc.focus()
	except Exception as e:
		showerror("Failure","Can't Convert" + str(e))
		conv_entfeet.delete(0,END)		
		conv_entinc.delete(0,END)
			

def f11():
	nowdate=str(nowd)
	nowtime=str(nowt)
	time=nowtime.split('.')
	timet= ''.join(map(str, time)) 
	print(timet)
	timehr=timet.split(':')
	print(timehr)
	print(timehr[0])
	print(timehr[1])
	print(timehr[2])

	sql='select * into outfile "D:/Mysql_project/patient_record_'+nowdate+'_'+timehr[0]+'_'+timehr[1]+'_'+timehr[2]+'.csv" from person_info'
	try:
		mycursor.execute(sql)
		showinfo("Success","Exported Successfully")
	except (mysql.connector.Error, mysql.connector.Warning) as e:
		print(e)
		showerror("Error","Failed to Export")



'''***********************************************************************'''


root=Tk()
root.title("B.M.I")
root.geometry("800x600+400+100")


label=Label(root, font=('algerian',30,'bold'),fg='blue',text = "BMI Calculator By Yogita Mahajan" ).pack(pady=20)
go=Button(root,text='START',font=('arial',20,'bold'),command=f1)

go.pack(pady=10)
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("background1.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)




e = Example(root)
e.pack(fill=BOTH, expand=YES)

bmi=Toplevel(root)

bmi.title("MENU")
bmi.geometry("800x600+400+100")

bmi.configure(background="#003300")

now = datetime.datetime.now()


currentTime = int(time.strftime('%H'))   

if currentTime < 12 :
     bmi_msg=Label(bmi,text='Good Morning',font=('arial',20,'bold'))
if currentTime == 12 :
     bmi_msg=Label(bmi,text='Good Noon',font=('arial',20,'bold'))
if currentTime > 12 :
     bmi_msg=Label(bmi,text='Good Afternoon',font=('arial',20,'bold'))
if currentTime > 6 :
     bmi_msg=Label(bmi,text='Good Night',font=('arial',20,'bold'))

bmi_date=Label(bmi,text=now.strftime("%Y-%m-%d %H:%M:%S"),font=('arial',20,'bold'))
bmi_btncal=Button(bmi,text='Calculate BMI',font=('arial',20,'bold'),command=f3)
bmi_btnview=Button(bmi,text='View History',font=('arial',20,'bold'),command=f5)
bmi_btnexp=Button(bmi,text='Export Data',font=('arial',20,'bold'),command=f11)
bmi_btnback=Button(bmi,text='Back',font=('arial',20,'bold'),command=f2)
bmi_date.pack(pady=10)
bmi_msg.pack(pady=10)
bmi_btncal.pack(pady=10)
bmi_btnview.pack(pady=10)
bmi_btnexp.pack(pady=10)
bmi_btnback.pack(pady=10)
mycursor.execute("select count(*) from person_info")
bmi_countlabel=Label(bmi,text='Count  ',font=('arial',30,'bold'))
bmi_count=Label(bmi,text=list(mycursor),font=('arial',30,'bold'))
bmi_countlabel.place(x=320,y=450)
bmi_count.place(x=450,y=450)



bmi.withdraw()




data=Toplevel(root)
data.title("Add Data And Calculate BMI")
data.geometry("800x600+400+100")
data.configure(background="#1A5276")

data_lblname=Label(data,text='Enter Name:',font=('arial',15,'bold'))
data_entname=Entry(data,bd=5,font=('arial',20,'bold'))


data_lblname.place(x=20,y=25)
data_entname.place(x=280,y=25)

data_lblage=Label(data,text='Enter Age:',font=('arial',15,'bold'))
data_entage=Entry(data,bd=5,font=('arial',20,'bold'))

data_lblage.place(x=20,y=70)
data_entage.place(x=280,y=70)


data_lblmno=Label(data,text='Enter Mobile No:',font=('arial',15,'bold'))
data_entmno=Entry(data,bd=5,font=('arial',20,'bold'))

data_lblmno.place(x=20,y=120)
data_entmno.place(x=280,y=120)


data_lblgen=Label(data,text='Gender:',font=('arial',15,'bold'))
data_lblgen.place(x=20,y=170)
data_entgen=Entry(data,bd=5,font=('arial',20,'bold'))



radio = StringVar()     
R1 = Radiobutton(data, text="Female",font=('arial',15), variable=radio, value='female',  
                  )  
R1.place(x=280,y=170)  
  
R2 = Radiobutton(data, text="Male",font=('arial',15), variable=radio, value='male',  
                  )  
R2.place(x=400,y=170)  




data_lblhgt=Label(data,text='Enter Height In meter:',font=('arial',15,'bold'))
data_enthgt=Entry(data,bd=5,font=('arial',20,'bold'))


data_btnconv=Button(data,text='CONVERT',font=('arial',20,'bold'),command=f8)

data_lblhgt.place(x=20,y=210)
data_enthgt.place(x=280,y=210)

data_btnconv.place(x=600,y=260)

data_lblwgt=Label(data,text='Enter Weight In kg:',font=('arial',15,'bold'))
data_entwgt=Entry(data,bd=5,font=('arial',20,'bold'))


data_lblwgt.place(x=20,y=320)
data_entwgt.place(x=280,y=320)





data_btnsave=Button(data,text='CALCULATE BMI',font=('arial',20,'bold'),command=f7)
data_btnback=Button(data,text='BACK',font=('arial',20,'bold'),command=f4)





data_btnsave.place(x=250,y=430)
data_btnback.place(x=330,y=500)

data.withdraw()



conv=Toplevel(root)
conv.title("Height Converter")
conv.geometry("800x600+400+100")
conv.configure(background="#4d004d")
conv_lblname=Label(conv,text='Enter Your Height',font=('algerian',30,'bold'))

conv_lblname.place(x=220,y=25)


conv_lblfeet=Label(conv,text='Feet',font=('arial',25,'bold'))
conv_entfeet=Entry(conv,bd=5,font=('arial',20,'bold'))

conv_lblfeet.place(x=380,y=105)
conv_entfeet.place(x=260,y=175)


conv_lblinc=Label(conv,text='Inches',font=('arial',25,'bold'))
conv_entinc=Entry(conv,bd=5,font=('arial',20,'bold'))

conv_lblinc.place(x=380,y=250)
conv_entinc.place(x=260,y=320)



conv_btnconv=Button(conv,text='CONVERT',font=('arial',20,'bold'),command=f10)
conv_btnback=Button(conv,text='BACK',font=('arial',20,'bold'),command=f9)
conv_btnconv.place(x=250,y=400)
conv_btnback.place(x=490,y=400)
conv.withdraw()


vist=Toplevel(root)
vist.title("View History")
vist.geometry("800x600+400+100")
vist.configure(background="#DE3163")

vist_stdata=ScrolledText(vist,width=40,height=10,font=('arial',20,'bold'))
vist_btnback=Button(vist,text='BACK',font=('arial',20,'bold'),command=f6)
vist_stdata.pack(pady=10)
vist_btnback.pack(pady=10)

vist.withdraw()

root.mainloop()


































