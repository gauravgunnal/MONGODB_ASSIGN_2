'''Q1'''
'''I'm sorry, but I can't directly execute code or functions here. However, I can certainly provide you with a list of five common functions from the pandas library in Python along with examples of how you might use them.

1. **`pd.read_csv()`**: Used to read data from a CSV file and create a DataFrame.'''
import pandas as pd
data = pd.read_csv('data.csv')
print(data.head())

#2. **`df.head()`**: Returns the first n rows of a DataFrame (by default, n=5).
import pandas as pd
data = pd.read_csv('data.csv')
print(data.head())

#3. **`df.info()`**: Provides a concise summary of a DataFrame, including data types and non-null values.
import pandas as pd
data = pd.read_csv('data.csv')
print(data.info())

#4. **`df.groupby()`**: Used to group data in a DataFrame based on one or more columns.
import pandas as pd
data = pd.read_csv('data.csv')
grouped_data = data.groupby('category')['value'].sum()
print(grouped_data)

#5. **`df.plot()`**: Creates various types of plots using the data in a DataFrame.
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv')
data.plot(x='date', y='value', kind='line')
plt.show()

#Remember, these examples assume you have a CSV file named "data.csv" with appropriate data.
# Make sure to adapt the code to your specific use case and data structure.'''

'''Q2'''
import pandas as pd

def reindex_with_increment(df):
    new_index = pd.Index(range(1, len(df)*2 + 1, 2))
    new_df = df.copy()
    new_df.index = new_index
    return new_df

# Example usage
data = {
    'A': [10, 20, 30],
    'B': [15, 25, 35],
    'C': [5, 8, 12]
}

df = pd.DataFrame(data)
new_df = reindex_with_increment(df)
print(new_df)

'''Q3'''
import pandas as pd

def calculate_sum_of_first_three(df):
    total = df['Values'].iloc[:3].sum()
    print("Sum of the first three values:", total)

# Example usage
data = {
    'Values': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)
calculate_sum_of_first_three(df)

'''Q4'''
import pandas as pd

def add_word_count_column(df):
    df['Word_Count'] = df['Text'].apply(lambda x: len(str(x).split()))
    return df

# Example usage
data = {
    'Text': [
        "This is a sample sentence.",
        "Another sentence with more words.",
        "Short sentence."
    ]
}

df = pd.DataFrame(data)
df = add_word_count_column(df)
print(df)

'''Q5'''
'''Both `DataFrame.size` and `DataFrame.shape` are attributes of a Pandas DataFrame, but they provide different types of information about the DataFrame.

1. **`DataFrame.size`**:
   - This attribute returns the total number of elements in the DataFrame, which is the product of the number of rows and the number of columns.
   - It gives you the total count of cells in the DataFrame, including both empty cells and cells with actual data.
   - The value returned by `DataFrame.size` is an integer.

Example:
```python
import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

size = df.size
print(size)  # Output: 6 (3 rows * 2 columns = 6 elements)
```

2. **`DataFrame.shape`**:
   - This attribute returns a tuple representing the dimensions of the DataFrame in the form `(number_of_rows, number_of_columns)`.
   - It gives you the actual structure of the DataFrame, specifying the number of rows and columns.
   - The values returned by `DataFrame.shape` are integers.

Example:
```python
import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

shape = df.shape
print(shape)  # Output: (3, 2) (3 rows, 2 columns)
```

In summary, `DataFrame.size` provides the total number of elements (cells) in the DataFrame, while `
DataFrame.shape` provides the dimensions of the DataFrame in terms of rows and columns.'''

'''q6'''
import pandas as pd

# Read an Excel file and create a DataFrame
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# Print the DataFrame
print(df)

'''Q7'''
import pandas as pd

def extract_username(df):
    df['Username'] = df['Email'].apply(lambda email: email.split('@')[0])
    return df

# Example usage
data = {
    'Email': [
        'john.doe@example.com',
        'jane.smith@example.com',
        'bob.johnson@example.com'
    ]
}

df = pd.DataFrame(data)
df = extract_username(df)
print(df)

'''Q8'''
import pandas as pd

def select_rows(df):
    selected_rows = df[(df['A'] > 5) & (df['B'] < 10)]
    return selected_rows

# Sample DataFrame
data = {'A': [3, 8, 6, 2, 9],
        'B': [5, 2, 9, 3, 1],
        'C': [1, 7, 4, 5, 2]}
df = pd.DataFrame(data)

# Select rows based on conditions
selected_df = select_rows(df)
print(selected_df)

'''Q9'''
import pandas as pd


def calculate_stats(df):
    mean_value = df['Values'].mean()
    median_value = df['Values'].median()
    std_deviation = df['Values'].std()

    return mean_value, median_value, std_deviation


# Sample DataFrame
data = {'Values': [3, 8, 6, 2, 9]}
df = pd.DataFrame(data)

# Calculate statistics
mean, median, std = calculate_stats(df)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)

'''Q10'''
import pandas as pd

def add_moving_average(df):
    df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
    return df

# Sample DataFrame
data = {'Date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05', '2023-08-06', '2023-08-07'],
        'Sales': [100, 150, 200, 180, 220, 250, 230]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Add moving average column
df = add_moving_average(df)

print(df)

'''Q11'''
import pandas as pd

def add_weekday_column(df):
    df['Weekday'] = df['Date'].dt.strftime('%A')
    return df

# Sample DataFrame
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Add weekday column
df = add_weekday_column(df)

print(df)

'''Q12'''
import pandas as pd


def select_rows_between_dates(df):
    start_date = '2023-01-01'
    end_date = '2023-01-31'

    selected_rows = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    return selected_rows


# Sample DataFrame
data = {'Date': ['2023-01-01', '2023-01-15', '2023-01-20', '2023-02-05']}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Select rows between dates
selected_df = select_rows_between_dates(df)

print(selected_df)

'''Q13'''
'''The first and foremost library that needs to be imported to use the basic functions of pandas is, of course, the Pandas library itself. You can import it using the following line of code:

```python
import pandas as pd
```

By convention, most people alias `pandas` as `pd` for brevity. This allows you to use the Pandas functions and classes using the `pd` prefix, making your code shorter and more readable.'''