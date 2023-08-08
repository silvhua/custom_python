# DataCamp SQL for Data Analysis

Function/Method | Description
--- | ---
`COALESCE` | For each row, return the first non-null value.
`CAST(value AS new_type)` or <br>`value::new_type` | Convert from one data type to another in the query.
`STDDEV()` | Standard deviation.
`TRUNC(number, integer)` | Truncate values to the precision indicated by the integer. Positive integer indicates number of decimal places to keep. Negative integer indicates places before decimal to replace with zero.
`GENERATE_SERIES(start number, end number, step)` |


The `coalesce()` function can be useful for specifying a default or backup value when a column contains NULL values.
`Coalesce()` checks arguments in order and returns the first non-NULL value, if one exists.
* coalesce(NULL, 1, 2) = 1
* coalesce(NULL, NULL) = NULL
* coalesce(2, 3, NULL) = 2

## More complex stats

What to calculate | Function/Method | Description
--- | ---- | ---
Correlation | `corr(column1, column2)` |
Value corresponding to a certain percentile - discrete | `percentile_disc(float) WITHIN GROUP (ORDER BY column)` | This value must exist in the data set.
Value corresponding to a certain percentile - continuous | `percentile_cont(float) WITHIN GROUP (ORDER BY column)` | This value is interpolated using the data set and may not necessarily exist in the data set.

# DataCamp Intro to Docker
Action | Script
--- | ---
Run container in the background and rename it | `docker run -d --name new_name existing_name`
List running  containers | `docker ps` <br>`docker ps -f "name=container_name"`
View logs | `docker logs` <br>`docker logs container_name`

## Chapter 3 Creating your own Docker images
### Basic shell commands
Action | Script
--- | ---
Open a file to read/edit | `nano`
Read the contents of a file without opening it | `cat filename`
Append to the end of a text file without opening it | `echo "text to append" >> filename`
Allow commands to span multiple lines (`\`) and Chain commands (`&&`)| `\&&`

### Docker commands

Action | Script
--- | ---
Starting an image interactively with a custom start command | `docker run -it image_name bash` <br>or <br>`docker run -it <image> <shell-command>`
Build an image without caching | `docker build --no-cache -t image_name .`
Clear builder cache | `docker builder prune -a -f`
Remove unused images, containers, etc. | `Docker system prune -f`


### Basic work flow after `Dockerfile` (no filename extension) is created
```
docker build -t image_name .
docker run image_name
```
# DataCamp Web Scraping with Python

Although we haven't yet gone deep into XPath, one thing we can do is select elements by their attributes using an XPath. For example, if we want to direct to the div element within the HTML document whose id attribute is "uid", then we could write the XPath string `'//div[@id="uid"]'`. The first part of this string, `//div`, first looks at all `div` elements in the HTML document. Then, using the brackets, we specify that we want only the `div` element with a specific id attribute (in this case `uid`). To note, the phrase `@id="uid"` in the brackets would be read as "attribute id equals uid".

Action | XPath | CSS
--- | --- | ---
Select elements where the specified attribute is a substring of a given string | `'contains(@attri-name,"string-expr")'`
Select the attribute value  | `'/@attri-name'`<br>e.g. `'//p[@id="p2"]/a/@href'` | `'> ::attr(attri-name)'`
Extract text from that generation | `'/text()'` | `'::text'` to only extract from that generation
Extract text from that and subsequent generations | `'//text()'` | `' ::text'` (space in front)

# Codecademy
[learn-javascript-introduction/cheatsheet](https://www.codecademy.com/learn/introduction-to-javascript/modules/learn-javascript-introduction/cheatsheet)
[learn-javascript-control-flow/cheatsheet](https://www.codecademy.com/learn/introduction-to-javascript/modules/learn-javascript-control-flow/cheatsheet)


<br>

```JavaScript
// Print variable name
console.log(typeof variable_name)

// Create an f-string to interpolate variables into a string
console.log(`This is a string literal ${variable_name}.`)
```

### Ternary Operator
```JS
// Example 1
let isNightTime = true;
 
isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');
// Is equivalent to
if (isNightTime) {
  console.log('Turn on the lights!');
} else {
  console.log('Turn off the lights!');
}

// Example 2
let favoritePhrase = 'Love That!';

favoritePhrase === 'Love That!' ? console.log('I love that!') : console.log("I don't love that!");

// Is equivalent to
if (favoritePhrase === 'Love That!') {
  console.log('I love that!');
} else {
  console.log("I don't love that!");
}
```

### Conditional statements
Logical operators | Description
--- | ---
`&&` or `and` | checks if both provided expressions are truthy.
`or` or 2 pipe symbols | checks if either provided expression is truthy.
The bang operator, `!` | switches the truthiness and falsiness of a value.

```JavaScript
let groceryItem = 'papaya';
 
if (groceryItem === 'tomato') {
  console.log('Tomatoes are $0.49');
} else if (groceryItem === 'papaya'){
  console.log('Papayas are $1.29');
} else {
  console.log('Invalid item');
}
```

### Switch statement 
This is an alternative statement that is easier to read and write.
```JavaScript
// Can also be written as:
let groceryItem = 'papaya';
 
switch (groceryItem) {
  case 'tomato':
    console.log('Tomatoes are $0.49');
    break;
  case 'lime':
    console.log('Limes are $1.49');
    break;
  case 'papaya':
    console.log('Papayas are $1.29');
    break;
  default:
    console.log('Invalid item');
    break;
}
 
// Prints 'Papayas are $1.29'
```
## Functions

```JavaScript
function greet(name='stranger') {
  console.log(`Hello, ${name}`!);
}
```
Use a return statement like in Python if needed.
* The default result of a function is `undefined` if there is no `return` statement.

### Function expressions

```JavaScript
// Declare the function expression
const calculateArea = function(width, height) {
  return wedith * height;
}

// Invoke the function expression
variableName(argument1, argument2)
```

### Arrow functions
Alternative to standard function syntax.
```JavaScript
const rectangleArea = (width, height) => {
  let area = width * height;
  return area;
};
```

### Concise Body Arrow Functions
Functions that take only 1 parameter do not be enclosed in `()`. 

`const functionName = paramOne => {};`

A function body composed of a single line block does not need curly braces nor the `return` keyword (an implicity return).

`const sumNumbers = number => number + number;`

## Arrays
[DataCamp Docs: Arrays and Array Methods](https://www.codecademy.com/resources/docs/javascript/arrays)

## Loops
A `do...while` statement says to do a task once and then keep doing it until a specified condition is no longer met. The syntax for a `do...while` statement looks like this:
```JavaScript
let countString = '';
let i = 0;
 
do {
  countString = countString + i;
  i++;
} while (i < 5);
 
console.log(countString);
```

## Iterators

Function/Method | Description
--- | ---
`.forEach()` | Performs a callback function on each element and returns `undefined`
`.map()` | Same as `.forEach()` but returns a new array.
`.filter()` | returns an array of elements after filtering out certain elements from the original array. 

### Syntax options

Function expression
```JavaScript
const groceries = ['brown sugar', 'salt', 'cranberries']
groceries.forEach(function(groceryItem) {console.log(' - ' + groceryItem);});
```

Arrow function
```JavaScript
groceries.forEach(groceryItem => console.log(groceryItem));
```

Function declaraton
```JavaScript
function printGrocery(element){
  console.log(element);
}
 
groceries.forEach(printGrocery);
```

# DataCamp ETL in Python

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Create the engine
engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/database_name")

# Create the session
session = Session(engine)
```

## Associate user-defined Python classes, called data models, with database tables.
```python
from ssqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Initialize the base and set inheritance
Base = declarative_base()

class TableName(Base):
  __tablename__ = 'database_table_name'
  # map a class attribute to each column
  id = Column(Integer, primary_key=True) # Set the primary key
  title = Column(String(55))
  description = Column(String(255))
```
## Add rows to tables



## Example from DataCamp Chapter 2 'Put transform operations together' exercises
### This is the script in `base.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Create the engine
engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/database_name")

# Create the session
session = Session(engine)

from ssqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Initialize the base and set inheritance
Base = declarative_base()
```
This is in `create_tables.py`
```python
from base import Base, engine
# Import the PprRawAll table
from tables import PprRawAll

# Create the table in the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)
```

### This is the script in `transform.py` to clean raw data:
```python
import os
import csv
from datetime import datetime

from common.tables import PprRawAll
from common.base import session
from sqlalchemy import text

# Settings
base_path = os.path.abspath(__file__ + "/../../")

# START - Paths for new February 2021 data available

# Raw path where we want to extract the new CSV data
raw_path = f"{base_path}/data/raw/downloaded_at=2021-02-01/ppr-all.csv"

# END - Paths for new February 2021 data available

def transform_case(input_string):
    """
    Lowercase string fields
    """
    return input_string.lower()


def update_date_of_sale(date_input):
    """
    Update date format from DD/MM/YYYY to YYYY-MM-DD
    """
    current_format = datetime.strptime(date_input, "%d/%m/%Y")
    new_format = current_format.strftime("%Y-%m-%d")
    return new_format


def update_description(description_input):
    """
    Simplify the description field for potentialy future analysis, just return:
    - "new" if string contains "new" substring
    - "second-hand" if string contains "second-hand" substring
    """
    description_input = transform_case(description_input)
    if "new" in description_input:
        return "new"
    elif "second-hand" in description_input:
        return "second-hand"
    return description_input


def update_price(price_input):
    """
    Return price as integer by removing:
    - "€" symbol
    - "," to convert the number into float first (e.g. from "€100,000.00" to "100000.00")
    """
    price_input = price_input.replace("€", "")
    price_input = float(price_input.replace(",", ""))
    return int(price_input)


def truncate_table():
    """
    Ensure that "ppr_raw_all" table is always in empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("TRUNCATE TABLE ppr_raw_all;ALTER SEQUENCE ppr_raw_all_id_seq RESTART;")
    )
    session.commit()


def transform_new_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """
    with open(raw_path, mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our PprRawAll objects
        ppr_raw_objects = []
        for row in reader:
            # Apply transformations and save as PprRawAll object
            ppr_raw_objects.append(
                PprRawAll(
                    date_of_sale=update_date_of_sale(row["date_of_sale"]),
                    address=transform_case(row["address"]),
                    postal_code=transform_case(row["postal_code"]),
                    county=transform_case(row["county"]),
                    price=update_price(row["price"]),
                    description=update_description(row["description"]),
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(ppr_raw_objects) # This method is a legacy feature as of the 2.0 series of SQLAlchemy
        session.commit()


def main():
    print("[Transform] Start")
    print("[Transform] Remove any old data from ppr_raw_all table")
    truncate_table()
    print("[Transform] Transform new data available in ppr_raw_all table")
    transform_new_data()
    print("[Transform] End")
```
### This is in `extract.py`
```python
import os
import csv
import tempfile
from zipfile import ZipFile

import requests

# Settings
base_path = os.path.abspath(__file__ + "/../../")

# START - Paths for new February 2021 data available

# External website file url
source_url = "https://assets.datacamp.com/production/repositories/5899/datasets/66691278303f789ca4acd3c6406baa5fc6adaf28/PPR-ALL.zip"

# Source path where we want to save the .zip file downloaded from the website
source_path = f"{base_path}/data/source/downloaded_at=2021-02-01/PPR-ALL.zip"

# Raw path where we want to extract the new .csv data
raw_path = f"{base_path}/data/raw/downloaded_at=2021-02-01/ppr-all.csv"

# END - Paths for new February 2021 data available


def create_folder_if_not_exists(path):
    """
    Create a new folder if it doesn't exists
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)


def download_snapshot():
    """
    Download a new snapshot from the source
    """
    create_folder_if_not_exists(source_path)
    with open(source_path, "wb") as source_ppr:
        response = requests.get(source_url, verify=False)
        source_ppr.write(response.content)


def save_new_raw_data():
    """
    Save new raw data from the current snapshot from the source
    """

    create_folder_if_not_exists(raw_path)
    with tempfile.TemporaryDirectory() as dirpath:
        with ZipFile(
            source_path,
            "r",
        ) as zipfile:
            names_list = zipfile.namelist()
            csv_file_path = zipfile.extract(names_list[0], path=dirpath)
            # Open the CSV file in read mode
            with open(csv_file_path, mode="r", encoding="windows-1252") as csv_file:
                reader = csv.DictReader(csv_file)

                row = next(reader)  # Get first row from reader
                print("[Extract] First row example:", row)

                # Open the CSV file in write mode
                with open(
                    raw_path,
                    mode="w",
                    encoding="windows-1252",
                ) as csv_file:
                    # Rename field names so they're ready for the next step
                    fieldnames = {
                        "Date of Sale (dd/mm/yyyy)": "date_of_sale",
                        "Address": "address",
                        "Postal Code": "postal_code",
                        "County": "county",
                        "Price (€)": "price",
                        "Description of Property": "description",
                    }
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    # Write headers as first line
                    writer.writerow(fieldnames)
                    for row in reader:
                        # Write all rows in file
                        writer.writerow(row)


def main():
    print("[Extract] Start")
    print("[Extract] Downloading snapshot")
    download_snapshot()
    print(f"[Extract] Saving data from '{source_path}' to '{raw_path}'")
    save_new_raw_data()
    print(f"[Extract] End")
```
### Execute the scripts: `execute.py`
```python
# Import the transform script
import extract
import transform

# Call its main function
if __name__ == "__main__":
    extract.main()
    transform.main()  
```

## Creating unique keys

Use `column_property`
```python
from sqlalchemy import cast, Column, Integer, String, Date
# Import the function required
from sqlalchemy.orm import column_property

from base import Base

class PprRawAll(Base):
    __tablename__ = "ppr_raw_all"

    id = Column(Integer, primary_key=True)
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(255))
    # Create a unique transaction id
    transaction_id = column_property(
        date_of_sale + "_" + address + "_" + county + "_" + price
    )
# Cast to other data types
class PprCleanAll(Base):
    __tablename__ = "ppr_clean_all"

    id = Column(Integer, primary_key=True)
    date_of_sale = Column(Date)
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(Integer)
    description = Column(String(255))
    # Create a unique transaction id
    # all non-string columns are casted as string
    transaction_id = column_property(
        cast(date_of_sale, String) + "_" + address + "_" + county + "_" + cast(price, String)
    )
```
## Query API

Function/Method | Description | SQL equivalent
--- | ---- | ---
`session.query(table).filter(filter_expression)` | Select rows using filter | `SELECT * FROM table WHERE ...`
`session.query(table).all()` | Select rows | `SELECT * FROM table`
`table_name.column_name` | Get values from a given column | Same as for Python

## Inserting Rows 
```python
# Import the function required
from sqlalchemy.dialects.postgresql import insert
  
values = [{"date_of_sale": "2021-01-01",
           "address": "14 bow street",
           "postal_code": "dublin 7",
           "county": "dublin",
           "price": 350000,
           "description":"second-hand"}]

# Insert values in PprCleanAll
stmt = insert(table_name).values(values)

# Execute and commit
session.execute(stmt)
session.commit()
```
## Deleting Rows
```python
# Import the function required
from sqlalchemy import delete

# Delete rows lacking a description value
stmt = delete(PprCleanAll).filter(PprCleanAll.description=="")

# Execute and commit
session.execute(stmt)
session.commit()
``` 

# Datacamp Introduction to PySpark
Function/Method | Description | Imports
--- | ---- | ---
`spark = SparkSession.builder.getOrCreate()` | returns an existing SparkSession if there's already one in the environment, or creates a new one if necessary | from pyspark.sql import SparkSession
`.catalog.listTables()` | List tables in the catalogue
`.sql(query_string)` | Send an SQL query to the data
`.sql(query_string).show()` | Show the results of the SQL query
`.sql(query_string).toPandas()` | Convert the results to a pandas DataFrame


```python
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
# This returns an existing SparkSession if there's already one in the environment, or creates a new one if necessary!
spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(spark)

# Print the tables in the catalog
print(spark.catalog.listTables())
```
### Use SQL queries in PySpark
```python
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()

```
### Pandafy a Spark DataFrame
```python
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())
```
### Pandas or CSV to Spark
Function/Method | Description
--- | ---
`spark_temp = spark.createDataFrame(pandas_df)` | Put a pandas DataFrame into a Spark clsuter that is stored locally.
`spark_temp.createTempView("tempoary_table_name")` | registers the DataFrame as a table in the catalog, but as this table is temporary, it can only be accessed from the specific SparkSession used to create the Spark DataFrame.
`spark_temp.createOrReplaceTempView("tempoary_table_name")` | creates a new temporary table if nothing was there before, or updates an existing table if one was already defined
`spark.read.csv(file_path, header=True)` | Create a table from a CSV file

#### Read CSV files

```Python
# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()
```

## Manipulating data
Function/Method | Description | SQL equivalent
--- | --- | ---
`df = spark.table("table_name")` | Create a Spark DataFrame from a table in the `.catalog` by instantiating the `DataFrame` class.
`df = withColumn("new_col_name", new_column_values)` | Create a new DataFrame with a new column.
`df = withColumnRenamed("old_col_name", "new_column_name")` | Create a new DataFrame with a new column.
`df.filter("WHERE <SQL conditional expression>)` <br> `df.filter(<Spark column of boolean values>)` | | `WHERE`  
`df.select("column1", "column2")` <br>`df.select(df.column1, df.column2)` | Return selected columns of the DataFrame. | `SELECT`
`df.select("column1/60").alias("new_column_name")` <br>`df.selectExpr("column AS alias")` | Give the column a name | `AS`
`.groupby().min("column_name")` <br>`.groupby().max("column_name")` <br>`.groupby("groupby_column").avg("column_name")` <br>`.groupby("groupby_column1", "groupby_column2").sum("column_name")` | Aggregate function. `.groupby()` does not need arguments. | `GROUP BY`
`.agg(F.stddev("dep_delay"))` | Aggregate using the passed function. Required import: <br>`import pyspark.sql.functions as F` | `GROUP BY`
`table1.join(table2, on="common_column", how="leftouter")` | Join tables | `LEFT JOIN`
`df.withColumn("column_name", df.column_name.cast("integer"))`  | Create new df with the column as integer data type | `CAST`
`df.withColumn("column_name", df.column_name.cast("double"))` | Create new df with the column as float data type | `CAST`
 
### Creating columns
```python
# Create the DataFrame flights
flights = spark.table("flights")

# create a new column in the flights dataframe by dividing values of the `air_time` column in two.
flights = flights.withColumn("duration_hours", flights.air_time/2) 
```
### Filtering data
```python
# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)
```
### Selecting columns
```python
# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)
```
### Selecting columns with calculations
```python
# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
```
### Aggregating
```Python
# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == 'PDX').groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == 'SEA').groupBy().max("air_time").show()

# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()
```
#### Using the `.agg()` method
The `pyspark.sql.functions` submodule has several aggregate functions that can be used with `.agg()` method 
```python
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")

# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()
```
### Joining
```python
table1.join(
  table2, on="common_column",
  how="leftouter"
)
```

```python

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(
    airports, on="dest",
    how='leftouter'
    )
```
### Cast to another data type
```python
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
```
## Machine Learning

Function/Method | Description
--- | ---
`StringIndexer(inputCol='categorical_col', outputCol='index_col')` <br>`OneHotEncoder(inputCol='index_col', outputCol='result_col')` | `StringIndexer` and `OneHotEncoder` are each required to convert string to numeric data
`VectorAssembler(input_cols=['col1', 'col2'], outputCol='feature_col')` | Spark modeliling requires data to be assembled into a single column


### Transforming categorical to numeric data
```python
# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")
```
### Assemble a vector

```python
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")
```