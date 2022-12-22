# Basic tkinter template
from tkinter import*
import random
root=Tk()
root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_id=Label(root)
label_name=Label(root)
label_dob=Label(root)
label_pin=Label(root)
label_address=Label(root)
label_vehicle_type=Label(root)
# Define the function
def driver():
    iddd=8475924365
    print(type(iddd))
    name="Alice in Wonderland"
    print(type(name))
    dob="4/4/2004"
    print(type(dob))
    pin=430985
    print(type(pin))
    address="Rose Square,New England,Great Britan"
    print(type(address))
    vehicle=["Two Wheel,Four Wheel"]
    print(type(vehicle))
    label_id["text"]=iddd
    label_name["text"]=name
    label_dob["text"]=dob
    label_address["text"]=pin
    label_pin["text"]=address
    label_vehicle_type["text"]=vehicle    
    
# Create a button
btn1=Button(root,text="Show my ID card",command=driver)
btn1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
btn1_window = canvas.create_window(200, 235, anchor=CENTER, window=btn1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
root.mainloop()