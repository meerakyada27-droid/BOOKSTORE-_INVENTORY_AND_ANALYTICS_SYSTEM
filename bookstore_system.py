
# ==============================================
# BOOKSTORE INVENTORY AND ANALYTICS SYSTEM
# ==============================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime


# ==============================================
# 1. BOOKSTORE CLASS (OOP)
# ==============================================

class Bookstore:

    def __init__(self):

        self.inventory = pd.read_csv("inventory.csv")
        self.sales = pd.read_csv("sales.csv")

        self.clean_data()
        self.update_book_array()

    # ------------------------------------------
    # DATA CLEANING
    # ------------------------------------------

    def clean_data(self):

        self.inventory["Price"] = pd.to_numeric(
            self.inventory["Price"], errors="coerce"
        )

        self.inventory["Quantity"] = pd.to_numeric(
            self.inventory["Quantity"], errors="coerce"
        )

        self.sales["Quantity Sold"] = pd.to_numeric(
            self.sales["Quantity Sold"], errors="coerce"
        )

        self.sales["Total Revenue"] = pd.to_numeric(
            self.sales["Total Revenue"], errors="coerce"
        )

        self.inventory.dropna(inplace=True)
        self.sales.dropna(inplace=True)

        self.inventory = self.inventory[
            (self.inventory["Price"] > 0) &
            (self.inventory["Quantity"] >= 0)
        ]

        self.sales = self.sales[
            (self.sales["Quantity Sold"] > 0) &
            (self.sales["Total Revenue"] >= 0)
        ]

        self.sales["Date"] = pd.to_datetime(
            self.sales["Date"], errors="coerce"
        )

        self.sales.dropna(subset=["Date"], inplace=True)

        self.inventory.reset_index(drop=True, inplace=True)
        self.sales.reset_index(drop=True, inplace=True)

        self.save_data()

    # ------------------------------------------
    # SAVE DATA
    # ------------------------------------------

    def save_data(self):

        self.inventory.to_csv("inventory.csv", index=False)
        self.sales.to_csv("sales.csv", index=False)

    # ------------------------------------------
    # NUMPY ARRAY
    # ------------------------------------------

    def update_book_array(self):

        self.book_titles = np.array(
            self.inventory["Title"]
        )

    # ------------------------------------------
    # DISPLAY INVENTORY
    # ------------------------------------------

    def display_inventory(self):

        print("\n========== BOOK INVENTORY ==========\n")

        if self.inventory.empty:
            print("No books available.")
        else:
            print(self.inventory.to_string(index=False))

        self.update_book_array()

        print("\nBook Titles Array:")
        print(self.book_titles)

    # ------------------------------------------
    # ADD BOOK
    # ------------------------------------------

    def add_book(self, title, author, price, quantity, genre):

        if title.strip() == "" or author.strip() == "":
            print("Title and author cannot be empty.")
            return

        if price <= 0 or quantity < 0:
            print("Invalid price or quantity.")
            return

        if title in self.inventory["Title"].values:
            print("Book already exists!")
            return

        new_book = {
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Price": price,
            "Quantity": quantity
        }

        self.inventory.loc[len(self.inventory)] = new_book

        self.update_book_array()
        self.save_data()

        print("Book added successfully!")

    # ------------------------------------------
    # REMOVE BOOK
    # ------------------------------------------

    def remove_book(self, title):

        if title not in self.inventory["Title"].values:
            print("Book not found!")
            return

        self.inventory = self.inventory[
            self.inventory["Title"] != title
        ]

        self.update_book_array()
        self.save_data()

        print("Book removed successfully!")

    # ------------------------------------------
    # UPDATE INVENTORY
    # ------------------------------------------

    def update_inventory(self, title, quantity):

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        if title not in self.inventory["Title"].values:
            print("Book not found!")
            return

        self.inventory.loc[
            self.inventory["Title"] == title, "Quantity"
        ] = quantity

        self.save_data()

        print("Inventory updated successfully!")

    # ------------------------------------------
    # RECORD SALE
    # ------------------------------------------

    def record_sale(self, title, quantity):

        if quantity <= 0:
            print("Sale quantity must be positive.")
            return

        if title not in self.inventory["Title"].values:
            print("Book not found!")
            return

        book = self.inventory[
            self.inventory["Title"] == title
        ]

        available_quantity = int(book.iloc[0]["Quantity"])
        price = float(book.iloc[0]["Price"])

        if quantity > available_quantity:
            print("Insufficient stock!")
            print("Available stock:", available_quantity)
            return

        total_revenue = price * quantity

        self.inventory.loc[
            self.inventory["Title"] == title, "Quantity"
        ] -= quantity

        new_sale = {
            "Date": datetime.today().strftime("%Y-%m-%d"),
            "Title": title,
            "Quantity Sold": quantity,
            "Total Revenue": total_revenue
        }

        self.sales.loc[len(self.sales)] = new_sale

        self.save_data()

        print("\nSale recorded successfully!")
        print("Book:", title)
        print("Quantity Sold:", quantity)
        print("Total Revenue: Rs.", total_revenue)

    # ------------------------------------------
    # GENERATE REPORT
    # ------------------------------------------

    def generate_report(self):

        print("\n========== BOOKSTORE REPORT ==========\n")

        if self.sales.empty:
            print("No sales data available.")
            return

        total_revenue = np.sum(
            self.sales["Total Revenue"].to_numpy()
        )

        total_books_sold = np.sum(
            self.sales["Quantity Sold"].to_numpy()
        )

        average_price = np.mean(
            self.inventory["Price"].to_numpy()
        ) if not self.inventory.empty else 0

        print("Total Books in Inventory:",
              self.inventory["Quantity"].sum())

        print("Total Books Sold:", total_books_sold)

        print("Total Revenue: Rs.", total_revenue)

        print("Average Book Price: Rs.", round(average_price, 2))

        # SALES BY BOOK

        print("\nSales by Book:")

        book_sales = self.sales.groupby("Title")[
            "Quantity Sold"
        ].sum().sort_values(ascending=False)

        print(book_sales)

        # BEST SELLING BOOK

        print("\nBest Selling Book:")

        print(book_sales.idxmax())

        # MERGE DATA

        analysis = self.sales.merge(
            self.inventory[["Title", "Genre", "Author"]],
            on="Title",
            how="left"
        )

        # REVENUE BY GENRE

        print("\nRevenue by Genre:")

        genre_revenue = analysis.groupby("Genre")[
            "Total Revenue"
        ].sum().sort_values(ascending=False)

        print(genre_revenue)

        # SALES BY AUTHOR

        print("\nSales by Author:")

        author_sales = analysis.groupby("Author")[
            "Quantity Sold"
        ].sum().sort_values(ascending=False)

        print(author_sales)

        # MONTHLY SALES

        print("\nMonthly Sales:")

        analysis["Date"] = pd.to_datetime(
            analysis["Date"], errors="coerce"
        )

        analysis.dropna(subset=["Date"], inplace=True)

        analysis["Month"] = analysis["Date"].dt.to_period("M")

        monthly_sales = analysis.groupby("Month")[
            "Total Revenue"
        ].sum()

        print(monthly_sales)

    # ==========================================
    # 2. DATA VISUALIZATION
    # ==========================================

    def visualize_data(self):

        if self.sales.empty:
            print("No sales data available.")
            return

        print("\n========== CHART MENU ==========")
        print("1. Bar Chart - Sales by Genre")
        print("2. Line Chart - Monthly Sales")
        print("3. Pie Chart - Revenue by Genre")
        print("4. Heatmap - Price and Sales Correlation")
        print("5. Generate All Charts")
        print("6. Back to Main Menu")

        choice = input("\nSelect Chart: ")

        if choice == "6":
            return

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Please select between 1 and 6.")
            return

        analysis = self.sales.merge(
            self.inventory[["Title", "Genre", "Author", "Price"]],
            on="Title",
            how="left"
        )

        analysis["Date"] = pd.to_datetime(
            analysis["Date"], errors="coerce"
        )

        analysis.dropna(subset=["Date"], inplace=True)

        # --------------------------------------
        # BAR CHART
        # --------------------------------------

        def bar_chart():

            genre_sales = analysis.groupby("Genre")[
                "Quantity Sold"
            ].sum().sort_values(ascending=False)

            plt.figure(figsize=(10, 5))

            sns.barplot(
                x=genre_sales.index,
                y=genre_sales.values
            )

            plt.title("Total Book Sales by Genre")
            plt.xlabel("Genre")
            plt.ylabel("Quantity Sold")
            plt.xticks(rotation=30)
            plt.tight_layout()

            plt.savefig("bar_chart.png")
            plt.show()
            plt.close()

            print("Bar Chart saved successfully!")

        # --------------------------------------
        # LINE CHART
        # --------------------------------------

        def line_chart():

            analysis["Month"] = analysis["Date"].dt.to_period("M")

            monthly_sales = analysis.groupby("Month")[
                "Total Revenue"
            ].sum()

            plt.figure(figsize=(10, 5))

            plt.plot(
                monthly_sales.index.astype(str),
                monthly_sales.values,
                marker="o"
            )

            plt.title("Monthly Sales Trends")
            plt.xlabel("Month")
            plt.ylabel("Total Revenue")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()

            plt.savefig("line_chart.png")
            plt.show()
            plt.close()

            print("Line Chart saved successfully!")

        # --------------------------------------
        # PIE CHART
        # --------------------------------------

        def pie_chart():

            genre_revenue = analysis.groupby("Genre")[
                "Total Revenue"
            ].sum()

            plt.figure(figsize=(8, 8))

            plt.pie(
                genre_revenue.values,
                labels=genre_revenue.index,
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title("Revenue Distribution by Genre")
            plt.tight_layout()

            plt.savefig("pie_chart.png")
            plt.show()
            plt.close()

            print("Pie Chart saved successfully!")

        # --------------------------------------
        # HEATMAP
        # --------------------------------------

        def heatmap_chart():

            book_analysis = analysis.groupby("Title").agg({
                "Price": "first",
                "Quantity Sold": "sum"
            })

            if len(book_analysis) < 2:
                print("Not enough data to generate Heatmap.")
                return

            correlation = book_analysis.corr()

            plt.figure(figsize=(7, 5))

            sns.heatmap(
                correlation,
                annot=True,
                cmap="coolwarm",
                fmt=".2f"
            )

            plt.title("Book Price and Sales Correlation")
            plt.tight_layout()

            plt.savefig("heatmap.png")
            plt.show()
            plt.close()

            print("Heatmap saved successfully!")

        # --------------------------------------
        # CHART SELECTION
        # --------------------------------------

        if choice == "1":
            bar_chart()

        elif choice == "2":
            line_chart()

        elif choice == "3":
            pie_chart()

        elif choice == "4":
            heatmap_chart()

        elif choice == "5":

            bar_chart()
            line_chart()
            pie_chart()
            heatmap_chart()

            print("\nAll Charts Generated Successfully!")


# ==============================================
# 3. MAIN MENU (CONTROL STRUCTURES)
# ==============================================

def main():

    bookstore = Bookstore()

    while True:

        print("\n======================================")
        print("     BOOKSTORE INVENTORY SYSTEM")
        print("======================================")

        print("1. Display Inventory")
        print("2. Add New Book")
        print("3. Remove Book")
        print("4. Update Inventory")
        print("5. Record Sale")
        print("6. Generate Report")
        print("7. Data Visualization")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            bookstore.display_inventory()

        elif choice == "2":

            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            genre = input("Enter Genre: ")

            try:
                price = float(input("Enter Book Price: "))
                quantity = int(input("Enter Quantity: "))

                bookstore.add_book(
                    title, author, price, quantity, genre
                )

            except ValueError:
                print("Please enter valid numeric values!")

        elif choice == "3":

            title = input("Enter Book Title to Remove: ")

            bookstore.remove_book(title)

        elif choice == "4":

            title = input("Enter Book Title: ")

            try:
                quantity = int(input("Enter New Quantity: "))

                bookstore.update_inventory(title, quantity)

            except ValueError:
                print("Please enter a valid quantity!")

        elif choice == "5":

            title = input("Enter Book Title: ")

            try:
                quantity = int(input("Enter Quantity Sold: "))

                bookstore.record_sale(title, quantity)

            except ValueError:
                print("Please enter a valid quantity!")

        elif choice == "6":

            bookstore.generate_report()

        elif choice == "7":

            bookstore.visualize_data()

        elif choice == "8":

            print("\nThank you for using Bookstore System!")
            break

        else:

            print("Invalid choice! Please select between 1 and 8.")


# ==============================================
# 4. PROGRAM EXECUTION
# ==============================================

if __name__ == "__main__":

    main()
