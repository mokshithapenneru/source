import tkinter as tk
from time import strftime

# Function to update the time on the clock
def time():
    string = strftime('%H:%M:%S %p')  # Format for hours:minutes:seconds AM/PM
    label.config(text=string)
    label.after(1000, time)  # Call this function again after 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Clock")

# Set the background color
root.configure(bg="black")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the time function to update the clock
time()

# Run the Tkinter event loop
root.mainloop()
