# SQLite Database Management Package

This Python package provides an interface for interacting with a SQLite database.

## Functions

### `conect_db(name)`

Establishes a connection to a SQLite database.

**Parameters**:

- `name (str)`: The name of the SQLite database.

**Returns**: 

- `con`: The database connection object.
- `message (str)`: A string indicating whether the database connection was established or not.

### `create_cursor(con)`

Creates a cursor object which can be used to execute SQL statements on a SQLite database.

**Parameters**:

- `con`: The database connection object.

**Returns**: 

- `cur`: The cursor object.
- `message (str)`: A string indicating whether the cursor was created successfully or not.

## Class `tabla`

This class is used to interact with a specific table within a SQLite database.

**Parameters**:

- `name (str)`: The name of the table.
- `campos (list)`: A list of strings representing the fields (columns) in the table.

### Methods

Each method is demonstrated with a practical usage example.

#### `__init__(self, name, campos)`

Initializes a new instance of the tabla class. This also creates the table in the database if it does not already exist.

#### `print(self)`

Fetches all records from the table and prints them.

```python
users_table = tabla("Users", ["id", "name", "email"])
users_table.print()  # prints all records in the table
```

#### `consult(self, campo0)`

Fetches records from the table where the value in the first field matches the specified value.

```python
data, msg = users_table.consult("1")
print(data)  # [('1', 'John Doe', 'johndoe@example.com')]
```

#### `insert(self, data)`

Inserts a new record into the table.

```python
users_table.insert({"id": "1", "name": "John Doe", "email": "johndoe@example.com"})
```

#### `delet(self, campo0)`

Deletes records from the table where the value in the first field matches the specified value.

```python
users_table.delet("1")  # Deletes the record where id is "1"
```

#### `update(self, campo0, data)`

Updates records in the table where the value in the first field matches the specified value.

```python
users_table.update("1", {"name": "Jane Doe"})  # Update the name of the user with id "1"
```

#### `get_data(self)`

Fetches all records from the table.

```python
data, msg = users_table.get_data()
print(data)  # Prints all records in the table
```

#### `delet_duplicated(self)`

Deletes all duplicate records in the table, keeping only the first occurrence.

```python
users_table.delet_duplicated()  # Deletes all duplicate records in the table
```

## Usage

To use this package, first import it, then create a new instance of the `tabla` class, specifying the table name and fields. You can then use the methods of the class to interact with the table.

```python
from my_package import tabla

my_table = tabla("Users", ["id", "name", "email"])
my_table.insert({"id": "1", "name": "John Doe", "email": "johndoe@example.com"})
my_table.print()
```
