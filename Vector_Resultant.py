import math
import tkinter as tk

# Function to calculate the resultant value
def calculate_resultant():
    #try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        z = float(entry_z.get())
        resultant_value = math.sqrt(x**2 + y**2 + z**2)
        return resultant_value
    #except ValueError:
        return None

# Function to update the result in the Text widgets
def update_result():
    resultant_value = calculate_resultant()
    result_text.delete('1.0', tk.END)  # Clear the resultant display
    status_text.delete('1.0', tk.END)  # Clear the Pass/Fail display
    
    if resultant_value is not None:
        result_text.insert(tk.END, f"{resultant_value:.5f}")  # Display the resultant value
        
        if 2032 <= round(resultant_value) <= 2064:  # Check if the resultant is in the range
            status_text.insert(tk.END, "Pass")
            status_text.config(bg="green", fg="white")  # Green background, white font for Pass
        else:
            status_text.insert(tk.END, "Fail")
            status_text.config(bg="red", fg="white")  # Red background, white font for Fail
    else:
        result_text.insert(tk.END, "Invalid")
        status_text.insert(tk.END, "Invalid Input")
        status_text.config(bg="orange", fg="white")  # Orange for invalid input

# Create the main window
app = tk.Tk()
app.title("Vector Resultant Calculator")
app.geometry("400x500")

# Labels and Entry Widgets
tk.Label(app, text="Enter the value of x:", font=("Arial", 12)).pack(pady=11)
entry_x = tk.Entry(app, font=("Arial", 12))
entry_x.pack()

tk.Label(app, text="Enter the value of y:", font=("Arial", 12)).pack(pady=11)
entry_y = tk.Entry(app, font=("Arial", 12))
entry_y.pack()

tk.Label(app, text="Enter the value of z:", font=("Arial", 12)).pack(pady=11)
entry_z = tk.Entry(app, font=("Arial", 12))
entry_z.pack()

# Calculate Button
calculate_button = tk.Button(app, text="Calculate", font=("Arial", 12), command=update_result)
calculate_button.pack(pady=20)

# Resultant Value Display
tk.Label(app, text="Resultant Value:", font=("Arial", 12)).pack(pady=11)
result_text = tk.Text(app, font=("Arial", 12), height=1, width=15)
result_text.pack()

# Pass/Fail Status Display
tk.Label(app, text="Pass/Fail Status:", font=("Arial", 12)).pack(pady=11)
status_text = tk.Text(app, font=("Arial", 12), height=1, width=15, bg="white", fg="black")
status_text.pack()

# Run the application
app.mainloop()
