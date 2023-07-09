# DataBase_Controler-Demo

# SQLite Database Management Package

This Python package provides an interface for interacting with a SQLite database, and includes functions for creating a database, connecting to a database, and creating and interacting with tables within a database.

## Functions

### `conect_db(name)`

This function establishes a connection to a SQLite database.

- **Parameters**:
  - `name (str)`: The name of the SQLite database.
- **Returns**: 
  - `con`: The database connection object.
  - `message (str)`: A string indicating whether the database connection was established or not.

### `create_cursor(con)`

This function creates a cursor object which can be used to execute SQL statements on a SQLite database.

- **Parameters**:
  - `con`: The database connection object.
- **Returns**: 
  - `cur`: The cursor object.
  - `message (str)`: A string indicating whether the cursor was created successfully or not.

## Class `tabla`

This class is used to interact with a specific table within a SQLite database.

- **Parameters**:
  - `name (str)`: The name of the table.
  - `campos (list)`: A list of strings representing the fields (columns) in the table.

### Methods

#### `__init__(self, name, campos)`

Initializes a new instance of the tabla class. This also creates the table in the database if it does not already exist.

#### `print(self)`

This method fetches all records from the table and prints them.

#### `consult(self, campo0)`

Fetches records from the table where the value in the first field matches the specified value.

- **Parameters**:
  - `campo0`: The value to match in the first field of the table.
- **Returns**: 
  - `data`: The fetched records.
  - `message (str)`: A string indicating whether the data was consulted correctly or not.

#### `insert(self, data)`

Inserts a new record into the table.

- **Parameters**:
  - `data (dict)`: A dictionary where the keys are field names and the values are the corresponding values for the new record.

#### `delet(self, campo0)`

Deletes records from the table where the value in the first field matches the specified value.

- **Parameters**:
  - `campo0`: The value to match in the first field of the table.

#### `update(self, campo0, data)`

Updates records in the table where the value in the first field matches the specified value.

- **Parameters**:
  - `campo0`: The value to match in the first field of the table.
  - `data (dict)`: A dictionary where the keys are field names and the values are the new values for these fields.

#### `get_data(self)`

Fetches all records from the table.

- **Returns**: 
  - `data`: The fetched records.
  - `message (str)`: A string indicating whether the data was consulted correctly or not.

#### `delet_duplicated(self)`

Deletes all duplicate records in the table, keeping only the first occurrence.

## Usage

To use this package, first import it, then create a new instance of the `tabla` class, specifying the table name and fields. You can then use the methods of the class to interact with the table.

```python
from my_package import tabla

my_table = tabla("Users", ["id", "name", "email"])
my_table.insert({"id": "1", "name": "John Doe", "email": "johndoe@example.com"})
my_table.print()
```
