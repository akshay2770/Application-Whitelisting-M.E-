import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
from tkinter import ttk
# Start
def add_to_whitelist():
    name = entry_name.get()
    path = entry_path.get()
    app_name = os.path.basename(path)

    blacklist_file = "blacklist.txt"
    whitelist_file = "whitelist.txt"

    try:
        # Add the app_name to the whitelist
        with open(whitelist_file, "a") as white_file:
            white_file.write(app_name + "\n")
        print(f"Added digital signature data of {name} to the whitelist")
    except IOError as e:
        print(f"Error whitelisting {name}: {str(e)}")

        
    filename = os.path.basename(path)
    message = "Saved digital signature info of {} into whitelist".format(name)
    messagebox.showinfo("Success!",message)
    print("Adding to Whitelist:",app_name)
    print("Path:", path)

def remove_from_whitelist():
    name = entry_name.get()
    path = entry_path.get()
    app_name = os.path.basename(path)
    blacklist_file = "blacklist.txt"
    whitelist_file = "whitelist.txt"

    try:
        # Check if the app_name is in the whitelist
        with open(whitelist_file, "r") as white_file:
            lines = white_file.readlines()
        if app_name in [line.strip() for line in lines]:
            # Remove the app_name from the whitelist
            lines.remove(app_name + "\n")
            with open(whitelist_file, "w") as white_file:
                white_file.writelines(lines)
                
            print("Removing from Whitelist:")
            print("Path:", app_name)
            message = "Removed digital signature info of {} from whitelist".format(app_name)
            messagebox.showinfo("Success!",message)
        else:
            message = "Error removing {}".format(name)
            messagebox.showinfo("Alert!",message)  
    except IOError as e:
        print(f"Error removing {app_name}: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Whitelist Manager")
root.geometry("400x200")  # Set the initial size of the window

# Style
style = ttk.Style()
style.configure("TButton", padding=(10, 5, 10, 5), font='Helvetica 10')

# Name entry
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Path entry and browse button
label_path = tk.Label(root, text="Path:")
label_path.grid(row=1, column=0, padx=10, pady=10)
entry_path = tk.Entry(root)
entry_path.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=lambda: entry_path.insert(tk.END, filedialog.askopenfilename()))
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Add to Whitelist button (using ttk.Button for styling)
add_button = ttk.Button(root, text="Add to Whitelist", command=add_to_whitelist, style="TButton")
add_button.grid(row=2, column=0, padx=10, pady=10)

# Remove from Whitelist button (using ttk.Button for styling)
remove_button = ttk.Button(root, text="Remove from Whitelist", command=remove_from_whitelist, style="TButton")
remove_button.grid(row=2, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
