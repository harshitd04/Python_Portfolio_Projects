import customtkinter as ctk

MORSE_CODE_DICT ={
    'a': '. -',      'b': '- . . .',   'c': '- . - .',   'd': '- . .',    'e': '.',
    'f': '. . - .',  'g': '- - .',     'h': '. . . .',   'i': '. .',      'j': '. - - -',
    'k': '- . -',    'l': '. - . .',   'm': '- -',       'n': '- .',      'o': '- - -',
    'p': '. - - .',  'q': '- - . -',   'r': '. - .',     's': '. . .',    't': '-',
    'u': '. . -',    'v': '. . . -',   'w': '. - -',     'x': '- . . -',  'y': '- . - -',
    'z': '- - . .',

    '0': '- - - - -',  '1': '. - - - -',  '2': '. . - - -',  '3': '. . . - -',
    '4': '. . . . -',  '5': '. . . . .',  '6': '- . . . .',  '7': '- - . . .',
    '8': '- - - . .',  '9': '- - - - .'
}#Space b/w parts of the same letter = 3 units

# user_input = input("Enter text(Only Numbers and Words): ").lower()
def find_morse_code(user_input):
    morse_code = ""
    for i in user_input:
        if i == " ":
            morse_code = morse_code + "       "  #Space b/w text = 7 units 
        elif i in MORSE_CODE_DICT:
            morse_code = morse_code + MORSE_CODE_DICT[i]
            morse_code = morse_code + "   "      #Space b/w letter = 3 units
        else:
            morse_code = "Wrong Input! Only letters and numbers allowed."
            break

    output_label.configure(text = morse_code)

        # print(f"For input: {user_input}")
        # print(f"Morse Code is: {morse_code}\n")


ctk.set_appearance_mode("Dark")
app = ctk.CTk()
app.geometry("450x340")
app.title("Text to Morse Code Converter")


user_entry_label = ctk.CTkLabel(master=app, text="Enter text")
user_entry_label.pack(pady=10)

user_entry = ctk.CTkEntry(master=app, width=200 ,placeholder_text = "(Only Numbers and Words)")
user_entry.pack(pady=0)

def on_enter_button_click():
    user_input = user_entry.get().lower()
    print(f"User entered: {user_input}")
    find_morse_code(user_input=user_input)

enter_button = ctk.CTkButton(master=app, text="Submit", command=on_enter_button_click)
enter_button.pack(pady=13)

pre_output_label = ctk.CTkLabel(master=app, text="Morse Code", wraplength=350)
pre_output_label.pack(pady=17)
output_label = ctk.CTkLabel(master=app, text="", wraplength=350)
output_label.pack(pady=17)



app.mainloop()