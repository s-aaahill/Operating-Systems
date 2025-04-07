def parse_input(process_str, resource_str, available_str, max_need_str, allocation_str):
    try:
        processes = [p.strip() for p in process_str.split(',')]
        resources = [r.strip() for r in resource_str.split(',')]
        available = list(map(int, available_str.split(',')))

        max_need = []
        for row in max_need_str.split(';'):
            max_need.append(list(map(int, row.split(','))))

        allocation = []
        for row in allocation_str.split(';'):
            allocation.append(list(map(int, row.split(','))))

        return processes, resources, available, max_need, allocation
    except Exception as e:
        raise ValueError(f"Invalid input format: {str(e)}")

def export_results_to_file(file_path, is_safe, safe_sequence=None, deadlock_detected=None):
    with open(file_path, 'w') as file:
        if is_safe is not None:
            if is_safe:
                file.write(f"Safe State. Safe sequence: {safe_sequence}\n")
            else:
                file.write("Unsafe State. Deadlock may occur.\n")
        if deadlock_detected is not None:
            if deadlock_detected:
                file.write("Deadlock Detected\n")
            else:
                file.write("No Deadlock Detected\n")
