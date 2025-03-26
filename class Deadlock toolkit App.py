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
        self.resources_label = ttk.Label(self.main_frame, text="Resources (comma-separated):")
        self.resources_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.resources_entry = ttk.Entry(self.main_frame, width=50)
        self.resources_entry.grid(row=1, column=1, pady=5)

        self.available_label = ttk.Label(self.main_frame, text="Available Resources (comma-separated):")
        self.available_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.available_entry = ttk.Entry(self.main_frame, width=50)
        self.available_entry.grid(row=2, column=1, pady=5)

        self.max_need_label = ttk.Label(self.main_frame, text="Max Need (rows for processes, comma-separated):")
        self.max_need_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.max_need_entry = ttk.Entry(self.main_frame, width=50)
        self.max_need_entry.grid(row=3, column=1, pady=5)

        self.allocation_label = ttk.Label(self.main_frame, text="Allocation (rows for processes, comma-separated):")
        self.allocation_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.allocation_entry = ttk.Entry(self.main_frame, width=50)
        self.allocation_entry.grid(row=4, column=1, pady=5)
        # Buttons Frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.grid(row=5, column=0, columnspan=2, pady=20)

        self.check_safe_button = ttk.Button(self.buttons_frame, text="Check Safe State", command=self.check_safe_state)
        self.check_safe_button.grid(row=0, column=0, padx=10)

        self.detect_deadlock_button = ttk.Button(self.buttons_frame, text="Detect Deadlock", command=self.detect_deadlock)
        self.detect_deadlock_button.grid(row=0, column=1, padx=10)

        self.draw_graph_button = ttk.Button(self.buttons_frame, text="Draw Resource Allocation Graph", command=self.draw_graph)
        self.draw_graph_button.grid(row=0, column=2, padx=10)

        self.terminate_process_button = ttk.Button(self.buttons_frame, text="Terminate Process", command=self.terminate_process)
        self.terminate_process_button.grid(row=1, column=0, padx=10, pady=10)

        self.preempt_resource_button = ttk.Button(self.buttons_frame, text="Preempt Resource", command=self.preempt_resource)
        self.preempt_resource_button.grid(row=1, column=1, padx=10, pady=10)

        self.export_graph_button = ttk.Button(self.buttons_frame, text="Export Graph", command=self.export_graph)
        self.export_graph_button.grid(row=1, column=2, padx=10, pady=10)

        self.export_results_button = ttk.Button(self.buttons_frame, text="Export Results", command=self.export_results)
        self.export_results_button.grid(row=1, column=3, padx=10, pady=10)

    def check_safe_state(self):
        try:
            processes = self.processes_entry.get().split(',')
            resources = self.resources_entry.get().split(',')
            available = list(map(int, self.available_entry.get().split(',')))
            max_need = [list(map(int, row.split(','))) for row in self.max_need_entry.get().split(';')]
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split(';')]

            banker = BankersAlgorithm(processes, resources, available, max_need, allocation)
            is_safe, safe_sequence = banker.is_safe()

            if is_safe:
                messagebox.showinfo("Safe State", f"The system is in a safe state. Safe sequence: {safe_sequence}")
            else:
                messagebox.showwarning("Unsafe State", "The system is in an unsafe state. Deadlock may occur.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
