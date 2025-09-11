"""
Story:
Ama runs a small bookshop in her community. 
She wants to use Python to organize her shop records. She has different types of books, 
their prices, and customers who bought them. Your task is to help her write a Python program.

Your Tasks:

1. Create a list called books with these titles:
    - "Math"
    - "English"
    - "Science"
    - "History"

2. Create a tuple called prices for the cost of each book in cedis:
    - Math → 20
    - English → 15
    - Science → 25
    - History → 18

3. Ama sold the following books: "Math", "English", "Math", "Science", "English".
    - Store this in a list called sold_books.
    - Convert it to a set to know the unique books sold.

4. Using variables and operators:
    - Ama had 30 books in stock. She sold 5 books today.
    - Write code to subtract and print how many books are left.

5. Use an if statement:
    - If the remaining books are less than 10, print "Restock soon!"
    - Otherwise, print "Stock is enough."

6. Use an f-string to print a receipt like this:
    Customer bought 2 Math books at 20 cedis each.
    Total = 40 cedis

7. Write the data type of each of the following:
    - "English"
    - 25
    - 15.5
    - True
"""

books = ["Math", "English", "Science", "History"]
prices = (20, 15, 25, 18)
sold_books = ["Math", "English", "Math", "Science", "English"]
unique_sold_books = set(sold_books)
print(unique_sold_books)
total_books = 30
sold_count = 5
remaining_books = total_books - sold_count
print(f'Books left in stock: {remaining_books}')

if remaining_books < 10:
    print("Restock soon!")
else:
    print("Stock is enough.")

math_price = prices[0]
math_sold = sold_books.count("Math")    
total_cost = math_price * math_sold
print(f'Customer bought {math_sold} Math books at {math_price} cedis each.\nTotal = {total_cost} cedis')
