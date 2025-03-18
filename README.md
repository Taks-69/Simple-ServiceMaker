# Simple-ServiceMaker

Service Maker is a **GUI-based tool** that allows users to create, install, manage, and remove **Windows Services** from Python scripts.

---

## 🚀 Features

✅ **Convert Python scripts into Windows services**  
✅ **Start, stop, install, and remove services easily**  
✅ **User-friendly GUI with intuitive controls**  
✅ **Automated service script generation**  
✅ **Works with `pywin32` to manage Windows services**  

---

## 📂 Repository Structure

```
Simple-ServiceMaker/
│── main.py  # Main GUI script for managing services
│── requirements.txt  # Dependencies list
```

---

## 📥 Installation

### **Prerequisites**
- **Windows OS** (as services are Windows-specific)
- **Python 3.x**
- **pip** (Python Package Installer)
- **Administrator privileges** (required for managing services)

### **Clone the Repository**
```bash
git clone https://github.com/Taks-69/Simple-ServiceMaker.git
cd Simple-ServiceMaker
```

### **Install Required Libraries**
```bash
pip install -r requirements.txt
```

### **Required Dependencies** (included in `requirements.txt`)
- `pywin32`
- `tkinter`

---

## 🛠 Usage

### **Run the Application**
```bash
python main.py
```

### **How It Works**
1. **Select a Python file** to be converted into a service.
2. **Assign a service name** using the input field.
3. Click **"Create Service"** to generate the Windows Service script.
4. Click **"Install Service"** to register it in the system.
5. Use **"Start"**, **"Stop"**, and **"Remove"** to manage the service.

---

## 🔄 Workflow

1. **Select a Python script** from the file browser.
2. **Service Maker generates a Windows Service script** with start and stop functions.
3. **Install the service** to make it persistent.
4. **Manage the service** from the interface.

---

## 🔮 Future Features
  
🔹 Linux Support - Extend compatibility to Linux using `systemd`.  
🔹 GUI Enhancements - Add more customization options.

---

## ⚠️ Disclaimer
> This tool requires **administrator privileges** to install services. Make sure you understand what you are doing before installing system-wide services.

---

## 📚 License

This project is licensed under the **GNU General Public License v3.0**.

---

🔥 **Feel free to star ⭐ the repository if you find this project useful!** 🚀

