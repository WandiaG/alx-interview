from collections import Counter

def parse_line(line):
    """Parses a line from stdin and returns a dictionary with extracted data.

    Args:
        line (str): The line to parse.

    Returns:
        dict: A dictionary containing extracted data or None if the format is invalid.
    """
    try:
        # Split the line based on spaces and quotes
        parts = line.strip().split('"')
        ip, date_time, request, status_code, file_size = parts[0].split(), parts[1].split()[1], parts[2].split()

        # Convert status code and file size to integers
        status_code, file_size = int(status_code[0]), int(file_size[-1])

        return {
            'ip': ip[0],
            'date': date_time[0],
            'path': request,
            'status_code': status_code,
            'file_size': file_size,
        }
    except (IndexError, ValueError):
        return None

def main():
    total_size = 0
    status_code_counts = Counter()
    line_count = 0

    try:
        while True:
            line = input()
            parsed_data = parse_line(line)

            if parsed_data:
                total_size += parsed_data['file_size']
                status_code_counts[parsed_data['status_code']] += 1
                line_count += 1

            if line_count % 10 == 0 or line_count == 1:
                # Print statistics
                print(f"Total file size: {total_size}")

                # Sort status code counts and print them in ascending order
                for code, count in sorted(status_code_counts.items()):
                    print(f"{code}: {count}")

                # Reset counters for next iteration
                status_code_counts = Counter()

    except KeyboardInterrupt:
        # Print statistics on keyboard interrupt
        print(f"Total file size: {total_size}")

        # Sort status code counts and print them in ascending order
        for code, count in sorted(status_code_counts.items()):
            print(f"{code}: {count}")

if __name__ == "__main__":
    main()

