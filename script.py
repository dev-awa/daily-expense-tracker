import sqlite3
import os

# Database name
DB_NAME = "database.db"

def get_connection():
	"""Establishes connection to the SQLite database."""
	return sqlite3.connect(DB_NAME);

def add_expense():
	"""Prompts user for details and adds a new expense to the database."""
	print("\n--- Add New Expense ---")
	title = input("Enter title (e.g., Coffee, Bus Ticket): ").strip()
	
	if not title:
		print("Error: Title cannot be empty.")
		return
	
	try:
		amount = int(input("Enter amount (integer): "))
	except ValueError:
		print("Error: Amount must be a valid number.")
		return
	
	date = input("Enter date (e.g., 2026-09-26): ").strip()
	
	if not date:
		print("Error: Date cannot be empty.")
		return
	conn = get_connection()
	cursor = conn.cursor()
	
	# Insert into the 'expences' table
	cursor.execute(
		"INSERT INTO expences (title, amount, date) VALUES (?, ?, ?)",
		(title, amount, date)
	)
	
	conn.commit()
	conn.close()
	print(f"Success: '{title}' added successfully!")
	
def show_all():
	"""Fetches and displays all expenses from the database."""
	print("\n--- All Expenses ---")
	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute("SELECT id, title, amount, date From expences")
	rows = cursor.fetchall()
	
	if not rows:
		print("No expenses found.")
	else:
		print(f"{'ID':<5} | {'Title':<15} | {'Amount':<8} | {'Date':<12}")
		print("-" * 50)
		for row in rows:
			# row[0]=id, row[1]=title, row[2]=amount, row[3]=date
			print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<8} | {row[3]:<12}")
	
	conn.close()

def delete_expense():
	"""Deletes an expense by its ID."""
	print("\n--- Delete Expense ---")
	try:
		expense_id = int(input("Enter the ID of the expense to delete: "))
	except ValueError:
		print("Enter: ID must be a number.")
		return
	
	conn = get_connection()
	cursor = conn.cursor()
	
	# Check if ID exists first (optional but good for UX)
	cursor.execute("SELECT * FROM expences WHERE id = ?", (expense_id,))
	if not cursor.fetchone():
		print(f"Error: No expense found with ID {expense_id}.")
		conn.close()
		return
		
	cursor.execute("DELETE FROM expences WHERE id = ?", (expense_id,))
	conn.commit()
	conn.close()
	print(f"Success: Expense with ID {expense_id} deleted.")

def show_total():
	"""Calculates and displays the total sum of all expenses."""
	print("\n--- Total Expenses ---")
	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute("SELECT SUM(amount) FROM expences")
	total = cursor.fetchone()[0]
	
	if total is None:
		total = 0
	
	print(f"Total Amount Spent: ${total}")
	conn.close()
	
def main():
	"""Main Menu loop for the CLI application."""
	while True:
		print("\n=============================================")
		print("		DAILY EXPENSES TRACKER		")
		print("==========================================")
		print("1. Add Expense")
		print("2. Show All Expenses")
		print("3. Delete Expense")
		print("4. Show Total")
		print("5. Exit")
		print("==========================================")
		
		choice = input("Choose an option (1-5): ").strip()
		
		if choice == '1':
			add_expense()
		elif choice == '2':
			show_all()
		elif choice == '3':
			delete_expense()
		elif choice == '4':
			show_total()
		elif choice == '5':
			print("Goodbye!")
			break
		else:
			print("Invalid option. Please try again.")

if __name__ == "__main__":
	main()
