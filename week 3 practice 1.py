def represent_student_data_tabular():
    """
    Represents student data (girls and boys) in a tabular format.
    Includes names, ages, heights, and scores for both groups.
    """

    # Data for Girls
    girls_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
    girls_age = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
    girls_height = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
    girls_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

    # Data for Boys
    boys_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
    boys_age = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
    boys_height = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7] # Corrected '61' to '6.1' based on context
    boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

    # Combine data for easier processing
    all_names = girls_names + boys_names
    all_age = girls_age + boys_age
    all_height = girls_height + boys_height
    all_scores = girls_scores + boys_scores

    # Define the header for the table
    header = ["Name", "Age", "Height", "Score"]

    # Determine maximum width for each column to ensure proper alignment
    # Initialize with header lengths
    max_name_len = max(len(name) for name in all_names)
    max_age_len = max(len(str(age)) for age in all_age)
    max_height_len = max(len(str(height)) for height in all_height)
    max_score_len = max(len(str(score)) for score in all_scores)

    # Adjust max lengths to be at least as long as header names
    max_name_len = max(max_name_len, len(header[0]))
    max_age_len = max(max_age_len, len(header[1]))
    max_height_len = max(max_height_len, len(header[2]))
    max_score_len = max(max_score_len, len(header[3]))

    # Print the header row
    print(f"{header[0]:<{max_name_len}} | {header[1]:<{max_age_len}} | {header[2]:<{max_height_len}} | {header[3]:<{max_score_len}}")
    # Print a separator line
    print("-" * (max_name_len + max_age_len + max_height_len + max_score_len + 9)) # 9 for separators and padding

    # Print data for girls
    print("\n--- Girls Data ---")
    for i in range(len(girls_names)):
        print(
            f"{girls_names[i]:<{max_name_len}} | "
            f"{girls_age[i]:<{max_age_len}} | "
            f"{girls_height[i]:<{max_height_len}.1f} | " # Format height to one decimal place
            f"{girls_scores[i]:<{max_score_len}}"
        )

    # Print data for boys
    print("\n--- Boys Data ---")
    for i in range(len(boys_names)):
        print(
            f"{boys_names[i]:<{max_name_len}} | "
            f"{boys_age[i]:<{max_age_len}} | "
            f"{boys_height[i]:<{max_height_len}.1f} | " # Format height to one decimal place
            f"{boys_scores[i]:<{max_score_len}}"
        )

# Execute the function when the script is run
if __name__ == "__main__":
    represent_student_data_tabular()
