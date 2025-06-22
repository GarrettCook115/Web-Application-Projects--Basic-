from flask import Flask, render_template, request
import subprocess
import sys

app = Flask(__name__)

# Command Execution
if sys.platform =="win32":
    command_map={
        "ipconfig": "ipconfig ",
        "arp": "arp -a",
        "nslookup": "nslookup google.com"
    }
else:
    command_map = {
        "ifconfig": "ifconfig",
        "arp": "arp -a",
        "nslookup": "nslookup google.com"
        
    }

def execute_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

@app.route("/")
def index():

    return render_template("FlaskApp1.html")

@app.route("/run_command", methods=["POST"])
def run_command():
    command = request.form["command"].lower()
    cmd = command_map.get(command)
    if not cmd:
        return "Invalid command selected!"
    
    output = execute_command(cmd)
    return f"<pre>{output}</pre>"

if __name__=="__main__":
    if sys.platform =="win32":
        app.run(debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)