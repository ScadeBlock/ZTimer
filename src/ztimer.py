# ZTimer 1.0 - ScadeBlock
import time,sys
import customtkinter,threading
from customtkinter import *
from tkinter import messagebox
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue") 
func = None
root = CTk()
root.geometry('150x150')
root.attributes('-toolwindow',True)
root.attributes('-topmost',True)
root.title("Time Counter")
hour=StringVar()
minute=StringVar()
second=StringVar()
hour.set("00")
minute.set("00")
second.set("00")

# frame1
iy = CTkFrame(root,fg_color='transparent')
hourLab= CTkLabel(iy, width=9, font=customtkinter.CTkFont(size=12, weight="normal"),
				text="Hour")
hourLab.pack(side=LEFT, anchor='center',padx=5,pady=10)

minuteLab= CTkLabel(iy, width=9, font=customtkinter.CTkFont(size=12, weight="normal"),
				text="Minute")
minuteLab.pack(side=LEFT, anchor='center',padx=3,pady=10)

secondLab= CTkLabel(iy, width=9, font=customtkinter.CTkFont(size=12, weight="normal"),
				text="Second")
secondLab.pack(side=LEFT, anchor='center',padx=3,pady=10)

# frame
ix = CTkFrame(root,fg_color="transparent")

hourEntry= CTkEntry(ix, width=30, font=customtkinter.CTkFont(size=15, weight="normal"),
				textvariable=hour)
hourEntry.pack(side=LEFT, anchor='center',padx=8,pady=10)

minuteEntry= CTkEntry(ix, width=30, font=customtkinter.CTkFont(size=15, weight="normal"),
				textvariable=minute)
minuteEntry.pack(side=LEFT, anchor='center',padx=8,pady=10)

secondEntry= CTkEntry(ix, width=30, font=customtkinter.CTkFont(size=15, weight="normal"),
				textvariable=second)
secondEntry.pack(side=LEFT, anchor='center',padx=8,pady=10)

def reset():
	hour.set("00")
	minute.set("00")
	second.set("00")
	func = None

def submit_px():
	global func
	try:
		# the input provided by the user is
		# stored in here :temp
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while temp >-1:
		if func == None:
			reset()
			sys.exit()	
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
		hours=0
		if mins >60:
			
			# divmod(firstvalue = temp//60, secondvalue 
			# = temp%60)
			hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
		root.update()
		time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
		if (temp == 0):
			reset()
			messagebox.showinfo("Time Countdown", "Time's up ")
		
		# after every one sec the value of temp will be decremented
		# by one
		temp -= 1

# button widget
def submit():
	global func
	if func is None:
		func = threading.Thread(target=submit_px,daemon=True)
		func.start()
	else:
		func = None
iy.pack(side=TOP,anchor="n")
ix.pack(side=TOP,anchor="n")
btn = CTkButton(root, text='Set Time Countdown', corner_radius=5,
			command= submit)
btn.pack(side=BOTTOM,anchor="s",pady=5)
root.mainloop()
