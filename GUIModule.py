import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from BankersAlgorithmModule import BankersAlgorithm, detect_deadlock
from GraphVisualizationModule import draw_resource_allocation_graph, export_graph_to_file
from UtilityModule import parse_input, export_results_to_file

class DeadlockToolkitApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        
    def setup_ui(self):
        self.root.title("Deadlock Prevention and Recovery Toolkit")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12), padding=10)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.create_input_fields()
        self.create_action_buttons()

    def create_input_fields(self):
        fields = [
            ("Processes (comma-separated):", "processes_entry"),
            ("Resources (comma-separated):", "resources_entry"),
            ("Available Resources (comma-separated):", "available_entry"),
            ("Max Need (rows for processes, semicolon-separated):", "max_need_entry"),
            ("Allocation (rows for processes, semicolon-separated):", "allocation_entry")
        ]
        
        for i, (label_text, entry_name) in enumerate(fields):
            label = ttk.Label(self.main_frame, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(self.main_frame, width=50)
            entry.grid(row=i, column=1, pady=5)
            setattr(self, entry_name, entry)

    def create_action_buttons(self):
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.grid(row=5, column=0, columnspan=2, pady=20)

        buttons = [
            ("Check Safe State", self.check_safe_state),
            ("Detect Deadlock", self.detect_deadlock),
            ("Draw Graph", self.draw_graph),
            ("Terminate Process", self.terminate_process),
            ("Preempt Resource", self.preempt_resource),
            ("Export Graph", self.export_graph),
            ("Export Results", self.export_results)
        ]

        for i, (text, command) in enumerate(buttons):
            row = i // 3
            col = i % 3
            button = ttk.Button(buttons_frame, text=text, command=command)
            button.grid(row=row, column=col, padx=10, pady=10)

    def check_safe_state(self):
        try:
            processes, resources, available, max_need, allocation = parse_input(
                self.processes_entry.get(),
                self.resources_entry.get(),
                self.available_entry.get(),
                self.max_need_entry.get(),
                self.allocation_entry.get()
            )
            
            banker = BankersAlgorithm(processes, resources, available, max_need, allocation)
            is_safe, safe_sequence = banker.is_safe()
            
            if is_safe:
                messagebox.showinfo("Safe State", f"Safe sequence: {safe_sequence}")
            else:
                messagebox.showwarning("Unsafe State", "System is in an unsafe state.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    def detect_deadlock(self):
        try:
            processes, resources, available, max_need, allocation = parse_input(
                self.processes_entry.get(),
                self.resources_entry.get(),
                self.available_entry.get(),
                self.max_need_entry.get(),
                self.allocation_entry.get()
            )

            need = [
                [max_need[i][j] - allocation[i][j] for j in range(len(resources))]
                for i in range(len(processes))
            ]

            deadlock_detected = detect_deadlock(allocation, need, available)

            if deadlock_detected:
                messagebox.showwarning("Deadlock Detected", "Deadlock has been detected!")
            else:
                messagebox.showinfo("No Deadlock", "No deadlock detected.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    def draw_graph(self):
        try:
            processes, resources, available, max_need, allocation = parse_input(
                self.processes_entry.get(),
                self.resources_entry.get(),
                self.available_entry.get(),
                self.max_need_entry.get(),
                self.allocation_entry.get()
            )

            draw_resource_allocation_graph(processes, resources, allocation, available)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    def terminate_process(self):
        try:
            process_to_terminate = simpledialog.askstring("Terminate Process", "Enter process to terminate:")
            if not process_to_terminate:
                return

            processes, resources, available, max_need, allocation = parse_input(
                self.processes_entry.get(),
                self.resources_entry.get(),
                self.available_entry.get(),
                self.max_need_entry.get(),
                self.allocation_entry.get()
            )

            if process_to_terminate not in processes:
                messagebox.showerror("Error", "Process not found.")
                return

            index = processes.index(process_to_terminate)

            for j in range(len(resources)):
                available[j] += allocation[index][j]
                allocation[index][j] = 0
                max_need[index][j] = 0

            self.available_entry.delete(0, tk.END)
            self.available_entry.insert(0, ','.join(map(str, available)))

            allocation_str = ';'.join([','.join(map(str, row)) for row in allocation])
            self.allocation_entry.delete(0, tk.END)
            self.allocation_entry.insert(0, allocation_str)

            max_need_str = ';'.join([','.join(map(str, row)) for row in max_need])
            self.max_need_entry.delete(0, tk.END)
            self.max_need_entry.insert(0, max_need_str)

            messagebox.showinfo("Success", f"Process {process_to_terminate} terminated successfully.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    def preempt_resource(self):
        try:
            resource_to_preempt = simpledialog.askstring("Preempt Resource", "Enter resource to preempt:")
            if not resource_to_preempt:
                return

            processes, resources, available, max_need, allocation = parse_input(
                self.processes_entry.get(),
                self.resources_entry.get(),
                self.available_entry.get(),
                self.max_need_entry.get(),
                self.allocation_entry.get()
            )

            if resource_to_preempt not in resources:
                messagebox.showerror("Error", "Resource not found.")
                return

            resource_index = resources.index(resource_to_preempt)

            for i in range(len(processes)):
                if allocation[i][resource_index] > 0:
                    allocation[i][resource_index] -= 1
                    available[resource_index] += 1
                    break  # Preempt from first process found

            self.available_entry.delete(0, tk.END)
            self.available_entry.insert(0, ','.join(map(str, available)))

            allocation_str = ';'.join([','.join(map(str, row)) for row in allocation])
            self.allocation_entry.delete(0, tk.END)
            self.allocation_entry.insert(0, allocation_str)

            messagebox.showinfo("Success", f"Resource {resource_to_preempt} preempted successfully.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    def export_graph(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if filename:
                processes, resources, available, max_need, allocation = parse_input(
                    self.processes_entry.get(),
                    self.resources_entry.get(),
                    self.available_entry.get(),
                    self.max_need_entry.get(),
                    self.allocation_entry.get()
                )
                export_graph_to_file(processes, resources, allocation, available, filename)
                messagebox.showinfo("Exported", f"Graph exported to {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", str(e))

    def export_results(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if filename:
                export_results_to_file(
                    self.processes_entry.get(),
                    self.resources_entry.get(),
                    self.available_entry.get(),
                    self.max_need_entry.get(),
                    self.allocation_entry.get(),
                    filename
                )
                messagebox.showinfo("Exported", f"Results exported to {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", str(e))
