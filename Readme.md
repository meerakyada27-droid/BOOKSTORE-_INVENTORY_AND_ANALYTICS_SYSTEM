# 📚 BOOKSTORE INVENTORY AND ANALYTICS SYSTEM

**Author:** Meera Kyada

## 📌 Project Description

Bookstore Inventory and Analytics System is a Python-based project developed to manage bookstore inventory and analyze sales data. It allows users to add, remove, and update book records, maintain stock, record sales, and generate detailed reports.

This project uses NumPy, Pandas, Matplotlib, and Seaborn to perform data analysis and create meaningful visualizations. Inventory and sales information are stored in CSV files.

## 🎯 Project Objectives

- To manage bookstore inventory efficiently.
- To maintain book details and stock quantities.
- To add, remove, and update book records.
- To record sales and calculate total revenue.
- To generate reports using sales data.
- To analyze book, author, and genre-wise sales.
- To understand monthly sales performance.
- To represent data through different charts.

## ✨ Project Features

- **Display Inventory:** View available books with their title, author, price, quantity, and genre.
- **Add New Book:** Add new book records to the inventory.
- **Remove Book:** Remove an existing book from the inventory.
- **Update Inventory:** Modify the available quantity of books.
- **Record Sale:** Record book sales and automatically update stock.
- **Generate Report:** Calculate total inventory, books sold, revenue, and average book price.
- **Sales Analysis:** Display sales by book, best-selling book, revenue by genre, and sales by author.
- **Monthly Analysis:** Analyze sales according to months.
- **Data Visualization:** Generate different charts for better understanding of data.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main Programming Language |
| NumPy | Array Operations |
| Pandas | Data Analysis and Manipulation |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| CSV | Data Storage |
| VS Code | Code Editor |

## 📂 Dataset Information

This project uses two CSV files to store and manage bookstore information.

**1. inventory.csv**

Contains book inventory details:
- Title
- Author
- Price
- Quantity
- Genre

**2. sales.csv**

Contains book sales information:
- Title
- Quantity Sold
- Total Revenue
- Date

These datasets are used for inventory management, sales tracking, and data analysis.

## 🔍 Project Modules

### 1. Data Loading and Exploration
- Import required Python libraries.
- Load inventory and sales CSV files using Pandas.
- Display book records.
- Create a NumPy array of book titles.

### 2. Data Cleaning and Preprocessing
- Convert columns into appropriate data types.
- Handle missing and invalid values using `dropna()`.
- Remove invalid price and quantity records.
- Convert sales dates into datetime format.
- Save cleaned data into CSV files.

### 3. Inventory Management
- Display all available books.
- Add new books with complete details.
- Remove existing books.
- Update book quantities.
- Save inventory changes.

### 4. Sales Management
- Record book sales.
- Check book availability.
- Calculate total revenue.
- Automatically update stock after sales.
- Store sales details with the current date.

### 5. Statistical Analysis and Reporting
- Calculate total books in inventory.
- Calculate total books sold.
- Calculate total revenue.
- Find average book price.
- Display best-selling book.
- Analyze genre-wise, author-wise, and monthly sales.

### 6. Data Visualization
- Create Bar Chart for sales by genre.
- Create Line Chart for monthly sales.
- Create Pie Chart for revenue by genre.
- Create Heatmap for price and sales correlation.

## 🔢 NumPy Operations

NumPy is used to perform array-related operations.

- Creating NumPy arrays.
- Storing book titles in arrays.
- Displaying array elements.
- Working with numerical data.

## 🐼 Pandas Operations

Pandas is used to manage, clean, and analyze bookstore datasets.

- `pd.read_csv()` – Read CSV files.
- `pd.DataFrame()` – Create DataFrames.
- `head()` – Display the first five records.
- `dropna()` – Remove missing values.
- `to_numeric()` – Convert values into numeric format.
- `to_datetime()` – Convert dates into datetime format.
- `groupby()` – Group records for analysis.
- `sum()` – Calculate total values.
- `mean()` – Calculate average values.
- `merge()` – Combine inventory and sales data.
- `reset_index()` – Reset DataFrame indexes.
- `to_csv()` – Save data into CSV files.

## 📊 Data Visualization

Matplotlib and Seaborn are used to represent bookstore data graphically.

- **Bar Chart:** Shows the number of books sold in different genres.
- **Line Chart:** Displays monthly sales trends.
- **Pie Chart:** Represents revenue distribution across genres.
- **Heatmap:** Shows the correlation between price and sales-related numerical data.

Generated chart files:
- `output.png`
- `pie_chat.png`

## 🧠 Concepts Covered

### Python Fundamentals
- Variables and Data Types
- Operators
- Conditional Statements
- Loops
- Input and Output

### Strings and Collections
- String Operations
- Lists
- Dictionaries
- Arrays

### Functions
- User Defined Functions
- Function Arguments
- Return Statements

### Object-Oriented Programming
- Classes and Objects
- Constructor
- Methods
- Encapsulation

### Exception and File Handling
- Try and Except
- CSV File Handling
- Data Validation

### Modules and Packages
- Importing Modules
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Datetime

## 📁 Project Structure

    Practical Exam/
    │
    ├── bookstore_system.py
    ├── inventory.csv
    ├── output.png
    ├── pie_chat.png
    ├── readme.md
    └── sales.csv

## ⚙️ Installation and Setup

**Step 1: Install Python**

Install Python on your computer.

**Step 2: Install Required Libraries**

    pip install numpy pandas matplotlib seaborn

**Step 3: Open Project Folder**

Open the Practical Exam folder in Visual Studio Code.

**Step 4: Run Python File**

    python bookstore_system.py

**Step 5: Execute the Program**

Select the required option from the main menu to manage inventory, record sales, generate reports, and visualize data.

## 📤 Project Deliverables

- `bookstore_system.py` – Main Python application.
- `inventory.csv` – Stores book inventory details.
- `sales.csv` – Stores book sales records.
- `output.png` – Saved chart output.
- `pie_chat.png` – Saved pie chart output.
- `readme.md` – Project documentation.

## 📷 Sample Output

The project provides different outputs for bookstore management and analysis.

- Displaying complete book inventory.
- Adding a new book to the inventory.
- Removing an existing book.
- Updating book quantities.
- Recording book sales.
- Generating bookstore reports.
- Displaying sales analysis.
- Creating graphical visualizations.

## 📌 Key Findings

- The system makes bookstore inventory management easier.
- Stock quantities are updated after recording sales.
- Sales reports provide information about book performance.
- Genre-wise and author-wise analysis helps understand sales distribution.
- Monthly sales analysis helps identify sales trends.
- Charts make the results easier to understand.

## 🌎 Real-World Applications

- Small and medium-sized bookstores.
- Book inventory management systems.
- Sales tracking applications.
- Stock management systems.
- Business data analysis and reporting.

## 🚀 Future Improvements

- Add a graphical user interface (GUI).
- Connect the project with a MySQL database.
- Add a book search feature.
- Generate PDF sales reports.
- Add customer management functionality.
- Improve reporting and visualization features.

## 🎓 Learning Outcomes

Through this project, I learned how to develop a practical Python application, manage CSV files, perform data cleaning, work with NumPy arrays, analyze datasets using Pandas, apply OOP concepts, and create visualizations using Matplotlib and Seaborn.

## 📌 Project Status

**Status:** Completed

This project demonstrates the practical implementation of Python programming, inventory management, data analysis, and visualization concepts.

## 🙏 Thank You

Thank you for visiting my Bookstore Inventory and Analytics System project!
```