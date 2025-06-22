import tkinter
import subprocess
from tkinter import messagebox
from tkinter import ttk
import tkinter.ttk
import sys
import kivy



print(kivy.__version__)

if sys.platform != "win32":
    print("This application only functions on a Windows System")
    sys.exit()

# Executes Windows Specific Commands 
window =tkinter.Tk()
window.geometry("400x500")
window.title("Windows Command Execution Application")
window.configure(bg="black")


#Different functions with nested variable commands to be executed per button press. Depending on selection. 
def ip():
    ip=subprocess.run("Ipconfig /all", shell=True, capture_output=True, text=True)
    messagebox.showinfo("IPconfig Output:",ip.stdout)
def arp():
    arp=subprocess.run("ARP  -a", shell=True, capture_output=True, text=True)
    messagebox.showinfo("ARP Output", arp.stdout) #shows a warning box. Practice

def ns_lookup():
    selection=ns_var.get() #Executes whichever command we selected from the ns_var variable combobox then executes based on which chosen. "youtube, or google."

    if selection == "Nslookup google.com":
        command = "nslookup google.com"
    elif selection =="Nslookup youtube.com":
        command = "nslookup youtube.com"
    else:
        messagebox.showerror("Error")
        return
    result = subprocess.run(command,shell=True,capture_output=True,text=True)
    messagebox.showinfo("NS Output",result.stdout)
def ping():
    selection=ns_var.get()
    # trt= subprocess.run("Tracert -h 10 google.com", shell=True, capture_output=True,text=True)
    # messagebox.showinfo("Tracert output,10 hops", trt.stdout)
    if selection == "ping Google.com":
        command = "ping www.google.com"
    elif selection =="ping youtube.com":
        command = "ping www.youtube.com"
    result = subprocess.run(command,shell=True,capture_output=True,text=True)
    messagebox.showinfo("Ping Output",result.stdout)


frame=tkinter.Frame(bg="white")        #Main Frame color and selection. Frame 1

title_label=tkinter.Label(frame,text="Click to execute a command",font = ("Arial",30))

#Labels and buttons associated to each label. Formated and placed side by side.
#Each button with its respective execution command. "Command =..."

ip_label = tkinter.Label(frame,text="Click for IPconfig", font=("Arial",16))
ip_button= tkinter.Button(frame, text="Ip Config", command = ip,bg = "black", fg="green",font = ("Arial",16))

arp_label =tkinter.Label(frame,text="Click to execute arp",font = ("Arial",16))
arp_button=tkinter.Button(frame,text="Address Resolution Protocol", command= arp,bg="black", fg="green",font = ("Arial",16))

ns_label=tkinter.Label(frame,text="Click for Nslookup",font = ("Arial",16))
ns_var = tkinter.StringVar()
ns_var.set("Select NS Site")

ns_combobox=ttk.Combobox(frame,textvariable=ns_var, values =["Nslookup google.com","Nslookup youtube.com"],state ="readonly")  #Combobox to sleect which nslookup  website will be executed
ns_button=tkinter.Button(frame,text="NSlookup",command = ns_lookup,bg="black", fg="green",font = ("Arial",16))

trt_Label=tkinter.Label(frame,text="Select from dropdown to ping",font=("Arial",16))
trt_combo=ttk.Combobox(frame,textvariable=ns_var,values =["ping Google.com", "ping youtube.com"],state = "readonly",font=("Arial",16))
trt_button=tkinter.Button(frame,text="Click for ping ",command=ping, bg="black",fg="Green", font=("Arial",16))

frame.pack()
#Positioning and gridding of each labe with associated button.
title_label.grid(row =0,column =0,columnspan =2, sticky ="news", pady = 20)
arp_label.grid(row=1,column=0, pady = 10)
arp_button.grid(row=1,column =1)

ns_label.grid(row=2,column=0, pady = 10)
ns_button.grid(row=2,column=1)
ns_combobox.grid(row=2, column=2,pady=6) #Combobox selection dropdown

trt_Label.grid(row=3,column =0)
trt_combo.grid(row =3,column=2)
trt_button.grid(row=3,column=1)

ip_label.grid(row=4,column =0)
ip_button.grid(row= 4, column=1)


window.mainloop()