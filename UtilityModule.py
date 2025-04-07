def parse_input(process_str, resource_str, available_str, max_need_str, allocation_str):

    try:
        processes = [p.strip() for p in process_str.split(',') if p.strip()]
        resources = [r.strip() for r in resource_str.split(',') if r.strip()]
        available = list(map(int, available_str.strip().split(',')))

        max_need = []
        for row in max_need_str.strip().split(';'):
            if row.strip():
                max_need.append(list(map(int, row.strip().split(','))))

        allocation = []
        for row in allocation_str.strip().split(';'):
            if row.strip():
                allocation.append(list(map(int, row.strip().split(','))))

        # Validate dimensions
        if len(available) != len(resources):
            raise ValueError("Available resources count must match number of resources.")
        if len(max_need) != len(processes) or len(allocation) != len(processes):
            raise ValueError("Each matrix row must correspond to a process.")
        for row in max_need + allocation:
            if len(row) != len(resources):
                raise ValueError("Each matrix row must have the same number of columns as resources.")

        return processes, resources, available, max_need, allocation

    except Exception as e:
        raise ValueError(f"Invalid input format: {str(e)}")


def export_results_to_file(file_path, is_safe, safe_sequence=None, deadlock_detected=None):
    """
    Exports the results (safe state or deadlock info) to a text file.
    """
    try:
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
    except Exception as e:
        raise IOError(f"Failed to export results: {str(e)}")
