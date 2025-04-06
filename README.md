Deadlock Prevention and Recovery Toolkit
📚 About the Project
This project is built to simulate and handle deadlocks in operating systems. Deadlocks can freeze a system when processes compete for resources — and this toolkit shows how to prevent them before they happen and recover gracefully if they do.

It’s a practical, hands-on way to understand how deadlocks work, how dangerous they can be, and how operating systems tackle them smartly.

🖥️ Topics We Covered
1.Deadlock Detection
2.Deadlock Prevention
3.Deadlock Avoidance (Banker’s Algorithm)
4.Deadlock Recovery

Each strategy is demonstrated with real examples and user inputs to show exactly how systems behave under different conditions.

🛠️ Tools and Tech Stack
Programming Language: Python

Compiler: GCC

Operating System: Windows

✨ Key Features
->Detects deadlocks in a multi-process system
->Prevents deadlocks by smart resource allocation
->Avoids deadlocks using the Banker's Algorithm
->Recovers from deadlocks if they occur
->User-friendly interface to input process and resource data
->Clear outputs showing system state and decision-making steps

🧠 How the Toolkit Works
Input Phase:
Enter number of processes and resource types.
Provide details like allocation matrix, maximum demand, and available resources.

Processing Phase:
Select what you want: detection, prevention, avoidance, or recovery.
The toolkit simulates the selected strategy and analyzes the system state.

Output Phase:
Displays results clearly — safe sequences, detection results, or recovery actions.
Shows whether the system is in a safe or unsafe state.

📊 What We Learned
After testing different cases:
Deadlock Prevention can be expensive but saves the system early.
Deadlock Avoidance (especially Banker’s Algorithm) works efficiently if we predict maximum needs properly.
Detection and Recovery allow flexibility but can risk system performance if deadlocks occur frequently.
Every method has trade-offs — it's all about balancing safety and performance.

🔥 Future Improvements
Adding a graphical dashboard to visualize safe and unsafe states
Simulating real-time processes with dynamic resource requests
Integrating multi-threaded resource allocation simulation

👩‍💻 Team Members
Kangan Sharma
Janvee
Sahil Shaikh
