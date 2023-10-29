import tkinter as tk
from tkinter import simpledialog

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder App")

        self.reminders = []

        self.reminder_listbox = tk.Listbox(root)
        self.reminder_listbox.pack(pady=10)

        add_button = tk.Button(root, text="Add Reminder", command=self.add_reminder)
        add_button.pack()

        remove_button = tk.Button(root, text="Remove Selected", command=self.remove_reminder)
        remove_button.pack()

    def add_reminder(self):
        reminder_text = simpledialog.askstring("Add Reminder", "Enter a reminder:")
        if reminder_text:
            self.reminders.append(reminder_text)
            self.update_reminder_listbox()

    def remove_reminder(self):
        selected_index = self.reminder_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            del self.reminders[index]
            self.update_reminder_listbox()

    def update_reminder_listbox(self):
        self.reminder_listbox.delete(0, tk.END)
        for reminder in self.reminders:
            self.reminder_listbox.insert(tk.END, reminder)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()

