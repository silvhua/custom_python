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

# Docker ETL in Python

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Create the engine
engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/database_name")

# Create the session
session = Session(eingine)
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