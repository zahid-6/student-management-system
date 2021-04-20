from tkinter import *
from tkinter import ttk


class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("SMS")
        self.root.geometry("1370x700+0+0")

        title = Label(self.root, text="SMS", bd=10, relief=GROOVE, font=("arial", 50, "italic bold"), bg="light blue",
                      fg="black")
        title.pack(side=TOP, fill=X)

        ############################################################## ManageFrame

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light green")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        ##############################################################Labels

        m_title = Label(Manage_Frame, text="Student Info.", bg="light green", fg='red',
                        font=("arial", 40, "italic bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_ID = Label(Manage_Frame, text="S. ID", bg="light green", fg='black', font=("arial", 20, "italic bold"))
        lbl_ID.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_ID = Entry(Manage_Frame, font=("arial", 15, "italic bold"), bd=5, relief=GROOVE)
        txt_ID.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="S. Name", bg="light green", fg='black', font=("arial", 20, "italic bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, font=("arial", 15, "italic bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_RegS = Label(Manage_Frame, text="Reg. status", bg="light green", fg='black',
                         font=("arial", 16, "italic bold"))
        lbl_RegS.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_RegS = ttk.Combobox(Manage_Frame, font=("arial", 14, "italic bold"), state='readonly')
        combo_RegS['values'] = ("Pending", "Partially complete", "Complete")
        combo_RegS.grid(row=3, column=1, pady=10, padx=20)

        lbl_course = Label(Manage_Frame, text="List of course", bg="light green", fg='black',
                           font=("arial", 10, "italic bold"))
        lbl_course.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(Manage_Frame, width=22, height=3, font=("arial", 14, "italic bold"))
        self.txt_address.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        ############################################################## ButtonFrame
        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE, bg="light green")
        btn_Frame.place(x=10, y=500, width=430)
        Addbtn=Button(btn_Frame,text="ADD",width=10).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_Frame, text="update", width=10).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="clear", width=10).grid(row=0, column=3, padx=10, pady=10)

        ############################################################## DetailsFrame

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light green")
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg="light green", fg='black',
                           font=("arial", 20, "italic bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Details_Frame, font=("arial", 14, "italic bold"), width=10, state='readonly')
        combo_search['values'] = ("S. ID", "S. Name", "Reg. Satus")
        combo_search.grid(row=0, column=1, pady=10, padx=20)
        txt_search = Entry(Details_Frame, font=("arial", 10, "italic bold"), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Details_Frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Details_Frame, text="Show All", width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        ########################################table frame

        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="royal blue")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame, column=("S. ID", "S. Name", "Reg. status"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("S. ID", text="Student Id")
        self.Student_table.heading("S. Name", text="Student Name")
        self.Student_table.heading("Reg. status", text="Reg.Status")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("S. ID", width=100)
        self.Student_table.column("S. Name", width=100)
        self.Student_table.column("Reg. status", width=100)




class Student():
    pass
    root = Tk()
    obj= Student(root)
    root.mainloop()