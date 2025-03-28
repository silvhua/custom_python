# Node & nvm
[Node.js on WSL](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl#install-nvm-nodejs-and-npm)

Command | Description | Notes
--- | ---- | ---
`node --version` | Verify that Node.js is installed and the current default version
`nvm ls` | List the versions of node currently installed
`nvm use node` | switch to the Current version
`nvm use --lts` | switch to the LTS version.
`nvm use v14.21.3` | Switch to that version
`nvm ls-remote` | List all versions of Node available. 

# [Git Workflow](https://data.compass.lighthouselabs.ca/days/w01d1/activities/149)

Terminal commands (steps in bold are required each time to update a file)
* `mkdir <folder name>` # to create a new folder
* `git clone git@github.com:YOUR_USER_NAME/lighthouse-data-notes.git` to clone a repo
* `git init` to initialize a new Git repo in the current directory
* `git remote add origin <URL of repo>` to add new repo as a remote of  your local repo if not yet created
* **`git add <item>` to add the item to the repository** 
    * OR `git rm --cached -r <filename>` to remove item from remote repo without changing it on computer
* **`git commit -m "<comments>`** 
* **`git push -u origin master` to push changes to GitHub (main branch has since been updated to `main`)**

Description | Function/Method | Imports
--- | ---- | ---
See which branch you are on | `git branch` | The branch with an asterisk (*) next to it is your current branch.
Create a new branch | `git branch new-branch-name`
Switch to a given branch | `git checkout branch-name`
Create a new branch and switch to it | `git checkout -b new-branch-name` | This is a combination of `git branch` and `git checkout`

# DataCamp SQL for Data Analysis

Function/Method | Description
--- | ---
`COALESCE` | For each row, return the first non-null value.
`CAST(value AS new_type)` or <br>`value::new_type` | Convert from one data type to another in the query.
`STDDEV()` | Standard deviation.
`TRUNC(number, integer)` | Truncate values to the precision indicated by the integer. Positive integer indicates number of decimal places to keep. Negative integer indicates places before decimal to replace with zero.
`GENERATE_SERIES(start number, end number, step)` |
`round(column_name::numeric, decimal_places)`

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

## Tempororary Tables

Function/Method | Description
--- | ----
`DROP TABLE IF EXISTS` | Clear a temporary table if it exists.
`CREATE TEMP TABLE table_name AS SELECT ...` | Create a new temporary table
`SELECT 'custom_string_as_row_value'::varchar AS column_name` | Create a row with a custom string

### Correlation table

```sql
DROP TABLE IF EXISTS correlations;

CREATE TEMP TABLE correlations AS
SELECT 'profits'::varchar AS measure,
       corr(profits, profits) AS profits,
       corr(profits, profits_change) AS profits_change,
       corr(profits, revenues_change) AS revenues_change
  FROM fortune500;

INSERT INTO correlations
SELECT 'profits_change'::varchar AS measure,
       corr(profits_change, profits) AS profits,
       corr(profits_change, profits_change) AS profits_change,
       corr(profits_change, revenues_change) AS revenues_change
  FROM fortune500;

INSERT INTO correlations
SELECT 'revenues_change'::varchar AS measure,
       corr(revenues_change, profits) AS profits,
       corr(revenues_change, profits_change) AS profits_change,
       corr(revenues_change, revenues_change) AS revenues_change
  FROM fortune500;

-- Select each column, rounding the correlations
SELECT measure, 
       round(profits::numeric, 2) AS profits,
       round(profits_change::numeric, 2) AS profits_change,
       round(revenues_change::numeric, 2) AS revenues_change
  FROM correlations;
```
#### Result
| measure | profits | profits_change | revenues_change |
| --- | --- | --- | --- |
| profits | 1.00 | 0.02 | 0.02 |
| profits_change | 0.02 | 1.00 | -0.09 |
| revenues_change | 0.02 | -0.09 | 1.00 |

## Exploring categorical data and unstructured text

Function/Method | Description 
--- | ---
`lower('String')` | Convert to lower case
`upper('String')` | Convert to upper case
`trim(' string ')` | Remove spaces at start and end
`trim('string!', '<characters_to_trim>')` | Trim the specified characters. This can include multiple characters and any of those characters will be trimmed.
`rtrim('string ')` | Remove spaces at right end
`ltrim(' string')` | Remove spaces at left end

## Splitting and concatenating text

Function/Method | Description | Example
--- | --- | ---
`left('string', n_characters)` <br>`right('string', n_characters)` | Get the specified number of characters on the very left/right of the string. | `SELECT left('abcde', 2)` <br>--> Gets the first 2 characters to return `ab`
`substring('string' FROM start_position FOR character_length)` <br>OR<br> `substr('string', start_position, character_length)` | Get a substring. Position index starts at 1. | `SELECT substring('abcdef' FROM 2 FOR 3)` <br>OR<br> `substr('abcdef', 2, 3)` <br>--> Returns `bcd`
`split_part(string, delimiter, part)` | Split text on a delimiter. | `SELECT split_part('a,bc,d', ',', 2)` <br>--> `bc` <br>`SELECT split_part('cats and dogs and fish', ' and ', 1)` <br> --> `cats`
`SELECT concat('string1', joining_character, 'string2')` <br>OR <br> `SELECT 'string1' // joining_character // 'string2'` | **REPLACE `//` WITH 2 PIPE SYMBOLS**. Concatenate strings and join them with the specified joining character. | `SELECT concat('a', 2, 'cc')` <br>OR <br> `SELECT 'a' // 2 // 'cc'` <br>--> `a2cc`

## Multiple transformations
[See chapter 3 slides p. 27](../../../data%20and%20tech%20ed/DataCamp%20EDA%20in%20SQL/chapter3.pdf)

Example of how get the string before 3 possible delimiters: colon, hypthen, and pipe.
### Option 1: `CASE WHEN`
```sql
SELECT CASE WHEN category LIKE '%: %' THEN split_part(category, ': ' , 1)
    WHEN category LIKE '% - %' THEN split_part(category, '-', 1)
    ELSE split_part(category, ' | ', 1)
  END AS major_category, -- alias the result
  sum(businesses) -- also select number of businesses
FROM naics
GROUP BY major_category; -- Group by categories created above
```
### Option 2: Create a temp table and join it to the original table.
**Step 1**: 

Create a temp table with 1 column with the original values, a 2nd column with a placeholderfor the standardized values.
```sql
CREATE TEMP TABLE recode AS 
SELECT DISTINCT fav_fruit AS original, -- original, messy values
  fav_fruit AS standardized -- new standardized values
FROM fruit;
```
**Step 2**: Update table values.

Basic syntax: 
```sql
UPDATE table_name
    SET column_name = new_value 
  WHERE condition;
```

The `UPDATE` code block can be repeated multiple times based on the  number of transformation types needed.

**Step 3**: JOIN original and recode tables
```sql
SELECT standardized,
    count(*)
  FROM fruit
    LEFT JOIN recode
    ON fav_fruit=original
  GROUP BY standardized
```
## Chapter 4: Date/time types and formats
Data type | Format(s) | Example
--- | --- | ---
date
timestamp | ISO 860: YYYY-MM-DD HH:MM:SS<br>with timezone: YYYY-MM-DD HH:MM:SS+HH | `2018-01-05 09`<br> `2004-10-19 10:23:54+02`
interval | | `6 days 01:48:08`<br>`00:51:03`

`SELECT ...` | Description | Example
--- | ---- | ---
`SELECT '2018-01-01' > '2017-12-31'` | Date comparison can be done with `>`, `<`, `=`
`now()` | Current timestamp
`SELECT now() -'2018-01-01'` | Subtract dates to get an `interval`
`'2023-10-15'::date` | Convert string to date
`'2023-10-15'::date + 1` | Date plus 1 day
`'2023-10-15'::date + '1 year'::interval` | Date plus 1 year
`SELECT '2018-12-10'::date + '1 year 2 days 3 minutes'::interval`

### Commmon date/time fields
* `century`: 2019-01-01 = century 21
* `decade`: 2019-01-01 = decade 201
* `year`, `month`, `day`
* `hour`, `minute`, `second`
* `week`
* `dow`: day of week

Description | `SELECT ...` | Example
--- | ---- | ---
Extract a given date/time field | `date_part('field', timestamp)` | `SELECT date_part('month', now()), EXTRACT(MONTH FROM now());`
. | `EXTRACT(FIELD FROM timestamp)` | 
Truncate a date/time to a given field | `date_trunc('field', timestamp)` | `SELECT date_trunc('month', now());`
Get the day of the week | `to_char(timestamp, 'day')`

### Aggregating with date/time series
Description | `SELECT ...` | Example
--- | ---- | ---
Generate a time series column | `SELECT generate_series(from, to, interval);` | `SELECT generate_series('2018-01-01','2018-01-15','2 days'::interval);` 


To generate a series with the last day of each month:
1. Generate the series with the first day of the month.
2. Subtract 1 day.

#### Aggregation with series
Generate a series, then join with the data.
```sql
-- Create the series as a table called hour_series
WITH hour_series AS (
  SELECT generate_series('2018-04-23 09:00:00',-- 9am
    '2018-04-23 14:00:00',-- 2pm
    '1 hour'::interval) AS hours)
-- Hours from series, count date (NOT *) to count non-NULL
SELECT hours, count(date)
  -- Join series to sales data
  FROM hour_series
    LEFT JOIN sales
      ON hours=date_trunc('hour', date)
  GROUP BY hours
  ORDER BY hours;
```
#### Aggregation with bins
Create a series for the upper boundary and a series for the lower boundary, then join with the data.
```sql
-- Create bins
WITH bins AS (
  SELECT generate_series('2018-04-23 09:00:00',
      '2018-04-23 15:00:00',
      '3 hours'::interval) AS lower,
    generate_series('2018-04-23 12:00:00',
    '2018-04-23 18:00:00',
    '3 hours'::interval) AS upper)
-- Count values in each bin
SELECT lower, upper, count(date)
-- left join keeps all bins
  FROM bins
    LEFT JOIN sales
      ON date >= lower
      AND date < upper
-- Group by bin bounds to create the groups
GROUP BY lower, upper
ORDER BY lower;
```

#### Time between events
Description | `SELECT ...` | Example
--- | ---- | ---
Shift time series 1 row down | `lag(column_to_adjust) OVER (ORDER BY ordering_column)` | `lag(date) OVER (ORDER BY date)`
Shift time series 1 row up | `lead(column_to_adjust) OVER (ORDER BY ordering_column)`

| Example: Calculate time between events
```sql
SELECT date,
    date - lag(date) OVER (ORDER BY date) AS gap
  FROM sales;
```

| Example: Calculate average time between events
```sql
SELECT avg(gap)
    FROM (SELECT date - lag(date) OVER (ORDER BY date) AS gap
      FROM sales) AS gaps;
```

| Example: Calculate change in a time series
```sql
SELECT date,
  amount,
  lag(amount) OVER (ORDER BY date),
  amount - lag(amount) OVER (ORDER BY date) AS change
FROM sales;
```

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
Remove containers | `docker container prune -f`
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
`.findIndex()` | return the index of the first element that evaluates to true in the callback function.
`array.reduce((accumulator, currentValue, index, array) => {...}, initialValue)` | returns a single value after iterating through the elements of an array, thereby reducing the array. [documentation](https://www.codecademy.com/resources/docs/javascript/arrays/reduce?page_ref=catalog)
`.some(callback_function)` | returns `true` if at least one element in the array passes a test.

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
`.forEach()`
```javascript
const numbers = [1, 2, 4, 10];

const summedNums = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue
}, 100)  // <- Second argument for .reduce()

console.log(summedNums); // Output: 117
```
## Methods

We can include methods in our object literals by creating ordinary, colon-separated key-value pairs. The key serves as our method’s name, while the value is an anonymous function expression.
```javascript
const alienShip = {
  invade: function () { 
    console.log('Hello! We have come to dominate your planet. Instead of Earth, it shall be called New Xaculon.')
  }
};
```
With the new method syntax introduced in ES6 we can omit the colon and the function keyword.
```javascript
const alienShip = {
  invade () { 
    console.log('Hello! We have come to dominate your planet. Instead of Earth, it shall be called New Xaculon.')
  }
};
```
Object methods are invoked by appending the object’s name with the dot operator followed by the method name and parentheses:
```javascript
alienShip.invade(); // Prints 'Hello! We have come to dominate your planet. Instead of Earth, it shall be called New Xaculon.'
```
Methods can be added to an object the same way as adding properties.
```javascript
const alienShip = {
  retreat () {
    console.log(retreatMessage)
  }
}
alienShip.takeOff = function () {
  console.log('Spim... Borp... Glix... Blastoff!')
}
```

## Looping through objects
```JavaScript
let spaceship = {
  crew: {
    captain: { 
      name: 'Lily', 
      degree: 'Computer Engineering', 
      cheerTeam() { console.log('You got this!') } 
    },
    'chief officer': { 
      name: 'Dan', 
      degree: 'Aerospace Engineering', 
      agree() { console.log('I agree, captain!') } 
    },
    medic: { 
      name: 'Clementine', 
      degree: 'Physics', 
      announce() { console.log(`Jets on!`) } },
    translator: {
      name: 'Shauna', 
      degree: 'Conservation Science', 
      powerFuel() { console.log('The tank is full!') } 
    }
  }
}; 

// for...in
for (let crewMember in spaceship.crew) {
  console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`);
}
```
Our `for...in` will iterate through each element of the `spaceship.crew` object. In each iteration, the variable `crewMember` is set to one of `spaceship.crew`'s keys, enabling us to log a list of crew members’ role and name.

## Getters
Getters are methods that get and return the internal properties of an object. 
```JavaScript
const person = {
  _firstName: 'John',
  _lastName: 'Doe',
  get fullName() {
    if (this._firstName && this._lastName){
      return `${this._firstName} ${this._lastName}`;
    } else {
      return 'Missing a first name or a last name.';
    }
  }
}

// To call the getter method: 
person.fullName; // 'John Doe'
```
## Setters
```JavaScript
const person = {
  _age: 37,
  set age(newAge){
    if (typeof newAge === 'number'){
      this._age = newAge;
    } else {
      console.log('You must assign a number to age');
    }
  }
};

// To call the setter method:
person.age = 40;
console.log(person._age); // Logs: 40
person.age = '40'; // Logs: You must assign a number to age
```
## Factory functions
```JavaScript
const monsterFactory = (name, age, energySource, catchPhrase) => {
  return { 
    name: name,
    age: age, 
    energySource: energySource,
    scare() {
      console.log(catchPhrase);
    } 
  }
};
```

### Property value short hand

```JavaScript
const monsterFactory = (name, age) => {
  return { 
    name: name,
    age: age
  }
};
```
Equivalent:
```JavaScript
const monsterFactory = (name, age) => {
  return { 
    name,
    age 
  }
};
```
### Desctructured Assignment
Useful when creating a new variable that is a property of an object.
```JavaScript
const vampire = {
  name: 'Dracula',
  residence: 'Transylvania',
  preferences: {
    day: 'stay inside',
    night: 'satisfy appetite'
  }
};

const residence = vampire.residence; 
console.log(residence); // Prints 'Transylvania' 

// Equivalent short hand:
const { residence } = vampire; 
console.log(residence); // Prints 'Transylvania'

// Extracting a nested property:
const { day } = vampire.preferences; 
console.log(day); // Prints 'stay inside'
```

## Built-in Object Methods
[MDN’s object instance documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#Methods)

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
                print("[Extract] First row | example:", row)

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
`df.select("User").distinct()` | | `SELECT DISTINCT`
`df.select("column1/60").alias("new_column_name")` <br>`df.selectExpr("column AS alias")` | Give the column a name | `AS`
`.groupby().min("column_name")` <br>`.groupby().max("column_name")` <br>`.groupby("groupby_column").avg("column_name")` <br>`.groupby("groupby_column1", "groupby_column2").sum("column_name")` | Aggregate function. `.groupby()` does not need arguments. | `GROUP BY`
`.agg(F.stddev("dep_delay"))` | Aggregate using the passed function. Required import: <br>`import pyspark.sql.functions as F` | `GROUP BY`
`table1.join(table2, on="common_column", how="leftouter")` | Join tables | `LEFT JOIN`
`df.printSchema()` | Show the data types
`df.withColumn("column_name", df.column_name.cast("integer"))`  | Create new df with the column as integer data type | `CAST`
`df.withColumn("column_name", df.column_name.cast("double"))` | Create new df with the column as float data type | `CAST`
`df.sort("column_name", ascending = False)` | `ORDER BY column_name DESC`
 
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
```python
# Import the requisite packages
from pyspark.sql.functions import col

# Filter to show only userIds less than 100
ratings.filter(col("userId") < 100).show()

# Equivalent
ratings.filter(ratings.userId < 100).show()
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
`index_step = StringIndexer(inputCol='categorical_col', outputCol='index_col')` <br>`one_hot_step = OneHotEncoder(inputCol='index_col', outputCol='result_col')` | `StringIndexer` and `OneHotEncoder` are each required to convert string to numeric data
`vector_step = VectorAssembler(input_cols=['col1', 'col2'], outputCol='feature_col')` | Spark modeliling requires data to be assembled into a single column
`model_pipe = Pipeline(stages=[step1,step2, step3])` | Create an object that calls several methods on the dataframe in sequence.
`piped_data = model_pipe.fit(model_data).transform(model_data)` | Transform the model data. This should be done before splitting into train-test sets.
`train_data, test_data = piped_data.randomSplit([0.6, 0.4])` | Split the transformed data into train set and test set. The first number represents the % of data for the train set.

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
### Pipeline
```python
# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])

# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)

# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])
```
### Train-test split
```python
training, test = piped_data.randomSplit([0.6, 0.4])
```

### Logistic regression

```python
# Import LogisticRegression
from pyspark.ml.classification import LogisticRegression

# Create a LogisticRegression Estimator
lr = LogisticRegression()
```

### Model evaluation
```python
# Import the evaluation submodule
import pyspark.ml.evaluation as evals

# Create a BinaryClassificationEvaluator
evaluator = evals.BinaryClassificationEvaluator("areaUnderROC")
```
### Grid search for hyperparameter tuning
```python
# Import the tuning submodule
import pyspark.ml.tuning as tune

# Create the parameter grid
grid = tune.ParamGridBuilder()

# Add the hyperparameter
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01)) # This second call is a function from the numpy module (imported as np) that creates a list of numbers from 0 to .1, incrementing by .01.
grid = grid.addGrid(lr.elasticNetParam, [0, 1])

# Build the grid
grid = grid.build()
```

The submodule pyspark.ml.tuning also has a class called `CrossValidator` for performing cross validation. This `Estimator` takes the modeler you want to fit, the grid of hyperparameters you created, and the evaluator you want to use to compare your models.

```python
# Create the CrossValidator
cv = tune.CrossValidator(estimator=lr,
               estimatorParamMaps=grid,
               evaluator=evaluator
               )

# Fit cross validation models
models = cv.fit(training)

# Extract the best model
best_lr = models.bestModel
```
Cross validation selected the parameter values regParam=0 and elasticNetParam=0 as being the best. These are the default values, so you don't need to do anything else with lr before fitting the model.
```python
# Call lr.fit()
best_lr = lr.fit(training)

# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))
```
# DataCamp: Building Recommender Systems in Python
## Chapter 2

Reshape the ratings matrix
```python
# Import monotonically_increasing_id and show R
from pyspark.sql.functions import monotonically_increasing_id
# Use the to_long() user-defined function to convert the dataframe to the "long" format.
ratings = to_long(R)
ratings.show()

# Get unique users and repartition to 1 partition
users = ratings.select("User").distinct().coalesce(1)

# # Create a new column of unique integers called "userId" in the users dataframe.
users = users.withColumn("userId", monotonically_increasing_id()).persist()
users.show()

# Import monotonically_increasing_id and show R
from pyspark.sql.functions import monotonically_increasing_id
R.show()

# Use the to_long() function to convert the dataframe to the "long" format.
ratings = to_long(R)
ratings.show()

# Get unique users and repartition to 1 partition
users = ratings.select("User").distinct().coalesce(1)
```
Convert strings to integers 
```python
# # Create a new column of unique integers called "userId" in the users dataframe.
users = users.withColumn("userId", monotonically_increasing_id()).persist()
users.show()

# Extract the distinct movie id's
movies = ratings.select("Movie").distinct() 

# Repartition the data to have only one partition.
movies = movies.coalesce(1) 

# Create a new column of movieId integers. 
movies = movies.withColumn("Movie", monotonically_increasing_id()).persist() 

# Join the ratings, users and movies dataframes
movie_ratings = ratings.join(users, "User", "left").join(movies, "Movie", "left")
movie_ratings.show()
```
Train the model and make predictions
```python
# Split the ratings dataframe into training and test data
(training_data, test_data) = ratings.randomSplit([0.8, 0.2], seed=42)

# Set the ALS hyperparameters
from pyspark.ml.recommendation import ALS
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", rank =10, maxIter =15, regParam =0.1,
          coldStartStrategy="drop", nonnegative =True, implicitPrefs = False)

# Fit the mdoel to the training_data
model = als.fit(training_data)

# Generate predictions on the test_data
test_predictions = model.transform(test_data)
test_predictions.show()
```
Evaluate the model with RMSE
```python
# Import RegressionEvaluator
from pyspark.ml.evaluation import RegressionEvaluator

# Complete the evaluator code
evaluator = RegressionEvaluator(metricName="rmse", labelCol="ratings", predictionCol="prediction")

# Extract the 3 parameters
print(evaluator.getMetricName())
print(evaluator.getLabelCol())
print(evaluator.getPredictionCol())

# Evaluate the "test_predictions" dataframe
RMSE = evaluator.evaluate(test_predictions)
```
## MovieLens dataset
Calculate sparsity
```python
# Count the total number of ratings in the dataset
numerator = ratings.select("Rating").count()

# Count the number of distinct userIds and distinct movieIds
num_users = ratings.select("userId").distinct().count()
num_movies = ratings.select("movieId").distinct().count()

# Set the denominator equal to the number of users multiplied by the number of movies
denominator = num_users * num_movies

# Divide the numerator by the denominator
sparsity = (1.0 - (numerator *1.0)/denominator)*100
print("The ratings dataframe is ", "%.2f" % sparsity + "% empty.")
```
Filter and aggregate
```python
# Import the requisite packages
from pyspark.sql.functions import col

# Filter to show only userIds less than 100
ratings.filter(col("userId") < 100).show()

# Group data by userId, count ratings
ratings.groupBy("userId").count().show()

# Min num ratings for movies
print("Movie with the fewest ratings: ")
ratings.groupBy("movieId").count().select(min("count")).show()

# Avg num ratings per movie
print("Avg num ratings per movie: ")
ratings.groupBy("movieId").count().select(avg("count")).show()

# Min num ratings for user
print("User with the fewest ratings: ")
ratings.groupBy("userId").count().select(min("count")).show()

# Avg num ratings per users
print("Avg num ratings per user: ")
ratings.groupBy("userId").count().select(avg("count")).show()
```
Convert the data types
```python
# Use .printSchema() to see the datatypes of the ratings dataset
ratings.printSchema()

# Tell Spark to convert the columns to the proper data types
ratings = ratings.select(ratings.userId.cast("integer"), ratings.movieId.cast("integer"), ratings.rating.cast("double"))

# Call .printSchema() again to confirm the columns are now in the correct format
ratings.printSchema()
```
### Build the model and evaluate it
```python
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Create test and train set
(train, test) = ratings.randomSplit([0.8, 0.2], seed = 1234)

# Create ALS model
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", nonnegative = True, implicitPrefs = False)
# Add hyperparameters and their respective values to param_grid
param_grid = ParamGridBuilder() \
            .addGrid(als.rank, [10, 50, 100, 150]) \
            .addGrid(als.maxIter, [5, 50, 100, 200]) \
            .addGrid(als.regParam, [.01, .05, .1, .15]) \
            .build()
           
# Define evaluator as RMSE and print length of evaluator
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction") 
print ("Num models to be tested: ", len(param_grid))

# Build cross validation using CrossValidator
cv = CrossValidator(estimator=als, estimatorParamMaps=param_grid, evaluator=evaluator, numFolds=5)

#Fit cross validator to the 'train' dataset
model = cv.fit(train)

#Extract best model from the cv model above
best_model = model.bestModel

# Print "Rank"
print("  Rank:", best_model.getRank())

# Print "MaxIter"
print("  MaxIter:", best_model.getMaxIter())

# Print "RegParam"
print("  RegParam:", best_model.getRegParam())
```
Make predictions and evaluate results
```python
test_predictions = best_model.transform(test)

# Calculate and print the RMSE of test_predictions
RMSE = evaluator.evaluate(test_predictions)
```
### Getting recommendations
```python
# Look at user 60's ratings
print("User 60's Ratings:")
original_ratings.filter(col("userId") == 60).sort("rating", ascending = False).show()

# Look at the movies recommended to user 60
print("User 60s Recommendations:")
recommendations.filter(col("userId") == 60).show()
```
[See chapter 3 slides: "Cleaning up recommendation output"](../../z%20resources/DataCamp%20Building%20Recommendation%20Engines%20in%20Pyspark/chapter3%20Intro%20to%20the%20MovieLens%20dataset.pdf)

## Implicit Ratings
```python
# Min num implicit ratings for a song
print("Minimum implicit ratings for a song: ")
msd.filter(col("num_plays") > 0).groupBy("songId").count().select(min("count")).show()

# Avg num implicit ratings per songs
print("Average implicit ratings per song: ")
msd.filter(col("num_plays") > 0).groupBy("songId").count().select(avg("count")).show()

# Min num implicit ratings from a user
print("Minimum implicit ratings from a user: ")
msd.filter(col("num_plays") > 0).groupBy("userId").count().select(min("count")).show()

# Avg num implicit ratings for users
print("Average implicit ratings per user: ")
msd.filter(col("num_plays") > 0).groupBy("userId").count().select(avg("count")).show()
```
Get implicit ratings from number of purchases per product for each customer.
```python
# View the data
Z.show()

# Extract distinct userIds and productIds
users = Z.select("userId").distinct()
products = Z.select("productId").distinct()

# Cross join users and products
cj = users.crossJoin(products)

# Join cj and Z
Z_expanded = cj.join(Z, ["userId", "productId"], "left").fillna(0)

# View Z_expanded
Z_expanded.show()
```
This is what Z_expanded dataframe looks like
```python
    +------+---------+-------------+
    |userId|productId|num_purchases|
    +------+---------+-------------+
    |    22|       44|            0|
    |    22|      777|            0|
    |    22|     1811|           96|
    |    22|      227|            0|
    |    22|     1662|            0|
    |    22|     1492|            0|
    |    22|     2390|            0|
    |    22|     1981|            0|
    |   686|       44|            0|
    |   686|      777|            0|
    |   686|     1811|            0|
    |   686|      227|            0|
    |   686|     1662|            0|
    |   686|     1492|            0|
    |   686|     2390|            0|
    |   686|     1981|            2|
    |    13|       44|            0|
    |    13|      777|            0|
    |    13|     1811|            0|
    |    13|      227|            0|
    +------+---------+-------------+
```


Build a model
```python
ranks = [10, 20, 30, 40]
maxIters = [10, 20, 30, 40]
regParams = [.05, .1, .15]
alphas = [20, 40, 60, 80]

# For loop will automatically create and store ALS models
for r in ranks:
    for mi in maxIters:
        for rp in regParams:
            for a in alphas:
                model_list.append(ALS(userCol= "userId", itemCol= "songId", ratingCol= "num_plays", rank = r, maxIter = mi, regParam = rp, alpha = a, coldStartStrategy="drop", nonnegative = True, implicitPrefs = True))

# Print the model list, and the length of model_list
print (model_list, "Length of model_list: ", len(model_list))
```
### Cross-validating implicit ratings
PySpark does not have built-in cross-validation methods for evaluating implicit ALS models.
Rank ordering error metric (ROEM) can be used to evaluate the model for implicity ratings. The higher the ROEM, the poorer the predictions.
`np*rank` = `num_plays` * `rank`

```python
numerator = bp.groupBy().sum("np*rank").collect()[0][0]
denominator = bp.groupBy().sum("num_plays").collect()[0][0]
print ("ROEM: "), numerator * 1.0/ denominator
```

```python
# Split the data into training and test sets
(training, test) = msd.randomSplit([0.8, 0.2])

#Building 5 folds within the training set.
train1, train2, train3, train4, train5 = training.randomSplit([0.2, 0.2, 0.2, 0.2, 0.2], seed = 1)
fold1 = train2.union(train3).union(train4).union(train5)
fold2 = train3.union(train4).union(train5).union(train1)
fold3 = train4.union(train5).union(train1).union(train2)
fold4 = train5.union(train1).union(train2).union(train3)
fold5 = train1.union(train2).union(train3).union(train4)

foldlist = [(fold1, train1), (fold2, train2), (fold3, train3), (fold4, train4), (fold5, train5)]

# Empty list to fill with ROEMs from each model
ROEMS = []

# Loops through all models and all folds
for model in model_list:
    for ft_pair in foldlist:

        # Fits model to fold within training data
        fitted_model = model.fit(ft_pair[0])

        # Generates predictions using fitted_model on respective CV test data
        predictions = fitted_model.transform(ft_pair[1])

        # Generates and prints a ROEM metric CV test data
        r = ROEM(predictions)
        print ("ROEM: ", r)

    # Fits model to all of training data and generates preds for test data
    v_fitted_model = model.fit(training)
    v_predictions = v_fitted_model.transform(test)
    v_ROEM = ROEM(v_predictions) # `ROEM()` is a user-defined function provided by the DataCamp course

    # Adds validation ROEM to ROEM list
    ROEMS.append(v_ROEM)
    print ("Validation ROEM: ", v_ROEM)

import numpy

# Find the index of the smallest ROEM
i = numpy.argmin(ROEMS)
print("Index of smallest ROEM:", i)

# Find ith element of ROEMS
print("Smallest ROEM: ", ROEMS[i])
```
Extract best model hyperparameters
* Assume model 38 of index 38 is the best model
```python
# Extract the best_model
best_model = model_list[38]

# Extract the Rank
print ("Rank: ", best_model.getRank())

# Extract the MaxIter value
print ("MaxIter: ", best_model.getMaxIter())

# Extract the RegParam value
print ("RegParam: ", best_model.getRegParam())

# Extract the Alpha value
print ("Alpha: ", best_model.getAlpha())
```
# CloudWolf AWS
## EC2
Task | Command | Note
--- | ---- | ---
`aws s3 ls` | List s3 buckets
`aws s3 ls s3://s3_bucket_name` | List contents of the named s3 bucket


# AWS Serverless Application Model

Description | AWS SAM CLI command | Notes
--- | --- | ---
scaffold a new project | `sam init`
invoke a Lambda function locally | `sam local invoke LambdaResourceName --event path/event.json`
run a Serverless app locally by running a local HTTP server that simulates API Gateway | 1. Run Docker desktop. <br>2. `cd` to project root folder. <br>3. `sam local start-api --port 8080` <br>
Run a pytest unit test | `pip3 install pytest pytest-mock`<br>`python3 -m pytest tests/unit`
Build a SAM project | [`cd` to root folder] <br>`sam build` | This command iterates through the functions in your application, looking for the manifest file (such as requirements.txt, package.json or pom.xml) that contain dependencies, and automatically creates deployment artifacts. 
Deploy the project. | `sam deploy` | Append the `--guided` flag to deploy in guided mode. It is recommended to deploy with guided mode for the first time as it will capture the configuration for future deployments in a new file samconfig.toml described at the end of this section. 
Delete an application | `sam delete`
create a new CodeCommit repository | `aws codecommit create-repository --repository-name sam-app`
Configure the git client with username and email | `git config --global user.name "your name"` <br>`git config --global user.email "your_email@example.com"`
Add your CodeCommit repository URL as a remote on your local git project. | `git remote add origin codecommit://sam-app` | If you mis-typed the origin url, you can remove it by running: `git remote rm origin`. `origin` is the name of the remote and can be renamed.
Push the code | `git push -u origin main`
check repository status | `git status`


## Inititialize Git repository
```shell
cd ~/environment/sam-app
git init -b main
echo -e "\n\n.aws-sam" >> .gitignore
echo -e "target" >> .gitignore
echo -e "samconfig.toml" >> .gitignore
git add .
git commit -m "Initial commit"

```

## [Creating the SAM Pipeline](https://catalog.workshops.aws/complete-aws-sam/en-US/module-4-cicd/module-4-cicd-gh/50-sampipeinit)

Step | Description | Imports
--- | ---- | ---
(1) Create the dev stage of the pipeline | `sam pipeline bootstrap --stage dev` | Make sure to be in the project directory
(2) Create the prod stage of the pipeline | `sam pipeline bootstrap --stage prod`
(3) Create GitHub Actions Workflow | `sam pipeline init`

## Deploy Pipeline template
```shell
cd ~/environment/sam-app
git add .
git commit -m "Adding SAM CI/CD Pipeline definition"
git push
```
Now that the configuration is checked into source control, you can create a new CloudFormation stack which will set up our CI/CD pipeline. 
* You will use the `sam deploy` command to launch this new stack. 
* It's important to recognize that you're using SAM's ability to launch arbitrary CloudFormation templates. SAM isn't building or deploying your serverless application here, rather launching the codepipeline.yaml CI/CD template.

```shell
sam deploy -t codepipeline.yaml --stack-name sam-app-pipeline --capabilities=CAPABILITY_IAM
```

## SAM Accelerate

Step | Function/Method | Imports
--- | ---- | ---
start SAM Accelerate |  `sam sync --watch --stack-name sam-app` | Navigate to where the `template.yaml` file for the application is first. Respond with Y if prompted to confirm that you want to use the preview feature. 
Test your application and check the logs | `sam logs --tail --stack-name sam-app`


The first time that you run the `sync --watch` command, AWS SAM starts an AWS CloudFormation deployment to get your function and associated resources into your AWS environment. After the deployment, AWS SAM Accelerate watches for changes to your serverless application and determines whether to use service APIs or CloudFormation based on the resource type.

* With the `sync --watch` process running, update your local Lambda function code.
* SAM Accelerate isn't only limited to Lambda code changes, it can also automate deployment of infrastructure changes in `template.yaml` through CloudFormation.

Output from `sam logs --tail --stack-name sam-app`:
```

(aws) C:\Users\silvh\OneDrive\lighthouse\portfolio-projects\sam-app>sam logs --tail --stack-name sam-app
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:35:24.685000 INIT_START Runtime Version: python:3.7.v39      Runtime Version ARN: arn:aws:lambda:us-west-2::runtime:7bc09ef0e805b878ecacb74a4b25c1f9563f44b1849c0216b7a543b7307ff1bb
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:35:24.801000 START RequestId: a7c2bcdf-7093-4763-8a2c-81617073df9b Version: $LATEST
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:35:24.802000 Change deployed with SAM Accelerate, attempt 2
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:35:24.816000 END RequestId: a7c2bcdf-7093-4763-8a2c-81617073df9b
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:35:24.816000 REPORT RequestId: a7c2bcdf-7093-4763-8a2c-81617073df9b  Duration: 14.45 ms      Billed Duration: 15 ms  Memory Size: 128 MB     Max Memory Used: 36 MB  Init Duration: 115.61 ms
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:37:06.990000 START RequestId: f89dc5ec-42dc-44d7-989b-b48cf72e309c Version: $LATEST
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:37:06.990000 Change deployed with SAM Accelerate, attempt 2
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:37:06.992000 END RequestId: f89dc5ec-42dc-44d7-989b-b48cf72e309c
2023/12/04/[$LATEST]871416c7625c401280ad2d1cc7467d99 2023-12-04T20:37:06.992000 REPORT RequestId: f89dc5ec-42dc-44d7-989b-b48cf72e309c  Duration: 1.81 ms       Billed Duration: 2 ms   Memory Size: 128 MB     Max Memory Used: 36 MB

```

## [Look at module 7 on Managing Permissions](https://catalog.workshops.aws/complete-aws-sam/en-US/module-7-permissions)

# Django
Task | Command | Notes
--- | --- | ---
Intialize a project | `django-admin startproject mysite` | Creates a new folder `mysite` in the current directory.  
Start the Django development server. | `python manage.py runserver` | By default, the runserver command starts the development server on the internal IP at port 8000. If you want to change the server’s port, pass it as a command-line argument. e.g. `python manage.py runserver 8080`
Create a new app | `python manage.py startapp app_name` | Generates the basic directory structure of an app in a directory called `app_name`.
Create the required tables in the database. | `python manage.py migrate`
Tell Django that you've made changes to your models and that you'd like changes to be stored as a migration. | `python manage.py makemigrations polls`
See the SQL that migration would run based on the file creted by the `makemigration` command | `python manage.py sqlmigrate polls 0001` | After this step, run `python manage.py migrate` again to apply the migration (e.g. generate new tables)
Create admin user | `python manage.py createsuperuser`

# Codecademy: Learn C#

Terminal Command | Description | Notes
--- | ---- | ---
`dotnet run` | Run interactive code
`dotnet new console -n ProjectName` |
`dotnet --list-sdks` | List available SDKs

Function | Description | Notes
--- | ---- | ---
`Console.WriteLine("Hello world")` | Print to console
`Console.Write("Message to user")` | Prompt the user.
`Console.ReadLine()` | Capture text that a user types into the console.
`Math.Abs()` | find the absolute value of a number. | Example: Math.Abs(-5) returns 5.
`Math.Sqrt()` | find the square root of a number. | Example: Math.Sqrt(16) returns 4.
`Math.Floor()` | round the given double or decimal down to the nearest whole number. | Example: Math.Floor(8.65) returns 8.
`Math.Min()` | returns the smaller of two numbers. | Example: Math.Min(39, 12) returns 12.
`Math.Pow()`
`Math.Max()`
`Math.Ceiling()`

```csharp
Console.Write("Please provide your input");
string input = Console.ReadLine(); // capture the text typed into the console.
```

## String interpolation
```C#
int id = 100

// We can use an expression with a string interpolation.
string multipliedNumber = $"The multiplied ID is {id * 10}.";

Console.WriteLine(multipliedNumber);
```

## Arrays
```csharp
int[] plantHeights;

// define and initialize an array at the same time
int[] plantHeights = { 3, 4, 6 };

// `new` signifies instantiation of a new array
int[] plantHeights = new int[] { 3, 4, 6 };

// declare an array and then initialize it later
int[] plantHeights;
plantHeights = new int[] { 3, 4, 6 };   

//  initialize an array that has a length of 3 without specifying what those values are
// plantHeights will be equal to [0, 0, 0]
int[] plantHeights = new int[3]; 
```

### Array methods
Command | Description | Notes
--- | ---- | ---
`Array.Sort(array)` | Done in place.
`Array.IndexOf(array, element)` | Find the index of an element in the array | If the value appears more than once in an array, it returns only the index of the first occurrence within the specified range. If it does not find the value at all, it returns `-1`.
 `Array.Reverse(array)` | Returns the array with the original elements in reverse order. | Done in place.

Check if an element exists in an array:
```csharp
int[] numbers = { 1, 2, 3, 4, 5 };
int valueToCheck = 3;

bool exists = Array.Exists(numbers, element => element == valueToCheck);

Console.WriteLine(exists);  // Output: True

```

## Loops
### `do...while`
This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.

```csharp
do
{
  statement;
} while (condition);
```
### `foreach`

```csharp
// pseudocode
foreach (type element in sequence)
{
  statement;
}

// example
string[] melody = { "a", "b", "c", "c", "b" };
foreach (string note in melody)
{
  Console.WriteLine(note);
}
```

### Jump statements
* Jump statements include `break`, `continue`, `return`

## Lists
* Basic construction uses parentheses ( ) and no values.
* Object initialization uses curly braces { } and the actual values go in-between.
```csharp
// To use lists, we’ll need to add this to the top of our file
using System.Collections.Generic;

// We create a list using the new keyword. We specify the element type inside angle brackets: < >. In this example, the list is named citiesList and it holds instances of the type string
// Basic construction
List<string> citiesList = new List<string>();
citiesList.Add("Delhi");
citiesList.Add("Los Angeles");

// Create the same list using object initialization
List<string> citiesList2 = new List<string> { "Delhi", "Los Angeles" };
```

### Methods

Method | Description | Example
--- | ---- | ---
`.Add(element)` | Add element |
`.Remove(element)` | Returns `true` if the item has been removed, or `false` otherwise.
`.Count` | Find the number of elements in the list
`.Contains(element)` | Check if an element exists in the list
`.Clear()` | Remove all elements from a list.
`AddRange(arrayOrList)` | Adds the values to the end of the list | `places.AddRange(new string[] { "fifth", "sixth" });`
`InsertRange(index, arrayOrList)` | Adds the values at the index. | `places.InsertRange(2, new string[] { "third", "fourth"});`
`RemoveRange(index, nElementsToRemove)` | the first `int` is the index at which to begin removing, and the second `int` is the number of elements to remove. 
`GetRange(index, nElements)` | Get a slice of the list.

## Strings

Command | Description | Notes
--- | ---- | ---
`.IndexOf(char)` | Find the index of a character in a string.
`.Substring(startIndex, length)` | Get a substring.
`.ToLower()` | Convert to lower case.
`.ToUpper()`

## Methods
`out` allows a function to set the value of a variable.

```csharp
int number;
bool success = Int32.TryParse("10602", out number); 
// `number` is 10602 and success is true
int number2;
bool success2 = Int32.TryParse(" !!! ", out number2);
// `number2` is 0 and success2 is false

// For a shortcut, we can declare the int variable within the method call:
bool success = Int32.TryParse("10602", out int number);
```
## Classes
A constructor looks like a method but lacks a return type and has the same name as its class.
```csharp
class Polygon
{
  public int sides;

  public Polygon(int sides)
  {
    this.sides = sides;
  }
}
```

### Overloading constructors
Use `: this()` to refer to another constructor in the same class. This is useful when the second constructor has additional functionality:
```csharp
public Book(string title, string author)
{
  this.title = title;
  this.author = author;
}

public Book(string title) : this(title, "Unknown")
{
  Console.WriteLine("Author not specified. Value defaulted to 'Unknown'.");
}
```
Here, the second constructor calls the first and prints additional information to the console.

## Encapsulation

Code | Description | Notes
--- | ---- | ---
`public` | Any class can access a public member.
`private` | A private member can only be accessed by code within the same class. | C# encourages encapsulation by defaulting all class members to `private`.
`protected` | A protected member can be accessed by the current class and any class that inherits from it.

* Access modifiers apply to all class members, including fields and methods.

### Properties

A property controls access to a field, allowing us to validate values before they are set. A property consists of two methods:

* a `get()` method, or getter, called when the property is accessed
* a `set()` method, or setter, called when the property is assigned a value
  * The `set()` method uses the keyword value, representing the value assigned to the property. 
* Note that the get and set method definitions do NOT include a pair of parentheses following the method name.
* It’s common to name a property with the title-cased version of its field’s name

```csharp
private int area;
public int Area
{
  get { return area; }
  set 
  { 
    if (value < 0) { area = 0; }
    else { area = value; }
  }
}

Shape s = new Shape();
s.Area = -1; // set() is called
Console.WriteLine(s.Area); // get() is called -- Prints 0
// s.area = 2; // would throw error CS0122, as area is not accessible here
```

Auto-implemented property

This:
```csharp
private string size;
public string Size
{
  get { return size; }
  set { size = value; }
}
```
Can be re-written as:
```csharp
public string Size
{ get; set; }

```
The field is automatically created in the background with an auto-implemented property.

If we want programs to be able to get the value, but not set it, we can do one of the following:
1. Omit the `set()` method.
```csharp
public string Area
{
  get { return area; }
}
```
2. Make the `set()` method private.
```csharp
public int Area
{
  get { return area; }
  private set { area = value; }  
}


public static int ForestsCreated 
  { get; private set; }
```
### Static Fields and Properties
* Static members are members that are associated with the class itself. 
* They are defined using the `static` keyword, which should follow the access modifier if one is present.

### Static constructors
* We can use a static constructor to handle setup for a class that only needs to be run once before the class is used. 
* Typically, we use static constructors to set values for static fields and properties.

### Static classes
* A static class cannot be instantiated and may only contain static members, so we should only create one if we are making a utility or library, like `Math` or `Console`.

## Inheritance
A subclass inherits, or “extends”, a superclass using the colon syntax:
```csharp
class Vehicle
{
}

class Sedan : Vehicle
{
}
// Sedan will inherit all the functionality of the `Vehicle` class.
```
### base
We can refer to a superclass inside a subclass with the `base` keyword.

There’s a special syntax for calling the superclass constructor:

```csharpclass Sedan : Vehicle
{
  public Sedan (double speed) : base(speed)
  {
  }
}

```
The preceding code shows a `Sedan` that inherits from `Vehicle`. The Sedan constructor calls the `Vehicle` constructor with one argument, `speed`. This works as long as `Vehicl`e has a constructor with one parameter of type `double`.

Without an explicit call to `base()`, any subclass constructor will implicitly call the default parameterless constructor for its superclass. For example, this code implicitly calls `Vehicle()`:
```csharp
class Sedan : Vehicle
{
  // Implicitly calls base(), aka Vehicle()
  public Sedan (double speed)
  {
  }
}
// The preceding code is equivalent to this:
{
  public Sedan (double speed) : base()
  {
  }
}
```
This code will only work if the constructor `Vehicle()` exists. If it doesn’t, then an error will be thrown.

## Polymorphism
* A virtual method is a method in the base class that can be overridden in derived classes. 
* The `virtual` keyword is used to allow derived classes to provide specific implementations of this method.
* The `override` keyword is used to indicate that a method in a derived class is intended to replace a method in the base class.

```csharp
{
  class Animal
  {
    public virtual void MakeSound()
    {
      Console.WriteLine("Animal makes a sound.");
    }
  }

  class Dog : Animal
  {
    public override void MakeSound()
    {
      Console.WriteLine("Dog barks.");
    }
  }

  // Define the Cat class here
  class Cat : Animal
  {
    public override void MakeSound()
    {
      Console.WriteLine("Cat meows.");
    }
  }
}
```

### Upcasting objects
In some cases, we may want to create an instance of our base class with access to the overridden methods of a derived class. This is where we would use upcasting.

Basic syntax:
```csharp
BaseClass upcastInstance = derivedInstance;
```

Example:
```csharp
class Animal {
  public void Walk() {
    Console.WriteLine("Animal walks.");
  } 
  
  public virtual void MakeSound() {
    Console.WriteLine("Animal makes noise.");
  } 
}

class Dog : Animal {
  public void Sleep() {
    Console.WriteLine("Dog sleeps.");
  } 
  
  public override void MakeSound() {
    Console.WriteLine("Dog barks.");
  } 
}

class Program {
  static void Main(string[] args) {
    // Create a Dog object
    Dog myDog = new Dog();

    // Upcast the Dog object to an Animal reference
    Animal myAnimal = myDog;

    myAnimal.MakeSound(); // Output: Dog barks.
    myAnimal.Walk(); // Output: Animal walks.
    myAnimal.Sleep(); // Output: ERROR
  }
}
```
An instance that has been upcast to a base class instance, will have access to the following:
* The derived class’s overridden methods
* The base class’s non-virtual methods
It is important to note that any method in the derived class that does not override a method in the base class, will not be accessible from an upcast instance.

### Downcasting objects

Downcasting in C# refers to converting an upcast instance to a derived one. This process allows us to access the derived class members that are unavailable in the base class.

Downcasting is an explicit operation and requires extra syntax:
```csharp
BaseClass upcastInstance = new DerivedClass() 
DerivedClass downcastInstance = (DerviedClass)upcastInstance;
```
This gives the downcastInstance access to both the `BaseClass` and the `DerivedClass` methods.

Example:
```csharp
class Animal {
  public void Walk() {
    Console.WriteLine("Animal walks.");
  } 
  
  public virtual void MakeSound() {
    Console.WriteLine("Animal makes noise.");
  } 
}

class Dog : Animal {
  public void Sleep() {
    Console.WriteLine("Dog sleeps.");
  } 
  
  public override void MakeSound() {
    Console.WriteLine("Dog barks.");
  } 
}

class Program {
  static void Main(string[] args) {
    // Create an upcast Animal object
    Animal myAnimal = new Dog();

    // Downcast the myAnimal object
    Dog myDog = (Dog)myAnimal;

    myDog.MakeSound(); // Output: Dog barks.
    myDog.Walk(); // Output: Animal walks.
    myDog.Sleep(); // Output: Dog sleeps.
  }
}
```
### Using `is` Operators
The is operator results to `true` if an object can be upcast or downcast to a specified type and `false` if it can not. This can be a useful check before performing these casting operations.

### Using `as` Operators
The `as` operator attempts to cast an object to a given type, returning `null` if the cast fails. This is useful for safely trying to downcast an object to a more derived type without risking an exception.

```csharp
class Program
{
  static void Main(string[] args)
  {
    // Create an Animal reference pointing to a Dog object
    Animal myAnimal = new Dog();

    // Use the 'as' operator to attempt to cast the Animal reference to a Dog
    Dog myDog = myAnimal as Dog;
    
    if (myDog != null)
    {
      myDog.Fetch();
    }

    // Use the 'as' operator to attempt to cast the Animal reference to a Cat
    Cat myCat = myAnimal as Cat;
    
    if (myCat == null)
    {
      Console.WriteLine("Downcasting failed using 'as' operator.");
    }
  }
}
```
### Abstract Classes
an abstract class provides a blueprint of what derived classes need to implement. This is done through the use of implemented and unimplemented methods.

```csharp
abstract class Animal
{
  // Abstract Method
  public abstract void MakeSound();

  // Virtual Method
  public virtual void Move()
  {
    Console.WriteLine("Animal moves.");
  }

  // Non-Virtual Method
  public void Sleep()
  {
    Console.WriteLine("Animal sleeps.");
  }
}

class Dog : Animal
{
  public override void MakeSound()
  {
    Console.WriteLine("Dog barks.");
  }

  public override void Move()
  {
    Console.WriteLine("Dog runs.");
  }
}

class Cat : Animal
{
  public override void MakeSound()
  {
    Console.WriteLine("Cat meows.");
  }
}

```
Looking at the above derived classes we can see that both `Dog` and `Cat` classes implement the `MakeSound()` method using the `override` keyword. This is because it was labeled `abstract` in the Animal class, so it is the job of the derived classes to implement.

Abstract classes fulfill the practice of Polymorphism by defining necessary behaviors without implementing them. They pass the task of implementation on to the more specific derived classes.

## Interfaces
* The interface is a set of properties, methods, and other members. They are declared with a signature, but their behaviors are not defined. 
* A class implements an interface if it defines those properties, methods, and other members.
* We can add members, like properties and methods, to the interface
```csharp
{
  interface IAutomobile
  {
    string LicensePlate { get; }
    double Speed { get; }
    int Wheels { get; }
    void Honk();
  }
}
class Sedan : IAutomobile
{
  public string LicensePlate
  { get; }
  
  // And so on...
}
```

A class in C# can even implement multiple interfaces by separating the interface names with a comma:
```csharp
class Cat : IQuadruped, IFeline
{  
  // member implementation for both IQuadruped and IFeline
}
```
* While inheritance allows one class to pass members along to a subclass, an interface is like a contract, specifying members that a class is obligated to implement.
* Note that when inheriting and implementing an interface, the superclass must be specified first, followed by any interfaces the class will implement, separated by commas.

## Reference Fundamentals
* Classes are reference types. That means that when we create a new instance of a class and store it in a variable, the variable is a reference to the object.
  * When we compare reference types with `==`, the C# compiler performs a referential comparison, which means it checks if two variables refer to the same memory location
* Value-type variables, e.g. `int num = 6`, hold the actual data.
  * Every “primitive” data type is a value type

### References of Different Types
* An object can be referenced using the name of any type in its inheritance hierarchy or of any interface it implements.

Example:
```csharp
class Encyclopedia: Book, IFlippable {
    //...
}

Encyclopedia enc = new Encyclopedia();
IFlippable fEnc = enc;
Book bEnc = enc;
```
A reference only has access to members of the type it is defined as. 
* `fEnc` can only access members in the `IFlippable` interface, and `bEnc` can only access members in the `Book` superclass.

## The Object Class
Method | Description | Notes
--- | ---- | ---
`.Equals(Object)` |  returns `true` if the current instance and the argument are equal | Uses value equality for value types and referential equality for reference types | Can be overridden because it is virtual
`GetType()` | returns the type of the object
`ToString()` | returns a string describing the object | Can be overridden because it is virtual

## String
Code | Description | Notes
--- | ---- | ---
`String.IsNullOrEmpty(string)` | check for null OR empty string
`.Contains(substring)` | will return `true` if the substring occurs within the string object the method is called on
`.Replace(target, replacement)` | Replace a occurrences of the target substring with another substring

## LINQ
Use this import to use `LINQ`:
```csharp
using System.Linq;
```
* Every LINQ query returns either a single value or an object of type `IEnumerable<T>`
  * Number of elements is returned with `.Count()`.
* Since the single value type and/or the parameter type `T` is not always known, it’s common to store a query’s returned value in a variable of type `var`.
  * `var` is just an implicitly typed variable — we let the C# compiler determine the actual type for us.
* Technically, LINQ can be used with any type that supports `foreach` loops, e.g. `List`

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace LearnLinq
{
  class Program
  {
    static void Main()
    {
      string[] heroes = { "Zoe", "Liam", "Taryn", "Dorian", "Everett", "Marlena" };

      // Query syntax
      var queryResult = from x in heroes
                        where x.Contains("a")
                        select $"{x} contains an 'a'";
      
      // Method syntax
      var methodResult = heroes
        .Where(x => x.Contains("a"))
        .Select(x => $"{x} contains an 'a'");
     
      // Printing...
      Console.WriteLine("queryResult:");
      foreach (string s in queryResult)
      {
        Console.WriteLine(s);
      }
      
      Console.WriteLine("\nmethodResult:");
      foreach (string s in methodResult)
      {
        Console.WriteLine(s);
      }
    }
  }
}
```
# Poetry for Python dependency management

Description | Command | Notes
--- | ---- | ---
Add a dependency | `poetry add <dependency>` | It will automatically find a suitable version constraint and install the package and sub-dependencies. Dependency version is added to `pyproject.toml`. [Documentation](https://python-poetry.org/docs/cli/#add)
Activate the virtual environment | `poetry shell` | Navigate to the project folder.
Deactivate the virtual environment | `exit`
To run your script | `poetry run python your_script.py` | 
Install dependencies | `poetry install` | Not required if using `poetry add` for dependencies.
removes a package from the current list of installed packages. | `poetry remove <dependency>`

Poetry automatically creates a virtual environment for the project:
macOS: `~/Library/Caches/pypoetry`
Windows: `C:\Users\<username>\AppData\Local\pypoetry\Cache`# Dotnet commands

Description | Terminal command | Notes
--- | ---- | ---
Add NuGet package | `dotnet add package <package name>` | 
Build and run a Blazor app | `dotnet watch` | 

# Blazor

Method/directive | Description | Notes
--- | ---- | ---
`OnInitializedAsync()` | Blazor component base class method. When used in a component, this event fires when the component's initialization is complete and it has received initial parameters but before the page is rendered and displayed to the user. | A good place to call the registered data service (i.e. an instance of a class that will get data from the database) and obtain data.
`@page <path>` | Specify the webpage's path relative to the root page | e.g. `@page "/"` for home page.
`@code{ }` | Contains lines of c# code within a component.
`@if { } else if { } else { }` | | Commonly used to display different UI depending on if the data is available yet or not.
`@switch { }` | Works similar to c# `switch` statement |
`@foreach (var item in items) { }`
`@while`
`@do while`

## Blazor components

`Pizza.razor` component 
```csharp
<h2>New Pizza: @PizzaName</h2>

<p>@PizzaDescription</p>

@code {
    [Parameter]
    public string PizzaName { get; set; }
    
    [Parameter]
    public string PizzaDescription { get; set; } = "The best pizza you've ever tasted."
}
```

You can also use custom classes in your project as component parameters. Consider this class that describes a topping:
```csharp
public class PizzaTopping
{
    public string Name { get; set; }
    public string Ingredients { get; set; }
}
```
You can use that as a component parameter in the same way as a parameter value to access individual properties of the class by using dot syntax:

```csharp
// `PizzaTopping.razor`
<h2>New Topping: @Topping.Name</h2>

<p>Ingredients: @Topping.Ingredients</p>

@code {
    [Parameter]
    public PizzaTopping Topping { get; set; }
}
```
In the parent component, you set parameter values by using attributes of the child component's tags. You set simple components directly. With a parameter based on a custom class, you use inline C# code to create a new instance of that class and set its values:

```csharp
@page "/pizzas-toppings"

<h1>Our Latest Pizzas and Topping</h1>

<Pizza PizzaName="Hawaiian" PizzaDescription="The one with pineapple" />

<PizzaTopping Topping="@(new PizzaTopping() { Name = "Chilli Sauce", Ingredients = "Three kinds of chilli." })" />
```

### Cascading parameters
When you set the value of a cascading parameter in a component, its value is automatically available to all descendant components to any depth.

In the parent component, using the <CascadingValue> tag specifies the information that will cascade to all descendants. Any component that's rendered within that tag is able to access the value.
```csharp
@page "/specialoffers"

<h1>Special Offers</h1>

<CascadingValue Name="DealName" Value="Throwback Thursday">
    <!-- Any descendant component rendered here will be able to access the cascading value. -->
</CascadingValue>
```

In the descendant components, you can access the cascading value by using component members and decorating them with the `[CascadingParameter]` attribute.
```csharp
<h2>Deal: @DealName</h2>

@code {
    [CascadingParameter(Name="DealName")]
    private string DealName { get; set; }
}
```
In the preceding example, the `Name` attribute in the parent identifies the cascading value, which is matched with the `Name` value in the `[CascadingParameter]` attribute. You can optionally omit these names, in which case the attributes are matched by type. Omitting the name works well when you have only one parameter of that type. If you want to cascade two different string values, you must use parameter names to avoid any ambiguity.

## Share information by using AppState
You create a class that defines the properties you want to store, and register it as a scoped service. In any component where you want to set or use the AppState values, you inject the service, and then you can access its properties. Unlike component parameters and cascading parameters, values in AppState are available to all components in the application, even components that aren't children of the component that stored the value.

As an example, consider this class that stores a value about sales:
```csharp
public class PizzaSalesState
{
    public int PizzasSoldToday { get; set; }
}
```
You would add the class as a scoped service in the Program.cs file:
```csharp
...
// Add services to the container
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

// Add the AppState class
builder.Services.AddScoped<PizzaSalesState>();
...
```
Now, in any component where you want to set or retrieve AppState values, you can inject the class, and then access properties:
```csharp
@page "/"
@inject PizzaSalesState SalesState

<h1>Welcome to Blazing Pizzas</h1>

<p>Today, we've sold this many pizzas: @SalesState.PizzasSoldToday</p>

<button @onclick="IncrementSales">Buy a Pizza</button>

@code {
    private void IncrementSales()
    {
        SalesState.PizzasSoldToday++;
    }
}
```# Dotnet commands

Description | Terminal command | Notes
--- | ---- | ---
Add NuGet package | `dotnet add package <package name>` | 
Build and run a Blazor app | `dotnet watch` | 

# Blazor

Method/directive | Description | Notes
--- | ---- | ---
`OnInitializedAsync()` | Blazor component base class method. When used in a component, this event fires when the component's initialization is complete and it has received initial parameters but before the page is rendered and displayed to the user. | A good place to call the registered data service (i.e. an instance of a class that will get data from the database) and obtain data.
`@page <path>` | Specify the webpage's path relative to the root page | e.g. `@page "/"` for home page.
`@code{ }` | Contains lines of c# code within a component.
`@if { } else if { } else { }` | | Commonly used to display different UI depending on if the data is available yet or not.
`@switch { }` | Works similar to c# `switch` statement |
`@foreach (var item in items) { }`
`@while`
`@do while`

## Blazor components

`Pizza.razor` component 
```csharp
<h2>New Pizza: @PizzaName</h2>

<p>@PizzaDescription</p>

@code {
    [Parameter]
    public string PizzaName { get; set; }
    
    [Parameter]
    public string PizzaDescription { get; set; } = "The best pizza you've ever tasted."
}
```

You can also use custom classes in your project as component parameters. Consider this class that describes a topping:
```csharp
public class PizzaTopping
{
    public string Name { get; set; }
    public string Ingredients { get; set; }
}
```
You can use that as a component parameter in the same way as a parameter value to access individual properties of the class by using dot syntax:

```csharp
// `PizzaTopping.razor`
<h2>New Topping: @Topping.Name</h2>

<p>Ingredients: @Topping.Ingredients</p>

@code {
    [Parameter]
    public PizzaTopping Topping { get; set; }
}
```
In the parent component, you set parameter values by using attributes of the child component's tags. You set simple components directly. With a parameter based on a custom class, you use inline C# code to create a new instance of that class and set its values:

```csharp
@page "/pizzas-toppings"

<h1>Our Latest Pizzas and Topping</h1>

<Pizza PizzaName="Hawaiian" PizzaDescription="The one with pineapple" />

<PizzaTopping Topping="@(new PizzaTopping() { Name = "Chilli Sauce", Ingredients = "Three kinds of chilli." })" />
```

### Cascading parameters
When you set the value of a cascading parameter in a component, its value is automatically available to all descendant components to any depth.

In the parent component, using the <CascadingValue> tag specifies the information that will cascade to all descendants. Any component that's rendered within that tag is able to access the value.
```csharp
@page "/specialoffers"

<h1>Special Offers</h1>

<CascadingValue Name="DealName" Value="Throwback Thursday">
    <!-- Any descendant component rendered here will be able to access the cascading value. -->
</CascadingValue>
```

In the descendant components, you can access the cascading value by using component members and decorating them with the `[CascadingParameter]` attribute.
```csharp
<h2>Deal: @DealName</h2>

@code {
    [CascadingParameter(Name="DealName")]
    private string DealName { get; set; }
}
```
In the preceding example, the `Name` attribute in the parent identifies the cascading value, which is matched with the `Name` value in the `[CascadingParameter]` attribute. You can optionally omit these names, in which case the attributes are matched by type. Omitting the name works well when you have only one parameter of that type. If you want to cascade two different string values, you must use parameter names to avoid any ambiguity.

## Share information by using AppState
You create a class that defines the properties you want to store, and register it as a scoped service. In any component where you want to set or use the AppState values, you inject the service, and then you can access its properties. Unlike component parameters and cascading parameters, values in AppState are available to all components in the application, even components that aren't children of the component that stored the value.

As an example, consider this class that stores a value about sales:
```csharp
public class PizzaSalesState
{
    public int PizzasSoldToday { get; set; }
}
```
You would add the class as a scoped service in the Program.cs file:
```csharp
...
// Add services to the container
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

// Add the AppState class
builder.Services.AddScoped<PizzaSalesState>();
...
```
Now, in any component where you want to set or retrieve AppState values, you can inject the class, and then access properties:
```csharp
@page "/"
@inject PizzaSalesState SalesState

<h1>Welcome to Blazing Pizzas</h1>

<p>Today, we've sold this many pizzas: @SalesState.PizzasSoldToday</p>

<button @onclick="IncrementSales">Buy a Pizza</button>

@code {
    private void IncrementSales()
    {
        SalesState.PizzasSoldToday++;
    }
}
```# Dotnet commands

Description | Terminal command | Notes
--- | ---- | ---
Add NuGet package | `dotnet add package <package name>` | 
Build and run a Blazor app | `dotnet watch` | 

# Blazor

Method/directive | Description | Notes
--- | ---- | ---
`OnInitializedAsync()` | Blazor component base class method. When used in a component, this event fires when the component's initialization is complete and it has received initial parameters but before the page is rendered and displayed to the user. | A good place to call the registered data service (i.e. an instance of a class that will get data from the database) and obtain data.
`@page <path>` | Specify the webpage's path relative to the root page | e.g. `@page "/"` for home page.
`@code{ }` | Contains lines of c# code within a component.
`@if { } else if { } else { }` | | Commonly used to display different UI depending on if the data is available yet or not.
`@switch { }` | Works similar to c# `switch` statement |
`@foreach (var item in items) { }`
`@while`
`@do while`

## Blazor components

`Pizza.razor` component 
```csharp
<h2>New Pizza: @PizzaName</h2>

<p>@PizzaDescription</p>

@code {
    [Parameter]
    public string PizzaName { get; set; }
    
    [Parameter]
    public string PizzaDescription { get; set; } = "The best pizza you've ever tasted."
}
```

You can also use custom classes in your project as component parameters. Consider this class that describes a topping:
```csharp
public class PizzaTopping
{
    public string Name { get; set; }
    public string Ingredients { get; set; }
}
```
You can use that as a component parameter in the same way as a parameter value to access individual properties of the class by using dot syntax:

```csharp
// `PizzaTopping.razor`
<h2>New Topping: @Topping.Name</h2>

<p>Ingredients: @Topping.Ingredients</p>

@code {
    [Parameter]
    public PizzaTopping Topping { get; set; }
}
```
In the parent component, you set parameter values by using attributes of the child component's tags. You set simple components directly. With a parameter based on a custom class, you use inline C# code to create a new instance of that class and set its values:

```csharp
@page "/pizzas-toppings"

<h1>Our Latest Pizzas and Topping</h1>

<Pizza PizzaName="Hawaiian" PizzaDescription="The one with pineapple" />

<PizzaTopping Topping="@(new PizzaTopping() { Name = "Chilli Sauce", Ingredients = "Three kinds of chilli." })" />
```

### Cascading parameters
When you set the value of a cascading parameter in a component, its value is automatically available to all descendant components to any depth.

In the parent component, using the <CascadingValue> tag specifies the information that will cascade to all descendants. Any component that's rendered within that tag is able to access the value.
```csharp
@page "/specialoffers"

<h1>Special Offers</h1>

<CascadingValue Name="DealName" Value="Throwback Thursday">
    <!-- Any descendant component rendered here will be able to access the cascading value. -->
</CascadingValue>
```

In the descendant components, you can access the cascading value by using component members and decorating them with the `[CascadingParameter]` attribute.
```csharp
<h2>Deal: @DealName</h2>

@code {
    [CascadingParameter(Name="DealName")]
    private string DealName { get; set; }
}
```
In the preceding example, the `Name` attribute in the parent identifies the cascading value, which is matched with the `Name` value in the `[CascadingParameter]` attribute. You can optionally omit these names, in which case the attributes are matched by type. Omitting the name works well when you have only one parameter of that type. If you want to cascade two different string values, you must use parameter names to avoid any ambiguity.

## Share information by using AppState
You create a class that defines the properties you want to store, and register it as a scoped service. In any component where you want to set or use the AppState values, you inject the service, and then you can access its properties. Unlike component parameters and cascading parameters, values in AppState are available to all components in the application, even components that aren't children of the component that stored the value.

As an example, consider this class that stores a value about sales:
```csharp
public class PizzaSalesState
{
    public int PizzasSoldToday { get; set; }
}
```
You would add the class as a scoped service in the Program.cs file:
```csharp
...
// Add services to the container
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

// Add the AppState class
builder.Services.AddScoped<PizzaSalesState>();
...
```
Now, in any component where you want to set or retrieve AppState values, you can inject the class, and then access properties:
```csharp
@page "/"
@inject PizzaSalesState SalesState

<h1>Welcome to Blazing Pizzas</h1>

<p>Today, we've sold this many pizzas: @SalesState.PizzasSoldToday</p>

<button @onclick="IncrementSales">Buy a Pizza</button>

@code {
    private void IncrementSales()
    {
        SalesState.PizzasSoldToday++;
    }
}
```# Dotnet commands

Description | Terminal command | Notes
--- | ---- | ---
Add NuGet package | `dotnet add package <package name>` | 
Build and run a Blazor app | `dotnet watch` | 

## Blazor

Method/directive | Description | Notes
--- | ---- | ---
`OnInitializedAsync()` | Blazor component base class method. When used in a component, this event fires when the component's initialization is complete and it has received initial parameters but before the page is rendered and displayed to the user. | A good place to call the registered data service (i.e. an instance of a class that will get data from the database) and obtain data.
`@page <path>` | Specify the webpage's path relative to the root page | e.g. `@page "/"` for home page.
`@code{ }` | Contains lines of c# code within a component.
`@if { } else if { } else { }` | | Commonly used to display different UI depending on if the data is available yet or not.
`@switch { }` | Works similar to c# `switch` statement |
`@foreach (var item in items) { }`
`@while`
`@do while`