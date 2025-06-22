import tkinter
import subprocess
from tkinter import messagebox, ttk
import platform #Detects which OS is being utilized 
#Identifies current OS and lists specific commands based on active OS. 
#OS Detectiong
os_name=platform.system()
print(f"Running on: {platform.system()}")


window =tkinter.Tk()
window.geometry("400x550")
window.title("Windows Command Execution Application")
window.configure(bg="black")

#Different commands can be executed Depending on OS. Testing here

#Commands listed for each OS
commands ={
    "Windows":{
        "ARP Table":"arp /a",
        "IP Config": "ipconfig",
        "System Info": "msinfo32.exe",
        "Performance Monitor": "Perfmon.msc",
        "System Version":"Winver",
        "Event log view": "eventvwr.msc"
    },
    "Linux":{
        "ARP Table":"arp -a",
        "IP addr TCP/IP Info": "ifconfig",
        "System's Uptime": "Uptime",
        "Memory usage and space": "free"
        
    },
    "Darwin":{
       "ARP Table":"arp -a",
        "IP addr TCP/IP Info": "ifconfig",
        
    }
}

def execute():                                                  #Shows Available Commands depending on OS detected.
    selected_command=command_Var.get()                          #Subprocess.run to execute selected_commands. When Run is clicked
    if selected_command in commands[os_name]:
        result = subprocess.run(commands[os_name][selected_command],shell=True,capture_output=True, text=True)
        messagebox.showinfo(tkinter.END, f"{selected_command}:\n{result.stdout}\n") #shows output in separate window/ CAn use without addition variables
        # output_text.insert(tkinter.END, f"{selected_command}:\n{result.stdout}\n") #shows output on same window as selections. Prints on the same window after completion. 

command_Var=tkinter.StringVar(window)
command_Var.set("Select Command")

command_label=tkinter.Label(window,text="Select Command")

command_menu=ttk.Combobox(window, textvariable=command_Var, values=list(commands[os_name].keys()),state="readonly")  #Dropdown menu to list all commands per OS
command_menu.pack(pady=10)


execute_button=tkinter.Button(window, text="Run", command =execute)      #Button that executes the selected command
execute_button.pack()

# output_text=tkinter.Text(window)  Outputs the results on the same window
# output_text.pack()

window.mainloop()