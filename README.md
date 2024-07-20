# Fruit Stock Management System

## Overview

The Fruit Stock Management System is a Python application designed to manage fruit stock for both managers and customers. It provides functionalities for adding, viewing, updating, and purchasing fruit stocks. The system uses file handling to log transactions and separate modules for better organization and reusability.

## Features

- **Manager Role:**
  - Add fruit stock
  - View fruit stock
  - Update fruit stock

- **Customer Role:**
  - View fruit stock
  - Purchase fruit

- **Logging:**
  - All transactions are logged to a file (`transaction_log.txt`).

## Files

- **`main.py`**: Entry point of the application. Handles the main menu and role selection.
- **`manager.py`**: Contains the business logic for managing fruit stock.
- **`customer.py`**: Contains the business logic for customer operations, including viewing and purchasing fruit.
- **`utils.py`**: Contains utility functions for logging transactions and other common operations.
