import tkinter as tk
import smtplib

gui = tk.Tk()
gui.title("Email generator")
gui.configure(background='light green')
gui.geometry('300x200')

flg: bool = False
message = "Hi, this was my second message"


def mailsent(message):

    global flg
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender mail id", "password")
    flg = True
    s.sendmail("sender mail id", "receiver mail id", message)
    s.quit()


btn = tk.Button(gui, text="Send Email", command=mailsent(message)).grid(row=6, column=1)

if flg:
    l01 = tk.Label(gui, text="Sent email successfully").grid(row=7, column=1)
else:
    l02 = tk.Label(gui, text="Unable to send email").grid(row=7, column=1)
    
    
gui.mainloop()
