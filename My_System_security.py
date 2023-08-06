import tkinter as tk
from tkinter import filedialog 
import  tkinter.messagebox
import os, psutil, webbrowser
from tkinter import *  


def miner_text_option(): 
    for proc in psutil.process_iter(['name']):
        if 'miner' in proc.info['name'].lower(): 
            proc.kill()
            os.system('taskmgr')
            tkinter.messagebox.showwarning('Найден опасный процесс!', f"Устранен процесс: {proc}")
            break 
        else: 
            tkinter.messagebox.showinfo('Опасных процессов не найдено', 'Process is security!') 
            os.system('taskmgr')
            break
def go_git(): 
    webbrowser.open_new_tab('https://github.com/vsdifficult')
    
def site(): 
    webbrowser.open_new_tab('')
    
def delete_files():
    
    folder_path = filedialog.askdirectory()

    
    if folder_path:
        for files in os.walk(folder_path):
            for file in files:
                
                if (file.endswith(".exe") or file.endswith(".py") or file.endswith(".bat")) and ("trojan" in file or "mainer" in file or "CryptoLocker" in file or "Zeus Gameover" in file ):
                    file_path = os.path.join(file)
                    
                    os.remove(file_path)
                    tkinter.messagebox.showwarning("Файлы успешно удалены") 
                    break
                     
                else: 
                    tkinter.messagebox.showinfo('system security', 'Вредоностных файлов не наденно') 
                    break

        
         
        

window = tk.Tk()


window.title("My system security")  

window.geometry('400x400') 
window.resizable(width=0, height=0)

header_frame = Frame(window, bg="green", height=50)
header_frame.pack(fill=X)

header_label = Label(header_frame, text="My Security System", fg="white", bg="green", font=("Arial", 18))

header_label.grid(row=1, column=1) 

frame = Frame(window, bg="green")
frame.pack(fill="both")

label = Label(frame, text="Security Menu", font=("Arial", 16, "bold"), bg="green", fg="white")
label.pack(pady=20)

virus_button = Button(frame, text="Virus Detect", command=delete_files)
virus_button.pack(side="left")

miner_button = Button(frame, text="Miner Detect", command=miner_text_option)
miner_button.pack(side="left")

github_button = Button(frame, text="GitHub", command=go_git)
github_button.pack(side="left") 

page_site = Button(frame, text = 'Site', command=site) 
page_site.pack(side="left") 

label_ = Label(window, text = 'My Security System .Inc') 
label_.pack(pady=100)

window.mainloop()
