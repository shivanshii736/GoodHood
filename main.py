import tkinter as tk
from tkinter import messagebox
import db

root = tk.Tk()
root.title("Community Connect")
root.geometry("500x400")

# ---- MAIN SCREEN ----

def open_create_event():
    create_window = tk.Toplevel(root)
    create_window.title("Create Event")
    create_window.geometry("400x300")

    tk.Label(create_window, text="Event Name:").pack()
    name_entry = tk.Entry(create_window)
    name_entry.pack()

    tk.Label(create_window, text="Location:").pack()
    location_entry = tk.Entry(create_window)
    location_entry.pack()

    tk.Label(create_window, text="Description:").pack()
    desc_entry = tk.Entry(create_window)
    desc_entry.pack()

    def save_event():
        name = name_entry.get()
        loc = location_entry.get()
        desc = desc_entry.get()

        if name.strip() == "":
            messagebox.showerror("Error", "Event name is required!")
            return

        db.add_event(name, loc, desc)
        messagebox.showinfo("Success", "Event created successfully!")
        create_window.destroy()

    tk.Button(create_window, text="Save Event", command=save_event).pack(pady=10)


def open_view_events():
    events_window = tk.Toplevel(root)
    events_window.title("View Events")
    events_window.geometry("400x300")

    events = db.get_events()

    if not events:
        tk.Label(events_window, text="No events available").pack()
        return

    for ev in events:
        text = f"{ev[1]} - {ev[2]}"
        tk.Label(events_window, text=text).pack(anchor="w", padx=10)


# ---- MAIN BUTTONS ----
tk.Label(root, text="Welcome to Community Connect!", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Create Event", width=20, command=open_create_event).pack(pady=10)
tk.Button(root, text="View Events", width=20, command=open_view_events).pack(pady=10)

root.mainloop()
