**Personal Expense Tracker (CLI)**

A menu-driven command-line expense tracker written in core Python basics only — no functions, no classes, no external libraries. Built as a beginner project to practice fundamentals before moving on to functions and OOP.

Description :
The program asks for your name and monthly budget, then runs a menu loop until you choose Exit. You can add, view, search and delete expenses, and get a summary report showing totals, category-wise spending, remaining budget and a spending level. All data lives in memory while the program runs (no file storage).

Features
1. Add expenses with description, amount and category (Food / Travel / Shopping / Bills / Other)
2. Input validation: amount must be a number greater than 0; category must be valid
3. Description cleanup: extra spaces removed and stored in Title Case
4. View all expenses as a numbered list
5. Search by category (case-insensitive) with category total
6. Delete an expense by its number
7. Summary report:
Total, average, highest and lowest expense
Category-wise totals
Budget remaining, or a ⚠ Budget exceeded by ₹... warning
Unique categories used
Spending level: Good (< 50%), Careful (50–90%), Danger (> 90%)

How to Run
Requires Python 3.6+.

bash : 
git clone https://github.com/sakshipathak-data/expense-tracker-python.git 
cd expense-tracker-python
python expense_tracker.py

Concepts Used
1. Variables and data types: store name, budget, amounts and totals 
2. input(), print() and f-strings: take user input and show formatted output
3. Type casting: float() and int() convert the typed text into numbers
4. operators: arithmetic for totals and average, comparison and logical for budget checks
5. if-elif-else: handles menu choices and the spending level (Good / Careful / Danger)
6. while loops: keep the main menu running and re-ask when input is invalid
7. for loops with enumerate: print the numbered expense list and calculate the summary
8. break and continue: exit a loop or retry after wrong input
9. String methods: strip, title, lower, split and join clean up the text
10. List: stores all the expenses
11. Tuple: holds the fixed set of allowed categories
12. Set: finds the unique categories that were used
13. Dictionary: each expense is a dictionary, and category-wise totals are a dictionary too
14. Nested data: a list of dictionaries holds everything together
15. try-except: safely converts the typed amount into a number without crashing

Sample Output
See sample_output.txt for a full run. 
A short excerpt:
Enter your name: rahul
Enter monthly budget: 15000

Welcome, Rahul! Budget: ₹15000.00

===== Expense Tracker =====
1. Add Expense
2. View All Expenses
3. Search by Category
4. Delete an Expense
5. Summary Report
6. Exit
Choose: 1
Description: lunch at cafe
Amount: 250
Category (Food/Travel/Shopping/Bills/Other): food
Expense added!

Future Improvements
1. Refactor into functions to remove repeated code (listing expenses, input validation)
2. Save and load expenses using file storage (CSV / JSON)
3. Rewrite using OOP (Expense and ExpenseTracker classes)
4. Sort expenses by amount, add an "Undo last expense" option
5. Text bar chart for category-wise spending
6. Monthly filtering using dates

License
MIT
