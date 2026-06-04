#tkinter for better ui(gui)
import tkinter as tk
#date and time for year and old
from datetime import datetime, timedelta
#massege box for ui
from tkinter import messagebox


def decode_nic():
    nic = nic_entry.get().strip().upper()
#try to get today date by builte in system
    try:
        today = datetime.today()

        # old or new identy
        if len(nic) == 10 and nic[:-1].isdigit() and nic[-1] in ("V", "X"):
            year = int("19" + nic[:2])
            day_code = int(nic[2:5])
            nic_type = "Old NIC"
        elif len(nic) == 12 and nic.isdigit():
            year = int(nic[:4])
            day_code = int(nic[4:7])
            nic_type = "New NIC"
        else:
            raise ValueError("Invalid NIC format")

       
        if day_code > 500:
            gender = "Female"
            day_of_year = day_code - 500
        else:
            gender = "Male"
            day_of_year = day_code

        if day_of_year < 1 or day_of_year > 366:
            raise ValueError("Invalid day code")#chat gpt

       
        dob = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)

        if dob > today:
            raise ValueError("Invalid birth date")

       
        age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)    #date of birth - today
        )

        
        result_label.config(
            text=
            f"NIC Type   : {nic_type}\n"
            f"DOB        : {dob.strftime('%Y-%m-%d')}\n"
            f"Gender     : {gender}\n"
            f"Age        : {age} years\n"
            f"NIC Status : Valid"
        )

    except:
        messagebox.showerror("wrong-nic",     "         invalid NIC Number"  "                                    [please chek nic number again]")
       # result_label.config(text="")


# tkinter ui

root = tk.Tk()
root.title("Sri Lanka NIC Decoder")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(
    root,
    text="NIC Decoder[sri-lanka]",
    font=("Ink Free", 16, "bold") #ink free is font if you want beter ui you want to install ink free font manually
).pack(pady=10)

tk.Label(root, text="Enter NIC Number in here").pack()

nic_entry = tk.Entry(root, width=35, font=("Arial", 11))
nic_entry.pack(pady=5)

tk.Button(
    root,
    text="Decode_NIC",
    command=decode_nic,
    width=15
).pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Consolas", 11),
    justify="left"
)
result_label.pack(pady=10)

tk.Label(
    root,
    text="contact_us > minecraft.tharupathi@gmail.com ",
    font=("Fixedsys", 9),#font-fixdays
    fg="green"
).pack(side="bottom", pady=5)

root.mainloop()
