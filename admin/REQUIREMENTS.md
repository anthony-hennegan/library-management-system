# Project Requirements

## Project Overview

The Personal Library application is a command-line program that allows users to create and manage a personal collection of books. Users can add, view, search, update, and delete books while saving their library to a local file so their data persists between sessions.

---

## Objective

The purpose of this project is to build a complete Python application while practicing fundamental programming concepts, including:

- Variables
- Data types
- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- User input
- File input/output
- Basic program organization
- Problem solving and debugging

---

## Functional Requirements

The application shall allow the user to:

- View all books in the library.
- Add a new book.
- Search for books by title or author.
- Update an existing book.
- Delete a book from the library.
- Save the library to a file.
- Load the library from a file when the program starts.
- Exit the application safely.

---

## Data Requirements

Each book shall contain the following information:

| Field | Description |
|--------|-------------|
| Title | Name of the book |
| Author | Name of the author |
| Checked_Out | Indicates whether the book has been checked out|

---

## User Interface Requirements

The application shall provide:

- A clear command-line main menu.
- Numbered menu options.
- Clear prompts for user input.
- Confirmation messages after successful actions.
- Helpful error messages for invalid input.
- A readable display of all books.
- The ability to return to the main menu after each completed operation.

---

## Technical Requirements

The application shall be developed using:

- Python
- Functions
- Lists
- Dictionaries
- Classes
- Loops
- Conditional statements
- JSON file storage

---

## Validation Requirements

The application must:

- Reject invalid menu selections.
- Prevent empty book titles.
- Prevent empty author names.
- Handle searches with no matching results.
- Confirm before deleting a book.
- Handle missing or empty save files without crashing.
- Continue running until the user chooses to exit.

---

## Stretch Goals (Optional)

After all required functionality has been completed, consider implementing:

- Search by checked out status.
- Sort books alphabetically.
- Book ratings.
- Personal notes for each book.
- Date added.
- Reading statistics.
- Export library to CSV.

---

# Definition of Done

The project is complete when all of the following are true:

- [x] Program runs without crashing.
- [x] User can add books.
- [x] User can view books.
- [x] User can search books.
- [x] User can update book information.
- [x] User can delete books.
- [x] Library saves to disk.
- [x] Library loads automatically on startup.
- [x] Invalid input is handled gracefully.
- [x] Code is organized into functions.
- [ ] Code is readable and appropriately commented.
- [x] README.md explains how to install and run the project.
- [x] Changes are committed to Git.