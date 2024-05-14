from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
import googletrans

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False, False)


def label_change():
    c = combo_1.get()
    c_1 = combo_2.get()
    label_1.configure(text=c)
    label_2.configure(text=c_1)
    root.after(1000, label_change)


def translate_now():
    try:

        text_ = text_1.get(1.0, END)
        t1 = Translator()
        trans_text = t1.translate(text_, src=combo_1.get(), dest=combo_2.get())
        trans_text = trans_text.text

        text_2.delete(1.0, END)
        text_2.insert(END, trans_text)
    except Exception as e:
        print(e)
        messagebox.showerror("Error message", f"Get the error : {e}")


image_icon = PhotoImage(file="Google_translate.png")
root.iconphoto(False, image_icon)

change_icon = PhotoImage(file="change_data.png")
image_label = Label(root, image=change_icon, width=150)
image_label.place(x=460, y=150)

language = googletrans.LANGUAGES
languange_values = list(language.values())
lang_1 = language.keys()

combo_1 = ttk.Combobox(root, values=languange_values,
                       font="Roboto 14", state="r")
combo_1.place(x=110, y=20)
combo_1.set("English")

label_1 = Label(root, text="English", font="segoe 30 bold",
                bg="white", width=18, bd=5, relief=GROOVE)
label_1.place(x=10, y=50)

f_1 = Frame(root, bg="Black", bd=5)
f_1.place(x=10, y=118, width=440, height=210)

text_1 = Text(f_1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_1.place(x=0, y=0, width=430, height=200)

scrollbar_1 = Scrollbar(f_1)
scrollbar_1.pack(side="right", fill="y")

scrollbar_1.configure(command=text_1.yview)
text_1.configure(yscrollcommand=scrollbar_1.set)

combo_2 = ttk.Combobox(root, values=languange_values,
                       font="RobotV 14", state="r")
combo_2.place(x=730, y=20)
combo_2.set("SELECT LANGUANGE")

label_2 = Label(root, text="ENGLISH", font="segoe 30 bold",
                bg="white", width=18, bd=5, relief=GROOVE)
label_2.place(x=620, y=50)

f_2 = Frame(root, bg="Black", bd=5)
f_2.place(x=620, y=118, width=440, height=210)

text_2 = Text(f_2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_2.place(x=0, y=0, width=430, height=200)

scrollbar_2 = Scrollbar(f_2)
scrollbar_2.pack(side="right", fill="y")

scrollbar_2.configure(command=text_2.yview)
text_2.configure(yscrollcommand=scrollbar_2.set)


translate_btn = Button(root, text="Translate", font=("Roboto 15"),
                       activebackground="purple", cursor="hand2", bd=5, bg='red', fg="white", command=translate_now)
translate_btn.place(x=480, y=300)

label_change()
root.configure(bg="white")
root.mainloop()
