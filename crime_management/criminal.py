from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Criminal:

    def __init__(self, root):
        max_width = 1080
        max_height = 720

        self.root = root
        self.root.geometry(f'{max_width}x{max_height}+0+0')
        self.root.title("CRIMINAL MANAGEMENT SYSTEM")
        self.root.resizable(False, False)

        lbl_title = Label(
            self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE', font=('Roboto', 30, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, width=max_width, height=70)

        # Logo Kepolisian
        img_logo = Image.open('./images/police_logo.jpg')
        img_logo = img_logo.resize((60, 60), Image.ADAPTIVE)
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=10, y=5, width=60, height=60)

        # Img_frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=70, width=max_width, height=130)

        img1 = Image.open('./images/image_1.jpg')
        img1 = img1.resize((360, 160), Image.ADAPTIVE)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=360, height=160)

        img2 = Image.open('./images/image_2.webp')
        img2 = img2.resize((360, 160), Image.ADAPTIVE)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=361, y=0, width=360, height=160)

        img3 = Image.open('./images/image_3.jpg')
        img3 = img3.resize((360, 160), Image.ADAPTIVE)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=721, y=0, width=360, height=160)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=200, width=1060, height=500)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information', font=(
            'Roboto', 11, 'bold'), bg='white', fg='black')
        upper_frame.place(x=10, y=10, width=1040, height=230)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information Table', font=(
            'Roboto', 11, 'bold'), bg='white', fg='black')
        down_frame.place(x=10, y=250, width=1040, height=230)

        down_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=(
            'Roboto', 11, 'bold'), bg='white', fg='black')
        down_frame.place(x=0, y=0, width=1030, height=50)


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
