# Importing the modules
import tkinter as tk
import subprocess
from subprocess import PIPE

# Creating the main window
window = tk.Tk()
window.title("C++ to Assembly Converter")

# Creating the input box for the C++ program
input_box = tk.Text(window)
input_box.pack()

# Creating the output box for the assembly output
output_box = tk.Text(window)
output_box.pack()

# Creating the UI configuration option for the optimization level
opt_label = tk.Label(window, text="Optimization level:")
opt_label.pack()
opt_var = tk.StringVar(window)
opt_var.set("-O0")
opt_menu = tk.OptionMenu(window, opt_var, "-O0", "-O1", "-O2", "-O3")
opt_menu.pack()

# Creating the UI configuration option for the compiler
comp_label = tk.Label(window, text="Compiler:")
comp_label.pack()
comp_var = tk.StringVar(window)
comp_var.set("g++")
comp_menu = tk.OptionMenu(window, comp_var, "g++", "clang++")
comp_menu.pack()

# Defining a function to update the assembly output
def update_output(event):
    # Getting the C++ code from the input box
    cpp_code = input_box.get("1.0", "end")

    # Saving the C++ code to a temporary file
    with open("temp.cpp", "w") as f:
        f.write(cpp_code)

    # Getting the optimization level and compiler from the UI options
    opt_level = opt_var.get()
    compiler = comp_var.get()

    # Running the compiler with the -S flag to generate assembly output
    command = [compiler, opt_level, "-S", "temp.cpp"]
    process = subprocess.run(command, capture_output=True)

    # Getting the assembly output from the process stdout
    asm_output = process.stdout.decode()

    # Deleting the temporary file
    subprocess.run(["rm", "temp.cpp"])

    # Clearing and inserting the assembly output to the output box
    output_box.delete("1.0", "end")
    output_box.insert("1.0", asm_output)

# Binding the update function to the input box key release event
input_box.bind("<KeyRelease>", update_output)

# Starting the main loop of the window
window.mainloop()
