# Cindy Hernandez
# 12/15/24
# Mod 10.2

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Canvas and frame setup
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Window properties
        self.title("Hernandez-ToDo")  # Change the title to "Hernandez-ToDo"
        self.geometry("300x400")

        # Text widget for creating tasks
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        # Scrollable canvas setup
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        # Task input and button to add tasks
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Instruction Label for deleting tasks
        self.instruction_label = tk.Label(self, text="Right-click on a task to delete it.", bg="blue", fg="white", pady=10)
        self.instruction_label.pack(fill=tk.X)

        # Initial task (to prevent an empty list when first starting)
        todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here ---", bg="red", fg="black", pady=10)
        todo1.bind("<Button-3>", self.remove_task)  # Use right-click to remove task

        self.tasks.append(todo1)

        # Pack existing tasks
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # Bind the Enter key to add a task
        self.bind("<Return>", self.add_task)

        # Bind window resizing and scrolling actions
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Color schemes for alternating task colors
        self.colour_schemes = [{"bg": "purple", "fg": "black"}, {"bg": "black", "fg": "white"}]

        # Menu setup
        self.create_menu()

    def create_menu(self):
        # Create a menu bar
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Create File menu with an Exit option
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        # Set background and text color for the "Exit" menu item
        self.file_menu.add_command(
            label="Exit", 
            command=self.exit_app, 
            activebackground="blue",  # Blue when hovered
            activeforeground="white",  # Text color when hovered
            background="red",  # Red background color of the menu item
            foreground="white"  # Text color of the menu item
        )

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:  # Only add the task if the text is not empty
            # Create a new task label with the entered text
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            # Set the color of the new task
            self.set_task_colour(len(self.tasks), new_task)

            # Bind right-click to delete the task
            new_task.bind("<Button-3>", self.remove_task)

            # Add the new task to the task list
            new_task.pack(side=tk.TOP, fill=tk.X)

            # Append the task to the tasks list
            self.tasks.append(new_task)

            # Clear the text field for the next task
            self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

    def exit_app(self):
        self.quit()

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
