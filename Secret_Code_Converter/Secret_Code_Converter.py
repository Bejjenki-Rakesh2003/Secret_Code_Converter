import tkinter as tk

#converting input into secret_Code...
def convert_to_uppercase():
    input_text = input_field.get()  # Get text from input field
    output_field.delete(1.0, tk.END)  # Clear output field
    input_string=input_text.lower() # Convert text into LowerCase
    db='abcdefghijklmnopqrstuvwxyz'
    rev=''
    for i in range(len(input_string)):
        if not(input_string[i]>='a' and input_string[i]<='z'):
            rev+=input_string[i]
            continue
        rr=db.index(input_string[i])-(2*db.index(input_string[i]))
        rev+=db[rr-1]
    
    output_field.insert(tk.END, rev)  # Insert the uppercase text into output field

#Main window Setup
root = tk.Tk()
root.title("Secret Code Converter")

#The window size (width x height)
root.geometry("500x350") 

#Canvas for window gradient background
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

for i in range(350):  # 350 is the window height
    color = f"#{int(255 - i / 350 * 255):02x}{int(i / 350 * 255):02x}ff"
    canvas.create_line(0, i, 500, i, fill=color)

# Create title label with underlined effect
title_label = tk.Label(root, text="Secret Code Converter", font=("Times New Roman", 18, "bold"), fg="green", bg="#f0f0f0")
title_label.place(x=130, y=20)  # Positioning title label above canvas


#Input field
input_field = tk.Entry(root, width=40, font=("Arial", 12), bg="#f0f0f0", relief="solid", bd=2)
input_field.place(x=70, y=100)

#Convert button 
convert_button = tk.Button(root, text="Convert to Secret Code", command=convert_to_uppercase, bg="gold", fg="black", font=("Arial", 12))
convert_button.place(x=160, y=160)

#Output field 
output_field = tk.Text(root, height=4, width=40, font=("Arial", 12), bg="#f0f0f0", relief="solid", bd=2)
output_field.place(x=70, y=220)

#Specil note
note_label = tk.Label(root, text="Note: It is for kepping our message as confidential, message encode and decode ", font=("Arial",9, "bold"), fg="red")
note_label.place(x=0, y=320)

# Run the main event loop
root.mainloop()
