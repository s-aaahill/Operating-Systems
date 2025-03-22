class DeadlockToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Prevention and Recovery Toolkit")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12), padding=10)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

        # Main Frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Input fields
        self.processes_label = ttk.Label(self.main_frame, text="Processes (comma-separated):")
        self.processes_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.processes_entry = ttk.Entry(self.main_frame, width=50)
        self.processes_entry.grid(row=0, column=1, pady=5)
        self.resources_label = ttk.Label(self.main_frame, text="Resources (comma-separated):")
        self.resources_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.resources_entry = ttk.Entry(self.main_frame, width=50)
        self.resources_entry.grid(row=1, column=1, pady=5)

        self.available_label = ttk.Label(self.main_frame, text="Available Resources (comma-separated):")
        self.available_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.available_entry = ttk.Entry(self.main_frame, width=50)
        self.available_entry.grid(row=2, column=1, pady=5)
