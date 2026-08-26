import tkinter
import random
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

BG = "#0F172A"
FRAME = "#1E293B"
PRIMARY = "#3B82F6"
ACCENT = "#06B6D4"
TEXT = "#F1F5F9"

window = tkinter.Tk()

# Adding Change between Pages Functions

def Back_To_Home_Page():
    Text_Editor_Frame.pack_forget()
    To_Do_List_Frame.pack_forget()
    Random_Page_Frame.pack_forget()
    Color_Chooser_Frame.pack_forget()
    Home_Frame.pack()

def Open_Text_Editor():
    Text_Editor_Frame.pack()
    Home_Frame.pack_forget()
    To_Do_List_Frame.pack_forget()
    Random_Page_Frame.pack_forget()
    Color_Chooser_Frame.pack_forget()

def Open_To_Do_List():
    To_Do_List_Frame.pack()
    Home_Frame.pack_forget()
    Text_Editor_Frame.pack_forget()
    Random_Page_Frame.pack_forget()
    Color_Chooser_Frame.pack_forget()

def Open_Random_Tool():
    Random_Page_Frame.pack()
    Home_Frame.pack_forget()
    Text_Editor_Frame.pack_forget()
    To_Do_List_Frame.pack_forget()
    Color_Chooser_Frame.pack_forget()

def Open_ColorChooser_Tool():
    Color_Chooser_Frame.pack()
    Home_Frame.pack_forget()
    Text_Editor_Frame.pack_forget()
    To_Do_List_Frame.pack_forget()
    Random_Page_Frame.pack_forget()

def Quit_App():
    window.destroy()

# Adding The menu buttons _______________________
menubar = tkinter.Menu()
window.config(menu=menubar)
window.geometry("900x800")

File_button = tkinter.Menu(menubar)
menubar.add_cascade(label="File", font=("Arial", 18), menu=File_button)
File_button_buttons = ["Home", "Exit"]
File_button_commands = [Back_To_Home_Page, Quit_App]
for loop in range(len(File_button_buttons)):
    if loop == 1:
        File_button.add_separator()
    File_button.add_command(label=File_button_buttons[loop], font=("Arial", 10), command=File_button_commands[loop])

Tool_Button = tkinter.Menu(menubar)
menubar.add_cascade(label="Tools", font=("Arial", 18), menu=Tool_Button)
Tool_Button_Buttons = ["Text Editor", "To Do List", "Random Tool", "Color Chooser"]
File_button_commands = [Open_Text_Editor, Open_To_Do_List, Open_Random_Tool, Open_ColorChooser_Tool]
for loop in range(len(Tool_Button_Buttons)):
    Tool_Button.add_command(label=Tool_Button_Buttons[loop], command=File_button_commands[loop], font=("Arial", 10))



# Adding Main Page Content __________________________

Home_Frame = tkinter.Frame(window)
Home_Frame.pack()
Home_First_Label = tkinter.Label(Home_Frame, text="RG : Tool Box", font=("Segui Ui", 30, "bold"), pady=20)
Home_First_Label.pack()
Main_frame = tkinter.Frame(Home_Frame, pady=20)
Main_frame.pack()
Text_Editor = tkinter.Button(Main_frame, text="📝Text Editor", font=("Roboto", 20), command=Open_Text_Editor, bd=0)
Text_Editor.grid(row=0, column=0, pady=20, padx=10)
List_Manager = tkinter.Button(Main_frame, text="📋 To Do List", font=("Roboto", 20), command=Open_To_Do_List, bd=0)
List_Manager.grid(row=1, column=0, pady=20, padx=10)
Random_Tool = tkinter.Button(Main_frame, text="🎲 Random", font=("Roboto", 20), command=Open_Random_Tool, bd=0)
Random_Tool.grid(row=0, column=1, pady=20, padx=10)
Color_Tool = tkinter.Button(Main_frame, text="🎨 Colors", font=("Roboto", 20), command=Open_ColorChooser_Tool, bd=0)
Color_Tool.grid(row=1, column=1, pady=20, padx=10)

# Adding Text Editor Functions ____________________________________

def Text_Editor_Save_Function():

    Text_Entered = Text_Editor_Text.get("1.0", "end") # Get The Text Entered From The User
    Text_Save_Location = filedialog.asksaveasfile(filetypes=[("text file", ".txt")]) # Ask The User For The Name And Path
    print(Text_Save_Location)
    Text_Save_Location.write(str(Text_Entered)) # Create A Text File And Enter What The User Has Type On Text Area
    Text_Save_Location.close() # Close The File Directory UI

def Text_Editor_Import_Function():
    Text_Import_Location = filedialog.askopenfilename(filetypes=[("text file", ".txt"), ("all files", ".*")])
    print(str(Text_Import_Location))
    Opened_Text_Import_Location = open(Text_Import_Location)
    Readed_Text_Imported = Opened_Text_Import_Location.read()
    print(Readed_Text_Imported)
    Text_Editor_Text.insert("1.0", str(Readed_Text_Imported))


# Adding Text Editor Page

Text_Editor_Frame = tkinter.Frame(window)
Text_Editor_Text = tkinter.Text(Text_Editor_Frame, font=("Ink free", 20), height=10, width=30, pady=5, padx=5, bg="light yellow")
Text_Editor_Text.pack()
Text_Editor_Button_Frame = tkinter.Frame(Text_Editor_Frame)
Text_Editor_Button_Frame.pack()
Text_Editor_Save_Button = tkinter.Button(Text_Editor_Button_Frame, font=("Arial", 15), text="Save", command=Text_Editor_Save_Function)
Text_Editor_Save_Button.pack(side="left")
Text_Editor_Import_Button = tkinter.Button(Text_Editor_Button_Frame, font=("Arial", 15), text="Import", command=Text_Editor_Import_Function)
Text_Editor_Import_Button.pack(side="right")

# Adding To Do List Functions______________________________
To_Do_Checkbuttons_Table = []
def To_Do_List_Added():
    To_Do_Name = To_Do_List_Entry.get()
    if len(To_Do_Name) > 0:
        Task = tkinter.Checkbutton(To_Do_List_LabelFrame, text=str(To_Do_Name), font=("Roboto", 20), anchor="w")
        Task.pack()
        To_Do_Checkbuttons_Table.append(Task)
        To_Do_List_Entry.delete(0, "end")
    
def To_Do_List_Delete():
    if To_Do_Checkbuttons_Table:
        Deleted_Task = To_Do_Checkbuttons_Table.pop() # Cut The last value of the table to the deleted task
        Deleted_Task.destroy() # delete the deleted task value

# Adding To Do List Page

To_Do_List_Frame = tkinter.Frame(window)
To_Do_List_Label = tkinter.Label(To_Do_List_Frame, text="📋 My Daily To-Do", font=("Roboto", 30, "bold"), pady=18, padx=30)
To_Do_List_Label.pack()
To_Do_List_Entry = tkinter.Entry(To_Do_List_Frame, font=("Arial", 20))
To_Do_List_Entry.pack(pady=20)
To_Do_List_Buttons = tkinter.Frame(To_Do_List_Frame)
To_Do_List_Buttons.pack()
To_Do_List_Addtask = tkinter.Button(To_Do_List_Buttons, text="+ Add Task", font=("Roboto", 25), bg="#00C230", fg="white", padx=20,
                                     bd=1, relief="solid", activebackground="#29FF5F", activeforeground="white", command=To_Do_List_Added)
To_Do_List_Addtask.pack(side="right",pady=20)
To_Do_List_Removetask = tkinter.Button(To_Do_List_Buttons, text="- Remove Task", font=("Roboto", 25), bg="#FF0800", fg="white",
                                       bd=1, relief="solid", activebackground="#E23D28", command=To_Do_List_Delete)
To_Do_List_Removetask.pack(side="left", pady=20)
To_Do_List_LabelFrame = tkinter.LabelFrame(To_Do_List_Frame, text="Tasks : ", font=("Arial", 20), width=400, height=400)
To_Do_List_LabelFrame.pack_propagate(False)
To_Do_List_LabelFrame.pack()

# Adding Randome Page Fucntions_______________________________

def Enter_First_Numberrange():
    global Random_First_Range
    Random_First_Range = int(Randome_Page_Firstentry.get())
    Random_Page_RangeLabel["text"] = "Min : " + str(Random_First_Range) + " Max : " + str(Random_Second_Range)

def Enter_Second_Numberrange():
    global Random_Second_Range
    Random_Second_Range = int(Randome_Page_secondentry.get())
    Random_Page_RangeLabel["text"] = "Min : " + str(Random_First_Range) + " Max : " + str(Random_Second_Range)

Random_First_Range = 0
Random_Second_Range = 10
Random_Number = random.randint(Random_First_Range, 10)

def Choose_Random_Number():
    global Random_Number
    try:
        Random_Number = random.randint(Random_First_Range, Random_Second_Range)
        Random_Page_Numberlabel["text"] = "The Number is : " + str(Random_Number)
    except ValueError:
        Random_Page_Numberlabel["text"] = "Please Enter A Valid Value ! "

# Adding Randome Page

Random_Page_Frame = tkinter.Frame(window)
Random_Page_Label = tkinter.Label(Random_Page_Frame, text="Choose A Random Number !", font=("Roboto", 25),)
Random_Page_Label.pack(pady= 10)
Random_Page_RangeLabel = tkinter.Label(Random_Page_Frame, font=("Roboto", 20), text="Min : 1 Max : 10")
Random_Page_RangeLabel.pack(pady=5)
Random_Page_Button = tkinter.Button(Random_Page_Frame, text="Click Me!", font=("Arial", 20), command=Choose_Random_Number)
Random_Page_Button.pack(pady=10)
Random_Page_Numberlabel = tkinter.Label(Random_Page_Frame, text="The Number is : ", font=("Arial", 25))
Random_Page_Numberlabel.pack(pady=10)
Random_Page_FirstEntry_Frame = tkinter.Frame(Random_Page_Frame)
Random_Page_FirstEntry_Frame.pack(pady=10)
Random_Page_FirstEntry_label = tkinter.Label(Random_Page_FirstEntry_Frame, font=("Arial", 20), text="Enter minimum Number :")
Random_Page_FirstEntry_label.grid(row=0, column=0)
Randome_Page_Firstentry = tkinter.Entry(Random_Page_FirstEntry_Frame, font=("Roboto", 20))
Randome_Page_Firstentry.grid(row=0, column=1)
Randome_Page_Firstentry_Enter = tkinter.Button(Random_Page_FirstEntry_Frame, text="Enter", font=("Arial", 20), command=Enter_First_Numberrange)
Randome_Page_Firstentry_Enter.grid(row=0, column=2)
Random_Page_SecondEntry_Frame = tkinter.Frame(Random_Page_Frame)
Random_Page_SecondEntry_Frame.pack(pady=10)
Random_Page_SecondEntry_label = tkinter.Label(Random_Page_SecondEntry_Frame, font=("Arial", 20), text="Enter Maximum Number :")
Random_Page_SecondEntry_label.grid(row=0, column=0)
Randome_Page_secondentry = tkinter.Entry(Random_Page_SecondEntry_Frame, font=("Roboto", 20))
Randome_Page_secondentry.grid(row=0, column=1)
Randome_Page_secondentry_Enter = tkinter.Button(Random_Page_SecondEntry_Frame, font=("Ariel", 20), text="Enter", command=Enter_Second_Numberrange)
Randome_Page_secondentry_Enter.grid(row=0, column=2)


# Adding Color Chooser Functions____________________

def Choose_Color():
    Choosed_Color = colorchooser.askcolor()
    Color_RGB = Choosed_Color[0]
    Color_HEX = Choosed_Color[1]
    Color_Chooser_RGBlabel["text"] = "RGB : " + str(Color_RGB)
    Color_Chooser_HEXlabel["text"] = "HEX : " + str(Color_HEX)
    Color_Chooser_RGBlabel["bg"] = str(Color_HEX)
    Color_Chooser_HEXlabel["bg"] = str(Color_HEX)
    Color_Chooser_clrLabelFrame["bg"] = str(Color_HEX)


# Adding Color Chooser Page

Color_Chooser_Frame = tkinter.Frame(window)
Color_Chooser_Label = tkinter.Label(Color_Chooser_Frame, text="Choose A Color !", font=("Roboto", 20))
Color_Chooser_Label.pack(pady=10)
Color_Chooser_Button = tkinter.Button(Color_Chooser_Frame, text="Click Me :)", font=("Roboto", 20), command=Choose_Color)
Color_Chooser_Button.pack(pady=10)
Color_Chooser_clrLabelFrame = tkinter.Frame(Color_Chooser_Frame)
Color_Chooser_clrLabelFrame.pack(pady=30)
Color_Chooser_RGBlabel = tkinter.Label(Color_Chooser_clrLabelFrame, text="RGB : ", font=("Roboto", 20))
Color_Chooser_RGBlabel.pack()
Color_Chooser_HEXlabel = tkinter.Label(Color_Chooser_clrLabelFrame, text="HEX : ", font=("Roboto", 20))
Color_Chooser_HEXlabel.pack()

# Adding Colors___________________

window.config(bg=BG) #Window Background

Title_Labels = [
    Home_First_Label,
    Random_Page_Label,
    Random_Page_FirstEntry_label,
    Random_Page_SecondEntry_label,
    Color_Chooser_Label
]

labels = [
    # To Do
    To_Do_List_Label,

    # Random
    Random_Page_RangeLabel,
    Random_Page_Numberlabel,

    # Color Chooser
    Color_Chooser_RGBlabel,
    Color_Chooser_HEXlabel
]

all_Frames = [
    Text_Editor_Frame,
    Text_Editor_Button_Frame,
    To_Do_List_Frame,
    To_Do_List_Buttons,
    Random_Page_Frame,
    Random_Page_FirstEntry_Frame,
    Random_Page_SecondEntry_Frame,
    Color_Chooser_Frame,
    Home_Frame,
    Main_frame
]

Page_Frames = [
    Text_Editor_Frame,
    To_Do_List_Frame,
    Random_Page_Frame,
    Color_Chooser_Frame,
    Home_Frame
]

for label in Title_Labels:
    label.config(bg=FRAME, fg=ACCENT)

for label in labels:
    label.config(bg=FRAME, fg=TEXT)

for loop in range(len(all_Frames)):
    Changedbg = all_Frames[loop]
    Changedbg["bg"] = FRAME

for frames in Page_Frames:
    frames.config(height=800, width=750)
    frames.pack_propagate(False)

window.mainloop()
