import mydb
import tkinter as tk
import showsearch
class search_user(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("search sales and salary of user")
        self.setup_ui()
    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.pack()
        tk.Label(row1,text="user name:",width=12,justify='right').grid(row=0,column=0)
        self.name = tk.StringVar()
        self.name.set("")
        tk.Entry(row1,textvariable=self.name,width=20).grid(row=0,column=1)

        row2 = tk.Frame(self)
        row2.pack()
        tk.Button(row2,text="comfirm",command=self.ok).grid(row=1,column=0)
        tk.Button(row2,text="cancel",command=self.cancel).grid(row=1,column=1)

    def ok(self):
        name = self.name.get()
        comm = mydb.Commission()
        user_id = list(comm.get_id_from_name(name))[0]
        res = comm.get_records_form_id(user_id)
        num = [0,"",name,0,0,0,0.,0.]
        sh = showsearch.show_salary()
        for r in res:
            num[0] += 1
            num[1] = r[0]
            num[3:] = r[1:]
            sh.showSearchData(num)

    def cancel(self):
        self.destroy()