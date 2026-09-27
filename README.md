# Daily Expense Tracker 💰

A simple, clean, and lightweight Command-Line Interface (CLI) application to track your daily expenses. Built with Python and SQLite, focusing on simplicity and a clean user experience.

## ✨ Features

- **Add Expense:** Quickly add a new expense with title, amount, and date.
- **Show All Expenses:** View a cleanly formatted table of all your recorded expenses.
- **Delete Expense:** Remove an expense by its unique ID.
- **Show Total:** Instantly calculate and view the total sum of all your expenses.
- **Data Persistence:** All data is safely stored in a local SQLite database.

## 🛠️ Technologies Used

- **Python 3:** Core logic and CLI management.
- **SQLite3:** Lightweight, file-based database for storing expenses.
- **SQL:** For database queries (Create, Insert, Select, Delete, Sum).

## 🚀 Getting Started

Follow these simple steps to get the project up and running on your local machine.

### Prerequisites

You only need **Python 3** installed on your system. SQLite comes built-in with Python, so no extra installation is needed.

### Project Structure

```text
Daily Expenses/
├── database.db       # SQLite database file (auto-generated if not exists)
├── script.py         # Main Python script
├── README.md         # Project documentation
├── LICENSE           # MIT License
└── .gitignore        # Git ignore rules
```

Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/dev-awa/daily-expense-tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd daily-expense-tracker
   ```
3. Run the application:
   ```bash
   python3 script.py
   ```
4. Follow the on-screen menu to manage your expenses.

🗄️ Database Schema

The application uses a single table named expences with the following structure:

Column Type Description

id INTEGER Primary Key, Auto Increment

title TEXT Title of the expense (e.g., Coffee)

amount INTEGER Amount spent

date TEXT Date of expense (YYYY-MM-DD)

🚀 Future Improvements

This project is currently a simple MVP (Minimum Viable Product). Here are some planned features for future releases:

· Search: Filter expenses by title or keyword.

· Filter by Date: View expenses for a specific month or date range.

· Edit/Update: Modify an existing expense by its ID.

· Export: Export expense data to CSV or JSON.

· Interactive UI: Improve the CLI with colored text and better formatting.

Feel free to check the [Issues Page](https://github.com/dev-awa/daily-expense-tracker/issues) to see what is currently being worked on!

🤝 Contributing & Workflow

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Here is our simple workflow for contributing to this project:

1. Fork the Project (Click the "Fork" button at the top right of this page).
2. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/daily-expense-tracker.git
   ```
3. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
4. Commit your changes with a clear message:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. Push your branch to your fork:
   ```bash
   git push origin feature/AmazingFeature
   ```
6. Open a Pull Request from your branch to the main branch of this repository.

📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

⭐ If you find this project useful, please give it a star!

[![GitHub stars](https://img.shields.io/github/stars/dev-awa/daily-expense-tracker?style=social)](https://github.com/dev-awa/daily-expense-tracker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/dev-awa/daily-expense-tracker?style=social)](https://github.com/dev-awa/daily-expense-tracker/network/members)


Made with ❤️ by [dev-awa](https://github.com/dev-awa)

</div>
