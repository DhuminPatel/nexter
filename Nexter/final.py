import tkinter as tk
from tkinter import Toplevel, LabelFrame
import tkintermapview

def show_map():
    # Create a new window for the map
    map_window = Toplevel(root)
    map_window.title("Map of Mississauga")
    map_window.geometry("800x600")

    # Create a frame for the map widget
    map_frame = LabelFrame(map_window)
    map_frame.pack(fill="both", expand=True)

    # Create the map widget
    map_widget = tkintermapview.TkinterMapView(map_frame, width=800, height=600)
    map_widget.pack(fill="both", expand=True)

    # Set the location to Mississauga
    map_widget.set_position(43.589, -79.644)
    map_widget.set_zoom(10)

def main():
    global root
    # Create the main window
    root = tk.Tk()
    root.title("Smart City Project")

    # Set the size of the window
    root.geometry("400x600")

    # Create a label with the welcome message
    welcome_label = tk.Label(root, text="Welcome to the City of Mississauga", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    # Create a frame for the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    # Create buttons for each module
    button_width = 40
    button_height = 3

    admin_button = tk.Button(button_frame, text="Administration Module", width=button_width, height=button_height)
    admin_button.grid(row=0, column=0, pady=10)

    tourism_button = tk.Button(button_frame, text="Tourism Module", width=button_width, height=button_height)
    tourism_button.grid(row=1, column=0, pady=10)

    student_button = tk.Button(button_frame, text="Student Module", width=button_width, height=button_height)
    student_button.grid(row=2, column=0, pady=10)

    jobseekers_button = tk.Button(button_frame, text="Jobseekers Module", width=button_width, height=button_height)
    jobseekers_button.grid(row=3, column=0, pady=10)

    business_button = tk.Button(button_frame, text="Business Module", width=button_width, height=button_height)
    business_button.grid(row=4, column=0, pady=10)

    map_button = tk.Button(button_frame, text="Map", width=button_width, height=button_height, command=show_map)
    map_button.grid(row=5, column=0, pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
