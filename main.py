# 2023 LUKKSHH 
import cv2
import qrcode
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def scan():
    get_image = filedialog.askopenfilename(filetypes=[('Images', ('*.png','*.jpeg','*.jpg'))])

    if not get_image:
        messagebox.showinfo(title='QrLukkshh Error', message='You Need Choose Image')
        return
    cv2img = cv2.imread(get_image)
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, _ , _ = qrCodeDetector.detectAndDecode(cv2img)
    scanner_output.configure(text=decodedText)
    if not decodedText:
        messagebox.showerror(title='QrLukkshh Error', message="Error Occured, Either you choose the wrong file or the QR code is not visible")
        return

def qrgen():
    user_inp = gen_entry.get()

    if not user_inp:
        messagebox.showinfo(title='QrLukkshh Error', message='You Need To Fill Entery')
        return

    qr_img = qrcode.make(user_inp)

    filename = filedialog.asksaveasfilename(filetypes=[('Image', '*.png')],defaultextension=".png")
    if not filename:
        messagebox.showinfo(title='QrLukkshh Error', message='You Need To Chose Name To Save File As')
        return
    
    qr_img.save(filename)
    gen_msg.configure(text='Image Saved Succsessfuly')
    

root = Tk()
root.geometry('350x400')
root.resizable(False,False)

root.title('QrLukkshh')
root.iconbitmap('lukkshh.ico')

notebook = ttk.Notebook(root, width=350 , height=400)
notebook.pack(expand=True)

generator_frame = ttk.Frame(notebook)
scanner_frame = ttk.Frame(notebook)

generator_frame.pack(fill='both', expand=True)
scanner_frame.pack(fill='both', expand=True)

notebook.add(generator_frame, text='Generator')
notebook.add(scanner_frame, text='Scanner')

# Generator Side
gen_label = Label(master=generator_frame,text='Generator', font='Arial 20 bold')
gen_label.pack(pady=20)

gen_entry = Entry(master=generator_frame , width=50)
gen_entry.pack(pady=6)

gen_msg = Label(master=generator_frame, text='', font='Arial 10' )
gen_msg.pack(pady=4)

gen_button = Button(master=generator_frame , text='Generate',command=qrgen)
gen_button.pack(pady=4)

# Scanner Side
scanner_label = Label(master=scanner_frame ,text='Scanner' ,font='Arial 20 bold')
scanner_label.pack(pady=20)

scanner_output = Label(master=scanner_frame, text='', font='Arial 13' )
scanner_output.pack(pady=2)

scanner_button = Button(master=scanner_frame, text='Choose Image' , width=15 , height=1 , command=scan)
scanner_button.pack(pady=50)

root.mainloop()
# 2023 LUKKSHH 