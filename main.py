import tkinter as tk
from tkinter import filedialog, messagebox
import win32serviceutil
import subprocess
import os

root = tk.Tk()
root.title("Service Maker")
root.geometry("500x400")
root.configure(bg="#2E2E2E")

selected_file = tk.StringVar()
selected_service = tk.StringVar()

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        selected_file.set(file_path)

def create_service():
    file_path = selected_file.get()
    service_name = selected_service.get().strip()
    
    if not file_path or not service_name:
        messagebox.showerror("Error", "Select a file and provide a service name!")
        return
    
    service_script = f"""
import win32serviceutil
import win32service
import win32event
import subprocess
import os
import sys

class CustomService(win32serviceutil.ServiceFramework):
    _svc_name_ = "{service_name}"
    _svc_display_name_ = "{service_name} Service"
    _svc_description_ = "A service that runs {os.path.basename(file_path)}."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.process = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        if self.process:
            self.process.terminate()
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.process = subprocess.Popen(["python", r"{file_path}"], shell=True)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(CustomService)
    """

    service_script_path = os.path.join(os.getcwd(), f"{service_name}_service.py")
    
    with open(service_script_path, "w", encoding="utf-8") as f:
        f.write(service_script)
    
    messagebox.showinfo("Success", f"Service script created: {service_script_path}\nInstall it using the button below.")

def install_service():
    service_name = selected_service.get().strip()
    if not service_name:
        messagebox.showerror("Error", "Provide a service name!")
        return
    try:
        subprocess.run(["python", f"{service_name}_service.py", "install"], check=True)
        messagebox.showinfo("Installation", f"Service '{service_name}' successfully installed!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Installation failed!")

def start_service():
    service_name = selected_service.get().strip()
    if not service_name:
        messagebox.showerror("Error", "Provide a service name!")
        return
    try:
        subprocess.run(["python", f"{service_name}_service.py", "start"], check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to start the service!")

def stop_service():
    service_name = selected_service.get().strip()
    if not service_name:
        messagebox.showerror("Error", "Provide a service name!")
        return
    try:
        subprocess.run(["python", f"{service_name}_service.py", "stop"], check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to stop the service!")

def remove_service():
    service_name = selected_service.get().strip()
    if not service_name:
        messagebox.showerror("Error", "Provide a service name!")
        return
    try:
        subprocess.run(["python", f"{service_name}_service.py", "remove"], check=True)
        os.remove(f"{service_name}_service.py")
        messagebox.showinfo("Removal", f"Service '{service_name}' successfully removed!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to remove the service!")

title_label = tk.Label(root, text="Service Maker", font=("Arial", 18, "bold"), fg="white", bg="#2E2E2E")
title_label.pack(pady=10)

file_frame = tk.Frame(root, bg="#2E2E2E")
file_frame.pack(pady=5)

file_label = tk.Label(file_frame, text="File to execute:", font=("Arial", 12), fg="white", bg="#2E2E2E")
file_label.pack(side=tk.LEFT, padx=5)

file_button = tk.Button(file_frame, text="📂 Select", command=choose_file, bg="#4A90E2", fg="white", font=("Arial", 10))
file_button.pack(side=tk.LEFT, padx=5)

file_path_label = tk.Label(root, textvariable=selected_file, font=("Arial", 10), fg="white", bg="#2E2E2E", wraplength=450)
file_path_label.pack(pady=5)

service_name_label = tk.Label(root, text="Service Name:", font=("Arial", 12), fg="white", bg="#2E2E2E")
service_name_label.pack()

service_name_entry = tk.Entry(root, textvariable=selected_service, font=("Arial", 12))
service_name_entry.pack(pady=5)

btn_style = {"font": ("Arial", 12), "fg": "white", "bg": "#4A90E2", "width": 25, "height": 1}

create_btn = tk.Button(root, text="🛠️ Create Service", command=create_service, **btn_style)
create_btn.pack(pady=5)

install_btn = tk.Button(root, text="📌 Install Service", command=install_service, **btn_style)
install_btn.pack(pady=5)

start_btn = tk.Button(root, text="▶️ Start Service", command=start_service, **btn_style)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="⏹️ Stop Service", command=stop_service, **btn_style)
stop_btn.pack(pady=5)

remove_btn = tk.Button(root, text="🗑️ Remove Service", command=remove_service, **btn_style)
remove_btn.pack(pady=5)

root.mainloop()
