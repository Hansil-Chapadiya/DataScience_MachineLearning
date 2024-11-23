# def pdf():
#     pass
# def chisquare_pdf():
#     row = int(input("Enter number of Row for Matrix : "))
#     column = int(input("Enter number of column for matrix"))


import pandas as pd
import matplotlib.pyplot as plt


def visualize_table(table):
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.axis('off')  # Turn off the axis
    ax.table(cellText=table.values, colLabels=table.columns, rowLabels=table.index, loc='center')
    plt.show()

def final_table(dynamic_table, expected_table):
    # Ensure both tables are DataFrames
    observed_table_df = pd.DataFrame(dynamic_table.iloc[:-1, :-1])  # Exclude totals
    expected_table_df = pd.DataFrame(expected_table)

    # Initialize the final table DataFrame
    cols = ["observed_value", "Expected_value", "(observed - expected)", "(observed - expected)^2", "(observed - expected)^2/E"]
    final_table = pd.DataFrame(columns=cols)

    # Flatten the observed and expected tables for processing
    observed_flat = observed_table_df.values.flatten()
    expected_flat = expected_table_df.values.flatten()

    # Compute the columns
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


    # Return the final DataFrame
    return final_table

def expected_table(dynamic_table):
    # Calculate totals
    row_totals = dynamic_table.iloc[:, :-1].sum(axis=1)  # Sum across rows (excluding "Row Total" column)
    column_totals = dynamic_table.iloc[:-1, :].sum(axis=0)  # Sum across columns (excluding "Column Total" row)
    grand_total = dynamic_table.iloc[:-1, :-1].values.sum()  # Sum of all table values (excluding totals)

    # Initialize an empty DataFrame for the expected table
    rows = dynamic_table.index[:-1]  # Exclude "Column Total" row
    cols = dynamic_table.columns[:-1]  # Exclude "Row Total" column
    expected = pd.DataFrame(index=rows, columns=cols)

    # Compute expected values for each cell
    for row in rows:
        for col in cols:
            expected.loc[row, col] = (row_totals[row] * column_totals[col]) / grand_total

    # Convert all expected values to numeric for compatibility
    expected = expected.apply(pd.to_numeric)
    print(expected)
    return expected

def create_dynamic_table(rows, cols):
    # Initialize an empty DataFrame with dynamic rows and columns
    table = pd.DataFrame(index=rows, columns=cols)

    # Ask the user to input values for each cell
    print("Enter data for the table:")
    for row in rows:
        for col in cols:
            value = input(f"Value for {row} - {col}: ")
            table.loc[row, col] = int(value) if value.isdigit() else 0

    # Add totals for rows and columns
    table["Row Total"] = table.sum(axis=1)
    table.loc["Column Total"] = table.sum(axis=0)

    #creation of Expected table:

    # Display the table
    print("\nGenerated Table:")
    print(table)
    print("\nExpected Table:")
    expected = expected_table(table)
    print("\nfinal Table:")
    print(final_table(table,expected))

    chi_square_value = final_table(table, expected)["(observed - expected)^2/E"].sum()
    print(f"Chi-Square Value: {chi_square_value}")


    return table


# Example: Dynamic Input
rows = ["Male", "Female"]  # Dynamic row names
cols = ["Yes", "No"]  # Dynamic column names
dynamic_table = create_dynamic_table(rows, cols)

# visualize_table(dynamic_table)