import pandas as pd
import matplotlib.pyplot as plt


def visualize_table(table):
    """
    Visualize a pandas DataFrame as a table using matplotlib.

    Args:
        table (pd.DataFrame): The table to visualize.
    """
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.axis('off')  # Turn off the axis
    ax.table(cellText=table.values, colLabels=table.columns, rowLabels=table.index, loc='center')
    plt.show()


def final_table(dynamic_table, expected_table):
    """
    Generate the final Chi-Square analysis table containing observed values, expected values, and intermediate calculations.

    Args:
        dynamic_table (pd.DataFrame): The observed values table (including totals).
        expected_table (pd.DataFrame): The expected values table.

    Returns:
        pd.DataFrame: A table with observed values, expected values, and Chi-Square contributions.
    """
    # Extract the observed table without totals
    observed_table_df = pd.DataFrame(dynamic_table.iloc[:-1, :-1])  # Exclude totals
    expected_table_df = pd.DataFrame(expected_table)

    # Define columns for the final table
    cols = ["observed_value", "Expected_value", "(observed - expected)", "(observed - expected)^2", "(observed - expected)^2/E"]
    final_table = pd.DataFrame(columns=cols)

    # Flatten the observed and expected tables for element-wise operations
    observed_flat = observed_table_df.values.flatten()
    expected_flat = expected_table_df.values.flatten()

    # Compute each column for the final table
    for obs, exp in zip(observed_flat, expected_flat):
        diff = obs - exp  # observed - expected
        diff_squared = diff ** 2  # (observed - expected)^2
        chi_square_contribution = diff_squared / exp if exp != 0 else 0  # Avoid division by zero
        final_table = pd.concat([final_table, pd.DataFrame({
            "observed_value": [obs],
            "Expected_value": [exp],
            "(observed - expected)": [diff],
            "(observed - expected)^2": [diff_squared],
            "(observed - expected)^2/E": [chi_square_contribution]
        })], ignore_index=True)

    return final_table


def expected_table(dynamic_table):
    """
    Calculate the expected values for a contingency table.

    Args:
        dynamic_table (pd.DataFrame): The observed values table with totals.

    Returns:
        pd.DataFrame: A table of expected values.
    """
    # Calculate totals
    row_totals = dynamic_table.iloc[:, :-1].sum(axis=1)  # Sum across rows (excluding "Row Total" column)
    column_totals = dynamic_table.iloc[:-1, :].sum(axis=0)  # Sum across columns (excluding "Column Total" row)
    grand_total = dynamic_table.iloc[:-1, :-1].values.sum()  # Total of all table values (excluding totals)

    # Initialize an empty DataFrame for expected values
    rows = dynamic_table.index[:-1]  # Exclude "Column Total" row
    cols = dynamic_table.columns[:-1]  # Exclude "Row Total" column
    expected = pd.DataFrame(index=rows, columns=cols)

    # Compute expected values for each cell
    for row in rows:
        for col in cols:
            expected.loc[row, col] = (row_totals[row] * column_totals[col]) / grand_total

    # Convert to numeric for compatibility
    expected = expected.apply(pd.to_numeric)
    print(expected)  # Optional: Show the expected table for verification
    return expected


def create_dynamic_table(rows, cols):
    """
    Create a dynamic contingency table with user inputs for observed values.

    Args:
        rows (list): List of row labels.
        cols (list): List of column labels.

    Returns:
        pd.DataFrame: A dynamically generated table with observed values and totals.
    """
    # Initialize an empty DataFrame with the given rows and columns
    table = pd.DataFrame(index=rows, columns=cols)

    # Ask the user to input values for each cell
    print("Enter data for the table:")
    for row in rows:
        for col in cols:
            while True:  # Loop to ensure valid numeric input
                value = input(f"Value for {row} - {col}: ")
                if value.isdigit():  # Accept only positive integers
                    table.loc[row, col] = int(value)
                    break
                else:
                    print("Invalid input! Please enter a valid integer.")

    # Add totals for rows and columns
    table["Row Total"] = table.sum(axis=1)
    table.loc["Column Total"] = table.sum(axis=0)

    # Display the generated table
    print("\nGenerated Table:")
    print(table)

    # Create and display the expected table
    print("\nExpected Table:")
    expected = expected_table(table)

    # Create and display the final Chi-Square analysis table
    print("\nFinal Table:")
    final = final_table(table, expected)
    print(final)

    return table


# Example usage: Define rows and columns
rows = ["Male", "Female"]  # Example row names
cols = ["Yes", "No"]  # Example column names

# Generate the dynamic table with user inputs
dynamic_table = create_dynamic_table(rows, cols)

# Optional: Visualize the generated table
# visualize_table(dynamic_table)
