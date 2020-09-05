import tkinter
from tkinter import *
from tkinter import ttk,messagebox
import pymysql

	
#window configuration
root = Tk()
root.geometry('550x800')
root.title("Registration form")
root.config(bg="white")

#creating function to clear the dialog boxes
def clear():
	Name_entry.delete(0,END)
	F_Name_entry.delete(0,END)
	M_Name_entry.delete(0,END)
	Contact_no_entry.delete(0,END)
	Father_contact_no_entry.delete(0,END)
	Mother_contact_no_entry.delete(0,END)
	DOB_entry.delete(0,END)
	S_Passing_year_entry.delete(0,END)
	Email_entry.delete(0,END)
	Address_entry.delete(0,END)
	Country_entry.current(0)
	Nationality_entry.current(0)
	Cast_entry.current(0)
	twelth_percent_entry.delete(0,END)
	Main_sub_percent_entry.delete(0,END)
	Stream_entry.current(0)
	Board_entry.delete(0,END)
	Course_entry.current(0)

#creating function for submitting the data
def submit_data():
	if Name_entry.get()=="" or F_Name_entry.get()=="" or M_Name_entry.get()=="" or Contact_no_entry.get()=="" or Father_contact_no_entry.get()=="" or DOB_entry.get()=="" or S_Passing_year_entry.get()=="" or Email_entry.get()=="" or Address_entry.get()=="" or Country_entry.get()=="Select" or Nationality_entry.get()=="Select" or Cast_entry.get()=="Select" or twelth_percent_entry.get()=="" or Main_sub_percent_entry.get()=="" or Stream_entry.get()=="Select" or Board_entry.get()=="" or Course_entry.get()=="Select":
		messagebox.showerror("Error","All Field Should be Filled",parent=root)
	elif Contact_no_entry.get()==Father_contact_no_entry.get() or Father_contact_no_entry.get()==Mother_contact_no_entry.get() or Contact_no_entry.get()==Mother_contact_no_entry.get():
		messagebox.showerror("Error","All Contact no. should be different",parent=root)
	elif gender_entry.get()==0 or region_entry.get()==0:
		messagebox.showerror("Error","All Field Should be Filled",parent=root)
	else:
		try:
			con=pymysql.connect(host="localhost",user="root",password="kun@ls@h.6841",database="final_form")
			cur=con.cursor()
			cur.execute("select * from final_form where Email_entry=%s",Email_entry.get())
			row=cur.fetchone()
			if row!=None:
				messagebox.showerror("Error","User already Exist, Please try with another email",parent=root)
			else:
				try:
					int(Contact_no_entry.get())
					int(Father_contact_no_entry.get())
					int(Mother_contact_no_entry.get())
					cur.execute("insert into final_form(Name_entry,F_Name_entry,M_Name_entry,Contact_no_entry,Father_contact_no_entry,Mother_contact_no_entry,DOB_entry,S_Passing_year_entry,Email_entry,gender_entry,Address_entry,region_entry,Country_entry,Nationality_entry,Cast_entry,twelth_percent_entry,Main_sub_percent_entry,Stream_entry,Board_entry,Course_entry) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
									(Name_entry.get(),
									F_Name_entry.get(),
									M_Name_entry.get(),
									Contact_no_entry.get(),
									Father_contact_no_entry.get(),
									Mother_contact_no_entry.get(),
									DOB_entry.get(),
									S_Passing_year_entry.get(),
									Email_entry.get(),
									gender_entry.get(),
									Address_entry.get(),
									region_entry.get(),
									Country_entry.get(),
									Nationality_entry.get(),
									Cast_entry.get(),
									twelth_percent_entry.get(),
									Main_sub_percent_entry.get(),
									Stream_entry.get(),
									Board_entry.get(),
									Course_entry.get()
									))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Register Successful", parent=root)
					clear()
					print(Name_entry.get(),
						  F_Name_entry.get(),
						  M_Name_entry.get(),
					      Contact_no_entry.get(),
						  Father_contact_no_entry.get(),
						  DOB_entry.get(),
						  S_Passing_year_entry.get(),
						  Email_entry.get(),
						  gender_entry.get(),
						  Address_entry.get(),
					      region_entry.get(),
						  Country_entry.get(),
						  Nationality_entry.get(),
						  Cast_entry.get(),
						  twelth_percent_entry.get(),
						  Main_sub_percent_entry.get(),
						  Stream_entry.get(),
						  Board_entry.get(),
						  Course_entry.get())
				except:
					messagebox.showerror("Error",f"All contact no. should be in a number form \n {str(es)}",parent=root)


		except Exception as es:
			messagebox.showerror("Error",f"Error dur to: {str(es)}",parent=root)
			print(Name_entry.get(),
						    F_Name_entry.get(),
							M_Name_entry.get(),
							Contact_no_entry.get(),
							Father_contact_no_entry.get(),
							DOB_entry.get(),
							S_Passing_year_entry.get(),
							Email_entry.get(),
							gender_entry.get(),
							Address_entry.get(),
							region_entry.get(),
							Country_entry.get(),
							Nationality_entry.get(),
							Cast_entry.get(),
							twelth_percent_entry.get(),
							Main_sub_percent_entry.get(),
							Stream_entry.get(),
							Board_entry.get(),
							Course_entry.get())
			

		
	




#creating label
Heading = Label (root, text="Application form",bg="white", fg="grey",font="none 25 bold").place(x=110,y=50)

Name = Label (root, text="Candidate name :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=140)
Name_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Name_entry.place(x=250,y=140)

F_Name = Label (root, text="Father's name :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=165)
F_Name_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
F_Name_entry.place(x=250,y=165)

M_Name = Label (root, text="Mother's name :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=190)
M_Name_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
M_Name_entry.place(x=250,y=190)

Contact_no = Label (root, text="Contact no. :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=215)
Contact_no_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Contact_no_entry.place(x=250,y=215)

Father_contact_No = Label (root, text="Father's Contact no. :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=240)
Father_contact_no_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Father_contact_no_entry.place(x=250,y=240)

Mother_contact_no = Label (root, text="Mother's contact no. :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=265)
Mother_contact_no_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Mother_contact_no_entry.place(x=250,y=265)

DOB = Label (root, text="Birth date :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=290)
DOB_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
DOB_entry.place(x=250,y=290)

S_Passing_year = Label (root, text="School Passing year:",bg="white", fg="grey",font="none 12 bold").place(x=15,y=315)
S_Passing_year_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
S_Passing_year_entry.place(x=250,y=315) 

Email = Label (root, text="Email :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=340)
Email_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Email_entry.place(x=250,y=340) 

Gender = Label (root, text="Gender :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=365)
gender_entry = IntVar()
Checkbutton(root, text="Male", bg="white",fg="grey",padx=5, cursor="hand2",variable=gender_entry, onvalue=1,offvalue=0,font=("none 8 bold")).place(x=250,y=365)
Checkbutton(root, text="Female",bg="white",fg="grey", padx= 20,cursor="hand2", variable=gender_entry, onvalue=2,offvalue=0,font=("none 8 bold")).place(x=305,y=365)

Address = Label (root, text="Full address :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=390)
Address_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Address_entry.place(x=250,y=390)

Region = Label (root, text="Region :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=415)
region_entry = IntVar()
Checkbutton(root, text="Rural", bg="white",fg="grey",padx=5,cursor="hand2", variable=region_entry, onvalue=1,offvalue=0,font=("none 8 bold")).place(x=250,y=415)
Checkbutton(root, text="Urban", bg="white",fg="grey",padx=20,cursor="hand2", variable=region_entry, onvalue=2,offvalue=0,font=("none 8 bold")).place(x=320,y=415)

Country = Label (root, text="Country :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=440)
Country_entry=ttk.Combobox(root,state="readonly",justify=CENTER, font=("Times new roman", 12, "normal"))
Country_entry['values']=('Select','Afghanistan','Albania','Algeria','Argentina','Australia','Austria','Bangladesh','Belgium','Bolivia','Botswana','Brazil','Bulgaria','Cambodia','Cameroon','Canada','Chile','China','Colombia','Costa Rica','Croatia','Cuba','Czech Republic','Denmark','Dominican Republic','Ecuador','Egypt','El Salvador','England','Estonia','Ethiopia','Fiji','Finland','France','Germany','Ghana','Greece','Guatemala','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kenya','Kuwait','Laos','Latvia','Lebanon','Libya','Lithuania','Madagascar','Malaysia','Mali','Malta','Mexico','Mongolia','Morocco','Mozambique','Namibia','Nepal','Netherlands','New Zealand','Nicaragua','Nigeria','Norway','Pakistan','Panama','Paraguay','Peru','Philippines','Poland','Portugal','Romania','Russia','Saudi Arabia','Scotland','Senegal','Serbia','Singapore','Slovakia','South Africa','South Korea','Spain','Sri Lanka','Sudan','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Thailand','Tonga','Tunisia','Turkey','Ukraine','United Arab Emirates',' United Kingdom', 'United States','Uruguay','Venezuela','Vietnam','Wales','Zambia','Zimbabwe')
Country_entry.current(0)
Country_entry.place(x=250,y=440)

Nationality = Label (root, text="Nationality :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=465)
Nationality_entry=ttk.Combobox(root,state='readonly', justify=CENTER, font=("Times new roman", 12, "normal"))
Nationality_entry['values']=('Select','Afghan','Albanian','Algerian','Argentine','Argentinian','Australian','Austrian','Bangladeshi','Belgian','Bolivian','Batswana','Brazilian','Bulgarian','Cambodian','Cameroonian','Canadian','Chilean','Chinese','Colombian','Costa Rican','Croatian','Cuban','Czech','Danish','Dominican','Ecuadorian','Egyptian','Salvadorian','English','Estonian','Ethiopian','Fijian','Finnish','French','German','Ghanaian','Greek','Guatemalan','Haitian','Hungarian','Icelandic','Indian','Indonesian','Iranian','Iraqi','Irish','Israeli','Italian','Jamaican','Japanese','Jordanian','Kenyan','Kuwaiti','Lao','Latvian','Lebanese','Libyan','Lithuanian','Malagasy','Malaysian','Malian','Maltese','Mexican','Mongolian','Moroccan','Mozambican','Namibian','Nepalese','Dutch','New Zealand','Nicaraguan','Nigerian','Norwegian','Pakistani','Panamanian','Paraguayan','Peruvian','Polish','Portuguese','Romanian','Russian','Saudi','Scottish','Senegalese','Serbian','Singaporean','Slovak','South African','Korean','Spanish','Sri Lankan','Sudanese','Swedish','Swiss','Syrian','Taiwanese','Tajikistani','Thai','Tongan','Tunisian','Turkish','Ukrainian','Emirati','British','American','Uruguayan','Venezuelan','Vietnamese','Welsh','Zambian','Zimbabwean')
Nationality_entry.current(0)
Nationality_entry.place(x=250,y=465)

Cast = Label (root, text="Cast :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=490)
Cast_entry=ttk.Combobox(root,state="readonly",justify=CENTER, font=("Times new roman", 12, "normal"))
Cast_entry['values']=('Select','SC','ST','OBC','General')
Cast_entry.current(0)
Cast_entry.place(x=250,y=490)

twelth_percent = Label (root, text="12th class percentage :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=530)
twelth_percent_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
twelth_percent_entry.place(x=250,y=530)

Main_sub_percent = Label (root, text="Main subject percentage :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=555)
Main_sub_percent_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Main_sub_percent_entry.place(x=250,y=555)

Stream = Label (root, text="Stream :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=580)
Stream_entry=ttk.Combobox(root,state="readonly",justify=CENTER, font=("Times new roman", 12, "normal"))
Stream_entry['values']=('Select','PCM','PCB','PCMB','Commerce','Arts')
Stream_entry.current(0)
Stream_entry.place(x=250,y=580)

Board = Label (root, text="Board Name :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=620)
Board_entry = Entry(root, width=40,bg="silver",fg="black",font=("none 10 bold"))
Board_entry.place(x=250,y=620)

Course_continuing = Label (root, text="Course you will continue :",bg="white", fg="grey",font="none 12 bold").place(x=15,y=650)
Course_entry=ttk.Combobox(root,state="readonly",justify=CENTER, font=("Times new roman", 12, "normal"))
Course_entry['values']=('Select','Management MBA/BBA','Engineering B.Tech and B.Arch, M.Tech, ME, BE','Computer Application-BCA/MCA','Designing - Fashion/Interior/Web','Mass-communication/Journalism BJMC','Hospitality (Hotel) - Hotel Management','Medical-BDS and MBBS','Finance -B.Com/CA','Arts Psychology and Sociology','Law B.ALLB/LLB','Education Teaching-B.Ed/M.Ed','Pharmacy B.Pharma/M.Pharma','Tourism management - B.Sc.','Fine Arts B.F.A','Nursing B.Sc. and M.Sc. in Nursing')
Course_entry.current(0)
Course_entry.place(x=250,y=650)

#exit function
def close_window():
 	root.destroy()
 	exit()
#add a exit button
Button(root, text="QUIT", width=14,bg="red",fg="black",cursor="hand2", font=("none 10 bold"),command= close_window).place(x=110,y=700)

#add a submit button
Button(root, text="Submit", width=20, bg="green", fg="black",cursor="hand2", font=("none 10 bold"),command=submit_data).place(x=250,y=700)


#running main loop
root.mainloop()