from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Criminal:

    def __init__(self, root):
        max_width = 1540
        max_height = 790

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
        Main_frame.place(x=10, y=200, width=1500, height=560)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information', font=(
            'Roboto', 11, 'bold'), bg='white', fg='black')
        upper_frame.place(x=10, y=10, width=1470, height=270)

        # Label Entry

        # id kasus
        case_id = Label(upper_frame, text='Case ID:', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        case_id.grid(row=0, column=0, padx=2, sticky=W)

        case_entry = ttk.Entry(upper_frame, width=22,
                               font=('Roboto', 11, 'bold'))
        case_entry.grid(row=0, column=1, padx=2, sticky=W)

        # No. Criminal
        no_criminal = Label(upper_frame, text='No. Criminal:', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        no_criminal.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_criminal_no = ttk.Entry(upper_frame, width=22,
                                    font=('Roboto', 11, 'bold'))
        txt_criminal_no.grid(row=0, column=3, padx=2, sticky=W, pady=7)

        # Nama Criminal
        criminal_name = Label(upper_frame, text='Nama Criminal:', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        criminal_name.grid(row=1, column=0, padx=2, sticky=W, pady=7)

        txt_criminal_name = ttk.Entry(upper_frame, width=22,
                                      font=('Roboto', 11, 'bold'))
        txt_criminal_name.grid(row=1, column=1, padx=2, sticky=W, pady=7)

        # Nickname
        nickname = Label(upper_frame, text='Nickname:', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        nickname.grid(row=1, column=2, padx=2, sticky=W, pady=7)

        txt_nickname = ttk.Entry(upper_frame, width=22,
                                 font=('Roboto', 11, 'bold'))
        txt_nickname.grid(row=1, column=3, padx=2, sticky=W, pady=7)

        # tanggal tangkap
        arrest_date = Label(upper_frame, text='Tanggal tangkap:', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        arrest_date.grid(row=2, column=0, padx=2, sticky=W, pady=7)

        txt_arrest_date = ttk.Entry(upper_frame, width=22,
                                    font=('Roboto', 11, 'bold'))
        txt_arrest_date.grid(row=2, column=1, padx=2, sticky=W, pady=7)

        # tanggal kriminal
        date_of_crime = Label(upper_frame, text='Tanggal Kriminal:', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        date_of_crime.grid(row=2, column=2, padx=2, sticky=W, pady=7)

        txt_date_of_crime = ttk.Entry(upper_frame, width=22,
                                      font=('Roboto', 11, 'bold'))
        txt_date_of_crime.grid(row=2, column=3, padx=2, sticky=W, pady=7)

        # Alamat
        address = Label(upper_frame, text='Alamat:', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        address.grid(row=3, column=0, padx=2, sticky=W, pady=7)

        txt_address = ttk.Entry(upper_frame, width=22,
                                font=('Roboto', 11, 'bold'))
        txt_address.grid(row=3, column=1, padx=2, sticky=W, pady=7)

        # Umur
        age = Label(upper_frame, text='Umur :', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        age.grid(row=3, column=2, padx=2, sticky=W, pady=7)

        txt_age = ttk.Entry(upper_frame, width=22,
                            font=('Roboto', 11, 'bold'))
        txt_age.grid(row=3, column=3, padx=2, sticky=W, pady=7)

        # Pekerjaan
        occupution = Label(upper_frame, text='Pekerjaan :', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        occupution.grid(row=4, column=0, padx=2, sticky=W, pady=7)

        txt_occupution = ttk.Entry(upper_frame, width=22,
                                   font=('Roboto', 11, 'bold'))
        txt_occupution.grid(row=4, column=1, padx=2, sticky=W, pady=7)

        # Tanda lahir
        birth_mark = Label(upper_frame, text='Tanda Lahir :', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        birth_mark.grid(row=4, column=2, padx=2, sticky=W, pady=7)

        txt_birth_mark = ttk.Entry(upper_frame, width=22,
                                   font=('Roboto', 11, 'bold'))
        txt_birth_mark.grid(row=4, column=3, padx=2, sticky=W, pady=7)

        # Jenis Kejahatan
        crime_type = Label(upper_frame, text='Jenis Kejahatan :', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        crime_type.grid(row=0, column=4, padx=2, sticky=W, pady=7)

        txt_crime_type = ttk.Entry(upper_frame, width=22,
                                   font=('Roboto', 11, 'bold'))
        txt_crime_type.grid(row=0, column=5, padx=2, sticky=W, pady=7)

        # Nama Ayah
        father_name = Label(upper_frame, text='Nama Ayah :', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        father_name.grid(row=1, column=4, padx=2, sticky=W, pady=7)

        txt_father_name = ttk.Entry(upper_frame, width=22,
                                    font=('Roboto', 11, 'bold'))
        txt_father_name.grid(row=1, column=5, padx=2, sticky=W, pady=7)

        # Jenis Kelamin
        gender = Label(upper_frame, text='Jenis Kelamin :', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        gender.grid(row=2, column=4, padx=2, sticky=W, pady=7)

        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=768, y=80, width=182, height=30)

        male = Radiobutton(radio_frame_gender,
                           text='Laki-laki', value='laki-laki', font=(
                               'Roboto', 8, 'bold'), bg='white')
        male.grid(row=0, column=0, padx=2, pady=2, sticky=W)
        female = Radiobutton(radio_frame_gender,
                             text='Perempuan', value='perempuan', font=(
                                 'Roboto', 8, 'bold'), bg='white')
        female.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        # Wanted?
        wanted = Label(upper_frame, text='DPO :', font=(
            'Roboto', 11, 'bold'), bg='white', fg='red')
        wanted.grid(row=3, column=4, padx=2, sticky=W, pady=7)

        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=768, y=115, width=182, height=30)

        yes = Radiobutton(radio_frame_wanted,
                          text='iya', value='iya', font=(
                               'Roboto', 8, 'bold'), bg='white')
        yes.grid(row=0, column=0, padx=2, pady=2, sticky=W)
        tidak = Radiobutton(radio_frame_wanted,
                            text='tidak', value='tidak', font=(
                                 'Roboto', 8, 'bold'), bg='white')
        tidak.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        # Button
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=630, height=45)

        # Button Tambah
        btn_add = Button(button_frame, text='Simpan Biodata', font=(
            'Roboto', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)

        # Button Perbarui
        btn_update = Button(button_frame, text='Perbarui', font=(
            'Roboto', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=5)

        # Button Hapus
        btn_delete = Button(button_frame, text='Hapus', font=(
            'Roboto', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        # Button Clear
        btn_clear = Button(button_frame, text='Clear', font=(
            'Roboto', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

        # Background right side image
        background_side_img = Image.open('./images/police_logo.jpg')
        background_side_img = background_side_img.resize(
            (470, 245), Image.ADAPTIVE)
        self.photoCrime = ImageTk.PhotoImage(background_side_img)

        self.img_crime = Label(upper_frame, image=self.photoCrime)
        self.img_crime.place(x=1000, y=0, width=470, height=245)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information Table', font=(
            'Roboto', 11, 'bold'), bg='white', fg='black')
        down_frame.place(x=10, y=280, width=1480, height=270)

        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=(
            'Roboto', 11, 'bold'), bg='white', fg='black')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, text='Search By :', font=(
            'Roboto', 11, 'bold'), bg='red', fg='white')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        combo_search_box = ttk.Combobox(
            search_frame, font=('Roboto', 11, 'bold'), width=18, state='readonly')
        combo_search_box['value'] = (
            'Select Option', 'Case_id', 'No. Criminal')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, padx=5, sticky=W)

        search_txt = ttk.Entry(search_frame, width=18,
                               font=('Roboto', 11, 'bold'))
        search_txt.grid(row=0, column=2, sticky=W, padx=5)

        btn_search = Button(search_frame, text='Search', font=(
            'Roboto', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=3, pady=5)

        btn_all = Button(search_frame, text='Lihat Semua', font=(
            'Roboto', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_all.grid(row=0, column=4, padx=3, pady=5)

        agency_crime = Label(search_frame, text='KEPOLISIAN BANDAR LAMPUNG', font=(
            'Roboto', 30, 'bold'), bg='white', fg='crimson')
        agency_crime.grid(row=0, column=5, padx=30, sticky=W, pady=0)

        # Tabel
        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, columns=(
            "1", "2", '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1', text='Case Id')
        self.criminal_table.heading('2', text='No. Crime')
        self.criminal_table.heading('3', text='Nama Kriminal')
        self.criminal_table.heading('4', text='Nickname')
        self.criminal_table.heading('5', text='Tanggal Ditangkap')
        self.criminal_table.heading('6', text='Tanggal Kriminal')
        self.criminal_table.heading('7', text='Alamat')
        self.criminal_table.heading('8', text='Umur')
        self.criminal_table.heading('9', text='Pekerjaan')
        self.criminal_table.heading('10', text='Tanda Lahir')
        self.criminal_table.heading('11', text='Jenis Kejahatan')
        self.criminal_table.heading('12', text='Nama Ayah')
        self.criminal_table.heading('13', text='Jenis Kelamin')
        self.criminal_table.heading('14', text='DPO')

        self.criminal_table['show'] = 'headings'

        self.criminal_table.column('1', width=100)
        self.criminal_table.column('2', width=100)
        self.criminal_table.column('3', width=100)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=100)
        self.criminal_table.column('6', width=100)
        self.criminal_table.column('7', width=100)
        self.criminal_table.column('8', width=100)
        self.criminal_table.column('9', width=100)
        self.criminal_table.column('10', width=100)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=100)
        self.criminal_table.column('13', width=100)
        self.criminal_table.column('14', width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
