
# Table of Contents
* [Sets](#sets)
* [Copy Objects](#copy-objects)
* [Date Time](#date-and-time)
* [APIs](#apis)
* [SQL](#sql)
* [Pandas](#pandas-series)

# [Python Arithmetic Operators](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)
* `% Modulus`: Gives the remainder following a division.
* `//` Floor division: Rounds down after a division.

# Handy 
## Formatted String Literals (Number Formatting)
[See Python documentation](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

Command | Description
--- | ---
`.1f` | One decimal place

```python
# Print string with number with 2 decimal places
print(f'RMSE: {rmse:.2f}')

# Create heatmap where annotations are floats with 1 decimal place
sns.heatmap(matrix, annot=True, fmt='.1f')
```
Passing an integer after the `:` will cause that field to be a minimum number of characters wide. This is useful for making columns line up.
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
```

## Docstring conventions
[See midterm project lecture slide](https://docs.google.com/presentation/d/1n_WPoygsG7qmIBamMc9aAnhwzX2dhh3u9X3f4-lbv8Y/edit#slide=id.gbb03a097b4_0_149)

## Print system path that Python searches
```python
import sys # importing the sys module
print(sys.path) # printing sys.path variable of sys module
print(sys.executable) # print the location of the Python it is running. It should be the same as the one in PATH when the environment was activated.
```

## [Print variable name](https://bobbyhadz.com/blog/python-print-variable-name)
```python
site = 'bobbyhadz.com'

result = f'{site=}'
print(result)  # 👉️ site='bobbyhadz.com'

# ✅ print variable name using f-string
variable_name = f'{site=}'.split('=')[0]
print(variable_name)  # 👉️ 'site'
```
## Save and load image
[Figures, plots & subplots: A simple cheatsheet for plotting graphs & images in Python](https://medium.com/fullstackai/why-is-plotting-figures-so-difficult-in-python-b3754f5d4c60)
```python
from PIL import Image 
fig.savefig('filename.png')

# If figure is an axes object
ax.figure.savefig('filename.png')
```
## Time how long it takes to execute code
[What is Online Machine Learning?. Making machines learn in real time | by Max Pagels | The Hands-on Advisors | Medium](https://medium.com/value-stream-design/online-machine-learning-515556ff72c5)

```python
import time
start_time = time.time()
### Put code here
elapsed_time = time.time() - start_time
```
## Load CSV from github
`data_url = 'https://raw.githubusercontent.com/<user_or_organization>/<repository>/master/<path_and_filename>'`

```python
data_url = 'https://raw.githubusercontent.com/silvhua-Lighthouse/2022-11-21-walkthrough-apriori/master/movie_dataset.csv'

df = pd.read_csv(data_url)
```
## Defining functions: Setting optional keyword arguments
[reference on Grepper](https://www.grepper.com/search.php?q=python%20create%20function%20with%20optional%20arguments)

```python
def myfunc(a,b, *args, **kwargs):
      c = kwargs.get('c', None)
      d = kwargs.get('d', None)
      
myfunc(a,b, c='nick', d='dog', ...)
```

# [Virtual Environment](https://data.compass.lighthouselabs.ca/activities/941)
## Anaconda Prompt

* `echo %PATH%` to see the environmental variable PATH, which specifies where to look for commands.
* `conda create -n test_env python=3.9`
* `conda activate test_env`
* `conda deactivate` to deactivate the virtual environment
* `conda remove --name ENV_NAME --all` to remove a virtual environment

## Gitbash
[Resource: Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
Command | Description
--- | ---
`python3 -m venv virtual_env-name` | Create a virtual environment (using Python 3.5)
`cd` to the `Scripts` directory, then `. activate` | Activate the virtual virtual environment

Manually set the virtual environment on VSCode: use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P). [Resource](https://code.visualstudio.com/docs/python/environments)

# [Git, Markdown, and the Dev Workflow](https://data.compass.lighthouselabs.ca/days/w01d1/activities/149)

Bash commands (steps in bold are required each time to update a file)
* `mkdir <folder name>` # to create a new folder
* `git clone git@github.com:YOUR_USER_NAME/lighthouse-data-notes.git` to clone a repo
* `git init` to initialize a new Git repo in the current directory
* `git remote add origin <URL of repo>` to add new repo as a remote of  your local repo if not yet created
* **`git add <item>` to add the item to the repository** 
    * OR `git rm --cached -r <filename>` to remove item from remote repo without changing it on computer
* **`git commit -m "<comments>`** 
* **`git push -u origin master` to push changes to GitHub (main branch has since been updated to `main`)**

# Sets
* [Reference: Real Python](https://realpython.com/python-sets/)

```Python
x = set(<iter>)
```

**See reference link for more methods**

Task | Operator | Method
--- | --- | ---
union (join) | `x1 \| x2` |  `x1.union(x2)`
intersection (common elements)    |   `x1 & x2` |   `x1.intersection(x2)`   |   `x1 \|= x2` |   `x1.update(x2,x3)`
difference  |    `x1 - x2`  |   `x1.difference(x2)`
symmetric difference (elements that are in one set but not both)    |   `x1 ^ x2`   |   `x1.symmetric_difference(x2)` *(only 1 argument allowed)*
boolean: `True` if no elements in common    |  (none) |   `x1.isdisjoint(x2)`
determine if a set is a subset of another set  |   `x1 <= x2`  |   `x1.issubset(x2)`
determine if a set is a proper subset (a subset that is non-identical) of another set   |  `x1 < x2`    |   (none) 
determine if a set is a superset (contains all elements) of another set |    `x1 >= x2` | `x1.issuperset(x2)`
is proper superset? |   `x1 > x2`   |   (none)
**Augmented Assignment**
modify a set by union   |   `x1 \|= x2` |   `x1.update(x2)`
modify a set by intersection, i.e. retain only elements found in all sets   |   `x1 &= x2`  | `x1.intersection_update(x2)`
modify by difference, i.e. remove elements found in x2  | `x1 -= x2`    |   `x1.difference_update(x2)
modify by symmetric difference, i.e. retain eelements found in either set, but not both | `x1 ^= x2`    | `x1.symmetric_difference_update(x2)`

# Collections
[Resource: Python’s Collections Module — High-performance container data types. | by Parul Pandey | Towards Data Science](https://towardsdatascience.com/pythons-collections-module-high-performance-container-data-types-cb4187afb5fc)

## Named tuple
Namedtuples are a memory-efficient option when defining an immutable class in Python. It is a function for tuples with Named Fields.

```python
from collections import namedtuple
fruit = namedtuple('fruit','number variety color')
guava = fruit(number=2,variety='HoneyCrisp',color='green')
apple = fruit(number=5,variety='Granny Smith',color='red')

# We can then call on the various attributes:
guava.color # >>> 'green'
apple.variety # >>> 'Granny Smith'
```
## Counter
Counter is a dict subclass which helps to count hashable objects. The elements are stored as dictionary keys while the object counts are stored as the value.

Function/Method | Description
--- | ---
`c = Counter(list)` | Return a dictionary. The elements are stored as dictionary keys while the object counts are stored as the value.
`.elements()` | Return an iterator over elements repeating each as many times as its count. Elements are returned in the order first encountered. If an element’s count is less than one, elements() will ignore it. [See documentation](https://docs.python.org/3/library/collections.html#collections.Counter.elements).
`most_common(n)` | Returns a list of the most common elements with their counts. The number of elements has to be specified as n.

```python
from collections import Counter

c = Counter('abcacdabcacd')
print(c) # >>> Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})

lst = [5,6,7,1,3,9,9,1,2,5,5,7,7]
c = Counter(lst)
print(c) # >>> Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})

s = 'the lazy dog jumped over another lazy dog'
words = s.split()
Counter(words).most_common(3) # >>> [('lazy', 2), ('dog', 2), ('the', 1)]

# Return the elements as a sorted list
print(sorted(c.elements()))
```
## `OrderedDict` Ordered Dictionary
An OrderedDict is a dictionary subclass that remembers the order in which that keys were first inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added. Since an ordered dictionary remembers its insertion order, it can be used in conjunction with sorting to make a sorted dictionary:

```python
# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[0])) 
    # Output:  OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    # Output: OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
```
## The deque
The deque is a list optimized for inserting and removing items.
```python
from collections import deque

list = ["a","b","c"]
deq = deque(list)

# To add an element to the right of the deque, you have to use append() method.
deq.append("d")
# If you want to add an element to the start of the deque, you have to use appendleft() method.
deq.appendleft("e")

# To remove an element from the right end, you can use pop() function and to remove an element from left, you can use popleft().
deq.pop()
deq.popleft()

# If you want to remove all elements from a deque, you can use clear() function.
deq.clear()

# If you want to find the count of a specific element, use count(x) function. You have to specify the element for which you need to find the count, as the argument.
list = ["a","b","c"]
deq = deque(list)
print(deq.count("a"))

```

# Copy Objects
[Reference: Python Shallow Copy and Deep Copy (With Examples) (programiz.com)](https://www.programiz.com/python-programming/shallow-deep-copy)
### Copy using `=` operator
```
oldlist = newlist
```

Changes to either variable will be visible in both because they point to the same object.
### Copy module
```python
import copy
```
Type of copy module | Description | Method
--- | --- | ---
shallow copy[^1] | Creates a new object with references to the original elements. Any changes to original elements are reflected in both lists. New elements to the old list do not get copied to the new list. | `new_list = copy.copy(old_list)`
deep copy | Creates a new object. Changes to elements in one list are not reflected in the other list. | `new_list = copy.deepcopy(old_list)`

[^1]: Shallow copy is not possible for immutable objects like integers or tuples.

# Python Classes
* [Tutorial notebook](/W04/2022-10-15%20notepad%20classes.ipynb)
* [2022-10-15 exercises](/W04/oop_exercise.ipynb)
* [Resource: Python @property: How to Use it and Why? - Programiz](https://www.programiz.com/python-programming/property)
* [Walkthrough page with embedded Youtube](https://data.compass.lighthouselabs.ca/activities/552)

# Date and Time
1. [Reference: Python Datetime Tutorial: Manipulate Times, Dates, and Time Spans (dataquest.io)](https://www.dataquest.io/blog/python-datetime-tutorial/)
2. [Reference: Python datetime (With Examples) (programiz.com)](https://www.programiz.com/python-programming/datetime)
3. [Pandas timeseries documentation](https://pandas.pydata.org/docs/user_guide/timeseries.html)

### `datetime` Objects
```python
from datetime import datetime

# Create a datetime object for current moment
datetime_object = datetime.now() 

# Create a date object from a string in a given time format
my_string = '2019-10-31'
my_date = datetime.strptime(my_string, "%Y-%m-%d")

# create date with year, month, day, hour, minute, and second
date1 = datetime(2017, 6, 21, 18, 25, 30)
```

* `strptime()` converts string to datetime object 
* `strftime()` converts datetime objects back into strings.

[See documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior). Format arguments (use quotes):
* `%Y` - year [0001,..., 2018, 2019,..., 9999]
* `%m` - numerical month [01, 02, ..., 11, 12]
* `%B` - full name of month (e.g. January)
* `%b` - short name of the month (first 3 characters) [Jan, Feb]
* `%d` - day [01, 02, ..., 30, 31]
* `%H` - hour in 24-h format [00, 01, ..., 22, 23]
* `%I` - hour in 12-h format
* `%M` - minute [00, 01, ..., 58, 59]
* `%S` - second [00, 01, ..., 58, 59]
* `%p` - time in AM/PM
* `%j` - day of the year

`datetime` class attributes:
* `my_date.year` Gets the year from the date
* `my_date.month` Gets the month
* `my_date.day` Gets the day of the month
* `my_date.hour`
* `my_date.minute`
* `my_date.strftime(<format>)`

`datetime` class methods:
Function/Method | Description
--- | ---
`.time()` | Create a time object

### `date` object 
```python
from datetime import date
date1 = date(2008, 8, 18)

datetoday = date.today()
```
`date` object attributes are similar as for `datetime`

### `time` object
```Python
from datetime import time
# time(hour, minute and second)
b = time(11, 34, 56) # output: b = 11:34:56

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566) # output: d = 11:34:56.234566
```
`time` object attributes are similar as for `datetime`:
* `b.hour`
* `b.minute`
* `b.second`
* `b.microsecond`


### Day of the week
```python
import calendar

# To get the day of the week from date as an integer. 0 = Monday, 1 = Tues, etc.
print(my_date.weekday())

# To get the name of the day of the week 
print(calendar.day_name[my_date.weekday()])
```
### ISO calendar
* Each week starts on Monday.
* The week starts counting from 1, so 1 = Monday.
```python
year, week, day = todays_date.isocalendar()
```
OR
```python
iso_date = todays_date.isocalendar() 
# returns object with 3 parameters: ISO year, ISO week number, and ISO weekday
```
### Unix Timestamp

* `datetime.timestamp(<time>)` converts a datetime object to a Unix time stamp
* `datetime.fromtimestamp(<timestamp>)` does the reverse

### `timedelta` Objects

These can be used with timedate objects to do math using operators (+ and -)
```python
#import datetime
from datetime import timedelta
# create timedelta object with difference of 2 weeks
d = timedelta(weeks=2)
```
* `timedelta.days`
* `timedelta.total_seconds()`

### Formatting Dates: More on strftime() and strptime()
```python
# current date and time
now = datetime.now()

# get year from date
year = now.strftime("%Y")
print("Year:", year)

# get month from date
month = now.strftime("%m")
print("Month;", month)

# get day from date
day = now.strftime("%d")
print("Day:", day)

# format time in HH:MM:SS
time = now.strftime("%H:%M:%S")
print("Time:", time)

# format date
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Date and Time:",date_time)
```

### Date rounding
[Resource: Pandas round DateTime to week (stephenallwright.com)](https://stephenallwright.com/pandas-round-datetime-to-week/)

**[Back to top](#table-of-contents)**
### Handling Timezones
Create a datetime object with the timezone entered as an argument:
```Python
from pytz import timezone
londontimezone = timezone('Europe/London')
londondatetime = datetime.now(londontimezone)
print(londondatetime)
```
*See documentation for how to use these:*
* `timezone()` to specify time zone using a string argument
* `localize` to add a time zone location to a Python datetime object
* `astimezone()` to convert the existing local time zone into any other time zone we specify 

[Reference from independent search: Python pytz - GeeksforGeeks](https://www.geeksforgeeks.org/python-pytz/)
```python
# To get a list of commonly used time zones to use with the timezone function:
import pytz
  
print('Commonly used time-zones:', pytz.common_timezones, '\n')
```

### pandas Datetime Objects
```python
# import pandas module as pd
import pandas as pd
```
* Create date object using `to_datetime()` function: `pd.to_datetime("8th of sep, 2019")`
* `to_timedelta()`: Finds differences in times in terms of days, hours, minutes, and seconds.

### How to get number of days in month
[Reference: How to get number of days in month in Python (TechOverflow)](https://techoverflow.net/2019/05/16/how-to-get-number-of-days-in-month-in-python/)

```Python
from calendar import monthrange
num_days = monthrange(2019, 2)
print(num_days) # Prints a tuple of weekday of first day of month (Mon = 0), days in the month
```
[Table of Contents](#table-of-contents)

**[Back to top](#table-of-contents)**

## `dateutil`

```python
from dateutil import parser
date = parser.parse("4th of July, 2015")
date
```

# SQL
```SQL
CREATE TABLE <table name> id <data type, e.g. INTEGER, TEXT, INTEGER PRIMARY KEY AUTOINCREMENT> <column title in lowercase> <DATA TYPE>

INSERT INTO <table name> VALUES (<value column 1>, <value column 2>, etc);
SELECT <attribute (or * for all attributes)> FROM <table name> WHERE attribute <boolean condition>;
SELECT <attribute> WHERE <attribute> IN (<value1,<value2>, etc.);

/* comment */
/* Queries can contain sub-queries */

SELECT * FROM table  WHERE <attribute> IN (SELECT type FROM <table 2 name> WHERE <attribute> LIKE "%value with wildcards%");
```
* `WHERE` ...
    * `<attribute> BETWEEN <(value)> AND <(value)>`
    * `(<condition 1> AND <condition 2>)`
    * `IS NULL` or `IS NOT NULL` 8 `limit 1` limits to 1 result

```sql
Select extract(month FROM date(fl_date)) from flights_test limit 100
```

## Functions
* `AVG`
* `MAX`
* `SUM`
* `COUNT`, `COUNT(DISTINCT <attribute>)`
* `ROUND`
* `GROUP BY` <attribute (, attribute 2)>
* `ORDER BY`, `ORDER BY` < attribute > `DESC`: Multiple attributes can be listed, separated by commas.

## Restricting grouped results with `HAVING`

If filtering aggregate results, use `HAVING` instead of `WHERE`
```SQL
SELECT type, AVG(calories) AS avg_calories FROM exercise_logs
    GROUP BY type /* Assigned new attribute name for AVG(calories)*/
    HAVING avg_calories > 70
    ; /* "HAVING" will create a filter based on the aggregate */

/* This  will show the types of entity instances (rows) from the exercise_logs table that have a count of 2 or more*/
SELECT type FROM exercise_logs GROUP BY type HAVING COUNT(*) >= 2;

```
## Calculating results with CASE
```SQL
SELECT type, heart rate,
    CASE
        WHEN heart_rate > 220-30 THEN "above max"
        WHEN heart_rate > ROUND(0.90 * (220-30)) THEN "above target"
        WHEN heart_rate > ROUND(0.50 * (220-30)) THEN "within target"
        ELSE "below target"
    END as "hr_zone" /* Creates new column specifying whether "above" or "below target" */
FROM exercise_logs;

SELECT COUNT(*),
    CASE 
        WHEN heart_rate > 220-30 THEN "above max"
        WHEN heart_rate > ROUND(0.90 * (220-30)) THEN "above target"
        WHEN heart_rate > ROUND(0.50 * (220-30)) THEN "within target"
        ELSE "below target"
    END as "hr_zone"
FROM exercise_logs
GROUP BY hr_zone;
```
## JOINing related tables
### Cross join: example
Not very useful as it doesn't necessarily relate the right entities */

```sql
SELECT * FROM student_grades, students;
```
### Implicit inner join: example
```sql
SELECT * FROM student_grades, students
    WHERE student_grades.student_id = students.id;
```
Inner joins only joins where there are matching records between the 2 tables.

### Explicit inner join - `JOIN`

Syntax for attributes: `<table name>.< attribute>`
```sql
SELECT <attribute(s)> FROM <table 1>
    JOIN <table 2>
    ON <table 1>.<attribute> = <table 2>.<attribute>
    WHERE <filter> /* optional */

/* Example */
SELECT students.first_name, students.last_name, students.email, student_grades.test, student_grades.grade FROM students
    JOIN student_grades
    ON students.id = student_grades.student_id
    WHERE grade > 90;
```
### Left outer joins

Allows for records in the left/first table (after the `FROM`)to be retained even if there Is no match in one of the tables
```sql
SELECT students.first_name, students.last_name, student_projects.title
    FROM students
    LEFT OUTER JOIN student_projects
    ON students.id = student_projects.student_id;
```
### Self-joins
* Create an **alias** for the table so it can be joined to itself just like for inner joins:
```sql
SELECT <attribute(s)> FROM <table>
    JOIN <table> <table alias> /* Can also be left outer join */
    ON <table>.<attribute> = <alias>.<attribute>

/* Example */
SELECT students.first_name, students.last_name, buddies.email as buddy_email
    FROM students
    JOIN students buddies
    ON students.buddy_id = buddies.id;
```
### Combining multiple joins
Use a second table to combine 2 entity instances (rows) in the first table
```sql
SELECT <alias 1>.<attribute>, <alias 2>.<attribute> FROM <2nd table>
    JOIN <primary table> <alias 1> 
    ON <2nd table>.<attribute 1> = <alias 1>.<primary key>
    JOIN <primary table> <alias 2> 
    ON <2nd table>.<attribute 2> = <alias 2>.<primary key>

/* Example */
SELECT a.title, b.title FROM project_pairs
    JOIN student_projects a
    ON project_pairs.project1_id = a.id
    JOIN student_projects b
    ON project_pairs.project2_id = b.id;
```
**[Back to top](#table-of-contents)**
## SQL Window Functions
[Reference: PostgreSQL Window Functions: The Ultimate Guide (postgresqltutorial.com)](https://www.postgresqltutorial.com/postgresql-window-function/)

Aggregate/window functions:
* `AVG`
* `MAX`
* `SUM`
* `COUNT`

Window Function | Description
--- | --- 
CUME_DIST | Return the relative rank of the current row.
DENSE_RANK | Rank the current row within its partition without gaps.
FIRST_VALUE(*attribute*) | Return a value evaluated against the first row within its partition.
LAG(*attribute, offset, default*) | Return a value evaluated at the row that is at a specified physical offset row before the current row within the partition. Default is `NULL` if omitted.
LAST_VALUE(<attribute>) | Return a value evaluated against the last row within its partition. This has optional frame clause at the end of the expression: `RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` because by default the frame clause is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
LEAD | Return a value evaluated at the row that is offset rows after the current row within the partition.
NTILE | Divide rows in a partition as equally as possible and assign each row an integer starting from 1 to the argument value.
NTH_VALUE | Return a value evaluated against the nth row in an ordered partition.
PERCENT_RANK | Return the relative rank of the current row (rank-1) / (total rows – 1)
RANK() | Rank the current row within its partition with gaps. 
ROW_NUMBER() | Number the current row within its partition starting from 1. (No arguments required in parentheses)
---


```sql
SELECT <attributes>,
    <window_function> OVER (
        PARTITION BY <partition_expression>
            ORDER BY <sort_expression> ASC | DESC NULLS {FIRST | LAST }
        ) AS <column_name>

```
Example window function: `AVG(price) OVER (PARTITION BY group_name)`

### frame_clause
The frame_clause defines a subset of rows in the current partition to which the window function is applied. This subset of rows is called a frame.

If you use multiple window functions in a query:
```sql
--Example
SELECT
    wf1() OVER(PARTITION BY c1 ORDER BY c2),
    wf2() OVER(PARTITION BY c1 ORDER BY c2)
FROM table_name;
```
you can use the WINDOW clause to shorten the query as shown in the following query:
```sql
--Example
SELECT 
   wf1() OVER w,
   wf2() OVER w,
FROM table_name
WINDOW w AS (PARTITION BY c1 ORDER BY c2);

```
#### Example of `RANK()`
```sql
RANK () OVER (
		PARTITION BY group_name
		ORDER BY
			price
	)
```
#### Example of `LAG()` 
The following statement uses the LAG() function to return the prices from the previous row and calculates the difference between the price of the current row and the previous row.
```sql
-- Using windows_functions_test_db database.
-- 
SELECT
	product_name,
	group_name,
	price,
	LAG (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS prev_price,
	price - LAG (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS cur_prev_diff
FROM
	products
INNER JOIN product_groups USING (group_id);
```

## Common Table Expressions (CTE)   
* [Resource: What Is a Common Table Expression (CTE) in SQL? | LearnSQL.com](https://learnsql.com/blog/what-is-common-table-expression/) 

```sql
-- Syntax 
WITH my_cte AS ( --> Start of CTE query
  SELECT a,b,c
  FROM T1
)
SELECT a,c --> Start of main/outer query
FROM my_cte
WHERE ....

-- Example
WITH highest AS (
  SELECT
    branch,
    date,
    MAX(unit_price) AS highest_price
  FROM sales
  GROUP BY branch, date
)
SELECT
  sales.*,
  h.highest_price
FROM sales
JOIN highest h
  ON sales.branch = h.branch
    AND sales.date = h.date
```
### Using CTEs in Advanced SQL Queries

You can define two or more CTEs and use them in the main query:
```sql
-- Example
WITH london1_monthly_revenue AS (
  SELECT
    EXTRACT(MONTH FROM date) as month,
    SUM(unit_price * quantity) AS revenue
  FROM sales
  WHERE EXTRACT(YEAR FROM date) = 2021
    AND branch = 'London-1'
  GROUP BY 1
), --> Separate the 2 CTE expressions with a comma.
london2_monthly_revenue AS (
  SELECT
    EXTRACT(MONTH FROM date) as month,
    SUM(unit_price * quantity) AS revenue
  FROM sales
  WHERE EXTRACT(YEAR FROM date) = 2021
    AND branch = 'London-2'
  GROUP BY 1
)
SELECT
  l1.month,
  l1.revenue + l2.revenue AS london_revenue,
  l1.revenue AS london1_revenue,
  l2.revenue AS london2_revenue
FROM london1_monthly_revenue l1, london2_monthly_revenue l2
WHERE l1.month = l2.month
```
## Nested CTEs in SQL Queries
This query has a nested CTE – note the FROM in the second CTE referring to the first. 
```sql
-- Example
WITH over_90_items AS (
  SELECT DISTINCT
    item,
    unit_price
  FROM sales
  WHERE unit_price >=90
), --> Separate the 2 CTE expressions with a comma.
london2_over_90 AS (
  SELECT
    o90.item,
    o90.unit_price,
    coalesce(SUM(s.quantity), 0) as total_sold
  FROM over_90_items o90
  LEFT JOIN sales s
  ON o90.item = s.item AND s.branch = 'London-2'
  GROUP BY o90.item, o90.unit_price
)
SELECT item, unit_price, total_sold
FROM   london2_over_90;
```
## SQL with SQLite in Python
* **See jupyter notebook or Compass walkthrough for full steps**:
C:\Users\silvh\OneDrive\lighthouse\data-exercises\drinks-tutorial-09-26\w02d01\src\notebooks\2022-09-27 SQLite in python.ipynb 
* [Link to walkthrough](https://data.compass.lighthouselabs.ca/b9e08cd5-68c6-490c-a32b-a66f01bf53e1)
* [Web resource from Data to Fish: Pandas DataFrame to SQL (with examples)](https://datatofish.com/pandas-dataframe-to-sql/)

```python
import sqlite3
from sqlite3 import Error

# The following script creates a connection to the SQLite database:
def create_connection(path):
    connection = None
    try: # Uses .connect() from the sqlite3 module and takes the SQLite database path as a parameter
        connection = sqlite3.connect(path) # 
        print("Connection to SQLite DB successful")
    except Error as e: # catches any exception that might be thrown if .connect() fails to establish a connection.
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("<filename>.sqlite")
# The database file will be created automatically if it doesn't exist. If it does the code above will connect Python to the existing database.
```
Dataframe can be converted into an SQL database using `df.to_sql`:
```python
df.to_sql(table_name, connection, if_exists="append", index=False) 
# This automatically creates columsn that match the dataframe
```
To fetch SQL data, use `pd.read_sql_query`:
```python
pd.read_sql_query(query_string, connection)
```
To write to the database, use `connection.cursor()` and `cursor.execute(<SQL query>` (`cursor` is just the user-defined delayed version of `connection.cursor`). 
* Optional: You can define a custom function to spit out if a query was successful or not.:
```python
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
```
## PostgreSQL in Python
[Working with PostgreSQL in Python (stackabuse.com)](https://stackabuse.com/working-with-postgresql-in-python/)

# Pandas Series

Function/Method | Description
--- | ---
`df.sample()` | Return a random sample of items from a dataframe. [See documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html).

### Pandas data types
```python
import pandas as pd
# Create a pandas series
series = pd.Series(data)

# Create a pandas dataframe
df = pd.DataFrame(data)

# Create dataframe from CSV file
df = pd.read_csv('filename.csv')

# Take a random sample of nrows
df = pd.read_csv('filename.csv').sample(n=nrows, random_state=0)

# Create CSV file from dataframe
df.to_csv('csv_example') 
```
* [Reference: Pandas DataFrame: Playing with CSV files | by Deepak K Gupta (DAKSH) | Towards Data Science](https://towardsdatascience.com/pandas-dataframe-playing-with-csv-files-944225d19ff)

**Optional parameters**

`series = pd.Series(<data, e.g.ndarray, dictionary>, index = [list of row indices], name = <name of a single series>, columns = <list of column indices>)`

Optional arguments for `pd.read_csv` and `df.to_csv` include:
* `index = False` if CSV file includes an index that we don't need
* `header = 0` to specify which row(s) act as header (use list if multiple), or `header = False` for no header
    * Dataframe data only starts after last header row
* `names = [<column names>]`
* `sep ='<delimiter>'`
* `index_col=<integer>` assigns the column that will act as the row index (use list if multiple)
* `nrows=<# of rows to load from CSV file`

Set the row index using a column from the CSV file:
* `df.set_index('<column name>')`: This requires that the DataFrame already exists.

[Reference: Pandas Basics I](https://data.compass.lighthouselabs.ca/298f04d4-a639-48bc-b200-ed687dbbcfb0)
* `df.head()` to show first few rows
* `df.tail()` to show last few rows


## Attributes of Pandas objects

* `df.shape` to get the rows x columns
* `df.dtypes` (or `df.StringDtype` for strings)
* `df.astype()` to convert one data type to another, making a copy as default (pass copy=False to change this behavior)
* `df.index` to access row indices
* `df.columns` to access column indices
* `df.values` to access values
* `df.<column name>` accesses the data for a particular column
* `df.<index name>.array` accessed the data as a type `pandas.core.arrays.numpy_.PandasArray`
* `Series.to_numpy()` converts a Series to ndarray (Numpy)
    * NumPy arrays have one dtype for the entire array, while Pandas DataFrames have one dtype per column. When you call DataFrame.to_numpy(), Pandas will find the NumPy dtype that can hold all of the dtypes in the DataFrame. This may end up being an object, which requires casting every value to a Python object. This can lead to very expensive (time and memory-consuming) operations.
* `df.groupby(<column>)`

[Reference: Pandas Basics II](https://data.compass.lighthouselabs.ca/28b18104-1a70-494d-928f-b39da3324ebd)
## Slicing
Slicing pandas data is different from regular python because end of the index is inclusive.
* `df.loc[rows,columns]` accesses the explicit index
* `df.iloc[rows,columns]` accesses the implicit index (i.e. based on sequence)
* `df.ix[rows,columns]` allows you to access either implicit or explicit index

## Descriptive Statistics
Generally speaking, these methods take an axis as an argument and the axis can be specified by name or integer. Think of axis as the **axis of the result**.
```python
df.mean(0) # Aggregation for each column

df.mean(1) # Aggregation for each index
```
Dataframe Method | Description | Index Function 
--- | --- | ---
`df.describe()` | Summary statistics for numerical data. For non-numerical series object, provides the number of unique values and most frequently occurring values
`count` | Number of non-NA observations | 
`sum` | Sum of values | 
`mean` | Mean of values | 
`mad` |Mean absolute deviation | 
`median` |Arithmetic median of values | 
`min` | Minimum | `idxmin()`
`max` | Maximum | `idxmax()`
`mode` | Mode(s) | 
`abs` | Absolute Value | 
`prod` | Product of values | 
`std` | Bessel-corrected sample standard deviation | 
`var` | Unbiased variance | 
`sem` | Standard error of the mean | 
`skew` | Sample skewness (3rd moment) | 
`kurt` | Sample kurtosis (4th moment) | 
`quantile` | Sample quantile (value at %) | 
`cumsum` | Cumulative sum | 
`cumprod` |Cumulative product | 
`cummax` | Cumulative maximum | 
`cummin` | Cumulative minimum | 

## Counting values in Series
* `series.value_counts()` computes a histogram of a 1D array of values. This does not work for dataframes, but can work a slice of the dataframe.

## Modifying
* `df.reindex(index=<list of row index>, columns=<list of column index>`
    * Existing data is re-ordered to match new labels
    * `NA` is inserted in if no data exists for new label
* `df.drop(<list of index>, axis=<0 or 1>)` removes the specified rows/columns
* `df.dropna()` drops missing values
* `rename()` method allows for relabelling an axis based mapping (dict or Series) or a function
    * Rename based on function: `series.rename(str.upper)`
    * Rename using a `dict` or `Series`:
        * `df.rename(columns={<originalName>: <newName>},index = {<originalName>: <newName>})`
        * `df.rename({mapping}, axis='index'`
    * Rename using a regular expression: `df.columns = df.columns.str.replace(r'<pattern>', r'<replacement>')`
* `df.copy()`
* `df.to_string()` 
* `df.unique()`, `df.nunique()`

Here's an example of how to split a column where each cell contains values (`ll` for longitude and lattitude) separated by a comma:
```python
data['ll'] = data['Latitude'].astype(str) + ',' + data['Longitude'].astype(str)
```

**[Back to top](#table-of-contents)**

## Sorting 

```python
# Sort by index names
df.sort_index() # sorts by row index
df.sort_index(ascending=False) # sorts by reverse order
df.sort_index(axis=1) # sorts by column names 

```
`DataFrame.sort_values()` method is used to sort a DataFrame by its column or row values:
```python
df.sort_values(by="<column or row name>") # the "by" parameter can also be a list for sorting by multiple columns/rows
```
## Grouping
* `df.groupby()`
    * Optional argument: `as_index=False` to keep the groupby column as data instead of as in index
* `df.sort_index()`
* `df.T` gives the transpose

## Aggregation
Combine multiple aggregate functions  using `.agg()` method
```python
df.groupby(<column_name>).agg(['min','max','mean'])

df.groupby(<column1_name>).agg({<column2_name>: np.sum, <column3_name>: np.max})

# Example: Create a column named "mean_weight" with the mean of Item_Weight:
data.groupby('Item_Type').agg(mean_weight=('Item_Weight','mean'))
```

## Filtering Dataframes
### Rows
Method | Description
--- |---
`df.where(<Boolean filter>)`
`df.select_dtypes(include=[<data type>])` | Takes only the selection of columns based on their dtype.
`isin(<filter>)` | Take only rows where the data matches one of the the specified items in the filter (filter can be a list).

### Columns
[Resource: Interesting Ways to Select Pandas DataFrame Columns | by Casey Whorton | Towards Data Science](https://towardsdatascience.com/interesting-ways-to-select-pandas-dataframe-columns-b29b82bbfb33#:~:text=Selecting%20columns%20based%20on%20their,Returns%20a%20pandas%20series.&text=Passing%20a%20list%20in%20the,columns%20at%20the%20same%20time.)

Description | Filter IN | Filter OUT
--- | --- | ---
Select columns based on a given string in column name |  | `df[df.columns[~df.columns.str.contains('string')]]`
Select columns based on a given regex in column name | `df.filter(regex='regex')` | `df.loc[:,[False if re.search('regex',column) else True for column in df.columns]]`

## Boolean comparisons
Series and DataFrame have binary comparison methods whose behavior is vectorized, e.g. `df1.eq(df2)`
* `eq`
* `ne`
* `lt`
* `gt`
* `le`
* `ge`
* `df.bool()`
* `df.between()`

Evaluate True or False:
Function | Description
--- | -
`df.isna()` | Return a boolean same-sized object indicating if the values are NA.
`df.notna()` | Inverse of `isna`
---

You can apply these reductions to summarize a boolean result.
* `any()`
* `all()`
* `bool()`
* `empty`
* `(<boolean_expression>).any().any()` returns a single Boolean result for entire dataframe/series.
* `equals(<data>)` method should be used instead of `==` in case there is a `NaN` in the data because `np.nan == np.nan`
    * Note that the Series or DataFrame index needs to be in the same order for the equality to be True.

Examples:
```python
# Returns Boolean for each row.
(df > 0).all()

# compares whether df+df is equal to df*2
(df + df).equals(df * 2)
```
Example: Filtering rows based on value counts
```python
# Create a series with the value counts for a particular column
count = world['continent'].value_counts()

# Specify the condition on which to filter
condition = count > 1 # Keep only rows where its 'continent' shows up in the dataframe more than once.

# Create the filter 
filter = world['continent'].isin(condition[condition].index)

# Confirm the filter worked correctly by doing a value_count with the filter applied
world[filter]['continent'].value_counts()
```

## Setting Values in the DataFrame
Method 1 | Description | Method 2
--- | --- | --- 
`df.iat[row,column]` = | Set value by implicit position | `df.iloc[row,column] =` 
`df.at[row,column name]` =  | Set value by label | `df.loc[row,column name]` = 

## Other handy functions

Function/Method | Description
--- | ---
`df.set_index(keys) | Set the DataFrame index (row labels) using one or more existing columns. [See documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html).

## Accessing Date and Time Properties from Series
[See Pandas documentation](https://pandas.pydata.org/pandas-docs/version/0.23/api.html#datetimelike-properties)

If a Series is datetime/period-like, date and time properties can be accessed and transformed with `.dt`:
* `s.dt.hour` obtains the hour
* `s.dt.second`
* `s.dt.day`
* `s.dt.dayofweek`
* `s.dt.isocalendar().week` for [week number of the year](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.isocalendar.html#pandas.Series.dt.isocalendar)
* `s.dt.tz_localize('US/Eastern')`
* `s.dt.tz` provides time zone information
* `s.dt.tz_convert('US/Eastern)`

**[Back to top](#table-of-contents)**
## Strings

String processing methods can be used on elements of the Pandas array using the `.str` attribute. 
*They generally have names matching the equivalent scalar methods*, e.g.:
* `s.str.lower()`
* `s.str.contains('string')` or `df.column.str.contains`('string')

## Iterations in Pandas
Iterating through Pandas objects is generally slow. In many cases, iterating manually over the rows is not needed and can be avoided.
* Basic iteration (for i in object) produces:
    * Series: values
    * DataFrame: column labels (not values)
* To iterate over the rows of a DataFrame, you can use the following methods:
    * `items()`: to iterate over the (key, value) pairs.
        * Series: (index, scalar value) pairs
        * DataFrame: (column, Series) pairs
    * `iterrows()`: Iterate over the rows of a DataFrame as (index, Series) pairs. 
        * It returns an iterator yielding each index value along with a Series containing the data in each row:
        * This converts the rows to Series objects, which can change the dtypes and has some performance implications.
    * `itertuples()`: Iterate over the rows of a DataFrame as namedtuples of the values. 
        * The first element of the tuple will be the row’s corresponding index value, while the remaining values are the row values.
        * This is a lot faster than iterrows() and is in most cases preferable to use to iterate over the values of a DataFrame.

### Creating column/index names with number appended

```python
col = ['first_column_name'] + ['column_name_%d'%i for i in range(1,10)]
```

**[Back to top](#table-of-contents)**

## [Pandas Merge and Groupby](https://data.compass.lighthouselabs.ca/51a4b566-8b66-4e76-a34e-3354a6cef47b)

Function | Description | SQL equivalent
-- | -- | --
`concat(<data>)` | Concatenate Pandas objects together. Default is vertical stacking (joining rows) | `UNION`
`merge(<df1>,<df2>, on=<key>)` | Inner join between tables. [See documentation](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). | `INNER JOIN`
`merge(<df1>,<df2>, on=<key>, how='outer')` | Outer left/right join between tables | `LEFT/RIGHT JOIN`

## Pandas Reshaping
[Walkthrough](https://data.compass.lighthouselabs.ca/44c3f2b9-5d55-4d63-bc74-3635c5c5ed0e)
* The `stack()` method "compresses" a level in the DataFrame's columns
* `unstack()` does the inverse, by default unstacks the last level unless specified
    * * `unstacked(0)` unstacks the first level

### Pivot Tables
`pandas.pivot_table(<data>)`

## Resetting Index
Description | Commamd | Nots
--- | ---- | ---
Convert Index to Column | `df.reset_index(inplace=True)`

## Pandas Apply Functions
[Walkthrough](https://data.compass.lighthouselabs.ca/ce0fc06d-9ed5-4024-9d67-179003ac67ee)

[I previously did this in data prep exercise](/W03/2022-10-05-data_preparation_exercise/data_prep_exercise.ipynb)


### tablewise function application: `pipe()` 
* [pandas doccumentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pipe.html?highlight=pipe#pandas.DataFrame.pipe)
### row or column-wise function application: `apply()`
```python
df.apply(<function>,args=(arg1,arg))
```
* args must be a tuple; if only 1 argument, `args=(arg,)`

# APIs
## Command Line API Calls
```commandline
curl --request GET \
     --url "https://api.foursquare.com/v3/places/search?ll=45.6387,-122.6615&radius=100" \
     --header 'Accept: application/json' \
     --header 'Authorization: '"$FOURSQUARE_API_KEY"''
```
## Python API Calls
[Reference: Python’s Requests Library (Guide) – Real Python](https://realpython.com/python-requests/)
### GET
```Python
import requests
import os

response = requests.get('https://api.github.com')

# Turn GET request to JSON data
json = response.json()
```
* `response.status_code` returns status code
    * If you use a `response` instance in a conditional expression, it will evaluate to `True` if the status code was between 200 and 400, and `False` otherwise
* `response.raise_for_status()` raises an `HTTPError` for certain status codes. If the response was successful, no Exception will be raised.
* `response.json()` turns JSON content into a dictionary
* `response.headers` returns the headers of the response when used alone
* `response.headers[<header key>]` allows for access to header values (case *in*sensitive)

### POST Method

```Python
response = requests.post(<URL>, data=<dictionary or list of tuples>)

# Or, for JSON data:
response = requests.post(<URL>, json={'key':'value'})
```
### Inspecting Your Request
* `response.request.headers`
* `response.request.headers[<header key>]`
* `response.request.url`
* `response.request.body`

### Parameters in requests (follow by `=`)
* `timeout`: 
    * An integer or float representing the number of seconds to wait on a response before timing out, or
    * A tuple of 2, where:
        * first element being a connect timeout (the time it allows for the client to establish a connection to the server)
        * second being a read timeout (the time it will wait on a response once your client has established a connection)

### [Session Object](https://realpython.com/python-requests/#the-session-object)
Sessions are used to persist parameters across requests. For example, if you want to use the same authentication across multiple requests, you could use a session:
```Python
import requests
from getpass import getpass
```
### [Resource: Retry the Same Request](https://realpython.com/python-requests/#max-retries)

# JSON
## Simple JSON Files
All arrays inside need to have arrays of same length for these functions to work:
* `read_json()` can load JSON either from a file or a url.
* `<data>.to_json()` writes the data object to a JSON file.

```python
url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json"
first_json = pd.read_json(url)
first_json.head()

first_json.to_json('json_columns.json', orient="columns")
first_json.to_json('json_index.json', orient="index")
```
## Nested JSON Files
Use:
* `json.load` from `json` library
* `json_normalize(<data>, record_path=<key>)` from `pandas.io.json import json_normalize`  
```python
import json

# Open the JSON file
with open("nested.json") as f:
    nested_json = json.load(f)

# use a function from Pandas json_normalize()
from pandas import json_normalize
json_normalize(nested_json, record_path=<key>, meta=[<list of columns to get>])
```
Handy package for printing JSON data so it's easier to read:
```python
from pprint import pprint
 
pprint.pprint(nested_json)
```
## Saving Python JSON objects to files
* [web reference](https://www.codegrepper.com/code-examples/python/save+request+response+json+to+file+python)

```python
with open(f'foursquareBar0','w') as json_file:
    json.dump(json_oject, json_file)

# If saving multiple API GET requests that are stored in a dictionary:
for key, value in responses.items():
    with open(f'foursquareBar{key}.json','w') as json_file: 
        json.dump(responses[key].json(), json_file)
```
## [Modes of file handling (e.g. for `open`)](https://www.w3schools.com/python/python_file_handling.asp)
* `'w'` means it is in write mode: New file created if not exising; if filename already exists, it gets overwritten. 
* `"r"` - Read - Default value. Opens a file for reading, error if the file does not exist
* `"a"` - Append - Opens a file for appending, creates the file if it does not exist
* `"x"` - Create - Creates the specified file, returns an error if the file exists

# [XML Parsing](https://data.compass.lighthouselabs.ca/activities/390)
* [Documentation: The ElementTree XML API for Python](https://docs.python.org/3/library/xml.etree.elementtree.html)
* [JSON formatter XML Parser](https://jsonformatter.org/xml-parser)

```python
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')

# To get the main (root) tag of the file:
root = tree.getroot()

firstchild = root[0]

first_child_of_firstchild = root[0][0]

# Get the tag
print('Tag of first child: ',firstchild.tag)

# Get the text inside grandchild
print('Text of first grandchild: ',first_child_of_firstchild.text)

```

* An XML tree consists of children and their children. These collectively are **elements**.
* All elements have tags.
* Elements have:
    * attributes,
    * attributes and children,
    * values, or
    * values and children.


container | info labelled using... | info contained
-- | -- | -- | 
Child | Tag | Text
Attribute | Key | Value

For example: `<country>` "Canada" `</country>`
- `country` is the tag
- `name="Canada"` is an attribute

Method | Input(s) | Output | Notes
---| --- | --- | -
`root.findall(<tag>)` | element | children | Argument can be a path to desired element: `"root./child/grandchild"`. `root.findall('.')` gets all top-level elements. See below.
`child.find(<child_of_child>).text` | element | text
`child.get(<child_attribute>)` | attribute key | attribute value
`<element_tag>.attrib`  | element | attribute key-value pairs
`root.tag` | element index | element tag
`len(root)` | element | Number of children
 
[Copied from Compass] Here are some tips and tricks on how to work with `root.findall()`:
```python
# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level elements
root.findall("./country/neighbor")

# elements with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' elements that are children of elements with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' elements that are the second child of their parent
root.findall(".//neighbor[2]")
```
## Iterating in XML
* Use `root.iter(<child>)` to iterate over the given child in a loop
    * e.g. `for neighbor in root.iter('neighbor'): [...]`
* Use `enumerate(<element>)` to get the index and elements in a loop:

```python
for i, child in enumerate(root):
    print(f"Child {i}: {child.tag}")
    for gc in child:
        print(f"\t\t{gc.tag}")
```
## Converting XML to JSON
```python
import xmltodict, json

obj = xmltodict.parse("""
<employees>
    <employee>
        <name>Dave</name>
        <role>Sale Assistant</role>
        <age>34</age>
    </employee>
</employees>
""")
print(json.dumps(obj))
```

# Other Data Types
## CSV
```python
# Create dataframe from CSV file
df = pd.read_csv('filename.csv')

# Take a random sample
df = pd.read_csv('filename.csv').sample(n=10000, random_state=0)

# Save dataframe to CSV:
df.to_csv('filename.csv')
```
## Excel

```python
import pandas as pd
import openpyxl

wine_xlsx = pd.read_excel('data/wine.xlsx', engine = 'openpyxl')

# If data not on first sheet
wine_2 = pd.read_excel('data/wine_2.xlsx', sheet_name='DATA', engine = 'openpyxl') 

# Export to Excel
df.to_excel("test2.xlsx", sheet_name="test")
```
## HTML
[Walkthrough: HTML](https://data.compass.lighthouselabs.ca/activities/395)
### Converting Tables to DataFrames
```python
import pandas as pd
import requests

# Perform a GET request
url = 'https://www.worldcoinindex.com/'
crypto_url = requests.get(url)

# Create an object with the full HTML source code 
body = crypto_url.text
```
If the HTML source has a table which is marked by the HTML tag `<table></table>` (this tag is used for defining a table in HTML), Pandas uses `pd.read_html()` to extract the table from the HTML document.
```python
crypto_data = pd.read_html(body)

# The above line creates a list with one element which is our table. Therefore:
crypto_data = crypto_data[0]
```

### HTML Scraping


If we want to extract information from HTML, which doesn't have a table, we need to use a different approach: Scraping. Fortunately, Python has a great package for this called Beautiful Soup.
```python
from bs4 import BeautifulSoup
import requests

scrape_url = 'https://canada.ca/en/services/science.html'
page = requests.get(scrape_url)
soup = BeautifulSoup(page.content, 'html.parser')
```

## Text
```python
with open('data/sample.txt', 'r') as f:
    data = f.readlines() # This stores the text file as a list of each line in the text

# Import required package
import nltk
# This might only be required the first time?
nltk.download('punkt') 

tokens = nltk.word_tokenize(data)
```
Read a table of fixed-width formatted lines into DataFrame.
```python
pandas.read_fwf('filepath_or_buffer')
```
## From 2022-09-28 lecture: Functions that help you Tidy your Data
Review on your own after class

* pd.pivot() - Return reshaped DataFrame organized by given index / column values. 
* pd.pivot_table()
* pd.melt()  - Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

**[Back to top](#table-of-contents)**

## Images
Key functions are: 
* `Image.open(<filename>)`
* `plt.figure(figsize=(x, y))`
* `plt.imshow(imageObject)`
```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

myImage = Image.open("./flower_square.jpg")
plt.figure(figsize=(9, 6))
plt.imshow(myImage) # Plot the image
```
Convert the image to a 3D NumPy array.
* In the array shape, the first two dimensions represent the size of the picture. 
* 3rd dimension is size 3, representing each layer for gred, blue, and green.
```python
imgmat = np.array(myImage) # Converts to a 3D array
plt.figure(figsize=(9,6))
plt.imshow(imgmat)
```
The Numpy array can be adjusted to adjust the image appearance.

# Regular expressions
* [Reference: RegexOne - Learn Regular Expressions - Python](https://regexone.com/references/python)

 Expression| What it means
 --- |-
\d | Any Digit
\D | Any Non-digit character
. | Any Character
\\. | Period
[abc] | Only a, b, or c
[^abc] | Not a, b, nor c
[a-z] | Characters a to z
[0-9] | Numbers 0 to 9
\w | Any Alphanumeric character
\W | Any Non-alphanumeric character
{m} | m Repetitions
{m,n} | m to n Repetitions 
 \* | Zero or more repetitions
\+ | One or more repetitions
? | Optional character
\s | Any Whitespace
\S | Any Non-whitespace character
^word | Starts with
$ | Ends with
(…) | Capture Group
(a(bc)) | Capture Sub-group
(.*) | Capture all
(abc\|def) | Matches abc or def
`\b` | word boundary on python
 
* Raw strings begin with a special prefix (r) and signal Python not to interpret backslashes and special metacharacters in the string, allowing you to pass them through directly to the regular expression engine.

## Regular Expressions in Python
Regular expressions are created in python by adding the prefix `r` in front of a string; this is known as a *raw string*.
Function (`re.`)/Method (`match.`) | Description
--- | ---
`re.search()` | Test whether a regular expression matches a specific string. Either returns `None` if the pattern doesn't match, or a `re.MatchObject` with additional information about which part of the string the match was found. This method stops after the first match.
`re.match()` | Similar to `re.search()` except only searches at the beginning of the string.
`re.fullmatch()` | If the whole string matches the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern.
`<match>.group(0)` or `<match>.group()` | always returns the fully matched string
`<match>.group(1)`, `<match>.group(2)`,... | will return the capture groups in order from left to right in the input string
`<match>.expand()` | Return the string obtained by doing backslash substitution on the template string template, as done by the `sub()` method.
`re.findall()` | perform a global search over the whole input string. If there are capture groups in the pattern, then it will return a list of all the captured data.
`re.finditer()` | an iterator of `re.MatchObjects` to walk through to provide more context for each match, such as `match.start()` and `match.end()`

```python
import re
matchObject = re.search(regex, input_string, flags=0)
```
### Iterating
```python
# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print("Match month: %s" % (match))

# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print("Match at index: %s, %s" % (match.start(), match.end()))
```

### Finding and replacing strings
Use `re.sub()` method
```python
replacedString = re.sub(pattern, replacement_pattern, input_str, count, flags=0)
```
### Referencing captured groups
many systems allow you to reference your captured groups by using `\0` (usually the full matched text), `\1` (group 1), `\2` (group 2), etc. 
```python
# Lets try and reverse the order of the day and month in a date 
# string. Notice how the replacement string also contains metacharacters
# (the back references to the captured groups) so we use a raw 
# string for that as well.
regex = r"([a-zA-Z]+) (\d+)"

# This will reorder the string and print:
#   24 of June, 9 of August, 12 of Dec
print(re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12"))
```
`flags` argument in python regular expression methods:
Flag | Description
--- | ---
re.IGNORECASE | makes the pattern case insensitive so that it matches strings of different capitalizations
re.MULTILINE | is necessary if your input string has newline characters (\n), this flag allows the start and end metacharacter (^ and $ respectively) to match at the beginning and end of each line instead of at the beginning and end of the whole input string
re.DOTALL | allows the dot (.) metacharacter match all characters, including the newline character (\n)

### Compiling a pattern for performance
This method returns a `re.RegexObject`, which has exactly the same methods as above, except that they take the input string and no longer require the pattern or flags for each call.
```python
regexObject = re.compile(pattern, flags=0)
```
Examples: 
```Python
# This will print:
# Hello
# Bonjour
# for each of the captured groups that matched
for result in regexObject.findall("Hello World, Bonjour World"):
    print(result)

# This will substitute "World" with "Earth" and print:
#   Hello Earth
print(regexObject.sub(r"\1 Earth", "Hello World"))
```
# Data Visualization: Matplotlib
[Reference: Introduction to Matplotlib — Data Visualization in Python | by Ehi Aigiomawu | Heartbeat (comet.ml)](https://heartbeat.comet.ml/introduction-to-matplotlib-data-visualization-in-python-d9143287ae39)

<img src ="https://cdn.discordapp.com/attachments/1017164944963280948/1029974050962939944/unknown.png">

```python
import matplotlib.pyplot as plt
%matplotlib inline # In Jupyter notebook, this turns on matplotlib mode to output the figure each time without having to write `plt.show()`
```

## Summary

Task | Functional Approach | Object-Oriented (Method/Stateless) Approach | Alternative Object-Oriented Approach
--- | --- | --- | --
Create the plot* | `plt.plot(x,y)` | `plt.figure()` (creates empty figure) | `fig, ax = plt.subplots(x,y)` 
Set the dimensions | *Optional*: `figsize()=(width,height)` in `plt.plot()` parameter | `ax = fig.add_axes([left_position, bottom_position, width, height])` | pass the parameters `figsize=(width,height)` to `plt.subplots()`
Create the plot part 2* | n/a | `ax.plot(x, y, 'purple')` | `ax.plot(x,y,'red')`
Label figure | `plt.title('title')` | `ax.set_title('Plot Title')` | `fig.suptitle('Figure title')`[See documentation](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html). | Add overall figure title if there are subplots
Create Axis |  | `ax = plt.axes()`
Label axes | `plt.xlabel('axis label')`| `ax.set_xlabel('axis label')`
. | `plt.ylabel('axis label')` | `ax.set_ylabel('Y Axis Label')`
Create subplots part 1| `plt.subplot(nRows, ncolumns, plt_number)` | `fig, axes = plt.subplots(nrows=3, ncols=3)`
 ...part 2| `plt.plot(x,y)` | `ax[0,1].plot(x,y)` [next line] `plt.tight_layout()`
 Add legend |  | [`leg = ax.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html)
`label='label'` param | | pass to `ax.plot()`
Legend Title | - | `leg.set_title(title='Legend Title')`
Set axis range |  | `ax.set_xlim([lower_bound,upper_bound])` | `fig.axis(ymin=lower_bound,ymax=upper_bound)`
Tightly fit axes | `plt.tight_laytout()` | `ax.axis('tight')` | [`fig.tight_layout(rect=[0, 0, 1, 0.98])`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.tight_layout)
Horizontal line | - | [`ax.axhline(y=0)`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html)
Set ticks | - | `ax.xaxis.set_ticks(xticklabels)`
Tick labels | - | `ax.set_xticklabels(xticklabels)`
Rotate tick labels | - | `ax.tick_params(axis='x', labelrotation = 30)`
Grid | - | `ax.grid()`
Annotate | `plt.annotate('annotation text')` | `ax.annotate('annotation text')`
Add grid | `plt.grid()` | 

Parameter | Description
--- | ---
`alpha=0.7` | Make the plot transparent
`marker='o'` | Change marker shape. [See documentation](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers).
`color=` | Set color of plot. [See documentation](https://matplotlib.org/stable/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py).

## Types of figures
* Default is line plot. Replace `.plot()` with any of the below:

Method (`ax._`) or function (`plt._`) | Description
--- | ---
`.hist()` | histogram
`.scatter()` | scatter plot
`.bar()`
`.hist(y)` | parameter: `bins=integer`

### Functional Approach

```python
x = np.linspace(0,10,20)
y = x**2
plt.plot(x,y)

plt.title('Figure Title')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

plt.show() # On last line if not in Jupyter
```
To specify figure size, aspect ratio, and DPI, use these parameters in `plt.figure()` or `plt.subplots()`:
* `figsize()=(width,height)`, where dimensions are in a tuple in **inches**.
* `dpi=100` for DPI

## Creating multi-plots using `plt.subplot()` method

`plt.subplot(nRows, nColumns, plot_number)`
```python
# Set the number of rows and columns int he figure, then specify which subplot you'll plot next
plt.subplot(1, 2, 1) # Figure has 1 row, 2 columns, then we make subplot #1.
plt.plot(x, y, 'red') # Colour attribute set to red.
```

## Object Oriented Interface
Create `Figure` objects and call methods off it.
```python
fig = plot.figure()

# Add the axes
ax = fig.add_axes([left_position, bottom_position, width, height])

# Plot the x and y arrays
ax.plot(x, y, 'purple')

# Add labels and title
ax.set_xlabel('X Axis Label')
ax.set_ylabel('Y Axis Label')
ax.set_title('Plot Title')
```

## Create multiple figures on the same canvas
### Option 1: Set the axes to the positions so the figures display the way you want.
This is useful if you want a plot within a plot.
```python
axes1 = fig.add_axes([<parameters for figure 1>])
axes2 = fig.add_axes([<parameters for figure 2>])
axes1.plt(x,y)
axes2.plt(y,x)
```

### Option 2: Using `plt.subplots()` method (note the `s` at the end)
`plt.subplots()` is a function which creates and returns a Figure object and either an Axes object or an array of Axes objects.
* Giving the Figure and Axes names allows us to add to, modify, and customize these objects individually.
* Useful for creating subplots of equal size in rows/columns.
```python
# Create an empty canvas of 3x3 subplots
fig, axes = plt.subplots(nrows=3, ncols=3) # 'fig' is the canvas

# Create subplot in first row, middle column of the 3x3 figure:
ax[0,1].plot(x,y)

# If you need to space out overlapping axes:
plt.tight_layout()
```
If you want multiple series to be in the same plot, omit `nrows` and `ncols` (optional: specify figure dimensions in inches): 
```python
fig, axis = plt.subplots(figsize=(width, height))
```
To specify figure size, aspect ratio, and DPI, use these parameters in `plt.figure()` or `plt.subplots()`:
* `figsize()=(width,height)`, where dimensions are in a tuple in **inches**.
* `dpi=100` for DPI

### Option 3: Plotting multiple series from a dataframe using `df.plot()` method
[Documentation: `DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)

`df.plot()` will plot the dataframe and return an axes object that has the same methods as for matplotlib.
* If no parameters are given, then the entire dataframe is plotted using the index as the x values.

```python
ax = df.plot(x='x axis column',y=df.columns[1:],figsize=(5,2))
ax.set_title('title')
```
## Legends
```python
fig = plot.figure()
ax = fig.add_axes([left_position, bottom_position, width, height])

# Label one line with 'plot label'
ax.plt(x,y, label='plot label')

# Show the legend
ax.legend()
```
## Customizing figures
[matplotlib documentation on default values and styling](https://matplotlib.org/stable/api/matplotlib_configuration_api.html?highlight=rcparams#matplotlib.rcParams)
* [`matplotlib.markers`](https://matplotlib.org/stable/api/markers_api.html)
* [`matpotlib.lines`](https://matplotlib.org/2.0.1/api/lines_api.html)
* [Choosing Colormaps in Matplotlib — Matplotlib 3.6.0 documentation](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
* [Rotate axis labels](https://www.pythoncharts.com/matplotlib/rotating-axis-labels/)
* [Improve figure resolution](https://blakeaw.github.io/2020-05-25-improve-matplotlib-notebook-inline-res/)

### Setting defaults

Example code| Description
--- | ---
`plt.rcParams["figure.figsize"] = (10,6)` | Set default figure dize
`plt.rcParams["savefig.bbox"] = 'tight'` | Make sure figure edges don't get cropped around edges (relevant for Google Colab)

### Annotating figures
To add annotations we used the `plt.annotate()` function or `ax.annotate` method. The `xy` parameter is a tuple containing the position to which the arrow is pointing. The `xytext` is a tuple containing the position where the text of the annotation is placed.

```python
# Example using functional approach
plt.annotate('annotation text', xy =(5.0,3.5),
             xytext = (4.25,4.0), arrowprops={'color':'red'})

# Example using method/stateless approach
ax.annotate('annotation text', xy =(5.0,3.5),
             xytext = (4.25,4.0), arrowprops={'color':'red'})
```

## Save figure
Use the `.savefig()` method:
```python
fig.savefig('filename.png')

# Confirm the image by displaying it:
import matplotlib.image as mpimg

plt.imshow(mpimg.imread('filename.png'))
```
# Data Visualization: Seaborn
* Refer to [2022-10-03 lecture notes](./z%20course%20material/2022-10-03-dataviz-tutorial.ipynb)
* [Resource: Seaborn Styling, Part 1: Figure Style and Scale | Codecademy](https://www.codecademy.com/article/seaborn-design-i)
* [Documentation: Seaborn](https://seaborn.pydata.org/api.html)
* [Resource: An introduction to seaborn — seaborn 0.12.0 documentation (pydata.org)](https://seaborn.pydata.org/tutorial/introduction)

This allows for data visualzation with less code than matplotlib, but uses matplotlib under the hood.
```python
import seaborn as sns

sns.scatterplot(x=x_series, y=y_series, data=df)
plt.show()
```
If you want to tweak the plots, use matplotlib:
```python
ax = sns.scatterplot(x='total_bill', y='tip', data=df) # sns returns an ax object

# Change the default axis labels
ax.set_xlabel('Total Bill (USD)')
ax.set_ylabel('Tip (USD)')

# Manually set the range of an axis
ax.set_ylim(bottom=0)

plt.show()
```
Function/Method | Description
--- | ---
`sns.barplot()` | Bar graph with lines indicating 25th and 75th percentile (through there are better ways to show distribution)
`sns.boxplot()` | [Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot)
`sns.catplot()` | Plots categorical data. Specify type with `kind=` parameter, e.g. `'swarm'`, `'violin'`, or `'bar'`
`sns.countplot()` | Show the counts of observations in each categorical bin using bars. ([Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot))
`sns.displot()` | Distribution representation, e.g. histogram, with optional kernal density estimation if `kde=True` parameter given. 
`sns.displot(kind='ecdf)` | Empirical cumulative distribution function. 
`sns.heatmap()` | [Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.heatmap.html?highlight=heatmap#seaborn.heatmap); see also example below
`sns.histplot()`
`sns.jointplot()` | Plots the joint distribution between 2 variables
`sns.lineplot()`
`sns.lmplot()` | Include a linear regression model in a plot.
`sns.pairplot()` | shows joint and marginal distributions for all pairwise relationships and for each variable
`sns.relplot()` | (relationship plot) shows the relationship between multiple variables in the dataset 
`sns.scatterplot()`
`sns.violinplot()`


Function/Method | Description
--- | ---
`sns.set_theme()` | Apply the default theme. There are five preset seaborn themes: `darkgrid` (default), `whitegrid`, `dark`, `white`, and `ticks`. affect how all matplotlib plots look, even if you don’t make them with seaborn.
`sns.reset_defaults()` | Restore all RC params to default settings.
`colors = sns.color_palette("coolwarm", as_cmap=True)` | Set colour palette using a continuous colour gradient. This variable is then passed into the `palette=` parameter in the plotting function. [See Seaborne documentation for palette options](https://seaborn.pydata.org/tutorial/color_palettes.html?highlight=colormap).
`colors = sns.color_palette("coolwarm", n_colors=hue_unique_values)` | Set colour palette with a certain number of hues (i.e. for categorical data). [See Matplotlib documentation for palette options](https://seaborn.pydata.org/tutorial/color_palettes.html?highlight=colormap).
`colors = sns.mpl_palette('PRGn', n_colors=hue_unique_values)` | Set colour palette using Matplotlib palettes. [See documentation](https://matplotlib.org/stable/tutorials/colors/colormaps.html).

Data Parameter | Description
--- | ---
`x=` | independent variable
`y=` | dependent variable
`hue=` | colour
`size=` | size of element (e.g. line, marker)
`style=` | style of element 
`units=` | Grouping variable identifying sampling units. When used, a separate line will be drawn for each unit with appropriate semantics, but no legend entry will be added. Useful for showing distribution of experimental replicates when exact identities are not needed.
`row=` , `col=` | subplot position
`errorbar=('se', 1.96)` | Error bar. Default is 95% confidence interval. [See documentation](https://seaborn.pydata.org/tutorial/error_bars.html).

Customization Parameter | Type | Description
--- | --- | ---
`col_wrap=` | int | “Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a row facet.
`row_order=`, `col_order=` | lists of strings | Order to organize the rows and/or columns of the grid in, otherwise the orders are inferred from the data objects.
`palette=` | string, list, dict, or sns.colors.Colormap | Method for choosing the colors to use when mapping the hue semantic. String values are passed to color_palette(). List or dict values imply categorical mapping, while a colormap object implies numeric mapping. [See documentation for palette options](https://seaborn.pydata.org/tutorial/color_palettes.html?highlight=colormap).
`hue_order=` | vector of strings | Specify the order of processing and plotting for categorical levels of the hue semantic.
`Sizes=` | list, dict, or tuple | An object that determines how sizes are chosen when size is used. List or dict arguments should provide a size for each unique data value, which forces a categorical interpretation. The argument may also be a min, max tuple.
`size_order=` | (list) | Specified order for appearance of the size variable levels, otherwise they are determined from the data. Not relevant when the size variable is numeric.
`style_order=` | (list) | Specified order for appearance of the style variable levels otherwise they are determined from the data. Not relevant when the style variable is numeric.
`dashes=` | boolean, list, or dictionary | Object determining how to draw the lines for different levels of the style variable. Setting to True will use default dash codes, or you can pass a list of dash codes or a dictionary mapping levels of the style variable to dash codes. Setting to False will use solid lines for all subsets. Dashes are specified as in matplotlib: a tuple of (segment, gap) lengths, or an empty string to draw a solid line.
`markers=` | boolean, list, or dictionary | Object determining how to draw the markers for different levels of the style variable. Setting to True will use default markers, or you can pass a list of markers or a dictionary mapping levels of the style variable to markers. Setting to False will draw marker-less lines. Markers are specified as in matplotlib.
`legend=` | “auto”, “brief”, “full”, or False | How to draw the legend. If “brief”, numeric hue and size variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If “auto”, choose between brief or full representation based on number of levels. If False, no legend data is added and no legend is drawn.
`kind=` | string | Kind of plot to draw, corresponding to a seaborn relational plot. Options are "scatter" or "line".
`height=` | scalar | Height (in inches) of each facet. See also: aspect.
`aspect=` | scalar | Aspect ratio of each facet, so that aspect * height gives the width of each facet in inches.
`annot=True` | bool or rectangular dataset, optional | If True, write the data value in each cell. If an array-like with the same shape as data, then use this to annotate the heatmap instead of the data. Note that DataFrames will match on position, not index.

## Example: Scatterplot
```python
# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips") # Alternatively, we could have loaded them with pandas.read_csv() or built them by hand

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
# This plot shows the relationship between five variables in the tips dataset using a single call to the seaborn function relplot(). Notice how we provided only the names of the variables and their roles in the plot. Unlike when using matplotlib directly
```
Parameters used with `sns.replot()`:
* `kind=`
    * `line` for line graph


[Resource: How to Create a Seaborn Correlation Heatmap in Python?](https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e)

```python
# Function for plotting a correlation matrix and getting correlation values
def correlation(df):
    """
    Plot the correlation matrix.
    Returns the dataframe with the correlation values.
    """

    # Create a mask to exclude the redundant cells that make up half of the graph.
    mask = np.triu(np.ones_like(df.corr(), dtype=bool))

    # Create the heatmap with the mask and with annotation
    sns.heatmap(data=df.corr(numeric_only=True),mask=mask,annot=True)
    return df.corr()
```
<details>
<summary>Example: Correlation heat map </summary>

```python
import numpy as np
# Select the relevant columns from the original dataframe, if applicable
df1 = df.loc[:,'First_Column':'Last_Column']

# Create a mask to exclude the redundant cells that make up half of the graph.
mask = np.triu(np.ones_like(df1.corr(), dtype=bool))

# Create the heatmap with the mask and with annotation
sns.heatmap(data=df1.corr(numeric_only=True),mask=mask,annot=True)
```

</details>

# Data Visualization: 3D Plotting with Matplotlib
* [Reference: Three-Dimensional Plotting in Matplotlib | Python Data Science Handbook (jakevdp.github.io)](https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html)
* [The mplot3d Toolkit — Matplotlib 3.6.0 documentation
](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html)

Types of plot
Type | Method | Description
--- | --- | ---
Line | `ax.plot3D()` | 
Scatter| `ax.scatter3D()`
Contour plot | `ax.contour3D()` | Parallel lines
Wireframe | `ax.plot_wireframe()` | Grid
Surface plot | `ax.plot_surface()` | Like a wireframe plot, but each face of the wireframe is a filled polygon. Adding a colormap to the filled polygons can aid perception of the topology of the surface being visualized
Surface triangulation | `ax.plot_trisurf()` | Creates a surface by first finding a set of triangles formed between adjacent points

Customization | Method | Description
--- | --- | ---
Set the default viewing angle. | `ax.view_init(elevation, azimuth)` | First angle is degrees above x-y plane. Second is CCW rotation about z-axis (if 0, then x-axis points away from viewer and y-axis is horizontal)


A three-dimensional axes can be created by passing the keyword `projection='3d'` to any of the normal axes creation routines:
```python
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
%matplotlib widget # to use interactive figures in the notebook
# use `%matplotlib notebook` instead if using Jupyter notebook online, 

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
```
## Gridded data
Gridded plots (e.g. `ax.contour3D`) require all the input data to be in the form of two-dimensional regular grids, with the Z data evaluated at each point. 
* Use `np.linspace(lowest_value,highest_value,n_values)` to get evenly spaced points between 2 numbers.
* Use `X,Y = np.meshgrid(x,y)` to make the 2D grid

```python
# Create the input values
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

# Create the grid
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create the 3D figure canvas
fig = plt.figure()
ax = plt.axes(projection='3d')

# Make contour plot
ax.contour3D(X, Y, Z, 50, cmap='binary')
```

```python
from scipy.stats import multivariate_normal
```
# Maps in Python
[Walkthrough: Maps in Python](https://data.compass.lighthouselabs.ca/976f2d02-24ef-41cd-950e-b6f0ad2a4b0a)
[Geopandas documentation](https://geopandas.org/en/stable/docs/reference.html)

* A `GeoPandas` dataframe has a `geometry` datatype, which contains three basics classes of geometric (`Shapely`) objects (points, lines, and polygons).
    * A `GeoPandas` data-frame may also contain other columns with geometrical (shapely) objects, but only one column can be the active geometry at a time
* In general, any options we can pass to `pyplot` in Matplotlib can be passed to the `plot()` method.

Method (`world` = variable name of GeoDataFrame) | Description
--- | ---
`gpd.read_file()`
`world.geometry.name` | print the active geometry
`world.rename(columns={'original_name': 'new_name'})` | Rename column
`world.set_geometry('column_name')` | Set the active geometry
`world.plot()` | Plot the map

---
`world.plot()` parameters | Description
--- | ---
`column=` | Column of data to plot
`legend=True` | Legend
`legend_kwds={'label': "column_name",'orientation': "horizontal"})`
`edgecolor=` | Border color
`linewidth=` | Border thickness

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# load the data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# print the active geometry
world.geometry.name

# If geometry is not set correctly, rename the column and set the geometry
world = world.rename(columns={'geometry': 'borders'}).set_geometry('borders')

# plot the geometry
world.plot()
```
To create choropleth maps, use the `.plot` command with the `column=` parameter set to the column whose values you want to use to assign colors. We can also enable a legend using the legend parameter.

```python
# create the figure and axes
fig, ax = plt.subplots(figsize=(15,12))

# create the map
world.plot(column='pop_est', ax=ax, legend=True,
           legend_kwds={'label': "Population by Country",
                        'orientation': "horizontal"})
```
The cities dataframe only has points, not polygons. This can be added as a layer on the map. After the code that creates the layer with the countries as outlined above, use markers to plot the cities:
```python
# Load the cities dataframe
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

# a layer of cities

cities.plot(ax=ax ,marker='*', color='white', markersize=5)
plt.show()
```

### Obtain geocode for a set of strings
Use [`geopandas.tools.geocode`](https://geopandas.org/en/stable/docs/reference/api/geopandas.tools.geocode.html)
```python
import geopy

# Make a list of strings for the search terms
selectCities = ['New York', 'Berlin', 'Paris','Toronto', 'Calgary', 'Tokyo']

# Perform the search. Specify the provider or it won't work.
selectCitiesDF = gpd.tools.geocode(selectCities,provider='photon')

# create figure and axes
fig, ax = plt.subplots()

# create map from world data-frame
world.plot(ax=ax)

# add cities
selectCitiesDF.plot(ax=ax,marker='*', markersize=5, color='red')
```

## Plotly
Making choropleth maps requires two main types of input:
1. Geometry information:
    * A supplied GeoJSON file where each feature has either an id field or some identifying value in properties; or
    * one of the built-in geometries within plotly: US states and world countries (see below)
2. A list of values indexed to match the identifying value in the geometry info.

Function/Method | Description
--- | ---
`px.choropleth()`| Chloropleth map
`px.scatter_geo()` | Bubble map

Create Plotly figures with these parameters:
Parameter | Description | Only applies to..
--- | --- | ---
`geojson=` | Name of GeoJSON object
`color=` | Data column in data object. 
`locations=` | data column with geometry id
`featureidkey=` | (Optional) ID column with the geometry info in the GeoJSON object
`hover_name="country"` | column to add to hover information
`size=` | Data to be represented with bubble size | `px.scatter_geo()`
`animation_frame=()` | Data from the independent variable that will change the plot, e.g. time variable to show how something changes with time.

### Plotly Choropleth Maps
[Plotly documentation on chlorpleth maps](https://plotly.com/python/choropleth-maps/)

```python
from urllib.request import urlopen
import json

# load a GeoJSON file containing the geometry information for US counties, where feature.id is a FIPS code.
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth(data_or_df, 
                        geojson=geoJSON_object, 
                        locations=data_column_with_geometry_id, 
                        color=data_column_with_data,
                        color_continuous_scale="Viridis",
                        range_color=(0, 12),
                        scope="usa",
                        labels={'unemp':'unemployment rate'}
                        )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
```

Plotly comes with two built-in geometries which do not require an external GeoJSON file:
* USA States
* Countries as defined in the Natural Earth dataset. To use the built-in countries geometry, provide locations as three-letter [ISO country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3).

```python
import plotly.express as px

# This creates a dataframe with these columns: 'country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap','iso_alpha', 'iso_num'
df = px.data.gapminder().query("year==2007")

fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)

# To use the USA States geometry, set locationmode='USA-states' and provide locations as two-letter state abbreviations
```
### Bubble map with Plotly Express

```python
import plotly.express as px
df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df, locations="iso_alpha", 
                color="continent",
                hover_name="country", size="pop",
                projection="natural earth")
```
### Bubble Map with Graph Objects
Example:
```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
df.head()

df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million'
limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 5000

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['pop']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig.update_layout(
        title_text = '2014 US city populations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )
```
# Data visualization: Plotly Express
```python
import plotly.express as px

# Basic syntax
fig = px.scatter(x=x_data, y=y_data)
fig.show()

# Basic syntax if using DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
```
Function/Method | Description
--- | ---
`fig = px.scatter()` 

Similar to with Seaborn, variables can be mapped to various plot attributes by passing them into the parametes:
Parameters | Description
--- | ---
`color=`
`size=`
`hover_data=`
`symbol=` | Marker symbol, e.g. circle, square, diamond

## Additional Plotly Documentation
* [Python API reference for plotly](https://plotly.com/python-api-reference/index.html)
* [Python Figure Reference: layout](https://plotly.com/python/reference/layout/#layout-paper_bgcolor)
    * [Theming and templates](https://plotly.com/python/templates/#specifying-themes-in-graph-object-figures)
* [Python Figure Reference: Edit Plotly Axis](https://plotly.com/python/reference/layout/xaxis/#layout-xaxis-showgrid)
* [Plotly: Subplots examples](https://plotly.com/python/subplots/)
    * [API documentation: `make_subplots`](https://plotly.com/python-api-reference/generated/plotly.subplots.make_subplots.html?highlight=make_subplots)
* [Plotly: Images](https://plotly.com/python/images/)

# Interactive Plots With Widgets
[Walkthrough](https://data.compass.lighthouselabs.ca/days/w03d2/activities/448)<br>
[Widget List — Jupyter Widgets 8.0.2 documentation (ipywidgets.readthedocs.io)](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html)

```python
# import the widgets
import ipywidgets as widgets

# import the interact and the interact_manual from widgetss
from ipywidgets.widgets import interact, interact_manual

# import pandas
import pandas as pd

# import plotly 
import plotly.graph_objects as go
import plotly.express as px
```
Function | Description
--- | ---
`@interact` | Decorator that creates a widget for arguments in functions
`@interact_manual` | creates dropdowns in the same was as the `@interact` decorator but also creates a button that allows us to confirm the selection
`widgets.IntSlider()` | Create a slider
`widgets.interact()` | Create an interactive widget that you can call on later using the `.widget` command
`widgets.DatePicker(value=pd.to_datetime('2022-10-10'))`
`widgets.Dropdown(options=[list])` 

Command | Description
--- | ---
`.value` | Get the current value of the slider
`.widget` | Use a previously-defined widget
`.observe()` |  make the options for one widget dependent on the value of another

## Create a slider
```python
slider = widgets.IntSlider(
    min=0,
    max=10,
    step=1,
    description='Slider:',
    value=3
)
# the current value of slider
print(slider.value)
```
## Filter a dataframe
Define a function that filters the data-frame based on the selected column and threshold:
```python
# create the filter function
def filter_df(column, threshold):
    return df[df[column] <= threshold]

# create a widget to set the parameters of the function. Let's say we want to use the columns 'spend' and 'visits' in our dropdown widget and values from the interval <0,30> with step 1 in a slider widget.
filter_widget = widgets.interact(filter_df,
                column=['spend','visits'], 
                threshold=(1, 30, 1))

# use filter later in code using this command:
filter_widget.widget
```
Alternatively, simply use a decorator command for one-off use:
```python
@interact
def filter_df(column=['spend','visits'], threshold=(1, 30, 1)):
    return df[df[column] <= threshold]
```

## Interactive Plots With Widgets

Define a function that creates a scatter plot from selected columns of a data-frame.
```python
@interact #decorator
def scatter_plot(x=list(df.select_dtypes('number').columns), 
                 y=list(df.select_dtypes('number').columns)[1:]):

    # trace
    trace = [go.Scatter(x=df[x], y=df[y], mode='markers')]

    # layout
    layout = go.Layout(
                title = 'Scatter plot', # Graph title
                xaxis = dict(title = x.title()), # x-axis label
                yaxis = dict(title = y.title()), # y-axis label
                hovermode ='closest' # handles multiple points landing on the same vertical
    )

    # fig
    fig = go.Figure(trace, layout)
    fig.show()
```
Histogram
```python
df=df  # Put name of dataframe variable here
@interact_manual #decorator
def exploreHistogram(x=list(df.select_dtypes('number').columns)[1:]):
    fig = px.histogram(x=df[x],title=x)
    fig.show()
```


## Make options for a widget dependent on the value of another
[Interactive Controls in Jupyter Notebooks | by Will Koehrsen | Towards Data Science](https://towardsdatascience.com/interactive-controls-for-jupyter-notebooks-f5c94829aee6)

If we want to make the options for one widget dependent on the value of another, we use `.observe()`. 
* Here, we alter the image browser function to choose both the directory and image. The list of images displayed is updated based on the directory we select.
```python
# Create widgets
directory = widgets.Dropdown(options=['images', 'nature', 'assorted'])
images = widgets.Dropdown(options=os.listdir(directory.value))

# Updates the image options based on directory value
def update_images(*args):
    images.options = os.listdir(directory.value)

# Tie the image options to directory value
directory.observe(update_images, 'value')

# Show the images
def show_images(fdir, file):
    display(Image(f'{fdir}/{file}'))

_ = interact(show_images, fdir=directory, file=images)
```

# Data Exploration
[Walkthrough: Data Exploration](https://data.compass.lighthouselabs.ca/6603399c-6f1e-44e7-8163-75e126ac95c0)
## Step 1: Explore target variable
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#check for dupes for Id
idsUnique = len(set(df_train.Id))
idsTotal = df_train.shape[0]
idsdupe = idsTotal - idsUnique

#drop id col since it is the same as the index
df_train.drop(['Id'],axis =1,inplace=True)

# Get descriptive stats and look at the distribution
df_train['SalePrice'].describe()
sns.displot(df_train['SalePrice'],kind='hist',kde=True)

# Print a list of all columns:
sorted(list(df_train.columns))

```
## Step 2: Look at the relationship between target variable and predictors (bivariate analysis)
* Plot the data with the appropriate plot type.
* Use domain knowledge to see if the data make sense.

## Step 3: Multivariate analysis
Look at a correlation matrix between numeric attributes using [`df.corr()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html?highlight=dataframe%20corr#pandas.DataFrame.corr)
```python
#correlation matrix
corrmat = df_train.corr() # Compute pairwise correlation of columns, excluding NA/null values.
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True,cmap="RdYlGn_r")
```
To make it more readable we can plot only those variables that correlate with the target variable more than 0.5:

```python
# most correlated features with SalePrice

corrmat = df_train.corr()
top_corr_features = corrmat.index[abs(corrmat["SalePrice"])>0.5]
```
Break the above code down:
1. `corrmat.index` returns a list of the row names of correlation matrix
2. `abs(corrmat["SalePrice"])>0.5` returns a boolean mask of the matrix: Does the absolute value in the 'SalePrice' column of each row exceed 0.5?
3. The boolean mask from step 2 is used to index the list of row names from the correlation matrix in step 1.

```python
plt.figure(figsize=(10,10))
g = sns.heatmap(df_train[top_corr_features].corr(),annot=True,cmap="RdYlGn_r")
```

# Outlier detection
[Outlier detection](https://data.compass.lighthouselabs.ca/41c6950b-b2c2-4a42-93aa-0c44ff8e2c15)
1. Use `df.drop(boolean_filter)` to drop rows
2. Re-set the index with `df.reset_index()`
3. Visualize the data with the outliers removed.
```python
# Example: Delete data rows of outliers, 
# i.e. TotalBsmtSF > 500) with SalePrice <3000000
df_train = df_train.drop(df_train[(df_train['TotalBsmtSF']>5000) & (df_train['SalePrice']<300000)].index)

# reset index
df_train = df_train.reset_index(drop=True)

```
## Handling missing data
 
Method | Description | Opposite Method | Description
--- | --- |--- | ---
`df.info()` | Indicates number of rows, columns, and non-null values per column.
`df.isnull()` | Generate a boolean mask indicating missing values (`NaN` or `None`) | `df.notnull()` | Opposite of isnull()
`df.dropna()` | Drops rows (or columns) in which a null value is present. Specify `axis=1` to drop columns. Default is `how='any'`, where even a single null value will cause that row/column to be dropped. Can also specify `how='all'`. For finer-grained control, the thresh parameter lets you specify a minimum number of non-null values for the row/column to be kept | `df.fillna()` | Return a copy of the data with missing values filled or imputed. 

Walkthrough
1. Drop columns with a lot of  missing data
```python
# count amount of missing values in each column
total = df_train.isnull().sum().sort_values(ascending=False) 
# % of rows with missing data from each column
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False) 

# create a table that lists total and % of missing values starting with the highest
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']) 

# drop 5 columns with the biggest ratio of null values
to_drop = missing_data.head(5).index.tolist()
df_train.drop(to_drop, axis=1, inplace=True)
```
2. For remaining data, create an indicator that raw data was missing (before these missing values are replaced).
```python
# extract the names of columns with missing values
cols_with_missing = missing_data[missing_data.Percent > 0].index.tolist()

# remove column names that are already removed from dataset
missing_cols = list(set(cols_with_missing) - set(to_drop))

# check the datatype
df_train.dtypes[missing_cols]
```
3. Identify columns with missing data and perform the appropriate fill.
* Numerical data
```python
# Create a list of the column names that contain missing float data
num_cols_with_missing = df_train.dtypes[missing_cols][df_train.dtypes[missing_cols] == 'float'].index.tolist()

# create new variables to indicate missing values in original data
for cl in num_cols_with_missing:
    # For each column, create a corresponding column that indicates presence missing data; default value is 0.
    # New column name is original column name followed by "_missing_ind"
    df_train[cl + "_missing_ind"] = 0 
    # Search for rows with null data and change the value from 0 to 1 in the corresponding column
    df_train.loc[df_train[cl].isnull(), cl + "_missing_ind"] = 1

# Perform a null value replacement using the appropriate value on the numerical data columns:
df_train["LotFrontage"] = df_train["LotFrontage"].fillna(df_train["LotFrontage"].mean())
```
* Categorical data
```python
# Identify non-numerical columns containing missing data
df_train.dtypes[missing_cols][df_train.dtypes[missing_cols] == 'object']
cat_cols_with_missing = df_train.dtypes[missing_cols][df_train.dtypes[missing_cols] == 'object'].index.tolist()
```
# Data transformation
[Resource: How, When, and Why Should You Normalize / Standardize / Rescale… – Towards AI](https://towardsai.net/p/data-science/how-when-and-why-should-you-normalize-standardize-rescale-your-data-3f083def38ff)

Transformation type | Code | Description | Notes
--- | --- | --- | ---
standardization | `StandardScaler() .fit_transform(data)` | Transforms data to have a mean of 0 and standard deviation of 1. | Assumes data has normal distribution. 
normalization | `MinMaxScaler() .fit_transform(data)` | data is scaled to a fixed range — usually 0 to 1 | Results in smaller standard deviations, which can suppress the effect of outliers. 
robust scalar | `RobustScaler() .fit_transform(data)` | Scaling using median and quantiles consists of subtracting the median to all the observations and then dividing by the interquartile difference (75th minus 25th quantile). | robust to outliers
dummy variable | `pd.get_dummies(df[columns])` | Convert values into categorical numbers. Each possible value is represented by a variable, which can have a value of 0 or 1. | e.g. If variable is male, 1 indicates male and 0 indicates female.

**First separate out numeric vs. categorical columns**. Then, basic syntax:
```python
# Standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() 
data_scaled = scaler.fit_transform(data)

# Normalize
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler() 
data_scaled = scaler.fit_transform(data)

# Robust Scaler
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler() 
data_scaled = scaler.fit_transform(data)

# Add back index containing cust_id after it was removed from the scaling function
scaledCustomerData.index = customer_data.index
```
### [Walkthrough](https://data.compass.lighthouselabs.ca/c33e5b19-8e02-4101-aa7b-7211720249be)
#### Numeric data
```python
# Extract the numeric feature names from the dataframe:
num_feats = df_train.dtypes[df_train.dtypes != 'object'].index.tolist()

# Do a log transformation on "1stFlrSF_log" data column to make the values have a more normal distribution. Add result as a new column.
df_train["1stFlrSF_log"] = df_train["1stFlrSF"].apply(np.log)

# Perform scaling 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Perform transformation on the columns listed in num_feats AND on the column of log-transformed data ("1stFlrSF_log"), and put that into a dataframe
df_train_scaled = pd.DataFrame(scaler.fit_transform(df_train[num_feats+["1stFlrSF_log"]].astype(float)))

# fit_transform returns data type numpy.array without any of its original column names. 
# Assign original column names to the DataFrame df_train_scaled:
df_train_scaled.columns = num_feats+["1stFlrSF_log"]
```
Some numerical data can be put into categorical bins represented by integers.

#### Categorical data
* Ordinal data can be converted to integers.
* For non-ordinal data, the most often used transformation is the creation of Dummy variables using `pd.get_dummies()`.

```python
# Create list of column names with categorical variables
cat_feats = df_train.dtypes[df_train.dtypes == 'object'].index.tolist()

#  create a new Pandas data-frame with dummy variables only
df_dummy = pd.get_dummies(df_train[cat_feats])
```
### [Transforming dataframe data containing both numerical and dummy variables in logistical regression](https://www.justintodata.com/logistic-regression-example-in-python/)
```python
# Identify the numeric and categorical columns
numeric_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
cat_cols = list(set(df.columns) - set(numeric_cols) - {'target'})
cat_cols.sort()

# Create the scaler based on the training dataset
scaler = StandardScaler()
scaler.fit(df_train[numeric_cols])

def get_features_and_target_arrays(df, numeric_cols, cat_cols, scaler):
    """
    After creating a class of StandardScaler, we calculate (fit) the mean and standard deviation for scaling using df_train’s numeric_cols. Then we create a function get_features_and_target_arrays that:
    - performs standardization on the numeric_cols of df to return the new array X_numeric_scaled. 
    - transforms cat_cols to a NumPy array X_categorical.
    - combines both arrays back to the entire feature array X.
    - assigns the target column to y.
    """
    X_numeric_scaled = scaler.transform(df[numeric_cols])
    X_categorical = df[cat_cols].to_numpy()
    X = np.hstack((X_categorical, X_numeric_scaled))
    y = df['target']
    return X, y
```


# Machine Learning

## Centroid Models
[Walkthrough: Centroid models](https://data.compass.lighthouselabs.ca/activities/476)

Required modules for all models:
```python
# import matplotlib
import matplotlib.pyplot as plt

# import Kmeans from sklearn
from sklearn.cluster import KMeans 

# import numpy
import numpy as np
```

Model | Function | Description | Required import
--- | --- | --- | ---
K-Means Clustering | `km = KMeans(n_clusters)` | Indicate how many clusters on which to create the model. | `from sklearn.cluster import KMeans`
Hierarchechal models | `ac = AgglomerativeClustering()` | Create an `an AgglomerativeClustering` object | `from sklearn.cluster import AgglomerativeClustering`
. | `dendrogram = sch.dendrogram(sch.linkage(X, method=method)` | Plot dendogram (hierarchechal clustering). Default method is 'single'. See [documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html). | `import scipy.cluster.hierarchy as sch`
. | `adjusted_rand_score(trueLevels, modelLabels)` | an external cluster validation index which results in a score between -1 and 1, where 1 means two clusterings are identical of how they grouped the samples in a dataset | `from sklearn.metrics import adjusted_rand_score`
Density models | `db = DBSCAN(eps=0.5, min_samples=5, metric='euclidean')` | Density-based clustering. Suitable for spherical or non-spherical  data | `from sklearn.cluster import DBSCAN`


Method | Description
--- | ---
`.fit(X)` | Fit the model. Returns a 1D array containing the cluster number for each data point 
`.predict(X)` | Use the model to predict 
`.fit_predict(X)` | combination of `.fit(X)` and `.predict(X)`
`.inertia_` | Obtain the inertia value

```python
# import make_blobs from sklearn
from sklearn.datasets import make_blobs

# import matplotlib
import matplotlib.pyplot as plt

# import Kmeans from sklearn
from sklearn.cluster import KMeans

# import numpy
import numpy as np
```

<Details>
<summary>For creating toy data: Generate clusters with `make_blobs()`</summary>

<br>[`make_blobs()` documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html)
```python
X, y = make_blobs(n_samples=150, # generates isotropic Gaussian blobs for clustering
                  n_features=2, # 2-D array
                  centers=3,
                  cluster_std=0.5,
                  random_state=0)
    # With the code above we generated 150 points in a 2-dimensional space. 
    # These points are divided into three clusters with standard deviations equal to 0.5 in each cluster.
```
</Details>
<br></br>

### `k-means` Clustering
The first thing we need to do before fitting the data is to instantiate the `KMeans class` from `Sklearn`:
```python
km = KMeans(n_clusters=3, # how many clusters we expected 
            n_init=10, # how many initial runs
            random_state=0) # set the random_state parameter to easily reproduce the results.

# Train the model
km.fit(X)

# predict (the cluster to which a given point will belong)
y_km = km.predict(X)
```

Alternatively, fit and predict with a single function:
`y_km = km.fit_predict(X)`.
* `.fit_predict()` is a combination of `.fit(X)` and `.predict(X)`
<br></br>

### Plot the model results
To plot how the k-means algorithm assigned the clusters to our data we need to define a function that does exactly this:
```python
def plot_clusters(X,y_res, plt_cluster_centers = False):
    X_centroids = []
    Y_centroids = []

    for cluster in set(y_res):
        # From array X, retrieve values from column 0 for rows where its `.fit()` label matches the cluster: 
        x = X[y_res == cluster,0] 
        # Same, but retrieve values from column 1:
        y = X[y_res == cluster,1]
        X_centroids.append(np.mean(x))
        Y_centroids.append(np.mean(y))

        plt.scatter(x,
                    y,
                    s=50, # marker size
                    marker='s',
                    label=f'cluster {cluster}')

    if plt_cluster_centers:
        plt.scatter(X_centroids,
                    Y_centroids,
                    marker='*',
                    c='red',
                    s=250,
                    label='centroids')
    plt.legend()
    plt.grid()
    plt.show()

 # plot clustering result
plot_clusters(X, y_km, plt_cluster_centers= True)
```
### Elbow Rule

**Distortion**, in `sklearn` called **inertia**, tells how far away the points within a cluster are. 
* A small of inertia is aimed for. The range of inertia’s value starts from zero and goes up.

To determine how many clusters to create, calculate the distortion for multiple k values and plot the result:
```python
def plot_distortion(X,max_clusters = 10):
    """
    Create a plot to help identify the elbow of the inertia graph.
    Parameter:
    - X: Array of the data. Use `.to_numpy()` method to convert dataframe to array if needed.
    """
    distortions = []
    for i in range(1, max_clusters +1):
        km = KMeans(n_clusters=i,
                    init='k-means++',
                    n_init=10,
                    random_state=0)
        km.fit(X)
        distortions.append(km.inertia_) # Calcuate the distortion for a given number of clusters

    plt.plot(range(1,max_clusters +1), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.show() 

# elbow rule
plot_distortion(X,max_clusters=10)
```
<br></br>

## Hierarchical models
[walkthrough: Hierarchical models](https://data.compass.lighthouselabs.ca/15b6e2f3-8310-43f5-be5e-296bee72d5f1)

 Agglomerative clustering performs a hierarchical clustering using a bottom-up approach:
```python
# aglomerative clustering
from sklearn.cluster import AgglomerativeClustering

# create an object
# set the Euclidean distance to the affinity parameter
ac = AgglomerativeClustering(affinity='euclidean', 
            linkage='ward', #set the `linkage` parameter to the "ward"
            n_clusters = 3) # set the number of clusters to three.

# fit and predict 
y_hc = ac.fit_predict(X)
```
The `linkage=` criteria determine the metric used for the merge strategy:
* `ward` minimizes the sum of squared differences within all clusters. It is a variance-minimizing approach and, in this sense, is similar to the k-means objective function but tackled with an agglomerative hierarchical approach.
* `maximum` or complete linkage minimizes the maximum distance between observations of pairs of clusters.
* `average` linkage minimizes the average of the distances between all observations of pairs of clusters.
* `single` linkage minimizes the distance between the closest observations of pairs of clusters.

<br></br>
To determine which clustering result better matches the original labels of the samples, we can use ```adjusted_rand_score``` which is an *external cluster validation index* which results in a score between -1 and 1, where 1 means two clusterings are identical of how they grouped the samples in a dataset (regardless of what label is assigned to each cluster).

```python
from sklearn.metrics import adjusted_rand_score

y_hc_ar_score = adjusted_rand_score(labels_true, y_hc) 
# y_hc is the cluster labels to evaluate 
```
<br></br>

#### Dendogram
To identify the right number of clusters we can plot a dendrogram. Let's define the function that plots a dendrogram:
```python
# cluster hierarchy
import scipy.cluster.hierarchy as sch

# define plot_dendrogram function
def plot_dendrogram(X,method ='ward'):
    dendrogram = sch.dendrogram(sch.linkage(X, method=method))
    plt.title("Dendrogram")
    plt.ylabel("Euclidean distances")
    plt.xlabel('Points')
    plt.show()

# Plot dendrogram
plot_dendrogram(X)
```
## Density models
[Walkthrough: Density models](https://data.compass.lighthouselabs.ca/activities/482)<br>
[Video from Big Data University: Machine Learning - Unsupervised Learning - Density Based Clustering](https://youtu.be/sJQHz97sCZ0?t=120)<br>
[Demo resource: Visualizing DBSCAN Clustering](https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/)
[Resource: How DBSCAN works and why should we use it? | by Kelvin Salton do Prado | Towards Data Science](https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80)

### How DBScan Works?

Consider a set of points in some space to be clustered. Let **R be a parameter specifying the radius of a neighborhood with respect to some point** and let **M be minimum number of points we want in a neighbourhood to define a cluster**. 

For the purpose of DBSCAN clustering, the points are classified as **core points**, **border points** and **outliers**, as follows:

* A point p is a **core point** if at least M points are within distance R of it (including p).
* A point s is a **border point** if it is near a core point but doesn't have M points in its R neighbourhood.
* A point q is **directly density-reachable** from p if point q is within distance R from core point p. Points are only said to be directly reachable from core points.
* A point t is **density-reachable** from p if there is a path p1, ..., pn with p1 = p and pn = t, where each pi+1 is directly reachable from pi. Note that this implies that the initial point and all points on the path must be core points, with the possible exception of t. In the image below point t is density reachable from point p via point q.
* All points in this chain path p1, ..., pn are called **density connected**.
* All points not reachable from any other point are **outliers or noise points**.

Now if p is a core point, then it forms a cluster together with all points (core or non-core) that are reachable from it. Each cluster contains at least one core point; non-core points can be part of a cluster, but they form its "edge", since they cannot be used to reach more points.

<img src='https://www.mdpi.com/applsci/applsci-09-04398/article_deploy/html/images/applsci-09-04398-g001.png' width="200"/>

Use `DBSCAN`, which has the following advantages:
* Can handle non-spherical data
* Identifies outliers
* No need to specify # of clusters

Disadvantages:
* Not entirely deterministic: Border points can be part of more than 1 cluster, depending on order the data is processed
* Cannot work well for high-dimensional data

```python
# import DBSCAN
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.5,
            min_samples=5,
            metric='euclidean')

# fit and predict
y_db = db.fit_predict(X)
```
`DBSCAN` parameters:
* `eps=`: The maximum distance between two samples for one to be considered as being in the neighborhood of the other.
    * *Imagine each point has a radius of `eps`; another point is considered 'reachable' if within this radius.*
* `min_samples=`: The number of samples in a neighborhood for a point to be considered as a core point. This includes the point itself.

<details>

<summary>Non-spherical data</summary>

Here's how you can make toy data that has spherical clusters:
```python
# import make_moons from sklearn
from sklearn.datasets import make_moons

# plot data
plt.scatter(X[:,0], X[:,1])
plt.show()
```
</details>

# Linear algebra
[Resource: Math is Fun Matrix Transformations](./z%20course%20material/2022-10-07%20Math%20is%20Fun%20Matrix%20Transformations.pdf)<br>
[Resource: Eigenvector and Eigenvalue (mathsisfun.com)](https://www.mathsisfun.com/algebra/eigenvalue.html)<br>
[Resource: Matrix determininant (mathisfun.com)](https://www.mathsisfun.com/algebra/matrix-determinant.html)

# Matrix Decomposition: Singular value decomposition (SVD)
* [Walkthrough](https://data.compass.lighthouselabs.ca/activities/493)
* [You Don’t Know SVD (Singular Value Decomposition) | by Hussein Abdulrahman | Towards Data Science](https://towardsdatascience.com/svd-8c2f72e264f)

Use function `np.linalg.svd()` to create a singular value decomposition.
```python
import matplotlib.pyplot as plt
import numpy as np

U, sigma, V = np.linalg.svd(data_array)

# To reconstruct the array:
reconst = np.matrix(U[:, :n_columns]) * np.diag(sigma) * np.matrix(V)
# n_columns should match length of sigma and # of columns in V.

# Equation from Kelvin the mentor
reconst = U[:, :n_columns].dot(np.diag(sigma)).dot(V)
```
# Minimum and Maximum of a Function in Python
[Resource: Scientific Python: Using SciPy for Optimization – Real Python](https://realpython.com/python-scipy-cluster-optimize/#using-the-cluster-module-in-scipy)

## Using the Cluster Module in SciPy
Tutorial using "SMSSpamCollection" dataset. The dataset consists of 4827 real and 747 spam text (or SMS) messages.
```python
from pathlib import Path
import numpy as np
from scipy.cluster.vq import whiten, kmeans, vq

data = Path("SMSSpamCollection").read_text()
data = data.strip()
data = data.split("\n") # split the string into a list 

# creating an empty NumPy array, digit_counts
digit_counts = np.empty((len(data), 2), dtype=int)

# process the data to record the number of digits and the status of the message:
for i, line in enumerate(data): # put the value from the list in line and create an index i for this list
    # Split the line on the tab character to create case and message. 
    # case is a string that says whether the message is ham or spam, while 
    # message is a string with the text of the message.
    case, message = line.split("\t")
    # Calculate the number of digits in the message by using the sum() of a comprehension. 
    num_digits = sum(c.isdigit() for c in message)
    # assign the first column of the i row to be 0 if the message was legitimate (ham) or 1 if the message was spam
    digit_counts[i, 0] = 0 if case == "ham" else 1
    # assign the second column of the i row to be the number of digits in the message.
    digit_counts[i, 1] = num_digits
```
`np.unique()` takes an array as the first argument and returns another array with the unique elements from the argument. 
* Use `return_counts=True` to instruct `np.unique()` to also return an array with the number of times each unique element is present in the input array. These two outputs are returned as a tuple that you store in unique_counts.
```python
unique_counts = np.unique(digit_counts[:, 1], return_counts=True)
```
You combine the two 1xN outputs from `np.unique()` into one 2xN array using `np.vstack()`, and then transpose them into an Nx2 array. This format is what you’ll use in the clustering functions. Each row in unique_counts now has two elements:
1. The number of digits in a message
2. The number of messages that had that number of digits

```python
# transform unique_counts into a shape that’s suitable for clustering:
unique_counts = np.transpose(np.vstack(unique_counts))
```
Apply the k-means clustering algorithm to this array:
* use `whiten()` to normalize each feature to have unit variance, which improves the results from `kmeans()`
```python
whitened_counts = whiten(unique_counts)
codebook, _ = kmeans(whitened_counts, 3)
```
`kmeans()` returns an array with three rows and two columns representing the centroids of each group: 
* optimal location of the centroid of each cluster by minimizing the distance from the observations to each centroid. This array is assigned to codebook.
* The mean Euclidian distance from the observations to the centroids. You won’t need that value for the rest of this example, so you can assign it to _.

Determine which cluster each observation belongs to by using `vq()`. It returns two values:
* An integer for each element representing which cluster that observation is assigned to. 
* The Euclidian distance between each observation and its centroid.
 ```python
codes, _ = vq(whitened_counts, codebook)

#  find the integer code associated with each cluster:
ham_code = codes[0] # 
spam_code = codes[-1]
unknown_code = list(set(range(3)) ^ set((ham_code, spam_code)))[0] # Find symmetric difference
```
According to our hypothesis above:
* the ham messages have the fewest digits, and the digit array was sorted from fewest to most digits. Thus, the ham message cluster starts at the beginning of codes.
* the spam messages have the most digits and form the last cluster in codes.
* Since there are only 3 options for the code and you have already identified two of them, you can use the `symmetric_difference` operator (`^`) on a Python set to determine the last code value.

## Using the Optimize Module in SciPy
[Resource: Using the Optimize Module in SciPy (Real Python)](https://realpython.com/python-scipy-cluster-optimize/#using-the-optimize-module-in-scipy)

`scipy.optimize` contains a number of useful methods for optimizing different kinds of functions:

Function/Method | Required imports | Parameters | Parameter description
--- | --- | --- | -
`minimize_scalar(function)` <br>univariate | `from scipy.optimize import minimize_scalar` | `method=bounded` | <br>Takes `bounds=(x1,x2)` to bound the search region.
. | - |  `method=brent` | Default method. Takes `bracket=(x1,x2[...])` for initial guess for the bounds of the minumum 
`minimize()` <br>(multivariate)| `from scipy.optimize import minimize, LinearConstraint` | `constraints=` | Constrain the solution to the problem using `LinearConstraint()` or `NonlinearConstraint()`
`LinearConstraint(constraint_matrix)` |  The constraint has the general inequality form <br>`lb <= constraint_matrix.dot(x) <= ub`<br> [(documentation link)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.LinearConstraint.html) | `lb=`, `ub=` | Lower and upper limits on the constraint. Each array must have the shape (m,) or be a scalar, in the latter case a bound will be the same for all components of the constraint.
`curve_fit()` | fit a function to a set of data
`root_scalar()` and `root()` | find the zeros of a function of one variable and many variables, respectively
`linprog()` | minimize a linear objective function with linear inequality and equality constraints

### Minimizing a Function With One Variable

```python
from scipy.optimize import minimize_scalar

# Define a function
def objective_function(x):
    return x ** 4 - x ** 2

# Find the minimum using the default method (Brent's algorithm)
res = minimize_scalar(objective_function, bracket=(-1, 0))

# Alternatively, use the bounded method with the bounds set 
res = minimize_scalar(objective_function, method='bounded', bounds=(-1, 0))
```

### Minimizing a Function With Many Variables
[Example from Real Python](https://realpython.com/python-scipy-cluster-optimize/#minimizing-a-function-with-many-variables)

[See my 2022-10-09 handwritten notes](https://onedrive.live.com/view.aspx?resid=93345F1C83A5C894%2149156&id=documents&wd=target%28Prep%20module.one%7C60B7F64E-9587-434E-9934-74899CB1BEDA%2FNotepad%3A%20Minimizing%20a%20Function%20With%20Many%20Variables%20%28Example%20from%7CA2B84CB2-DE64-4C9E-B3CA-96835FE41A21%2F%29
onenote:https://d.docs.live.net/93345f1c83a5c894/OneNote/Data%20Science/Prep%20module.one#Notepad%20Minimizing%20a%20Function%20With%20Many%20Variables%20(Example%20from&section-id={60B7F64E-9587-434E-9934-74899CB1BEDA}&page-id={A2B84CB2-DE64-4C9E-B3CA-96835FE41A21}&end")


Imagine you’re a stockbroker who’s interested in maximizing the total income from the sale of a fixed number of your stocks. You can phrase this problem as a constrained optimization problem. The objective function is that you want to maximize your income. 
* There is one constraint on the problem, which is that the sum of the total shares purchased by the buyers does not exceed the number of shares you have on hand. 
* There are also bounds on each of the solution variables because each buyer has an upper bound of cash available, and a lower bound of zero.
```python
import numpy as np
from scipy.optimize import minimize, LinearConstraint

n_buyers = 10
n_shares = 15

#  generate the array of prices the buyers will pay
prices = np.random.random(n_buyers)

#  generate an array representing the total cash each buyer has available
money_available = np.random.randint(1, 4, n_buyers)

# determine the maximum number of shares each buyer can purchase
n_shares_per_buyer = money_available / prices
```
Create the constraints and bounds for the solver. The constraint is that the sum of the total purchased shares can’t exceed the total number of shares available. This is a constraint rather than a bound because it involves more than one of the solution variables.
* To represent this mathematically, you could say that x[0] + x[1] + ... + x[n] = n_shares, where n is the total number of buyers. More succinctly, you could take the dot or inner product of a vector of ones with the solution values, and constrain that to be equal to n_shares.
```python
constraint = LinearConstraint(np.ones(n_buyers), lb=n_shares, ub=n_shares)
 # this will result in the sum of the purchased shares, whose value is constrained by the length of the array which corresponds with the number of buyers (n_buyers)
```
Since `lb = ub = n_shares`, this is an **equality constraint** because the sum of the values must be equal to both lb and ub. If lb were different from ub, then it would be an **inequality constraint**.

Next, create the bounds for the solution variable. The bounds limit the number of shares purchased to be 0 on the lower side and n_shares_per_buyer on the upper side. The format that minimize() expects for the bounds is a sequence of tuples of lower and upper bounds:
```python
# use a comprehension to generate a list of tuples for each buyer
bounds = [(0, n) for n in n_shares_per_buyer]
```
The last step before you run the optimization is to define the objective function. 
* Recall that you’re trying to maximize your income. Equivalently, you want to make the negative of your income as large a negative number as possible.
* The income that you generate from each sale is the price that the buyer pays multiplied by the number of shares they’re buying. Mathematically, you could write this as `prices[0]*x[0] + prices[1]*x[1] + ... + prices[n]*x[n]`, where `n` is again the total number of buyers. You can represent this more succinctly with the **inner product**, or x.dot(prices).
```python
def objective_function(x, prices):
    return -x.dot(prices)
    # take the dot product of x with prices and return the negative of that value
```
Call `minimize()`:
```python
res = minimize(
    objective_function, # The first positional argument must be the function that you’re optimizing.
    # an initial guess for the values of the solution. 
    # In this case, you’re just providing a random array of values between 0 and 10, with the length of n_buyers.
    x0=10 * np.random.random(n_buyers), # 
    args=(prices,),  # a tuple of other arguments required for the function to optimize
    constraints=constraint, # the constraint you generated earlier 
    bounds=bounds, #sequence of bounds on the solution variables generated previously
)
```
Output of the `minimize()` function:
* `fun` shows the value of the objective function at the optimized solution values
* `x` is an array of values of that optimize the function. 
    * In this case, the result is that you should sell about 1.3 shares to the first buyer, zero to the second buyer, 1.6 to the third buyer, 4.0 to the fourth, and so on

<img src='https://i.imgur.com/q9kkbvl.png' width=500>

# Principle Component Analysis
* [Resource from compass: Principal Component Analysis (PCA) from Scratch | Scott H. Hawley (drscotthawley.github.io)](https://drscotthawley.github.io/blog/2019/12/21/PCA-From-Scratch.html)
* [Resource: Reduce Data Dimensionality using PCA - Python - GeeksforGeeks](https://www.geeksforgeeks.org/reduce-data-dimentionality-using-pca-python/)
* [2022-10-10 lecture slides](https://docs.google.com/presentation/d/1quRSTkDshHvz4n6kHXc6DRYsejK5ivX2CLIViX6hTPk/edit?usp=sharing)
* [2022-10-10 lecture activity](https://github.com/EricElmoznino/lighthouse_dimensionality_reduction_tutorial/blob/master/PCA_demo.ipynb)
* [See exercise](./W04/2022-10-10-dimensionality_reduction_exercise/PCA_exercise.ipynb)

Function/Method | Description | Imports
--- | --- | ---
`pca=PCA(n_components=)` | | from sklearn.decomposition import PCA
`pca.fit(data_scaled)`
`data_pca = pca.transform(data_scaled)`
`pca.components_` | Get the projections ('loadings') of each dimension along each principal component
`plt.arrow(originX,originY,vectorX,vectorY)` | Plot the principal component vectors
`pca.explained_variance_ratio_` | Get relevant data for scree plot and cumulative explained ratio plot
`pca.inverse_transform(data_pca)` | Reconstruct the data using the eigenvectors from the principal component analysis (`PCA()` object)


```python
from sklearn.preprocessing import StandardScaler  # to standardize the features
from sklearn.decomposition import PCA  # to apply PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Scale the data
scaler = StandardScaler() 
data_scaled = pd.DataFrame(scaler.fit_transform(data))

# Apply PCA
pca = PCA(n_components=2)
pca.fit(data_scaled)
data_pca = pca.transform(data_scaled)
data_pca = pd.DataFrame(data_pca)

```
## Projecting the PCA Data
[Resource: Principal Component Analysis Visualization · (ostwalprasad.github.io)](https://ostwalprasad.github.io/machine-learning/PCA-using-python.html)
```python
# Get the projections ('loadings') of each dimension along each principal component:
loadings = pd.DataFrame(pca.components_)

# rename the columns from the PCA dataframe result
loadings.columns = data.columns

# Create a loading plot
for feature, vector in loadings.items():
    # Plot each feature using the two principal components as axes
    plt.arrow(0,0,vector[0],vector[1]) 
    # Label each arrow at the tip of the line
    plt.text(vector[0],vector[1],feature)
plt.xlabel('PC1')
plt.ylabel('PC2')

# To plot the raw data along with the loading plot, scale the raw data down:
xscale = 1/(data_pca[0].max()-data_pca[0].min())
yscale = 1/(data_pca[1].max()-data_pca[1].min())
# Make the plots
sns.scatterplot(x=data_pca[0]*xscale,y=data_pca[1]*yscale,hue=target)
for feature, vector in loadings.items():
    # Plot each feature using the two principal components as axes
    plt.arrow(0,0,vector[0],vector[1]) 
    # Label each arrow at the tip of the line
    plt.text(vector[0],vector[1],feature)
plt.xlabel('PC1')
plt.ylabel('PC2')
```
## Reconstruct data from PCA
```python
reconst = pca.inverse_transform(data_pca)

# Optional: convert to dataframe and add back column names
reconst = pd.DataFrame(reconst)
reconst.columns=data.columns 
```

## How to find the eigenvectors of a matrix
To do Principal Component Analysis, we need to find the aforementioned "components," and this requires **finding eigenvectors for our dataset's covariance matrix**. 

Given some matrix (or 'linear operator') ${\bf A}$ with dimensions $n\times n$ (i.e., n rows and n columns), there exist a set of n vectors $\vec{v}_i$ (each with dimension n, and i = 1...n and i=1...n counts which vector we're talking about) such that multiplying one of these vectors by ${\bf A}$ results in a vector (anti)parallel to $\vec{v}_i$, with a length that's multiplied by some constant $\lambda_i$. i.e.:
​
$$
A \vec{v}_{i} = \lambda_{i}\vec{v}_{i}
$$ 
* A: Matrix (linear operator). *In the context of PCA, this will be the covariation matrix of the features.*
* $\vec{v}_{i}: eigenvector_{i}$
* lambda:  eigenvalue

<details>

<summary>Example using `LA.eig()` function</summary>

Function/Method | Description
--- | ---
`np.var(x)` | Variance
`np.cov(data) ` | Create a coovariance matrix between each pair of dimensions
`lambdas, vs = LA.eig(A)` | Find the eigenvalues and eigenvectors of a covariate matrix

```python
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.feature_selection import f_regression, SelectKBest

N = 100 
x = np.random.normal(size=N)
y = 0.5*x + 0.2*(np.random.normal(size=N))

# Plot the data
fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='markers', 
                marker=dict(size=8,opacity=0.5), name="data" )])
fig.update_layout( xaxis_title="x", yaxis_title="y",
    yaxis = dict(scaleanchor = "x",scaleratio = 1) )
fig.show()

# pack the x & y data together in one 2D array
data = np.stack((x,y),axis=1)   
# Find the covariance. .T b/c numpy wants varibles along rows rather than down columns?
cov = np.cov(data.T)   
```

```python
from numpy import linalg as LA
lambdas, vs = LA.eig(cov)
lambdas, vs

A = np.array([[-2,2,1],[-5,5,1],[-4,2,3]])

def sorted_eig(A):  # For now we sort 'by convention'. For PCA the sorting is key. 
    lambdas, vs = LA.eig(A) # Returns eigenvalue and eigenvector, respectively
    # Next line just sorts values & vectors together in order of decreasing eigenvalues
    lambdas, vs = zip(*sorted(zip(list(lambdas), list(vs.T)),key=lambda x: x[0], reverse=True))
    return lambdas, np.array(vs).T  # un-doing the list-casting from the previous line

lambdas, vs = sorted_eig(A)

# Re-plot our data
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,mode='markers',  
        marker=dict(size=8,opacity=0.5), name="data" ) ])

# Draw some extra 'lines' showing eigenvector directions
n_ev_balls = 50    # the lines will be made of lots of balls in a line
ev_size= 3    # size of balls
t = np.linspace(0,1,num=n_ev_balls)  # parameterizer for drawing along vec directions

for i in range(3):   # do this for each eigenvector 
    # Uncomment the next line to scale (unit) vector by size of the eigenvalue
    # vs[:,i] *= lambdas[i] 
    ex, ey, ez = t*vs[0,i], t*vs[1,i],  t*vs[2,i]
    fig.add_trace(go.Scatter3d(x=ex, y=ey, z=ez,mode='markers',
                marker=dict(size=ev_size,opacity=0.8), name="v_"+str(i+1)))

fig.update_layout( xaxis_title="x", yaxis_title="y", yaxis = dict(scaleanchor = "x",scaleratio = 1) )
fig.show()
```
</details>

# Variable / Feature Selection
## Filter Methods

[Compass lesson: Filter Methods](https://i.imgur.com/JLPzxbs.png)
<img src='https://i.imgur.com/JLPzxbs.png'>
[Walkthrough](https://data.compass.lighthouselabs.ca/days/w04d1/activities/520)

Function/Method | Description | Required imports
--- | --- | -
`vt = VarianceThreshold(0.1)`<br> `vt.fit_transform(df)` | remove the columns with very little variance | from sklearn.feature_selection import VarianceThreshold
`.get_support()` | Get a mask, or integer index, of the features selected
`skb = SelectKBest(f_regression)` | select the k-best features in terms of the relationship with the target variable | from sklearn.feature_selection import f_regression, SelectKBest
`skb.fit_transform(df_transformed, target)`

Before doing any transformations we will extract our target variable to keep it as it is. Even though we can do some transformations to it, it is a good practice to do it separately:
```python
from sklearn.feature_selection import VarianceThreshold
import seaborn as sns
import numpy as np 

y = df_numeric.SalePrice
df_numeric.drop("SalePrice",axis=1, inplace=True)
```
### Part 1: Removing Features With Small Variance
```python
vt = VarianceThreshold(0.1)
df_transformed = vt.fit_transform(df_numeric)

# get_support() is method of VarianceThreshold and stores boolean of each variable in the numpy array.
selected_columns = df_numeric.columns[vt.get_support()]
# transforming an array back to a data-frame preserves column labels
df_transformed = pd.DataFrame(df_transformed, columns = selected_columns)
```

### Part 2: Removing Correlated Features
The goal of this part is to remove one feature from each highly correlated pair.
* The `zip(*iterable)` function allows you to iterate over several iterables in parallel, producing tuples with an item from each one.

```python
# step 1
df_corr = df_transformed.corr().abs()

# step 2: 
indices = np.where(df_corr > 0.8) 
indices = [(df_corr.index[x], df_corr.columns[y]) 
    for x, y in zip(*indices)
        if x != y and x < y] # `x < y` expression avoids dropping both columns

# step 3: Drop one column from each pair that is correlated at least 0.8
for idx in indices: #each pair
    try:
        df_transformed.drop(idx[1], axis = 1, inplace=True)
    except KeyError:
        pass
```
### Part 3: Forward Regression
select the k-best features in terms of the relationship with the target variable. We will use the forward wrapper method for that:

```python
skb = SelectKBest(f_regression, k=10)
X = skb.fit_transform(df_transformed, y)
# We have assigned our target variable SalePrice into y in the beginning of this tutorial.

# Convert X back to a data-frame and assign back the correct column names.
X = pd.DataFrame(X,columns=df_transformed.columns[skb.get_support()])
```

## Wrapper Methods
[Compass lesson](https://data.compass.lighthouselabs.ca/9a4b0f8f-14a1-4647-b8b1-ab89193f3ab7)

<img src='https://i.imgur.com/XwtNhxT.png'>

Some of the most popular examples of wrapper methods are:
* Forward selection
* Backward elimination
* Stepwise selection

# Supervised Learning
## Error
[Lesson](https://data.compass.lighthouselabs.ca/689547b2-da99-410b-a174-c4bdcc57d282)

Error Type | Description | Example
--- | --- | -
Approximation Error | If we choose an H (the pool of functions h we can choose from) or an l which are too simple, the accuracy of our model will be negatively affected by the approximation error. | For example, if we have an image classification task and we choose the H as any logistic regression (or another model not complex enough for this kind of task). In this case, no matter how much data we have, we will end up with a poor model because of a big approximation error.
Estimation Error  | We deal with the estimation error when we don't feed the model with enough data. Complex functions require more data to learn properly. | We have an image classification task and we correctly choose to train a model with Deep Neural Networks but we only have 100 pictures in our training set. No matter what we do, our model will be weak because of a huge estimation error.
Optimization Error | The optimization error occurs when we have a loss function which is too complex, and as a result we don't find the optimal solution. A huge amount of observations can increase the optimization error as well. | 

# Regression
[Resource: Linear Regression in Python using Statsmodels - Data to Fish](https://datatofish.com/statsmodels-linear-regression/)

[Walkthrough](https://data.compass.lighthouselabs.ca/activities/533)
* Linear regression can be performed in Python using either `statsmodels` package or `sklearn` package. Only `statsmodels` will provide the p-values.

## `statsmodels` method

Function/Method | Description | Imports
--- | --- | -
`model = sm.OLS(y, x).fit()` | Creates the linear regression object | import statsmodels.api as sm
`predictions = model.predict(x)` | 
`model.summary()` | prints the results of the linear regression

```python
import pandas as pd
import statsmodels.api as sm


data = {'year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
        'month': [12,11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
        'interest_rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
        'unemployment_rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
        'index_price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
        }

df = pd.DataFrame(data) 

x = df[['interest_rate','unemployment_rate']]
y = df['index_price']

# We have to add an intercept to our predictive dataset to also estimate the intercept. If we don't do that the intercept will be considered 0.
x = sm.add_constant(x)

model = sm.OLS(y, x).fit()
predictions = model.predict(x) 

print_model = model.summary()
print(print_model)
```

## `sklearn` method

Function/Method | Description | Import
--- | --- | -
`regressor = LinearRegression()` | Initialize linear regression object. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html). | from sklearn.linear_model import LinearRegression
`regressor.fit(X, y)` 
`regressor.coef_` | Obtain the beta coefficient for each parameter.
`regressor.score(X,y)` | Get R squared value.
`regressor = Ridge(alpha=1.0)` | Ridge regression. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html?highlight=ridge#sklearn.linear_model.Ridge). | from sklearn.linear_model import Ridge 
`regressor = linear_model.Lasso(alpha=1.0)` | Lasso regression. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html?highlight=lasso#sklearn.linear_model.Lasso).| from sklearn import linear_model

### Linear regression

```python
from sklearn.linear_model import LinearRegression
# initialize the object 
regressor = LinearRegression()

# fit the model on our data
regressor.fit(X, y)

print(regressor.coef_)
regressor.score(X,y)
```

### Ridge regression
```python
from sklearn.linear_model import Ridge

clf = Ridge(alpha=1.0)
clf.fit(X, y)
```
### Lasso Regression

```python
from sklearn import linear_model

clf = linear_model.Lasso(alpha=0.1)
clf.fit(X, y)
```

## Polynomial linear regression
Function/Method | Description
--- | ---
`np.poly1d([4,3,2,1])` | Creates a polynomial expression with the polynomial’s coefficients specified in the parameters in decreasing powers, or if the value of the second parameter is True, the polynomial’s roots. [See documentation](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html).
`np.dot(array1,array1)` | Dot product
`.T` or `.transpose()` | Take the transpose

```python
# Create a 3rd order polynomial
f = np.poly1d([4,3,2,1])
# This creates the polynomial expression 4 x**3 + 3 x**2 + 2 x + 1
```
# Logistical regression
## `sklearn`
* [Logistic Regression Example in Python: Step-by-Step Guide - Just into Data](https://www.justintodata.com/logistic-regression-example-in-python/)
* [Walkthrough](https://data.compass.lighthouselabs.ca/days/w05d2/activities/582)

When the probability is higher than 0.5, `.predict()` always returns 1.
* Sometimes, it's better to use the `.predict_proba()` method and apply a custom cut-off to decide between the labels. For example, in credit scoring, we can disapprove loans when the probability of default is higher than 0.2. The cut-off doesn't always need to be 0.5.

Function/Method | Description | Import
--- | --- | ---
`pd.get_dummies(df, columns=columns, drop_first=True)`
`LogisticRegression()` | | from sklearn.linear_model import LogisticRegression
`.fit(X,y)`
`.predict_proba(X)` | Probability estimates.
`label_binarize(y, classes=classes_list)` | Binarize labels in a one-vs-all fashion. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html).
`.coef_` | Coefficient of the features in the decision function.
`.intercept_` | Intercept (a.k.a. bias) added to the decision function.

```python
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X,y)

y_lr = lr.predict(X)

```

### Ridge classifier
```python
rr = RidgeClassifier(alpha=0.1)
rr.fit(X,y)
y_rr = rr.predict(X)
```

## Statsmodels
[Resource](https://www.andrewvillazon.com/logistic-regression-python-statsmodels/)

Function/Method | Description | Imports
--- | ---- | ---
`model = sm.Logit(y, sm.add_constant(X))` | Instantiate logistic regression. `sm.add_constant(X)` is necessary if model has a y-intercept. [See documentation](https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.Logit.html#statsmodels.discrete.discrete_model.Logit).[See documentation example](https://www.statsmodels.org/dev/examples/notebooks/generated/discrete_choice_overview.html). | import statsmodels.api as sm
`sm.GLM(y_train, sm.add_constant(X_train), family=sm.families.Binomial())` | Another way to instantiate logistic regression. [See documentation](https://www.statsmodels.org/dev/generated/statsmodels.genmod.generalized_linear_model.GLM.html#statsmodels.genmod.generalized_linear_model.GLM). [See documentation example](https://www.statsmodels.org/dev/examples/notebooks/generated/glm.html). | 
`fit_model.summary()` | Print the summary of the fit model
`fit_model.predict(sm.add_constant(X))` | Predict
`fit_model.params` | Get feature coefficcients

### `Logit` class
```python
import statsmodels.api as sm
from sklearn.metrics import classification_report

def run_statsmodel(model, X_test=X_test2, y_test=y_test):
    fit_model = model.fit()
    y_pred = fit_model.predict(sm.add_constant(X_test))
    print(f'Model coefficients: {fit_model.params}')
    print(classification_report(y_test, list(map(round, y_pred))))
    return y_pred

```

### `GLM` class
```python
import statsmodels.api as sm
model_GLM = sm.GLM(y_train, sm.add_constant(X_train), family=sm.families.Binomial())
fit_GLM = model_GLM.fit()
y_pred_GLM = fit_GLM.predict(sm.add_constant(X_test))

# Print model summary
print(fit_GLM.summary())
```
# Generalized Linear Model
[Resource: Regression Challenge: Day 1 (Python) | Kaggle](https://www.kaggle.com/code/ykondo/regression-challenge-day-1-python/notebook)

Function/Method | Description | Imports
--- | ---- | ---
`X = sm.add_constant(X)` | Add a column of ones to an array to account for the y-intercept. |  import statsmodels.api as sm
`model = sm.GLM(y, X, family=family)` | Initiate the GLM class. The default `family=` parameter is Gaussian.
`model.fit()` | Fit the data to the model
` model.fittedvalues` | Get the fitted values

This is the list of probability distributions and their canonical link functions.
* Normal distribution: identity function
* Poisson distribution: log function
* Binomial distribution: logit function

Parameter | Description
--- | ---
`family = sm.family.Binomial()`
`family=sm.families.Poisson()` 
`family=sm.families.Gaussian(sm.families.links.log)` | Fit normally-distributed data to exponential relationship

```python
import statsmodels.api as sm

# since I am predicting a count value, I should fit a poisson regression. 
X = bikes['Average Temp']
y = bikes['Total']

# add intercept to input variable
X = sm.add_constant(X)

# fit poisson regression model 
model = sm.GLM(y, X, family=sm.families.Poisson()).fit()

# add poisson fitted values to dataframe
bikes['reg_fit'] = model.fittedvalues
```

# Training Test Frameworks
[Resource: Understanding the data splitting functions in scikit-learn | by Julie Yin | Medium](https://medium.com/@julie.yin/understanding-the-data-splitting-functions-in-scikit-learn-9ae4046fbd26)

* Testing data should be scaled using the same scaler as the training data, i.e. if standard scaler was used, test data should be scaled to the same mean and SD as the training data.


Description | Function/Method | Imports
--- | ---- | ---
[Split data into 2 groups](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html?highlight=model_selection) | `X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75,test_size=0.25)`<br><br>`df_train, df_test = train_test_split(df, test_size=0.2, stratify=df['target'])` | from sklearn.model_selection import train_test_split
Cross validation | `kf = KFold(n_splits=5, shuffle=True)` | from sklearn.model_selection import KFold
[Leave one out](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html?highlight=leaveoneout#sklearn.model_selection.LeaveOneOut) | `loo = LeaveOneOut()`<br>`loo.get_n_splits(X)` | from sklearn.model_selection import LeaveOneOut
Iterate over the training and testing indices when there are multiple pairs. | `.split(X)` | 

## Splitting data 
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75,test_size=0.25, random_state=101)
```
If data is in a dataframe:
```python
df_train, df_test = train_test_split(df, test_size=0.2, random_state=random_seed, stratify=df['target'], random_state=1)
```
`stratify=df['target']` parameter: when the dataset is imbalanced, it’s good practice to do stratified sampling. In this way, both the training and test datasets will have similar portions of the target classes as the complete dataset.

## Cross validation with `KFold`
```python
from sklearn.model_selection import KFold
import numpy as np
kf = KFold(n_splits=5, shuffle=True)
X = np.array(X)
y = np.array(y)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
```
## Leave one out
```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()

# Get the number of splits
loo.get_n_splits(X)

for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    print("TRAIN:", train_index, "TEST:", test_index)
```
# Model evaluation with cross validation
* [sckilearn tutorial](https://scikit-learn.org/stable/modules/cross_validation.html?highlight=cross+validation)

Function/Method | Description | Imports
--- | ---- | ---
`cross_validate(model, X, y, cv=10, scoring=)` | Evaluate metric(s) by cross-validation. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate). | from sklearn.model_selection import cross_validate

```python
cv_results = cross_validate(model, X, y, cv=10,
    scoring=['r2', 'neg_mean_absolute_error']
    )
scores = dict()
scores['mae']= cv_results['test_neg_mean_absolute_error'].mean()
scores['r2'] = cv_results['test_r2'].mean()
```

# Hyperparameter selection
## Grid Search
By default, the `GridSearchCV`’s cross validation uses 3-fold KFold or StratifiedKFold depending on the situation.

Function/Method | Description | Imports
--- | ---- | ---
`grid = GridSearchCV(estimator=model, param_grid=param_grid)` | Grid search. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html?highlight=gridsearchcv#sklearn.model_selection.GridSearchCV). | from sklearn.model_selection import GridSearchCV
. | `score=` <br>Indicate which evaluation metric on which to base best estimator. [See documentation](https://scikit-learn.org/stable/modules/model_evaluation.html#the-scoring-parameter-defining-model-evaluation-rules).
`grid.fit(X_train, y_train)` | Train the classifier
`.best_estimator_` | View and/or create a new model objecting using the best model and its parameters from grid search
`.best_score_` | The best R^2 score obtained on the test data
`.best_params_` | The best parameter settings to achieve the highest R^2 (dictionary)
`..cv_results_` | Returns a table of the grid search cross-validation results

```python
from sklearn.model_selection import GridSearchCV

# Make a dictionary with model arguments as keys and lists of grid settings as values
param_grid = {
    'alpha': [0.001, 0.01, 0.1, 1],
    'l1_ratio': [0, 0.25, 0.5, 0.75, 1]
}

# initiate the grid search object using an estimator/model object, e.g. `LogisticRegression()`
grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=k_folds, scoring='r2') # see documentation for more details
grid_result = grid.fit(X_scaled, y)

best_r2 = grid_result.best_score_
best_alpha = grid_result.best_params_['alpha']
best_l1_ratio = grid_result.best_params_['l1_ratio']

# Using the best hyperparameters, retrain on the entire train set and evaluate on the test set
best_model = grid_result.best_estimator_    # Sklearn automatically retrains the model on the whole training set following cross-validation using the best hyperparameters
y_pred = best_model.predict(X_test)

#'R^2 on the test set:
r2_test = r2_score(y_test, y_pred)
```
## Random search

```python
from sklearn.model_selection import RandomizedSearchCV

distributions = dict(C=uniform(loc=0, scale=4),
        penalty=['l2', 'l1'])

clf = RandomizedSearchCV(logistic, distributions, random_state=0)
search = clf.fit(X_train, y_train)
search.best_params_

```

2022-10-17 lecture

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
reg = LinearRegression()
reg.fit(X_train, y_train)

y_train_pred = reg.predict(X_train)
y_test_pred = reg.predict(X_train)

r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)
```

```python
from sklearn.preprocessing import PolynomialFeatures

# Create polynomial feature set
Xpoly_train = PolynomialFeatures(degree=2).fit_transform(X_train)
Xpoly_test = PolynomialFeatures(degree=2).fit_transform(X_test)

# Train our model
reg.fit(Xpoly_train, y_train)
ypoly_train_pred = reg.predict(Xpoly_train)
ypoly_test_pred = reg.predict(Xpoly_test)

# Check performance on train and test set
r2poly_train = r2_score(y_train, ypoly_train_pred)
r2poly_test = r2_score(y_test, ypoly_test_pred)

```
To see if a model is under- or overfitting, try increasing model complexity to see if model performance improves or gets worse.

## K Fold Cross-Validation

```python
from sklearn.model_selection import KFold

# list that will accumulate test performance on each fold
cv_r2 = []

kf = KFold(nsplits=k_folds) #initialize

for tran_idx, test_indx in kf.split(X): # creates indices for training vs. testing data in that fold
    X_train, X_test, y_train, y_test = X[train_idx], X[test_idx], y[train_idx], y[test_idx]

    # train the model
```

```python
from sklearn.model_selection import cross_val_score

cv_r2 = cross_val_score(reg, X, y, cv=k_folds, scoring='r2')
print(f'Cross-validated R^2\nMean:\t:{cv_r2.mean()}\nStd.:\t{cv_r2.std()})

```
After cross-validation, train with all the data to get the final model.


# Evaluating Models
## Regression evaluation
* [Regression: An Explanation of Regression Metrics And What Can Go Wrong | by Divyanshu Mishra | Towards Data Science](https://towardsdatascience.com/regression-an-explanation-of-regression-metrics-and-what-can-go-wrong-a39a9793d914)
* [Walkthrough: Model Evaluation](https://data.compass.lighthouselabs.ca/days/w05d1/activities/573)

. | Description | Command | Import
--- | --- | --- | ---
Mean Squared Error (MSE) | the average of the squared difference between the target value and the value predicted by the regression model.| `MSE = mean_squared_error(y_true, y_pred)`<br>[See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html?highlight=mean_squared_error#sklearn.metrics.mean_squared_error). | from sklearn.metrics import mean_squared_error
Root-Mean-Squared-Error (RMSE) | square root of the averaged squared difference between the target value and the value predicted by the model | `RMSE = mean_squared_error(y_true, y_pred, squared=False)`<br>or<br>`np.sqrt(MSE)`
Mean-Absolute-Error (MAE) | absolute difference between the target value and the value predicted by the model. | `mean_absolute_error(y_true, y_pred)` <br>[See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html?highlight=mean_absolute_error#sklearn.metrics.mean_absolute_error). | from sklearn.metrics import mean_absolute_error
R² or Coefficient of Determination | compare our current model with a constant baseline and tells us how much our model is better. The constant baseline is chosen by taking the mean of the data and drawing a line at the mean | `r2_score(y_true, y_pred)`<br>[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html?highlight=r2_score) | from sklearn.metrics import r2_score
Adjusted R² | Adjusted R² is always lower than R² as it adjusts for the increasing predictors and only shows improvement if there is a real improvement

### Mean Squared Error (MSE) / Root Means Squared Error (RMSE)
```python
# import MSE from sklearn
from sklearn.metrics import mean_squared_error

# compute MSE
MSE = mean_squared_error(y_true,y_pred)  

# RMSE by Numpy
RMSE = np.sqrt(MSE)
print(RMSE)

# RMSE by sklearn
RMSE = mean_squared_error(y_true,y_pred,squared=False)
print(RMSE)
```
### $ R^2 $ Score

```python
# Train our model
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train, y_train)

# Check performance on train and test set
from sklearn.metrics import r2_score

y_train_pred = reg.predict(X_train)
y_test_pred = reg.predict(X_test)

r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)
```
### Adjusted R^2 score
[Resource: How to Calculate Adjusted R-Squared in Python - Statology](https://www.statology.org/adjusted-r-squared-in-python/)
![adjusted R-squared formula](https://miro.medium.com/max/640/0*WkdWEm2993yhYvUA.png)
```python
#fit regression model
model = LinearRegression()
X, y = data[["mpg", "wt", "drat", "qsec"]], data.hp
model.fit(X, y)

#display adjusted R-squared
1 - (1-model.score(X, y))*(len(y)-1)/(len(y)-X.shape[1]-1)
```

## Classification evaluation
[How to Choose Evaluation Metrics for Classification Models (analyticsvidhya.com)](read://https_www.analyticsvidhya.com/?url=https%3A%2F%2Fwww.analyticsvidhya.com%2Fblog%2F2020%2F10%2Fhow-to-choose-evaluation-metrics-for-classification-model%2F)

A common classification problem would be using a diagnostic test for a disease.

. | Description | Command | Import
--- | --- | --- | ---
confusion matrix | Table of true vs. predicted classifications | `ConfusionMatrixDisplay.from_predictions(y_true, y_pred)` or <br>`ConfusionMatrixDisplay.from_estimator` | from sklearn.metrics import ConfusionMatrixDisplay
.| Array of confusion matrix values without the plot | `confusion_matrix(y_true, y_pred)` | from sklearn.metrics import confusion_matrix
accuracy |  Number of correct predictions / Total number of predictions. | `accuracy = accuracy_score(y_true,y_pred)` | from sklearn.metrics import accuracy_score
Recall (Sensitivity or True positive rate) | Recall gives the fraction you correctly identified as positive out of all positives.<br> $ \frac{correctPositiveTests}{totalPositives} \ $ =  $ \frac{truePositives}{truePositives + falseNegatives} \ $ | `recall_score(y_true, y_pred)`<br>[See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html?highlight=recall_score#sklearn.metrics.recall_score). | from sklearn.metrics import recall_score
precision |  Precision gives the fraction of correctly identified as positive out of all predicted as positives.<br>$ \frac{truePositives}{totalPredictedPositive} \ $ = $ \frac{truePositives}{truePositives + falsePositives} \ $ | `precision_score(y_true, y_pred)`<br>[See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html?highlight=precision_score#sklearn.metrics.precision_score).<br><br>`PrecisionRecallDisplay.from_predictions` or `PrecisionRecallDisplay.from_estimator` | from sklearn.metrics import precision_score
F1 Score | Increasing precision reduces recall and vice versa. This is called precision/recall tradeoff.<br>F1 score = $ \frac{precision \times recall}{precision + recall} \ $ | `f1_score = f1_score(y_true, y_pred)` | from sklearn.metrics import f1_score
false positive, true positive rate | | `fpr, tpr, thr = metrics.roc_curve(y_test==label, y_proba[:,label])` | from sklearn import metrics
receiver operator characteristic (and area under the curve) | For a given classification threshold, plot the false positive rate against the true positive rate. The curve with the largest area under the curve is the best. Perfect score is 1.<br>- **False Positive Rate**: Fraction of negative instances that are incorrectly classified as positive.<br>- **True Positive Rate**: Fraction of positive instances that are correctly predicted as positive. | `auc = roc_auc_score(y_true, y_proba)`<br>[See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html?highlight=roc_auc_score#sklearn.metrics.roc_auc_score).<br><br>`RocCurveDisplay.from_estimator(estimator, X, y)`<br> [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions).<br><br>`RocCurveDisplay(fpr, tpr)` [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html?highlight=roccurvedisplay#sklearn.metrics.RocCurveDisplay.from_estimator).| from sklearn.metrics import roc_auc_score<br><br> from sklearn.metrics import RocCurveDisplay <br><br>from sklearn import metrics
log loss (cross-entropy loss) | | `sklearn.metrics.log_loss(y_true, y_proba` | from sklearn.metrics import log_loss
. | Obtain the precision, recall, f1-score, and accuracy and other info |  `classification_report(y_test, y_pred)` | from sklearn.metrics import classification_report

![ROC characteristic](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image3-9.png)
![ROC curve](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image4-9.png)


```python
# ground truth
y_true = [1,1,0,1,0,0,1,0,0,1]

# simulate probabilites of positive class
y_proba = [0.9,0.7,0.2,0.99,0.7,0.1,0.5,0.2,0.4,0.6]

# set the threshold to predict positive class
thres = 0.5

# class predictions
y_pred = [int(value > thres) for value in y_proba]
```
### Confusion matrix display
[See documentation example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py).
```python
disp = ConfusionMatrixDisplay.from_predictions(y_true, y_pred)
# Set the title
disp.ax_.set_title('title')
```

### Accuracy
```python
# import accuracy_score from sklearn
from sklearn.metrics import accuracy_score

# compute accuracy
accuracy = accuracy_score(y_true,y_pred)
```
### Recall
```python
from sklearn.metrics import recall_score

recall_score(y_true, y_pred)
```
### F1-score
```python
# import f1_score from sklearn
from sklearn.metrics import f1_score

# compute F1-score
f1_score = f1_score(y_true,y_pred)
```
### AUC score
In `roc_auc_score` we use probabilities (`y_proba`) instead of class labels.
```python
# import roc_auc_score from sklearn
from sklearn.metrics import roc_auc_score

# compute AUC-score
auc = roc_auc_score(y_true,y_score) # y_score corresponds to probability estimates or non-thresholded decision values
```

#### Calculate ROC for binary logistical regression
```python
lr = LogisticRegression()
lr.fit(X,y)

roc_lr = roc_auc_score(y, lr.predict_proba(X)[:, 1])
```
#### Calculate ROC for binary ridge regression
```python
rr = RidgeClassifier(alpha=0.1)
rr.fit(X,y)

roc_rr = roc_auc_score(y, rr.decision_function(X))
```
### ROC AOC plots
#### Binary classification
```python
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

fig, ax = plt.subplots()
RocCurveDisplay.from_estimator(lr, X, y, ax=ax) # logistic regression ROC plot
RocCurveDisplay.from_estimator(rr, X, y, ax=ax) # ridge classifier ROC plot
```
#### Multi-class
```python
for label in range(number_of_classes+1):
    fpr, tpr, thr = metrics.roc_curve(y_test==label, y_proba[:,label])
    print('threshold', label, ': ', thr)
    RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
### Precision score
```python
from sklearn.metrics import precision_score

precision_score(y_true, y_pred)
```
### Log Loss
```python
# Make sure to initiate the estimator and fit the data first
# Logistical regression
ll_logistical_regression = log_loss(y, lr.predict_proba(X))

# Ridge regression
ll_ridge_regression = roc_auc_score(y, rr.decision_function(X))

```
# Decision Tree
### Attribute Selection Measures

Function/Method | Description | Imports
--- | ---- | ---
Information gain | Decrease in entropy: Difference between entropy before split and average entropy after split based on given attribute values.
Gain ratio | Gain ratio handles the issue of bias by normalizing the information gain using Split Info. The attribute with the highest gain ratio is chosen as the splitting attribute.
Gini index | 

Function/Method | Description | Imports
--- | ---- | ---
`clf = DecisionTreeClassifier()` | Create Decision Tree classifer object | from sklearn.tree import DecisionTreeClassifier
`clf = clf.fit(X_train,y_train)` | Train Decision Tree Classifer
`y_pred = clf.predict(X_test)` | Predict the response for test dataset
`accuracy_score(y_test, y_pred)` | | from sklearn.metrics import accuracy_score
`model = DecisionTreeRegressor(max_depth=3 ).fit(X, y)` | Initiate object and train it | from sklearn.tree import DecisionTreeRegressor

## Classification decision trees
```python
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


#view the entire tree
import os     
os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'

graphviz.Source(export_graphviz(model,
                out_file=None,
                feature_names=X.columns,
                class_names=["blue", "red"],
                impurity=True))
```

<details>

<summary>Function for making decision tree plots</summary>

[See 2022-10-19 lecture notebook](./W05/trees-forests-lecture/Trees_Forests.ipynb)
```python
#function for plotting a decision tree
#input is feature data, class predictions, and the trained model.
def plot_tree(X, y, model, predict_proba = False):
    # Join data for plotting
    sample = (X.join(y))
    # Create a mesh for plotting
    step = (X.max() - X.min()) / 50
    x1, x2 = np.meshgrid(np.arange(sample.min()[0]-step[0], sample.max()[0]+step[0], step[0]),
                         np.arange(sample.min()[1]-step[1], sample.max()[1]+step[1], step[1]))

    # Store mesh in dataframe
    mesh_df = pd.DataFrame(np.c_[x1.ravel(), x2.ravel()], columns=['x1', 'x2'])

    # Mesh predictions
    if predict_proba:
        mesh_df['predictions'] = model.predict_proba(mesh_df[['x1', 'x2']])[:, 0]
        # Plot
        base_plot = alt.Chart(mesh_df).mark_rect(opacity=0.5).encode(
            x=alt.X('x1', bin=alt.Bin(step=step[0])),
            y=alt.Y('x2', bin=alt.Bin(step=step[1])),
            color=alt.Color('predictions', title='P(blue)', scale=alt.Scale(scheme='redblue'))
        ).properties(
            width=400,
            height=400
        )
        return alt.layer(base_plot).configure_axis(
            labelFontSize=20,
            titleFontSize=20
        ).configure_legend(
            titleFontSize=20,
            labelFontSize=20
        )
    else:
        mesh_df['predictions'] = model.predict(mesh_df[['x1', 'x2']])
        # Plot
        scat_plot = alt.Chart(sample).mark_circle(
            stroke='black',
            opacity=0.5,
            strokeWidth=1.5,
            size=100
        ).encode(
            x=alt.X(X.columns[0], axis=alt.Axis(labels=True, ticks=True, title=X.columns[0])),
            y=alt.Y(X.columns[1], axis=alt.Axis(labels=True, ticks=True, title=X.columns[1])),
            color=alt.Color(y.columns[0])
        )
        base_plot = alt.Chart(mesh_df).mark_rect(opacity=0.5).encode(
            x=alt.X('x1', bin=alt.Bin(step=step[0])),
            y=alt.Y('x2', bin=alt.Bin(step=step[1])),
            color=alt.Color('predictions', title='Legend')
        ).properties(
            width=400,
            height=400
        )
        return alt.layer(base_plot, scat_plot).configure_axis(
            labelFontSize=20,
            titleFontSize=20
        ).configure_legend(
            titleFontSize=20,
            labelFontSize=20
        )

## Call on the function
plot_tree(X_train, y_train, model)
```
</details>


## Regression trees
```python
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=3).fit(X, y)

#view decision tree
graphviz.Source(export_graphviz(model,
                out_file=None,
                feature_names=X.columns))

#visualize the decisions
feat1, feat2 = np.meshgrid(np.linspace(2, 8, 60), np.linspace(3, 10, 70))
feat1, feat2 = feat1.flatten(), feat2.flatten()
x = np.stack([feat1, feat2], axis=1)
ypred = model.predict(x)

fig, ax = plt.subplots(figsize=(6, 7))
im = plt.pcolormesh(feat1.reshape(70, 60), feat2.reshape(70, 60), ypred.reshape(70, 60), cmap='Blues')
fig.colorbar(im, ax=ax)
ax.set_xlabel('feat_1')
ax.set_ylabel('feat_2')
plt.show()
```

# Ensemble methods
[Resource: Interpret Logistic Regression Coefficients [For Beginners] – QUANTIFYING HEALTH](https://miro.medium.com/max/1100/1*kISLC1Udq0m6g5kwHhMuJg@2x.png)
<img src="https://miro.medium.com/max/1100/1*kISLC1Udq0m6g5kwHhMuJg@2x.png" width="500">

Function/Method | Description | Imports
--- | ---- | ---
`RandomForestClassifier(n_estimators = ntree)` | | from sklearn.ensemble import RandomForestClassifier
`RandomForestRegressor(max_depth=2, random_state=0)` | [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html?highlight=randomforest#sklearn.ensemble.RandomForestRegressor).| from sklearn.ensemble import RandomForestRegressor
`AdaBoostClassifier(base_estimator = model, n_estimators=3)` |  | from sklearn.ensemble import AdaBoostClassifier
`GradientBoostingRegressor(random_state=0)` | [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html?highlight=gradientboosting#sklearn.ensemble.GradientBoostingRegressor). | from sklearn.ensemble import GradientBoostingRegressor
`xgb.XGBRegressor(tree_method="hist", eval_metric=mean_absolute_error)` | [See documentation](https://xgboost.readthedocs.io/en/stable/python/python_api.html?highlight=xgb.XGBRegressor#xgboost.XGBRegressor). | import xgboost as xgb
`.fit(X_train, y_train)`

## Random forest classifier

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=ntree)
model.fit(X_train, y_train)
```
<details>

<summary>Function to plot training error and testing error, using various amounts of trees in the random forest</summary>

[See 2022-10-19 lecture notebook](./W05/trees-forests-lecture/Trees_Forests.ipynb)
```python
def make_num_tree_plot(X_train, y_train, X_test, y_test, num_trees):
    """
    Make number of trees vs error rate plot for RandomForestClassifier
   
    Parameters
    ----------
    X_train: numpy.ndarray        
        The X part of the train set
    y_train: numpy.ndarray
        The y part of the train set    
    X_test: numpy.ndarray        
        The X part of the test/validation set
    y_test: numpy.ndarray
        The y part of the test/validation set    
    num_trees: int
        The value for `n_estimators` argument of RandomForestClassifier
    Returns
    -------
        None
        Shows the number of trees vs error rate plot
            
    """    
    train_err = []
    test_err = []
    for ntree in num_trees:
        model = RandomForestClassifier(n_estimators=ntree)
        model.fit(X_train, y_train)
        train_err.append(1-model.score(X_train, y_train))
        test_err.append(1-model.score(X_test, y_test))

    fig, ax = plt.subplots()
    ax.plot(num_trees,train_err,label="train")
    ax.plot(num_trees,test_err,label="test")
    ax.set_xlabel('number of trees');
    ax.set_ylabel('error rate');
    ax.set_xscale('log')
    ax.legend()
    plt.show()

#fit a random forest for various n_estimators and plot the error
make_num_tree_plot(X_train, y_train, X_val, y_val, (1,5,10,25,50,100,200,500))
```

</details>

## Random forest regressor

```python
from sklearn.ensemble import RandomForestRegressor

regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(X, y)
```
## Adaptive boosting

```python
from sklearn.ensemble import AdaBoostClassifier

#create the adaboost classifier and fit it
ensemble = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=2), n_estimators=3)
ensemble.fit(X_train_circ, y_train_circ)
```
<details>

<summary>Custom function to plot adaptive boosting </summary>

[See 2022-10-19 lecture notebook](./W05/trees-forests-lecture/Trees_Forests.ipynb)
```python
#located in plotclassifier.py (contains plot_classifier function)
from plotclassifier import *

# Combine weak learners 
fig, axs = plt.subplots(2, 2, figsize=(20,20))
weights = ensemble.estimator_weights_
for i, estimator in enumerate(ensemble.estimators_): # needs scikit-learn-0.20
    ax = axs[i//2, i % 2]
    plot_classifier(X_train_circ, y_train_circ, estimator, ax=ax)
    tr_err = (1 - estimator.score(X_train_circ, y_train_circ))
    te_err = (1 - estimator.score(X_test_circ, y_test_circ))
    title = f'Round: {i + 1}; Train_error: {tr_err:0.3f}; Test error: {te_err:0.3f}; estimator weight: {weights[i]:0.3f}'
    ax.set_title(title);
    
ax = axs[1, 1]
plot_classifier(X_train_circ, y_train_circ, ensemble, ax=plt.gca())
tr_err = (1 - ensemble.score(X_train_circ, y_train_circ))
te_err = (1 - ensemble.score(X_test_circ, y_test_circ))
title = f'Ensemble model; Train_error: {tr_err:0.3f}; Test error: {te_err:0.3f}'
ax.set_title(title)

plt.show()
```
</details>

## Stacking

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier  #meta model

# Create a simple voting classifier using scikit-learn's VotingClassifier

classifiers = {
    "Decision tree"         : DecisionTreeClassifier(max_depth=5),
    "KNN"                   : KNeighborsClassifier(),
    "Naive Bayes"           : GaussianNB(),
    "Logistic Regression"   : LogisticRegression(),
}

# voting="soft" predicts the class label based on the argmax of the sums of the predicted probabilities
ensemble = VotingClassifier(classifiers.items(), voting="soft")

# note: sklearn doesn't seem to support passing pre-trained classifiers into VotingClassifier
ensemble.fit(X_train, np.ravel(y_train))

print('Ensemble performance: \n')
print("Training error:   %.2f" % (1-ensemble.score(X_train, y_train)))
print("Validation error: %.2f" % (1-ensemble.score(X_val, y_val)))

## What's the performance of individual classifiers in the ensemble?
for name, estimator in ensemble.named_estimators_.items(): # needs scikit-learn-0.20
    tr_err = (1 - estimator.score(X_train, y_train))
    te_err = (1 - estimator.score(X_val, y_val))
    print('%s: Train_error: %0.3f; Validation error: %0.3f'%(name, tr_err, te_err))
```
<details>

<summary>Plot the results using custom function </summary>

[See 2022-10-19 lecture notebook](./W05/trees-forests-lecture/Trees_Forests.ipynb)
```python
#located in plotclassifier.py (contains plot_classifier function)
from plotclassifier import *

plt.figure(figsize=(16,16))
count = 1
for name, estimator in ensemble.named_estimators_.items(): # needs scikit-learn-0.20
    plt.subplot(3,2,count)
    plot_classifier(X_train, y_train, estimator, ax=plt.gca());
    tr_err = (1 - estimator.score(X_train, y_train))
    te_err = (1 - estimator.score(X_val, y_val))
    title = '%s: Train_error: %0.3f; Test error: %0.3f'%(name, tr_err, te_err)    
    plt.title(title);
    count += 1
    
plt.subplot(3,2,6)
plot_classifier(X_train, y_train, ensemble, ax=plt.gca());
tr_err = 1 - ensemble.score(X_train, y_train)
te_err = 1 - ensemble.score(X_val, y_val)
title = '%s; Train_error: %0.3f; Test error: %0.3f'%('Ensemble', tr_err, te_err)    
plt.title(title);
```

</details>

## Gradient boost

```python
from sklearn.ensemble import GradientBoostingRegressor

reg = GradientBoostingRegressor(random_state=0)
```
## XGBoost
[resource: Using XGBoost in Python Tutorial | DataCamp](https://www.datacamp.com/tutorial/xgboost-in-python)

[XGBoost documentation](https://xgboost.readthedocs.io/en/stable/parameter.html)

Function/Method | Description | Imports
--- | ---- | ---
`.get_params`

```python
import xgboost as xgb
from sklearn.metrics import mean_squared_error

X, y = data.iloc[:,:-1],data.iloc[:,-1]

# instantiate an XGBoost regressor object
xg_reg = xgb.XGBRegressor()

# Fit the regressor to the training set and make predictions on the test set 
xg_reg.fit(X_train,y_train)
preds = xg_reg.predict(X_test)
```
XGBoost's hyperparameters
* learning_rate: step size shrinkage used to prevent overfitting. Range is [0,1]
* max_depth: determines how deeply each tree is allowed to grow during any boosting round.
* subsample: percentage of samples used per tree. Low value can lead to underfitting.
* colsample_bytree: percentage of features used per tree. High value can lead to overfitting.
* n_estimators: number of trees you want to build.
* objective: determines the loss function to be used like reg:squarederror (default) for regression problems, reg:logistic for classification problems with only decision, binary:logistic for classification problems with probability.

XGBoost also supports regularization parameters to penalize models as they become more complex and reduce them to simple (parsimonious) models.
* gamma: controls whether a given node will split based on the expected reduction in loss after the split. A higher value leads to fewer splits. Supported only for tree-based learners.
* alpha: L1 regularization on leaf weights. A large value leads to more regularization.
* lambda: L2 regularization on leaf weights and is smoother than L1 regularization.
<br><br>
### k-fold Cross Validation with XGBoost

XGBoost supports k-fold cross validation via the `cv()` method. All you have to do is specify the nfolds parameter, which is the number of cross validation sets you want to build. Also, it supports many other parameters (check out this link) like:
* num_boost_round: denotes the number of trees you build (analogous to n_estimators)
* metrics: tells the evaluation metrics to be watched during CV
* as_pandas: to return the results in a pandas DataFrame.
* early_stopping_rounds: finishes training of the model early if the hold-out metric ("rmse" in our case) does * not improve for a given number of rounds.
* seed: for reproducibility of results.

```python
# Convert the dataset (not yet split) into an optimized data structure called Dmatrix that XGBoost supports and gives it acclaimed performance and efficiency gains. 
data_dmatrix = xgb.DMatrix(data=X,label=y)

# You will use these parameters to build a 3-fold cross validation model by invoking XGBoost's cv() method and store the results in a cv_results DataFrame. 
params = {'colsample_bytree': 0.3,'learning_rate': 0.1,
        'max_depth': 5, 'alpha': 10}
# Default parameters https://xgboost.readthedocs.io/en/stable/parameter.html:
    # learning rate, aka `eta`, appears to be 0.3 
    # max_depth: 6
    # colsample_bytree: 1
    # alpha: 0

# cv_results contains train and test RMSE metrics for each boosting round.
cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3,
        num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)

# Extract and print the final boosting round metric.
print((cv_results["test-rmse-mean"]).tail(1))

# Train the model
xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=10)
```
### Visualize Boosting Trees and Feature Importance
Once you train a model using the XGBoost learning API, you can pass it to the `plot_tree()` function along with the number of trees you want to plot using the num_trees argument. These plots provide insight into how the model arrived at its final decisions and what splits it made to arrive at those decisions.
```python
import matplotlib.pyplot as plt

# Plotting the first tree
xgb.plot_tree(xg_reg,num_trees=0)
plt.rcParams['figure.figsize'] = [50, 10]
plt.show()
```
Visualize the result as a bar graph, with the features ordered according to how many times they appear using the `plot_importance()` function
```python
xgb.plot_importance(xg_reg)
plt.rcParams['figure.figsize'] = [5, 5]
plt.show()
```
# Bayes theorem
[Reference: 2022-10-20 W05d04 lecture notebook Copy of W5D4_NB.ipynb in google drive](https://colab.research.google.com/drive/1DeqB2t9e0IMUKBAtNVowJp_9qVw-unpQ#scrollTo=4UQRJ9Nraeph)

 $$P(A|B) = \frac{P(B|A) P(A)}{P(B)} $$

In a bayes classifier, the above is represented by:
 $$P(class|data) = \frac{P(data|class) P(class)}{P(data)} $$

* $P(class|data)$:  Posterior
* $P(data|class)$: Likelihood.
* $P(class)$: Prior
* $P(data)$: Marginal probability.

If any two events A and B are independent, then 
`P(A,B) = P(A)P(B)`
* P(A,B) is the probability of both A and B.

Hence, we reach to the result:

$$ P(y|x_1,...,x_n) = \frac{ P(x_1|y)P(x_2|y)...P(x_n|y)P(y)}{P(x_1)P(x_2)...P(x_n)}  $$

which can be expressed as:

$$ P(y|x_1,...,x_n) = \frac{P(y)\prod_{i=1}^{n}P(x_i|y)}{P(x_1)P(x_2)...P(x_n)}  $$


Function/Method | Description | Imports
--- | --- | ---
`GaussianNB()` | [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html?highlight=gaussiannb#sklearn.naive_bayes.GaussianNB). | from sklearn.naive_bayes import GaussianNB
`.fit(X_train, y_train)`
`.predict(X_test)`

```python
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)


from sklearn.naive_bayes import MultinomialNB

mnb = MultinomialNB()

mnb.fit(X_counts_train, y_counts_train)
```
# Support Vector Machines (SVM)
[2022-10-20 lecture notebook](https://colab.research.google.com/drive/1NwBjC4JD5WZBH3OEQhDbNz76tSFfEdI6#scrollTo=zMdjqOLrcXjf)<br>
[Resource: Scikit-learn SVM Tutorial with Python (Support Vector Machines) | DataCamp](https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python)

Gamma and  C control the complexity (fundamental trade-off), just like other hyperparameters we've seen.

[See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html?highlight=svc#sklearn.svm.SVC).

Hyperparamter | Description | High value | Low value
--- | ---- | --- | ---
`kernel` | {‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
`gamma` | Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’. | more complex | less complex
`C` | Regularization parameter | more complex (smaller regularization penatly) | less complex

```python
from sklearn.svm import SVC

svm = SVC(kernel="rbf", gamma=0.01, C=1.0) 
svm.fit(X_train, y_train)

```

<details>
<summary>To plot 2D SVC results </summary>

```python
!pip install git+https://github.com/mgelbart/plot-classifier

plt.title("SVC")
plot_classifier(X_train, y_train, svm, ax=plt.gca())

# circle support vectors
plt.scatter(*svm.support_vectors_.T, marker="o", edgecolor="yellow", facecolor="none", s=120);
```
</details>

<details>
<summary>Plot 2D SVC results with support vector and their projections </summary>

```python
plt.figure()
plot_classifier(X, y, svm, ax=plt.gca());
plt.scatter(*svm.support_vectors_.T, marker="o", edgecolor="yellow", facecolor="none", s=120);
plt.axis('equal');
plt.axis('square');

def SV_proj(svm):
    v = svm.support_vectors_
    s = np.array([svm.coef_.flatten()[1], -svm.coef_.flatten()[0]])
    w = svm.coef_
    return (v@s[:,None])/(s@s) * s - w/(w@w.T)*svm.intercept_
proj = SV_proj(svm)

for i in range(len(proj)):
    p = proj[i]
    sv = svm.support_vectors_[i]
    plt.plot((p[0],sv[0]),(p[1],sv[1]), 'yellow')
```
</details>


# Saving and loading python objects
## Pickle and pickling
[Python Pickling (tutorialspoint.com)](https://www.tutorialspoint.com/python-pickling)

```python
import pickle

# Pickle a simple list: Pickle_list1.py

import pickle
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)

# Unpickle a simple list: unpickle_list1.py
pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)

# Pickle a simple dictionary −
EmpID = {1:"Zack",2:"53050",3:"IT",4:"38",5:"Flipkart"}
pickling_on = open("EmpID.pickle","wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()

# Unpickle a dictionary −
pickle_off = open("EmpID.pickle", 'rb')
EmpID = pickle.load(pickle_off)
```
## `joblib`
[Resource: Persistence — joblib 1.3.0.dev0 documentation](https://joblib.readthedocs.io/en/latest/persistence.html)

In the specific case of Sklearn, it may be better to use joblib’s substitute of pickle (dump & load), which is more efficient on objects that carry large numpy arrays internally, which is often the case for fitted Sklearn estimators.

```python
import joblib

with open(filename, 'wb') as fo:  
   joblib.dump(to_persist, fo)
with open(filename, 'rb') as fo:  
   joblib.load(fo)
```
Setting the compress argument to True in joblib.dump() will allow to save space on disk:
```python
joblib.dump(to_persist, filename + '.compressed', compress=True)  
```
If the filename extension corresponds to one of the supported compression methods, the compressor will be used automatically:

```python
joblib.dump(to_persist, filename + '.z')  
```

# Pipelines
* [Building and optimizing pipelines in scikit-learn (Tutorial) | Italian Association for Machine Learning (archive.org)
](https://web.archive.org/web/20210507043615/https://iaml.it/blog/optimizing-sklearn-pipelines)
* [How to Improve Machine Learning Code Quality with Scikit-learn Pipeline and ColumnTransformer (freecodecamp.org)](https://www.freecodecamp.org/news/machine-learning-pipeline/)

Function/Method | Description | Imports
--- | ---- | ---
`Pipeline([('step_name': Object)])` | create pipeline with the various steps | from sklearn.pipeline import Pipeline
`.fit(X, y)`
`.transform(X)`
`.predict(X)`
`.score(X, y)`
`.get_params()` | Get the available parameters that can be adjusted in a pipeline.
`.set_params(model_C = 10)` | Set pipeline parameters directly
`.steps[element_index]` | Access specified element of the pipeline
`.steps[element_index][0]` | Access the name of the specified element of the pipeline
`.steps[element_index][1].<attribute>` | Retrieve the attribute of the particular step of the pipeline. <br>e.g. `.steps[1][1].explained_variance_` to access the explained variance of the PCA which is the second pipeline element.
`set_config(display='diagram')`<br>`display(clf_pipeline)` | Display the pipeline with expandable details.

On every object within the pipeline the methods `fit_transform` are invoked during training, while `transform` (or `predict`) are called during test.

##  Common Classes used in Pipelines
Function/Method | Description | Imports
--- | ---- | ---
`FunctionTransformer()` | Constructs a transformer from an arbitrary callable. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html?highlight=functiontransformer#sklearn.preprocessing.FunctionTransformer). | from sklearn.preprocessing import FunctionTransformer
`SimpleImputer()` | Univariate imputer for completing missing values with simple strategies. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html?highlight=simpleimputer#sklearn.impute.SimpleImputer). | from sklearn.impute import SimpleImputer
`OneHotEncoder(drop=None)` | Encode categorical features as a one-hot numeric array. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html?highlight=onehotencoder#sklearn.preprocessing.OneHotEncoder). | from sklearn.preprocessing import OneHotEncoder 
`ColumnTransformer()` | Applies transformers to columns of an array or pandas DataFrame. | from sklearn.compose import ColumnTransformer
`FeatureUnion()` | Concatenates results of multiple transformer objects. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html?highlight=featureunion#sklearn.pipeline.FeatureUnion). | from sklearn.pipeline import FeatureUnion


## Pipelines with Grid Search
[Resource: How to Improve Machine Learning Code Quality with Scikit-learn Pipeline and ColumnTransformer (freecodecamp.org)](https://www.freecodecamp.org/news/machine-learning-pipeline/)

**Specify data preparation steps to compare with grid search:**

[Method 1: If only comparing 2 variations, perform the search with only one option of a given step and skip the other.](https://www.freecodecamp.org/news/machine-learning-pipeline/)
```python
grid_step_params = [
    {pipeline_step1: ['passthrough']},
    {pipeline_step2: ['passthrough']}
    ]
# Then merge each of these dictionaries with the parameter grid for the remaining hyperparameters
```
[Method 2: Use a list of parameter dictionaries where each element contains all the parameters for each grid search](https://web.archive.org/web/20210507043615/https://iaml.it/blog/optimizing-sklearn-pipelines). e.g.:
```python
params = [
        {'scaler': scalers_to_test,
         'reduce_dim': [PCA()],
         'reduce_dim__n_components': n_features_to_test,\
         'regressor__alpha': alpha_to_test},

        {'scaler': scalers_to_test,
         'reduce_dim': [SelectKBest(f_regression)],
         'reduce_dim__k': n_features_to_test,\
         'regressor__alpha': alpha_to_test}
        ]
```

**Merge dictionaries for use in grid search parameter grid**

Double asterisk will unpack each dictionary. 
* If both the dictionary has the same key with different values, then the final output will contain the value of the second dictionary
```python
merge_dict = {**dict_1,**dict_2} 
```

<img src="https://miro.medium.com/max/1400/1*ZT7S2SuhMd4Zazb2lVWmcw.png" width="300">

<details>
<summary>Pipeline Steps without Grid Search</summary>

1. Import and Encode the Data
 * See link for all the steps of loading the data the initial data processing.
2. Define Sets of Columns to be Transformed in Different Ways

```python
num_cols = ['city_development_index','relevent_experience', 'experience','last_new_job', 'training_hours']

cat_cols = ['gender', 'enrolled_university', 'education_level', 'major_discipline', 'company_size', 'company_type']
```
3. Create Pipelines for Numerical and Categorical Features
```python
num_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('scale',MinMaxScaler())
])
cat_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('one-hot',OneHotEncoder(handle_unknown='ignore', sparse=False))
])
```
4. Create ColumnTransformer to Apply the Pipeline for Each Column Set
```python
col_trans = ColumnTransformer(transformers=[
    ('num_pipeline',num_pipeline,num_cols),
    ('cat_pipeline',cat_pipeline,cat_cols)
    ],
    remainder='drop', # remainder=’drop’ is specified to ignore other columns in a dataframe
    n_jobs=-1)
```
5. Add a Model to the Final Pipeline
```python
clf = LogisticRegression(random_state=0)
clf_pipeline = Pipeline(steps=[
    ('col_trans', col_trans),
    ('model', clf)
])
```
6. Display the Pipeline
```python
from sklearn import set_config

set_config(display='diagram')
display(clf_pipeline)
```
7. Split the Data into Train and Test Sets
8. Pass data through the pipeline.

</details>

<br><br>

### How to Find the Best Hyperparameters and Data Preparation Method
<br>
With the pipeline, we can create data transformation steps in the pipeline and perform a grid search to find the best step. A grid search will select which step to skip and compare the result of each case.

* I want to know which scaling method will work best for my data between MinMaxScaler and StandardScaler. I add a step StandardScaler in the num_pipeline. The rest doesn't change.
 
In grid search parameters, specify the steps you want to skip and set their value to passthrough using a list of dictionaries for the grid search parameters: `[{case 1},{case 2}]`
* If using a list of dictionaries, grid search will perform a combination of every parameter in case 1 until complete. Then, it will perform a combination of every parameter in case 2. 
    * So in this example there is no case where MinMaxScaler and StandardScaler are used together.

```python
num_pipeline2 = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('minmax_scale', MinMaxScaler()),
    ('std_scale', StandardScaler()),
])

col_trans2 = ColumnTransformer(transformers=[
    ('num_pipeline',num_pipeline2,num_cols),
    ('cat_pipeline',cat_pipeline,cat_cols)
    ],
    remainder='drop',
    n_jobs=-1)

clf = LogisticRegression(random_state=0)

clf_pipeline2 = Pipeline(steps=[
    ('col_trans', col_trans2),
    ('model', clf)
])

grid_step_params = [{'col_trans__num_pipeline__minmax_scale': ['passthrough']}, 
                    {'col_trans__num_pipeline__std_scale': ['passthrough']}]
# Pipeline will skip minmax_scale step in the first element of the list, and skip std_scale in the second element of the list.

# Perform Grid Search and print the results 
gs2 = GridSearchCV(clf_pipeline2, grid_step_params, scoring='accuracy')
gs2.fit(X_train, y_train)

# The best case is minmax_scale : ‘passthrough’, so StandardScaler is the best scaling method for this data.
```
You can find the best hyperparameter sets and the best data preparation method by adding tuning parameters to the dictionary of each case of the data preparation method.


```python
grid_params = {'model__penalty' : ['none', 'l2'],
               'model__C' : np.logspace(-4, 4, 20)}

# merge dictionaries using the syntax `merge_dict = {**dict_1,**dict_2}`     
grid_step_params = [{**{'col_trans__num_pipeline__minmax_scale': ['passthrough']}, **grid_params},
        {**{'col_trans__num_pipeline__std_scale': ['passthrough']}, **grid_params}]
# `grid_params` will be added to both case 1 (skip MinMaxScaler) and case 2 (skip StandardScaler).

# Perform Grid Search and print the results (like a normal grid search).
gs3 = GridSearchCV(clf_pipeline2, grid_step_params2, scoring='accuracy')
gs3.fit(X_train, y_train)

print("Best Score of train set: "+str(gs3.best_score_))
print("Best parameter set: "+str(gs3.best_params_))
print("Test Score: "+str(gs3.score(X_test,y_test)))
```
<br><br>

### Find the Best Machine Learning Model with Grid Search
Here are the steps we'll follow:
1. Create a class that receives a model as an input
2. Add the class to a pipeline
3. Perform grid search

Step 1: Create a class that receives a model as an input
```python
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

class ClfSwitcher(BaseEstimator):
# Create a class named ClfSwitcher which inherits the base class called BaseEstimator from sklearn.
    def __init__(self, estimator = LogisticRegression()):
            self.estimator = estimator # receives an estimator (model) as an input
            
    def fit(self, X, y=None, **kwargs):
            self.estimator.fit(X, y)
            return self
            
    def predict(self, X, y=None):
            return self.estimator.predict(X)
            
    def predict_proba(self, X):
            return self.estimator.predict_proba(X)
            
    def score(self, X, y):
            return self.estimator.score(X, y)
```
Step 2: Add the class in step 1 to a pipeline
```python
clf_pipeline = Pipeline(steps=[
    ('Encode', Encode()),
    ('col_trans', col_trans),
    ('model', ClfSwitcher())
])
```
Step 3: Perform Grid search
```python
# Use grid search to select between logistic regression and support vector machine.
grid_params = [
    {'model__estimator': [LogisticRegression()]},
    {'model__estimator': [SVC(gamma='auto')]}
]

gs = GridSearchCV(clf_pipeline, grid_params, scoring='accuracy')
gs.fit(X_train, y_train)

print("Best Score of train set: "+str(gs.best_score_))
print("Best parameter set: "+str(gs.best_params_))
print("Test Score: "+str(gs.score(X_test,y_test)))
```

<br>
<details>
<summary> Combining pipelines material from Lighthouse Labs </summary>

* [Walkthrough: Combining pipelines](https://data.compass.lighthouselabs.ca/activities/634)
* [W07D1 lecture notes](https://colab.research.google.com/drive/1jLT6an3LaptW9xSjeLBF32k-b6H48ycS)

This tutorial focuses on the implementation technique and it doesn't mean that this is the approach that will bring the best modeling results.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion

from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

# Load toy data set
iris = load_iris()
X, y = iris["data"], iris["target"]

# This dataset is way too high-dimensional. Better do PCA:
pca = PCA(n_components=2)

# Maybe some of the original features were good, too?
selection = SelectKBest(k=3)

# Now, we will combine these ouputs with FeatureUnion:
    # Build an transformer from PCA and Univariate selection:
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])

# We will create an object for classification now:
svm = SVC(kernel="linear")

# Let's finalize the pipeline and apply grid search to tune the parameters properly:
# create our pipeline from FeatureUnion 
pipeline = Pipeline([("features", combined_features), ("svm", svm)])

    # set up our parameters grid
param_grid = {"features__pca__n_components": [1, 2, 3],
                  "features__univ_select__k": [1, 2, 3],
                  "svm__C":[0.1, 1, 10]}

# create a Grid Search object
grid_search = GridSearchCV(pipeline, param_grid, verbose=10, refit=True)    

    # fit the model and tune parameters
grid_search.fit(X, y)
```

</details>

## Create lists of column names for each of the numeric and categorical features
```python
cat_feats = df.dtypes[df.dtypes == 'object'].index.tolist()
num_feats = df.dtypes[~df.dtypes.index.isin(cat_feats)].index.tolist()
```
# AWS and cloud computing
* [Compass | Setup AWS Instance for Data Science (lighthouselabs.ca)](https://data.compass.lighthouselabs.ca/activities/621)
* [Getting started with Tmux | Linuxize](https://linuxize.com/post/getting-started-with-tmux/#what-is-tmux)

Initiate a tmux session with `tmux new -s session_name`, or  re-attach to existing one (`tmux attach-session -t 0`)

Initiate jupyter lab
```git
jupyter lab --ip 0.0.0.0 --port 8888 --no-browser
```
Access jupyter notebook on browser: `<public_dns_name>:8888/lab`, e.g. 
```
http://ec2-35-180-186-185.eu-west-3.compute.amazonaws.com:8888/lab
```

# Flask APIs
* [Building a Python Flask application — Tutorial 01 | by Sashini Hettiarachchi | Medium](https://sashini-hettiarachchi.medium.com/building-a-python-flask-application-f051fffa0bfa)
* [Compass | Flask Advanced (lighthouselabs.ca)](https://data.compass.lighthouselabs.ca/activities/643)
* [Examples: My script for creating calculator API](/W07/flask/calculator.py)

Basic steps:
* For deployment int he cloud, `.py` script should be available in the instance:
    * using text editors such as Nano, VI or Jupyter Lab
    * cloned using github (recommended by Simon), or 
    * copied using `scp` command/module
* In `.py` script:
    * Initiate the app and api objects
    * Define the class for each endpoint with the `Resource` library as a parameter.
    * For each class, the only methods are HTTP request methods: get, post, put, ...
    * Assign the endpoint.
    * Create an application run when the file is called directly.
* If running the app on the local machine, use terminal to export the flask app:
    1. `export FLASK_APP=script_filename.py`
    2. `flask run`
* If deploying in the cloud:
    * Connect to the instance.
    * Start a `tmux` session.
* Run the saved script in command line: `python script_filename.py`
* URL for accessing the app:
    * Local: IP address, e.g. `http://127.0.0.1:5000/endpoint`
    * Cloud: `<public_dns_name>:<port_number>/endpoint`

Function/Method | Description
--- | ---
`app = Flask(__name__)` | Create an application
`api = Api(app)` | Create an API from the application
`parser = reqparse.RequestParser()` | Create request parser to parse optional arguments
`.add_argument('name', type=str)` | Create an argument for API requests
`.parse_args().get('name')` | Parse the specified argument 
`jsonify(key=object)` | Make json from the output of the function
`api.add_resource(class_name, '/endpoint_name',)` | Assign the endpoint of the API
`if __name__ == '__main__': app.run(debug=True)`<br><br>>Include the parameters `host="0.0.0.0"` and `port=5555` for deployment into the cloud | Create an application run when the `.py` file is called directly. <br><br>`host=0.0.0.0` indicates that app can be accessed from any IP address. `port=` can be any number >1000 and should be unique for each app.
`requests.post(url = URL, json = json_data)` | Making a get request from a python script (e.g. from jupyter)
```python
# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

# Create an application:
app = Flask(__name__)

# Create an API from the application:
api = Api(app)
```
Now that our API has been created, we need to add an endpoint. We can do that by creating a class with the name Greet (any other name will work as well). This class must inherit properties from the `Resources class` from the `flask_restful` module.

```python
class Greet(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('name', type=str) # the string in the first parameter is a key in the API

        # parse 'name'. If the user doesn't pass the argument name in an API call the value of the variable is NULL. 
        name = parser.parse_args().get('name') # object name is for internal reference

        if name:
            greeting = f'Hello {name}!'
        else:
            greeting = 'Hello person without name!'

        # make json from greeting string 
        return jsonify(greeting=greeting) # this can also be a dictionary; left side of equal sign becomes a key in the returned json 

# assign endpoint: The functionality of the Greet class will be available in the /greet endpoint.
api.add_resource(Greet, '/greet',)
```
If the app script is being run from the local machine:
In terminal, run:
```bash
 $ export FLASK_APP=app.py
 $ flask run
 ```
The app API can be accessed on the local machine at the specified IP address and endpoint, e.g. `http://127.0.0.1:5000/greet`. 

## Deploying machine learning with Flask
[Walkthrough: Deploying ML with Flask](https://data.compass.lighthouselabs.ca/activities/827)

Steps:
* Train the model on local computer
* Pickle the model
* Create `.py` script with:
    * Required python libraries
    * Flask app and API 
    * Any custom functions/classes
    * Command to load the pickled model
    * Class with a `post` method to communicate with the model

Here's an example `.py` file to deploy machine learning
```python
# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

# Custom pipeline step
class RawFeats:
    def __init__(self, feats):
        self.feats = feats

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):
        return X[self.feats]

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)

# Load model
model = pickle.load( open( "model.p", "rb" ) )
app = Flask(__name__)
api = Api(app)

# create an endpoint where we can communicate with our ML model.
class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict_proba(df)
        # we cannot send numpt array as a result
        return res.tolist() 

# assign endpoint
api.add_resource(Scoring, '/scoring')

# create an application run 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
We can see that our API is running on our local machine at http://127.0.0.1:5000/.

To test it, we need to send the information about wine in JSON to the endpoint: http://127.0.0.1:5000/scoring. We can now go back to Jupyter Notebook.

This is the structure of the JSON we need to send (values are from the first row of df in the original notebook where we created the model):
```python
json_data = {'alcohol': 14.23,
 'malic_acid': 1.71,
 'ash': 2.43,
 'alcalinity_of_ash': 15.6,
 'magnesium': 127.0,
 'total_phenols': 2.8,
 'flavanoids': 3.06,
 'nonflavanoid_phenols': 0.28,
 'proanthocyanins': 2.29,
 'color_intensity': 5.64,
 'hue': 1.04,
 'od280/od315_of_diluted_wines': 3.92,
 'proline': 1065.0}

 # Now, we can send our POST request from jupyter notebook:

import requests
URL = "http://127.0.0.1:5000/scoring"
# sending get request and saving the response as response object 
r = requests.post(url = URL, json = json_data) 

# and we can check results with:
print(r.json())
```

# MongoDB
* [Python and MongoDB: Connecting to NoSQL Databases – Real Python](https://realpython.com/introduction-to-mongodb-and-python/#using-mongodb-with-python-and-pymongo)

# Container as Dev Environment 
[Walkthrough](https://data.compass.lighthouselabs.ca/days/w07d3/activities/655)
* [How To Remove Docker Containers, Images, Volumes, and Networks | Linuxize](https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/)

Function/Method | Description
--- | ---
Install image | `docker pull <image_name>`
Test installation of image | `docker run <image_name>`
Run Docker container without saving | `docker run -p <host_port>:<container_port> docker_image_name`<br>`-p` Allows us to access the notebook on the port of our choice. Host port must be unique to each image being run on the local machine. Container port is specified externally.
Run Docker container so it will save | `docker run --rm -p <host_port>:<container_port> -v <host_directory>:<container_directory> docker_image_name`<br><br>`-v <host_directory>:<container_directory>` tells the Docker engine to mount the given host directory to the container directory
See list of all containers | `docker container ls`
See list of images | `docker image ls`

<details>
<summary>Example from Compass (this docker notebook won't save to local machine for some reaons): </summary>


```anaconda
docker pull jupyter/datascience-notebook

docker run  --rm  -p 8888:8888  -v ~/lhl_exercises/docker/:/home/jovyan/work/    jupyter/datascience-notebook

docker run  --rm  -p 8880:8888  -v C:\Users\silvh\OneDrive\lighthouse\dl\notebook:/home/jovyan/work/ -d    jupyter/datascience-notebook

docker run  --rm  -p 8880:8888  -v /work:/home/jovyan/work/ -d    jupyter/datascience-notebook

```
When it asks for a password/token, find it in the container details in Docker Desktop. The `-d` flag in the command prevents the token from being shown in command line.

</details>



For PySpark, use this one, then go to [http://localhost:8888/](http://localhost:8888/)
```
docker run  --rm  -p 8888:8888  -v C:\Users\silvh\OneDrive\lighthouse\dl\notebook:/notebook -d akaronte/jupyter-notebook
```
[akaronte/jupyter-notebook documentation](https://hub.docker.com/r/akaronte/jupyter-notebook).

# Neural networks & deep learning: Keras
* [Walkthrough: First Network](https://data.compass.lighthouselabs.ca/days/w07e/activities/676)
* [W08D1 lecture notebook](https://colab.research.google.com/drive/14Vcpm9_uZwESe3BFEcHp20htDXuo08AC#scrollTo=9EUzoGWQ0pHg)
* [2022-11-07 neural_networks_exercise](/W08/2022-11-07-deep_learning_exercise/neural_networks_exercise.ipynb)
* [W08D1 Lecture slide: Common non-linear activation functions](https://docs.google.com/presentation/d/1plQEKUX6mQeBLYGwEit6Fr6XLZoMdmTO/edit#slide=id.p20)

Layer | Description | Imports
--- | ---- | ---
`Dense()` | [See documentation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense). | from tensorflow.keras.layers import Dense 

Function/Method | Description | Imports
--- | ---- | ---
`model.compile()` | [See documentation](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile). <br>[`loss=` documentation](https://www.tensorflow.org/api_docs/python/tf/keras/losses). <br>[`optimizer=` documentation](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers).
`model.fit()` | [See documentation](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit).
`plt.imshow(array)` | Plot Display data as an image | import matplotlb.pyplot as plt
`model.summary()` | give an overview of the model and the number of parameters available for training
`clear_session()` | Re-starts training from the beginning (forgets previously computed weights) | from keras.backend import clear_session
`test_loss, test_acc = model.evaluate(test_images, test_labels)`

## Neural network
### Example for multi-class classification task
```python
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential        # Helper to build a network from a sequence of layers
from tensorflow.keras.layers import Dense             # Fully-connected layer
from tensorflow.keras.callbacks import EarlyStopping  # To stop training early if val loss stops decreasing
from tensorflow.keras.utils import to_categorical

fashion_mnist = fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# returns 4 numpy arrays: 2 training sets and 2 test sets
# images: 28x28 arrays, pixel values: 0 to 255
# labels: array of integers: 0 to 9 => class of clothings
# Training set: 60,000 images, Testing set: 10,000 images

# class names are not included, need to create them to plot the images  
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

## Example of using a neural network for a classification task
# normalize the data
def normalize(data):
    """
    Normalize the data so all values are between 0 and 1. For images, values can simply be divided by 255 since that's the range of pixel values.
    """
    return (data-np.min(data))/(np.max(data)-np.min(data))

scaled_train = normalize(train_images)
scaled_test = normalize(test_images)

# Build the architecture
model = Sequential()
model.add(Dense(30, activation='relu', input_shape=(28*28,)))
model.add(Dense(30, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# reshape our input into a format that the model can read: all pixels for each image in one row of a 2D array. 
train_images = train_images.reshape((-1, 28 * 28))
train_images = train_images.astype('float32') 
test_images = test_images.reshape((-1, 28 * 28))
test_images = test_images.astype('float32') 

# encode our target as categories:
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

bs = 128
model.fit(train_images, train_labels, epochs=5, batch_size=bs,
    validation_data=(test_images, test_labels), # defining 'validation_data' will also print validation loss alongside training loss
    callbacks=[EarlyStopping(patience=3)], # EarlyStopping with patience will stop training early if val_loss didnt get lower after 3 epochs (prevent over-fitting)
    )
test_loss, test_acc = model.evaluate(test_images, test_labels) 
print('test_acc:', test_acc, 'test_loss', test_loss)

y_pred = model.predict(test_images)
```
## Convoluted neural network
* [Walkthrough](https://data.compass.lighthouselabs.ca/days/w08d2/activities/696)
* [Create your first Image Recognition Classifier using CNN, Keras and Tensorflow backend | by Yash Agarwal | Nybles | Medium](https://medium.com/nybles/create-your-first-image-recognition-classifier-using-cnn-keras-and-tensorflow-backend-6eaab98d14dd)
* [How to Develop a CNN From Scratch for CIFAR-10 Photo Classification (machinelearningmastery.com)](https://machinelearningmastery.com/how-to-develop-a-cnn-from-scratch-for-cifar-10-photo-classification/)

### Example for classifying images as either dog or cat (binary classification) using saved images

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(
    32, # Filters, aka patch
    3, # Kernel_size
    3, # Strides
    input_shape = (64, 64, 3), activation = 'relu'))
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Step 3 - Flattening
classifier.add(Flatten())
# Step 4 - Full connection
classifier.add(Dense(128, activation = 'relu'))
classifier.add(Dense(1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
```
* Convolution preserves the spatial relationship between pixels by learning image features using small squares of input data. `Convolution2D` parameters [see documentation](https://keras.io/api/layers/convolution_layers/convolution2d/):
    * Filters: The dimensionality of the output space. We will end up with a convolved feature matrix of 32x32.
    * Kernel_size: Specifying the height and width of the 2D convolution window. It can be a tuple if we don't want a square.
    * Strides: Specifying the strides of the convolution along with the height and width. It can be a tuple if we want a different height and width.
        * Larger = faster but with less detail
    * Padding (not shown): Pad edges with zeros to preserve edge data
* MaxPooling2D `pool_size`: define a spatial neighborhood (in our case a 2×2 window) and take the largest element from the rectified feature map within that window

To get more data, we just need to make alterations to our existing dataset – minor changes such as flips, translations, or rotations – and our neural network will think these are distinct images anyway. Data augmentation is a way of reducing overfitting of models, where we increase the amount of training data using only the information from our training data.

```python
# Step 4 - Data Augmentation
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('./cat_dog_pics/dataset/training_set',
                    target_size = (64, 64),
                    batch_size = 32,
                    class_mode = 'binary')
# File names of data set already contain the image labels, which is why the labels do not need to be passed as an argument to `.flow_from_directory`
test_set = test_datagen.flow_from_directory('./cat_dog_pics/dataset/test_set',
                    target_size = (64, 64),
                    batch_size = 32,
                    class_mode = 'binary')

# Step 5: Training
history = classifier.fit_generator(training_set,
                         steps_per_epoch = 50,
                         epochs = 10,
                         validation_data = test_set)

```
Evaluate the results:
```python
# Plot the loss throughout the training
from matplotlib import pyplot as plt
# plot history
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()

import numpy as np
from tensorflow.keras.preprocessing import image
# loading an image from the disk
test_image = image.load_img('./cat_dog_pics/dataset/test_set/dogs/dog.4001.jpg', target_size = (64, 64))
# converting the image to a numpy array
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
# print(training_set.class_indices)
# our cut-off
if result[0][0] >= 0.5:
    prediction = 'dog'
else:
    prediction = 'cat'
print(prediction)
```
### Example for multi-class classification of images from data set
* [W08D2 exercise: deep_learning_challenge](./W08/2022-11-07-deep_learning_exercise/deep_learning_challenge.ipynb)
* [Long resource with more steps: How to Develop a CNN From Scratch for CIFAR-10 Photo Classification (machinelearningmastery.com)](https://machinelearningmastery.com/how-to-develop-a-cnn-from-scratch-for-cifar-10-photo-classification/)

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import cifar10
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load data
cifar10 = cifar10
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# Build a simple CNN model
classifier = Sequential()
# feature detector part of the model
classifier.add(Convolution2D(
    32,
    3,
    3,
    input_shape=test_images[0].shape,
    activation='relu'
))
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Flatten and classify
classifier.add(Flatten())
classifier.add(Dense(128,activation = 'relu'))
nclasses = len(np.unique(test_labels)) # number of classes in data set
classifier.add(Dense(nclasses, activation='softmax')) # softmax because there are 10 classes

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
# Use `loss = 'sparse_categorical_crossentropy'` instead of `'categorical_crossentropy'` because labels are vectors, not one-hot encoded

# Data augmentation
train_datagen = ImageDataGenerator(rescale=1./255,
    shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow(train_images,
    train_labels,
    batch_size = 64 
    )
test_set = test_datagen.flow(test_images,
    test_labels,
    batch_size = 64 
    )

# Fit the data
history = classifier.fit_generator(
    training_set, # Training_set already includes training_labels, so no need to pass that as an argument here
    epochs = 5,
    validation_data = test_set
)

# Print evaluation metrics
test_loss, test_acc = classifier.evaluate(test_set)  # test_set already includes training_labels, so no need to pass that as an argument here
print('test_acc:', test_acc, 'test_loss', test_loss) 

# Print a summary of the model layers
classifier.summary()

# Predict for the first 8 images in test set
for i in range(8):
    print('Predicted: ',classifier.predict(test_images[i:i+1])) # Not sure why, but index for predict argument must be a range, not just a single value,  or it won't be the right input shape
    print('True label: ', test_labels[i])
```
# Natural language processing (NLP)
## Data preparation for NLP
* [How to Clean Text for Machine Learning with Python (machinelearningmastery.com)](https://machinelearningmastery.com/clean-text-machine-learning-python/)

Function/Method | Description | Imports
--- | ---- | ---
`sentences = sent_tokenize(text)` | Split text into sentences | from nltk import sent_tokenize
`tokens = word_tokenize(text)` | Split text into words | from nltk.tokenize import word_tokenize
`tokens = [w.lower() for w in tokens]` | Convert to lower case
`table = str.maketrans('', '', string.punctuation)`<br>`stripped = [w.translate(table) for w in words]` | Remove punctuation from within each word | import string
`words = [word for word in tokens if word.isalpha()]` | Remove tokens that are not alphabetic, e.g. standalone punctuation
`text = "".join([char for char in text if char not in string.punctuation])` | Remove all punctuation from text | import string
`stop_words = stopwords.words('english')`<br>`stop_words = set(stopwords.words('english'))` | Load a list of step words, all in lower case with punctuation removed | from nltk.corpus import stopwords
`words = [w for w in words if not w in stop_words]` | filter out stop words
`porter = PorterStemmer()`<br>`porter.stem(word)`<br>e.g. `stemmed = [porter.stem(word) for word in tokens]` | Reduce each word to its 'stem'. This reduces tokens to their lowercase. | from nltk.stem.porter import PorterStemmer
`wnl = WordNetLemmatizer()`<br>`wnl.lemmatize(word)`<br>e.g. `word = wnl.lemmatize(word)` | By default, wordnet assumes everything is a noun. Passing `pos='a'` as a parameter in `.lemmatize()` denotes adjective as the root. [See documentation](https://www.nltk.org/api/nltk.stem.wordnet.html). | from nltk.stem import WordNetLemmatizer

### Get words from text without punctuation
```python
# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

# convert to lower case
tokens = [w.lower() for w in tokens]

# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
```
### Get stem words from text
```python
# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# stemming of words
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
print(stemmed[:100])
```

## Feature Extraction
* [Resource: Preparing the text Data with scikit-learn — Feature Extraction | by Vasista Reddy | Medium](https://medium.com/@vasista/preparing-the-text-data-with-scikit-learn-b31a3df567e)
* [Resource: W08D3 lecture notebook](https://colab.research.google.com/drive/1u5PA0U3itw-WFzj-MW9uR_Mx56hXYbKM#scrollTo=JJb1BpwLGggF)

Function/Method | Description | Imports
--- | ---- | ---
`vectorizer = CountVectorizer()` | tokenize documents and obtain word counts. Default for each token is a word is 2 or more Unicode word characters surrounded by word boundaries. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html). | from sklearn.feature_extraction.text import CountVectorizer 
`vectorizer = TfidfVectorizer()` | obtain the Term Frequency and Inverse Document Frequency. [See documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html?highlight=tfidfvectorizer#sklearn.feature_extraction.text.TfidfVectorizer). | from sklearn.feature_extraction.text import TfidfVectorizer
`vectorizer.fit(docs)`
`vectorizer.transform(docs)`
`vectorizer.fit_transform(docs)`
`vectorizer.vocabulary_`| Obtain a dictionary of words as keys and count of each word as values. The vocabulary (dictionary keys) are sorted alphabetically.
`.get_feature_names_out()` | Returns a list of the words starting with least frequent
`.toarray()` | Transform the output from sparse to dense matrix
`.idf_` | Inverse document frequency vector, only defined if use_idf=True.

### Bag of words
This method returns a list of word counts for each item in docs.
```python
docs = ["SUPERB, I AM IN LOVE IN THIS PHONE", "I hate this phone"]
words = list(set([word for doc in docs for word in doc.lower().split()])) # list of the unique words in docs
# example of nested list comprehension

vectors = []
for doc in docs:
    vectors.append([1 if word in doc.lower().split() else 0 for word in words]) # output for each doc is a list since doc.lower().split() is also a list
print("vectors: ", vectors)
```

### CountVectorizer
This method returns an array with each row representing one item in docs.
```python
from sklearn.feature_extraction.text import CountVectorizer
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(docs)
print('vocabulary: ', vectorizer.vocabulary_)

# Return the vocabular as a dictionary sorted by the word index
dict(sorted(vectorizer.vocabulary_.items()))

# encode document
vector = vectorizer.transform(docs)
# summarize encoded vector
print('shape: ', vector.shape)
print('vectors: ', vector.toarray()) # `.toarray()` is for transforming sparse matrix to dense
```
#### Example with dataframe
```python
from sklearn.feature_extraction.text import CountVectorizer #for BoW
vectorizer = CountVectorizer()

# Convenience function
# This function will apply a vectorizer to a series of text
# Will return a dataframe with the results of the vectorizer.
def create_doc_term_matrix(text,vectorizer):
    doc_term_matrix = vectorizer.fit_transform(text)
    
    # Return the vectors as a dataframe
    return pd.DataFrame(doc_term_matrix.toarray(), columns=vectorizer.get_feature_names_out())

#example
ex_text = pd.Series(["The movie scary", " Tenet is a great movie", "Last movie I saw was in March"])

result = create_doc_term_matrix(ex_text,vectorizer) 
```
### TF-IDF
![idf formula](https://miro.medium.com/max/392/1*q6WuO-BoZFIFR9o8cgajRQ.png)
```python
from sklearn.feature_extraction.text import TfidfVectorizer
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(docs)
# summarize
print('vocabulary: ', vectorizer.vocabulary_)
print('idfs: ', vectorizer.idf_)

# encode document
vector = vectorizer.transform(docs)
# summarize encoded vector
print('vectors: ', vector.toarray())

# To vectorize only the first document:
vectorizer.transform([docs[0]]).toarray() # square brackets around docs[0] to treat entire value as single string
```
### Word2Vec
[Resource: Implementing Word2Vec with Gensim Library in Python (stackabuse.com)](https://stackabuse.com/implementing-word2vec-with-gensim-library-in-python/)

word2vec is a shallow 2 layer neural network that accepts text corpus as input and return word embeddings as output

Function/Method | Description | Imports
--- | ---- | ---
`word2vec = Word2Vec(all_words, min_count=2)` | value of 2 for min_count specifies to include only those words in the Word2Vec model that appear at least twice in the corpus. [See documentation](https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.Word2Vec).| from gensim.models import Word2Vec
`word2vec = Word2Vec(all_words, vector_size = 100, window = 3, min_count = 2, sg = 1)` | Skip Gram model
`vocabulary = word2vec.wv.vocab` | Obtain the dictionary of unique words
`vector = word2vec.wv['artificial']` | show the vector for a given word
`.wv.most_similar('intelligence')` | see the words most similar to "intelligence"
`.similarity("nice","good")` | Obtain similarity score of any two words


#### Why Word 2 Vec?
1. Preserves Relationship between words
2. Deals with addition of new words in vocabulary
3. Results in better predictions if word2vec processed data used as input to another larger NN

<details>
<summary>Parse and prepare the data: </summary> 

```python
import bs4 as bs
import urllib.request
import re
import nltk

# Scrape the data from Wikipedia
scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scrapped_data.read()

# Parse the article
parsed_article = bs.BeautifulSoup(article,'lxml')
paragraphs = parsed_article.find_all('p') # parsed_article has p html/xml tags

# we join all the paragraphs together
article_text = ""
for p in paragraphs:
    article_text += p.text

# Preprocessing
# Cleaing the text
processed_article = article_text.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article ) # replace non alpha characters with space

 # replace multiple white spaces with single space
processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
from nltk.corpus import stopwords
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]
    # all_words contains the list of all the words in the article.
```
</details>
<br>

Create the model:
```python
from gensim.models import Word2Vec

word2vec = Word2Vec(all_words, min_count=2)

# Obtain the dictionary of unique words that exist at least twice in the corpus
vocabulary = word2vec.wv.key_to_index
# By default, a hundred dimensional vector is created by Gensim Word2Vec. 
```
Explore the model:
```python
# show the vector for a given word:
v1 = word2vec.wv['artificial']

# see the words most similar to "intelligence"
sim_words = word2vec.wv.most_similar('intelligence')
```

#### Example with Skip Gram Model
* [Resource: W08D3 lecture notebook](https://colab.research.google.com/drive/1u5PA0U3itw-WFzj-MW9uR_Mx56hXYbKM#scrollTo=JJb1BpwLGggF)
```python
# Create Skip Gram model (notice sg parameter)
Model_SG = gensim.models.Word2Vec(messages['text_tokenized'], vector_size = 100, window = 3, min_count = 2, sg = 1)
  
#Vector represenation of the word 'king'
Model_SG.wv['king']
```
#### Pre-trained word2vec models
There are also pre-trained word2vec models. For example, word2vec-google-news-300 is trained on a Google News dataset consisting of about 100 billion words. The model consists of 300-dimensional vectors for 3 million words and phrases.
```python
import gensim.downloader as api

google_news_300['king']
google_news_300 = api.load('word2vec-google-news-300')
google_news_300.most_similar('now')
```

## Recurrent Neural Network (RNN) for Character Level Language Model
* [walkthrough: RNN](https://data.compass.lighthouselabs.ca/days/w08d3/activities/717)
* [See 2022-11-09 notepad](./W08/2022-11-09%20notepad%20NLP.ipynb)

*Overview:*
* Choose a language model that will best represent the input text.
* Clean and prepare the data for training.
* Build a basic Keras sequential neural network model.
* Apply recurrent neural network (RNN) to process character sequences.
* Generate 3 channel RGB color outputs.

There are some reasons you might choose to use the character-level language model over the more popular word-level model:
* Your text datasets contain a noticeable amount of out-of-vocabulary words or infrequent words.
* The majority of the text strings are short, bounded-length strings. Usually, the character-level language generation model can create text with more variety since its imagination is not constrained by a pre-defined dictionary of vocabulary.

You may also be aware of the limitation that came with adopting character-level language:
* Long sequences may not capture long-range dependencies as well as word-level language models. 
* Character-level models are also more computationally expensive to train.

### Data preparation of text data
```python
import tensorflow as tf
from tensorflow.python import keras
from tensorflow.keras import preprocessing
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM, Reshape

import numpy as np
import pandas as pd

data = pd.read_csv("./colors.csv")
names = data["name"]

maxlen = 25 # We’re limiting our color names to 25 characters in length
t = Tokenizer(char_level=True)
t.fit_on_texts(names)
tokenized = t.texts_to_sequences(names)
padded_names = preprocessing.sequence.pad_sequences(tokenized, maxlen=maxlen)
# padded_names will have the shape of (18606, 25), with 18,606 is the number of total training samples and 25 being the max sequence length. If a string has less than 25 characters, it will be padded with the value 0 from the beginning of the sequence.

print(t.word_index) # view the character to integer mapping starting from most frequent

# One-hot encode because  the integer values have no natural ordered relationship between each other and our model may not be able to harness any benefit from it
from tensorflow.python.keras.utils import np_utils
one_hot_names = np_utils.to_categorical(padded_names)
```
Data normalization is purely practical because in practice it could take a model forever to converge if the training data values are spread out too much. A common normalization technique is to scale values to [-1, 1]. In our model, we’re using a ReLu activation function in the last layer. Since ReLu outputs non-negative numbers, we’ll normalize the values to [0, 1].

```python
# The RGB values are between 0 - 255
# scale them to be between 0 - 1
def norm(value):
    return value / 255.0

normalized_values = np.column_stack([norm(data["red"]), norm(data["green"]), norm(data["blue"])])
```
### Building the model
To build our model we’re going to use two types of neural networks: a feed-forward neural network and a recurrent neural network. 
* The feed-forward neural network is by far the most common type of neural network. In this neural network, the information comes into the input units and flows in one direction through hidden layers until each reaches the output units.
* In recurrent neural networks, information can flow around in cycles. These networks can remember information for a long time. Recurrent networks are a very natural way to model sequential data. 
    * In our specific model, we’re using one of the most powerful recurrent networks named long short term memory (LSTM).

The easiest way to build a deep learning model in Keras is to use its sequential API, and we simply connect each of the neural network layers by calling its model.add() function like connecting LEGO bricks.
```python
# Build the model
model = Sequential()
model.add(LSTM(256, return_sequences=True, input_shape=(maxlen, 90)))
model.add(LSTM(128))
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='sigmoid'))

# specify the optimizer and the loss function.
model.compile(optimizer='adam', loss='mse', metrics=['acc'])

# train the model
history = model.fit(one_hot_names, normalized_values,
                    epochs=40,
                    batch_size=32,
                    validation_split=0.2)
```
<img src="https://i.imgur.com/Us8f5K3.png" width="300"> FC: fully connected layer

### Predict
For a color name input, we need to transform it into the same one-hot representation. To achieve this, we tokenize characters to integers with the same tokenizer with which we processed the training data, pad it to the max sequence length of 25, then apply the one-hot encoding to the integer sequence.

And for the output RGB values, we need to scale it back to 0–255, so we can display them correctly.
```python
# plot a color image
def plot_rgb(rgb):
    data = [[rgb]] # Keep the letters of the string input together instead of as separate list items
    plt.figure(figsize=(2,2))
    plt.imshow(data, interpolation='nearest')
    plt.show()

def scale(n):
    return int(n * 255) 

def predict(name):
    name = name.lower()
    tokenized = t.texts_to_sequences([name])
    padded = preprocessing.sequence.pad_sequences(tokenized, maxlen=maxlen)
    one_hot = np_utils.to_categorical(padded, num_classes=90)
    pred = model.predict(np.array(one_hot))[0]
    r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
    print(name + ',', 'R,G,B:', r,g,b)
    plot_rgb(pred)

# predict
predict("forest")
predict("ocean")
```
## Sentiment analysis
1. Obtain data
2. Preprocessing
    * Vectorization
3. Numeric representation
4. Model Output

### Word embeddings
[Resource: Practical Text Classification With Python and Keras – Real Python](https://realpython.com/python-keras-text-classification/)


Their aim is to map semantic meaning into a geometric space. This geometric space is then called the embedding space.


Function/Method | Description | Imports
--- | ---- | ---
`tokenizer = Tokenizer(num_words=5000)` |  vectorize a text corpus into a list of integers where integer maps to a value in a dictionary that encodes the entire corpus, with the keys in the dictionary being the vocabulary terms themselves.<br>The indexing is ordered after the most common words in the text, which you can see by the word the having the index 1. [See documentation](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer). | from keras.preprocessing.text import Tokenizer
`tokenizer.fit_on_texts(sentences_train)` 
`vector = tokenizer.texts_to_sequences(sentences_train)` | 
`tokenizer.word_index[word]` | Get the index for a particular word in the vocabular dictionary of the `Tokenizer` object. Index 0 is reserved and is not assigned to any word. 
`pad_sequences(X_train, padding='post', maxlen=maxlen)` | Pads the sequence of words with zeros. By default, it prepends zeros | from keras.preprocessing.sequence import pad_sequences
`.word_index` | Access the vocabular dictionary of the `Tokenizer` object. [See documentation](https://faroit.com/keras-docs/1.2.2/preprocessing/text/).
`.word_counts` | dictionary mapping words (str) to the number of times they appeared on during fit. Only set after fit_on_texts was called. 


#### Example uses product/service review data from Yelp, Amazon, imdb.

Create vector representations 

```python
from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(sentences_train)

# Obtain Tokenizer vectors for the documents
X_train = tokenizer.texts_to_sequences(sentences_train)
X_test = tokenizer.texts_to_sequences(sentences_test)

vocab_size = len(tokenizer.word_index) + 1  # Adding 1 because of reserved 0 index

# Pad vectors with zeros to make them all equal size
from keras_preprocessing.sequence import pad_sequences
maxlen = 100
X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)
```
Create the word embeddings in a neural network
```python
from keras.models import Sequential
from keras import layers

# Set the number of dimensions in the embeddings
embedding_dim = 50

model = Sequential()
model.add(layers.Embedding(input_dim=vocab_size, 
                           output_dim=embedding_dim, 
                           input_length=maxlen))
```
Add a pooling layer, which will:
* Reduce the number of dimensions.
* look at local and sequential information instead of absolute positional information
```python
# take the maximum value of all features in the pool for each feature dimension, 
    # SH 2022-11-11 10:41 i.e. for each dimension, which word has the largest value?
model.add(layers.GlobalMaxPool1D())
```
Pass the output to a `Dense` layer.
* If no pooling layer is used, the `Embedding` layer can be passed into a `Flatten` layer to prepare the input for the `Dense` layer (replace `GlobalMaxPool1D()` layer with `model.add(layers.Flatten())`).

```python
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train,
                    epochs=20,
                    validation_data=(X_test, y_test),
                    batch_size=10)

model.summary()
# You can now see that we have 87350 new parameters to train. This number comes from vocab_size times the embedding_dim.
```
Additional examples:
* [Using Pretrained Word Embeddings by GloVe](https://realpython.com/python-keras-text-classification/#using-pretrained-word-embeddings)
* [Using grid search with `KerasClassifier`](https://realpython.com/python-keras-text-classification/#hyperparameters-optimization)

## Topic modelling
[Resource: NLP-A Complete Guide for Topic Modeling- Latent Dirichlet Allocation (LDA) using Gensim! | LinkedIn](https://www.linkedin.com/pulse/nlp-a-complete-guide-topic-modeling-latent-dirichlet-sahil-m/)

<img src = "https://media-exp1.licdn.com/dms/image/C4D12AQHpMb56sRa0Ng/article-inline_image-shrink_1000_1488/0/1608580261257?e=1673481600&v=beta&t=iZJL4Jz0IaZKRL0uKWGjSfFPEZbS2rScTui0P4jf1Vg" width = "500">
<img src = "https://media-exp1.licdn.com/dms/image/C4D12AQGXN-_UNe7a_Q/article-inline_image-shrink_1000_1488/0/1608580495063?e=1673481600&v=beta&t=UyJ5c7rIWgyuiPVvEzzoHh0uLDZR-UjyGCU220C0_RE" width = "400">








* K: Number of topics
* N: Number of words in the document
* M: Number of documents to analyze
* α : Per-document topic distribution
    * High α means every document is likely to contain a mixture of most of the topics and not just any single topic specifically.
    * Low α means A document is more likely to be represented by just few of the topic.
* β : Per topic word distribution
    * High β means each topic is likely to contain a mixture of most of the words not just any word specifically.
    * Low β means topic may contain a mixture of just a few of words.
* φ(k): Word distribution for topic k (Topic probability per word)
* ϴ(i): Topic distribution for for document I (Topic probability per document)
* Z(i,j): Topic assignment for w(i,j)
* w(i,j): j-th word in i-th document
<br><br>

### Example using `gensim`: Getting the topics for news stories
* Prepare the data, i.e. remove emails, lemmatize, etc.
* In the code below, `data_lemmatized` is a list where each element is a list containing a document's bag of words.
```python
import re
import nltk
import spacy
import gensim
import pandas as pd
import numpy as np
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from pyLDAvis import * # Not sure why `import pyLDAvis[...]` gives ModuleNotFoundError
from pyLDAvis.sklearn import *
from pyLDAvis.gensim_models import *

# Create dictionary
id2word = corpora.Dictionary(data_lemmatized)
print(id2word)

# Create corpus
texts = data_lemmatized
corpus = [id2word.doc2bow(text) for text in texts] 
# `corpus` is a list (one element per document) of tuples where first value is the index of the word and second value is the number of times the word is in the document

# Create the LDA model
    # final LDA model after hyperparameter adjustment
lda_model_final = gensim.models.ldamodel.LdaModel(
    corpus=corpus,
    id2word=id2word,
    num_topics=5,
    random_state=100,
    chunksize=200,
    passes=10,
    alpha = 0.01,
    eta='symmetric',
    per_word_topics=True
)
```
The model can be queried by passing in document(s) in the same format as the corpus (output of `.doc2bow()` method). This returns a tuple where each element is a list:
* First list contains tuples of topic # and topic distribution in the document.
* Second list contains tuples of word # and the topic(s) it belongs to.
* Third list contains tuples of the word # and its distribution within the topics.
<br><br>

#### Obtain the model coherence score

Topic coherence measures the average similarity between top words having the highest weights in a topic i.e relative distance between the top words
```python
coherence_model_lda = CoherenceModel(model=lda_model_final, texts = data_lemmatized,
    dictionary= id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('Coherence score: ', coherence_lda)
```

#### Visualize the topic-keywords
```python
enable_notebook() # May need to run `pyLDAvis.enable_notebook()` depending on the import command used
LDAvis_prepared = prepare(lda_model_final, corpus, id2word) # May need to run `pyLDAvis.gensim.prepare()`
LDAvis_prepared
```
Here's a function to list the topic keywords and put them into a dataframe along with the dominant topic and its percentage distribution.

```python
# Define the function
def format_topics_sentences(ldamodel=None, corpus=corpus, texts=data):
    # Init output
    sent_topics_df = pd.DataFrame()

    # get main topic in each document
        # Iterate over each document
            # i represents the index of each document
    for i, row_list in enumerate(ldamodel[corpus]): # corpus is a list where each element a list of tuples representing a document
        
        row=row_list[0] if ldamodel.per_word_topics else row_list 
            # if ldamodel.per_word_topics: The `per_word_topics` boolean parameter was set when `LdaModel` was instantiated
            # per_word_topics: list of topics, sorted in descending order of most likely topics for each word, along with their phi values multiplied by the feature length (i.e. word count).
            # row_list[0] is a list of tuples for each topic in the document:
                # first number is an integer representing the topic
                # second number is the topic distribution in that document. The sum of these values in the document will be approximately 1 (may be a bit lower)

        # Sort by the largest topic distribution
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # print(row)

        # Get the dominant topic, perc contributions and keywords for each document
            # Iterate over each topic in the document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j==0: # Dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ', '.join([word for word, prop in wp]) # keywords for that topic
                # print(topic_keywords)
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num),
                    round(prop_topic, 4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominamnt_Topic', 'Perc_Contribution', 'Topic_Keywords']
    # add original text to the end of the output
    contents = pd.Series(texts, name='Text')
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return sent_topics_df

# Run the function
row1 = 0
row_n = 10
df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model_final, corpus=corpus[row1:row_n], texts=data[row1:row_n])
```
See #12 in the resource for creating a word cloud of top words in each topic. 

### Example using `sklearn`
[See W08D4 notebook](https://colab.research.google.com/drive/19lU9Xz2rhTCZmdzDo2BKWEkbhOomxPgq#scrollTo=DX3KEemJg5J6)

#### "Normalizing" the text

spaCy is a powerful library and it can do many other things, but we'll be using it for preprocessing. With this library, you can run the NLP pipeline by simply calling the function `nlp`. You can then access information about each token in a for loop.
```python
import re #regular expression
import spacy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

# !python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

def normalize_text(documents, 
                   min_token_len=2, 
                   irrelevant_pos=['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE']):
    """
    Given text, min_token_len, and irrelevant_pos carry out preprocessing of the text 
    and return a preprocessed string. 
    
    Keyword arguments:
    documents -- (np.array[str]) the list of documents to be preprocessed
    min_token_len -- (int) min_token_length required
    irrelevant_pos -- (list) a list of irrelevant pos tags
    
    Returns: np.array[str] the normalized documents
    """
    normalized_documents = []
    
    for text in documents:
        # Remove Emails
        text = re.sub(r'\S*@\S*\s?', '', text)

        # Remove extra space characters
        text = re.sub(r'\s+', ' ', text)

        # Remove distracting characters
        text = re.sub(r'''[\*\~]+''', "", text)

        doc = nlp(text) #covert text into spacy object
        clean_text = []

        for token in doc:
            if (token.is_stop == False # Check if it's not a stopword
                and token.is_alpha # Check if it's an alphanumerics char
                and len(token) > min_token_len # Check if the word meets minimum threshold
                and token.pos_ not in irrelevant_pos): # Check if the POS is in the acceptable POS tags
                lemma = token.lemma_ # Take the lemma of the word
                clean_text.append(lemma)
                
        clean_text = ' '.join(clean_text) #merge list of tokens back into string
        normalized_documents.append(clean_text) #append to list of normalized documents
        
    normalized_documents = np.array(normalized_documents) #convert list of normalized documents into numpy array
    return normalized_documents

#
# Create a Transformer from the function so that we can use it in a Pipeline
normalizer = FunctionTransformer(normalize_text)

# Vectorize the text
n_features = 5000

    #keep 5000 most common tokens that appear in atleast 2 documents, less than 95% of documents
    #notice binary=False by default
vectorizer = CountVectorizer(min_df=2, max_df=0.95, max_features=n_features)

# Create a preprocesssing pipeline
preprocessor = Pipeline([('normalizer', normalizer), 
                         ('vectorizer', vectorizer)])
```
#### Modelling
```python
from sklearn.decomposition import LatentDirichletAllocation
from sklearn import set_config

set_config(display='diagram')

n_topics = 10

#alpha = doc_topic_prior = 1 / n_components (every topic is equally likely in a document)
#eta = topic_word_prior = 1 / n_components (every word is equally likely in a topic)
lda = LatentDirichletAllocation(n_components=n_topics, 
                                max_iter=5,
                                learning_method='online',
                                random_state=27)

pipeline = Pipeline([('preprocessor', preprocessor), 
                     ('model', lda)])
pipeline.fit(X)

# Let's what the predictions look like for a datapoint.
# As discussed, we should get a probability distribution over n_topics
pipeline.transform(X[0:1])[0]
```
#### Explore topics
 To find out which are the most important words per topic, we can look at the `lda.components_` attribute, which is a float matrix of shape `(n_topics, n_words)` signifying each word's importance to a given topic.

```python
from matplotlib import pyplot as plt
def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, round((n_topics+.5)/2), figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic_components in enumerate(model.components_): # components_[i, j] can be viewed as pseudocount that represents the number of times word j was assigned to topic i
        top_features_ind = topic_components.argsort()[:-n_top_words - 1:-1] # Get the top n_top_words, then put then in reverse order
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic_components[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f'Topic {topic_idx +1}',
                     fontdict={'fontsize': 30})
        ax.invert_yaxis()
        ax.tick_params(axis='both', which='major', labelsize=20)
        for i in 'top right left'.split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)
    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    
plot_top_words(lda, vectorizer.get_feature_names_out(), 10, 'Topics in LDA model')
```
We can also do this visualization with the convenient `pyLDAvis package`, which will also show us a low-dimensional representation of the topics so that we can see their relative similarities.
```python
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()

data_vectorized = preprocessor.transform(X)
vis = pyLDAvis.sklearn.prepare(lda, data_vectorized, vectorizer, mds='tsne')
vis
```

# Time series
* [Working with Time Series | Python Data Science Handbook (jakevdp.github.io)](https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html)

## Numpy `datetime`
[See Numpy datetime documentation](https://numpy.org/doc/stable/reference/arrays.datetime.html)

 The `datetime64` dtype encodes dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly
```python
import numpy as np
date = np.array('2015-07-04', dtype=np.datetime64)

# NumPy will infer the desired unit from the input; for example, here is a day-based datetime
np.datetime64('2015-07-04')

# Minute-based datetime
np.datetime64('2015-07-04 12:00')

# You can force any desired fundamental unit using one of many format codes; for example, here we'll force a nanosecond-based time:
np.datetime64('2015-07-04 12:59:59.50', 'ns')
```
## Pandsas `Timestamp`
data type | Index structure | Notes
--- | ----  | ---- 
Timestamp | DatetimeIndex
Period | PeriodIndex
Timedelta | TimedeltaIndex | A TimedeltaIndex is created when a date is subtracted from another


Function/Method | Description
--- | ---
`pd.to_datetime()` | Passing a snigle date yields a `Timestamp`; passing a series of dates by default yields a `DatetimeIndex`
`.to_period('frequency_code')` |  Convert `DatetimeIndex` to a `PeriodIndex`
`pd.date_range('2015-07-03', '2015-07-10')` |  create a regular sequence of dates using 2 time stamps. Default frequency is 1 day.
`pd.date_range('2015-07-03', periods=8, freq='D')` | Create a date range with a startpoint and a number of periods
`pd.period_range()`
`pd.timedelta_range()`

Frequencies and Offsets
Code | Description | Code | Description | Modifications
--- | --- | --- | --- | ---
`B` | Business day
`BH` | Business hours
`BM` | Business month end | `BMS` | Business month start 
`BQ` | Business quarter end | `QS` | Quarter start| you can change the month used to mark any quarterly or annual code by adding a three-letter month code as a suffix. `Q-JAN`, `BQ-FEB`, `QS-MAR`, `BQS-APR`, etc.
`BA` | Business year end | `BAS` | Business year start
`D` | Calendar day
`H` | Hours
`U` | Microseconds
`L` | Milliseonds
`T` | Minutes
`M` | Month end | `MS` | Month start
`N` | nanoseconds
`Q` | Quarter end
`S` | Seconds
`W` | Weekly | | | the split-point of the weekly frequency can be modified by adding a three-letter weekday code: `W-SUN`, `W-MON`, `W-TUE`, `W-WED`, etc.
`A` | Year end | `AS` | Year start

```python
import pandas as pd
date = pd.to_datetime("4th of July, 2015")
```
Where the Pandas time series tools really become useful is when you begin to index data by timestamps. For example, we can construct a Series object that has time indexed data:
```python
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04', '2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)

# Output:
# 2014-07-04    0
# 2014-08-04    1
# 2015-07-04    2
# 2015-08-04    3
# dtype: int64
```

codes can be combined with numbers to specify other frequencies. For example, for a frequency of 2 hours 30 minutes, we can combine the hour (`H`) and minute (`T`) codes as follows:
```python
pd.timedelta_range(0, periods=9, freq="2H30T")
```
we can create a business day offset directly as follows:
```python
from pandas.tseries.offsets import BDay
pd.date_range('2015-07-01', periods=5, freq=BDay())

# output:
# DatetimeIndex(['2015-07-01', '2015-07-02', '2015-07-03', '2015-07-06',
#                '2015-07-07'],
#               dtype='datetime64[ns]', freq='B')
```
## Resampling, Shifting, and Windowing
Function/Method | Description | Imports
--- | ---- | ---
`.resample()` | data aggregation of time series. e.g. `.resample('BA').mean()`, `.resample('D').sum()`
`.asfreq()` | data selection of time series
`.shift` | shifts the data in multiples of the frequency
`.tshift` | shifts the index in multiples of the frequency
`.rolling()` | Perform aggregation operations on a time series. e.g. `rolling.mean()`, `rolling.std()`, `.rolling().sum((`. <br>The `aggregate()` and `apply()` methods can be used for custom rolling computations. <br>Pass the window function parameter `win_type=` to smooth the data when plotting., e.g. `win_type='gaussian'`
`data.groupby(data.index.time).mean()` | Look at data as a function of a certain time feature, e.g. time of day

#### Downsampling
```python
from pandas_datareader import data
goog = data.DataReader('GOOG', start='2004', end='2016', data_source='yahoo')

# Select a single column of the dataframe
goog = goog['Close']

# Plot the data
goog.plot();

# Plot the original data and downsampled data 
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'],
           loc='upper left');
```
#### Upsampling
```python
fig, ax = plt.subplots(2, sharex=True)
data = goog.iloc[:10]

# Data with NA values due to upsampling
data.asfreq('D').plot(ax=ax[0], marker='o')

# Data with different impute methods
data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(["back-fill", "forward-fill"]);
```
#### Rolling windows
```python
import seaborn; seaborn.set()

# Plot the raw data
data.plot()
plt.ylabel('Hourly Bicycle Count');

# Plot a rolling mean to make the data easier to visualize
daily = data.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
plt.ylabel('mean hourly count');
```
We can get a smoother version of a rolling mean using a window function–for example, a Gaussian window. The following code specifies both the width of the window (we chose 50 days) and the width of the Gaussian within the window (we chose 10 days):
```python
daily.rolling(50, center=True,
              win_type='gaussian').sum(std=10).plot(style=[':', '--', '-']);
```
#### Aggregating the data
Example: To look at the average traffic as a function of the time of day, we can use the GroupBy functionality:
```python
by_time = data.groupby(data.index.time).mean()
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-']);
```
### Stationarity

Function/Method | Description | Imports
--- | ---- | ---
`adfuller(X)` | Perform the Augmented Dickey-Fuller test to test for stationarity for a time series. Null hypothesis is that data are non-stationary. Result is a dictionary: Key 0 is statistic, Key 1 is the p-value. [See documentation](https://www.statsmodels.org/dev/generated/statsmodels.tsa.stattools.adfuller.html). | from statsmodels.tsa.stattools import adfuller
`result = seasonal_decompose(series, model=model)`<br><br>`result.plot()` | Decompose a time series, then plot the trend, seasonality, and residual. Using `model=additive` or `model=multiplicative`. If not a pandas object, specify `period=` | from statsmodels.tsa.seasonal import seasonal_decompose

## Autoregressive Integrated Moving Average Model (ARIMA (p, d, q))
* [How to Create an ARIMA Model for Time Series Forecasting in Python (machinelearningmastery.com)](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)
* [For additional functions/methods: Quick way to find p, d and q values for ARIMA (analyticsindiamag.com)](https://analyticsindiamag.com/quick-way-to-find-p-d-and-q-values-for-arima/)

Hyperparameters
* p: The number of lag observations included in the model, also called the lag order.
* d: The number of times that the raw observations are differenced, also called the degree of differencing.
* q: The size of the moving average window, also called the order of moving average.

Two diagnostic plots can be used to help choose the p and q parameters of the ARMA or ARIMA:
* Autocorrelation Function (ACF). 
* Partial Autocorrelation Function (PACF).

Choosing the model
Model | Description | When to thoose this
--- | ---- | ---
Autoregressive model: AR | Uses observations from previous time points as input to a regression model to predict the value at the current time point. | ACF trails off after a lag and has a hard cut-off in the PACF after a lag. This lag is taken as the value for p.
Moving-average model: MA(q) | Uses the mean and current/previous errors to predict the value at the next time step. | PACF trails off after a lag and has a hard cut-off in the ACF after the lag. This lag value is taken as the value for q.
Autoregressive Moving-average model: ARMA(p,q) | Contains both the AR(p) and MA(q) models. | Both the ACF and PACF trail off.
Autoregressive Integrated Moving Average model: ARIMA(p,d,q) | ARMA but introduces differencing (to remove non-stationarity).

Function/Method | Description | Imports
--- | ---- | ---
`autocorrelation_plot(series)` | plot the autocorrelation for a large number of lags in the time series to help determine the `p` hyperparameter | from pandas.plotting import autocorrelation_plot
`model = ARIMA(series, order=(p, d, q))` | Instantiate the model with the series; specify integers for p, d, q. | from statsmodels.tsa.arima.model import ARIMA
`model_fit = model.fit()` | 
`model_fit.summary()` | Print the summary of the fit model, e.g. coefficients.
`model_fit.resid` | Obtain the residuals of the fit model. This should be looked at to ensure that it is stationary and centred at zero. Otherwise, it means the model is not capturing some trend info or has a bias.
`model_fit.forecast()` | forecast future time steps

### Example
Look at the autocorrelation plot
```python
# Create function to parse the date information from the data
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

# Load the data
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv'
series = pd.read_csv(url, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)

# Convert the dates (*likely optional*)
series.index = series.index.to_period('M')

# Autocorrelation plot
autocorrelation_plot(series)
```
Fit the model, i.e. parameter estimation
```python

from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot

# fit model
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit()
```
Model checking, i.e. look at the residuals
```python
# summary of fit model
print(model_fit.summary())
# line plot of residuals
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
# density plot of residuals
residuals.plot(kind='kde')
pyplot.show()
# summary stats of residuals
print(residuals.describe())
```

Use the model for predictions
```python
# split into train and test sets
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
# walk-forward validation
for t in range(len(test)):
	model = ARIMA(history, order=(5,1,0))
	model_fit = model.fit()
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))

# evaluate forecasts
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot forecasts against actual outcomes
plt.plot(test)
plt.plot(predictions, color='red')
```

## Prophet
* [Resource: Quick Start | Prophet (facebook.github.io)](https://facebook.github.io/prophet/docs/quick_start.html#python-api)

Function/Method | Description | Imports
--- | ---- | ---
`m = Prophet()` | Instantiate model | from prophet import Prophet
`m.fit(df)`
`future = m.make_future_dataframe(periods=365)` | get a suitable dataframe that extends into the future a specified number of days
`forecast = m.predict(future)` | assign each row in future a predicted value which it names `yhat`  with the forecast, as well as columns for components and uncertainty intervals
`m.plot(forecast, include_legend=True)` | plot the forecast by calling the `Prophet.plot` method and passing in your forecast dataframe
`m.plot_components(forecast)` | See the forecast components. By default you’ll see the trend, yearly seasonality, and weekly seasonality of the time series. If you include holidays, you’ll see those here, too.
`plot_plotly(m, forecast)` |  plot the forecast using Plotly | from prophet.plot import plot_plotly, plot_components_plotly
`plot_components_plotly(m, forecast)` | Plot the forecast components using Plotly | 
`.add_seasonality(name="monthly", period=30.5, fourier_order=5)` | A higher fourier order means we have higher frequency terms and so will be able to fit more quickly-changing and complex seasonality patterns. For yearly patterns, choose 10, for weekly, 3.
`fig = [...]`<br>`c = add_changepoints_to_plot(fig.gca(), m, forecast)` | Add changepoints (e.g. events which may affect data)

Parameter | Description | Associated class/method
--- | --- | ---
`interval_width=0.80` | width of the uncertainty intervals (by default 80%) | `Prophet()`
` daily_seasonality=<bool>`

The input to Prophet is always a dataframe with two columns: `ds` (datestamp) and `y`. By default it will also include the dates from the history, so we will see the model fit as well

```python
import pandas as pd
from prophet import Prophet
df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
df.head()

# Fit the model
m = Prophet()
m.fit(df)

# get a suitable dataframe that extends into the future a specified number of days
future = m.make_future_dataframe(periods=365)

# assign each row in future a predicted value which it names yhat.
forecast = m.predict(future)
```

Plot the results
```python

# plot the forecast by calling the Prophet.plot method and passing in your forecast dataframe
fig1 = m.plot(forecast)

# see the forecast components
fig2 = m.plot_components(forecast)

```
Plot the results using Plotly:
```python
from prophet.plot import plot_plotly, plot_components_plotly

plot_plotly(m, forecast)
plot_components_plotly(m, forecast)
```
Real time series frequently have abrupt changes in their trajectories.Prophet tries to detect these changepoints and will allow the trend to adapt appropriately, to see the points that create changes, we can do a changepoints plot.
```python
# Find Point/Dates For Change
from prophet.plot import add_changepoints_to_plot

fig = m.plot(prediction)
c = add_changepoints_to_plot(fig.gca(),m,forecast)
```

## Time series in supervised learning using Pandas `.shift()` method

[How to Convert a Time Series to a Supervised Learning Problem in Python (machinelearningmastery.com)](https://machinelearningmastery.com/convert-time-series-supervised-learning-problem-python/)

Use the `df[column].shift(n)` method to create columns where the data is shifted forward by n.
```python
df = pd.DataFrame()
df['t'] = [x for x in range(10)]
df['t-1'] = df['t'].shift(1)
df['t+1'] = df['t'].shift(-1)
```
Custom function for creating time series features
```python
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	"""
	Frame a time series as a supervised learning dataset.
	Arguments:
		data: Sequence of observations as a list or NumPy array.
		n_in: Number of lag observations as input (X).
		n_out: Number of observations as output (y).
		dropnan: Boolean whether or not to drop rows with NaN values.
	Returns:
		Pandas DataFrame of series framed for supervised learning.
	"""
	n_vars = 1 if type(data) is list else data.shape[1] # Allow for 1 or multiple time series
	df = pd.DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i)) # Create the lag time series columns
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)] # Name the colums, e.g. output for t-1 will be 'var1(t-1)'
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i)) # Create the output time series columns
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)] # Name the colums, e.g. output for t will be 'var1(t)'
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = pd.concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True) # rows with NaN values have been automatically removed from the DataFrame.
	return agg
```
## Time Series in Keras LSTM for Prediction
[Using a Keras Long Short-Term Memory (LSTM) Model to Predict Stock Prices | by Derrick Mwiti | Heartbeat (comet.ml)](https://heartbeat.comet.ml/using-a-keras-long-shortterm-memory-lstm-model-to-predict-stock-prices-a08c9f69aa74)

Function/Method | Description
--- | ---
`scaler.inverse_transform` | Convert scaled data back to pre-scaled units

### Data prep and feature engineering
```python
# Load the training data
dataset_train = pd.read_csv('NSE-TATAGLOBAL.csv')
training_set = dataset_train.iloc[:, 1:2].values

# scale our dataset to numbers between zero and one
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

import numpy as np
# LSTMs expect our data to be in a specific format, usually a 3D array. We start by creating data in 60 timesteps and converting it into an array using NumPy. Next, we convert the data into a 3D dimension array with X_train samples, 60 timestamps, and one feature at each step.
X_train = []
y_train = []
for i in range(60, 2035): # 60 time series features to create, 2035 rows in dataframe
    X_train.append(training_set_scaled[i-60:i, 0]) # historical data
    y_train.append(training_set_scaled[i, 0]) # current/target data
X_train, y_train = np.array(X_train), np.array(y_train)
print(X_train.shape, y_train.shape)

# Convert from 2D to 3D array: (nrow, ncols) --> (nrow, ncols, 1)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1)) 
```
### Modelling
In order to build the LSTM, we need to import a couple of modules from Keras:
* Sequential for initializing the neural network
* Dense for adding a densely connected neural network layer
* LSTM for adding the Long Short-Term Memory layer
* Dropout for adding dropout layers that prevent overfitting

```python
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

regressor = Sequential()

# We add the LSTM layer with the following arguments:
    # 50 units which is the dimensionality of the output space
    # return_sequences=True which determines whether to return the last output in the output sequence, or the full sequence
    # input_shape as the shape of our training set.
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))

# add a few Dropout layers to prevent overfitting. We specify 0.2, meaning that 20% of the layers will be dropped.
regressor.add(Dropout(0.2)) 

regressor.add(LSTM(units = 50, return_sequences = True))

regressor.add(Dropout(0.2)) 

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units = 1)) # output of 1 unit

regressor.compile(optimizer = 'adam', 
    loss = 'mean_squared_error') # set the loss as the mean_squarred_error

# fit the model to run on 100 epochs with a batch size of 32. 
regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)
```
### Predicting
```python
#  import the test set: 16 rows
dataset_test = pd.read_csv('tatatest.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# In order to predict future stock prices we need to do a couple of things after loading in the test set:
    # Merge the training set and the test set on the 0 axis.
    # Set the time step as 60 (as seen previously)
    # Use MinMaxScaler to transform the new dataset
    # Reshape the dataset as done previously

dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)

# Select the rows to be used for prediction. You only need the number of rows equal to the number of historical time series features plus the number of rows in the test data. In this case, it's 60 time series features + 16 test data points.
inputs = dataset_total.loc[len(dataset_total) - len(dataset_test) - 60:].values 
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs) # scale the data

# Engineer features for prediction
X_test = []
# For time points to predict on, get the data from previous time points up to 60 steps back. These will be features used for prediciton.
for i in range(60, 76):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)

# Reshape test data and make the predictions
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)

# use inverse_transform to get back the stock prices in normal readable format.
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# visualize the result of the predicted stock price and the real stock price.
plt.plot(real_stock_price, color = 'black', label = 'TATA Stock Price')
plt.plot(predicted_stock_price, color = 'green', label = 'Predicted TATA Stock Price')
plt.title('TATA Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('TATA Stock Price')
plt.legend()
```

# Network Analysis
## `networkx` package
* [Introduction to Graph Theory | Graphs in Python (analyticsvidhya.com)](https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/)
* [See 2022-11-16 notepad](/W09/2022-11-16%20notepad%20network%20analysis.ipynb)
* [2022-11-16 lecture notebook](https://colab.research.google.com/drive/1EWc9_yJksl4_FgvPiu-jE8H53oUsJnnw#scrollTo=46d7df40)

Function/Method | Description | Imports
--- | ---- | ---
`G = nx.Graph()` | Create a graph | import networkx as nx
`G.add_node(1)`  | Add a node
`G.add_nodes_from([2,3])` | Add a list of nodes
`G.add_edge(1,2)`
`G.add_edge(*e)`, where  `e = (2,3)` | Add an edge from a tuple
`G.add_edges_from([(1,2), (1,3)])` A| Add edges from a list
`G.nodes()`, `G.edges()` | Access nodes and edges. Individual nodes and edges can be accessed using the bracket/subscript notation
`G[1]` or `G.adj[1]` | Show adjacent nodes
`nx.draw_networkx(G)` | Draw the network | import matplotlib.pyplot as plt<br>import pygraphviz as pgv
`FG = nx.from_pandas_edgelist(df, source=column_name, target=column_name, edge_attr=True,)` | Create a graph from a dataframe

Measure | Function/Method | Description
--- | --- | ---
Degree | `nx.average_degree_connectivity(FG)` | For a node of degree k - What is the average of its neighbours' degree?
Degree | `nx.algorithms.degree_centrality(FG)` (FG is a graph) | Calculate for all nodes in the graph
Density | `nx.density(FG)` | Average edge density of the Graphs
Shortest path | `nx.shortest_path(graph, node1, node2, weight=weight)` | Picks the shortest path according to weight. [See documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path.html#shortest-path).
Shortest path | `nx.shortest_path_length(graph, node1, node2, weight=weight)` | Picks the shortest path length according to weight
Shortest path | `nx.average_shortest_path_length(FG)` | Average shortest path length for ALL paths in the Graph
path | `nx.all_simple_paths(FG, source='JAX', target='DFW')` | Get all paths available between two nodes
path | `nx.dijkstra_path(FG, source='JAX', target='DFW')` | Find shortest path using dijkstra algortihm. [See documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.dijkstra_path.html#dijkstra-path).
Centrality | `nx.eigenvector_centrality(G_weighted, weight=weight)`  | If no weight parameter is passed, then weight is not used.
Betweeness | `nx.betweenness_centrality(G_weighted, weight='weight')`

Function/Method | Description | Imports
--- | ---- | ---
`subgraph(G, nbunch)`   | induced subgraph view of G on nodes in nbunch
`union(G1,G2)`   | graph union
`disjoint_union(G1,G2)` | graph union assuming all nodes are different
`cartesian_product(G1,G2)` | return Cartesian product graph
`compose(G1,G2)` | combine graphs identifying nodes common to both
`complement(G)`  | graph complement
`create_empty_copy(G)`  | return an empty copy of the same graph class
`convert_to_undirected(G)`| return an undirected representation of G
`convert_to_directed(G)`| return a directed representation of G
`nx.DiGraph()` | Create a directed graph. First item feeds to the second item in the tuple.
`nx.MultiGraph` , `nx.MultiDiGraph`

Node and Edge attributes can be added along with the creation of Nodes and Edges by passing a tuple containing node and attribute dict.

### Visualize a graph
```python
# Let us create another Graph where we can individually control the colour of each node
B = pgv.AGraph()

# Setting node attributes that are common for all nodes 
B.node_attr['style']='filled'
B.node_attr['shape']='circle'
B.node_attr['fixedsize']='true'
B.node_attr['fontcolor']='#FFFFFF'

# Creating and setting node attributes that vary for each node (using a for loop)
for i in range(16):
    B.add_edge(0,i)
    n=B.get_node(i)
    n.attr['fillcolor']="#%2x0000"%(i*16)
    n.attr['height']="%s"%(i/16.0+0.5)
    n.attr['width']="%s"%(i/16.0+0.5)
B.draw('star.png',prog="circo") # This creates a .png file in the local directory. Displayed below.

# Display the image
from PIL import Image
Image.open('star.png') # The Graph visualization we created above.
```

```python
pos = nx.spring_layout(G_dir, seed=7)
nx.draw_networkx(G_dir, pos)
```

# Online learning
[What is Online Machine Learning?. Making machines learn in real time | by Max Pagels | The Hands-on Advisors | Medium](https://medium.com/value-stream-design/online-machine-learning-515556ff72c5)

In addition to the `fit()` method, the SGDRegressor also provides a `partial_fit(`) method, so that you can incrementally train on small batches of data. In fact, all learning algorithms that are compatible with standard optimisation algorithms like (stochastic) gradient decent, adam, RMSprop, and so on have this capability
```python
import numpy as np
from sklearn import linear_model
n_samples, n_features = 10, 5

# Create toy data
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)

# Model
clf = linear_model.SGDRegressor()
clf.fit(X, y)

clf.predict(np.random.randn(1, n_features))

# Incrementally train
clf.partial_fit(X, y)
```
# Market Basket Analysis (Affinity Analysis)
* [See 2022-11-19 notepad](/W09/2022-11-19%20notepad.ipynb)

<img src="https://devopedia.org/images/article/156/5125.1550432720.png" width="600">

## Example with `mlextend`
* [Market Basket Analysis with Python and Pandas - Python Data](https://pythondata.com/market-basket-analysis-with-python-and-pandas/)
* [See 2022-11-19 notepad](/W09/2022-11-19%20notepad.ipynb)

```python
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_excel('Online Retail.xlsx')
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]
# First, we’ll groupby the columns that we want to consider. For the purposes of this analysis, we’ll only look at the United Kingdom orders.
market_basket = df[df['Country'] =="United Kingdom"].groupby(['InvoiceNo', 'Description'])['Quantity']


# Next, we want to hot encode the data and get 1 transaction per row to prepare to run our mlxtend analysis.
market_basket = market_basket.sum().unstack().reset_index().fillna(0).set_index('InvoiceNo')

# Before we continue, we want to convert all of our numbers to either a `1` or a `0` (negative numbers are converted to zero, positive numbers are converted to 1). We can do this encoding step with the following function:
def encode_data(datapoint):
    if datapoint <= 0:
        return 0
    if datapoint >= 1:
        return 1
market_basket = market_basket.applymap(encode_data)
```
Now, lets find out which items are frequently purchased together. We do this by applying the mlxtend `apriori` fuuinction to our dataset.

There one thing we need to think about first. the `apriori` function requires us to provide a minimum level of ‘support’. 

```python
itemsets = apriori(market_basket, min_support=0.03, use_colnames=True)
```
The final step is to build your association rules using the mxltend `association_rules` function. You can set the metric that you are most interested in (either `lift` or `confidence` and set the minimum threshold for the condfidence level (called `min_threshold`). The `min_threshold` can be thought of as the level of confidence percentage that you want to return. For example, if you set `min_threshold` to 1, you will only see rules with 100% confidence. I
```python
rules = association_rules(itemsets, metric="lift", min_threshold=0.5)
```

## Lift
* [Apriori Algorithm in Python (Recommendation Engine) | by Deepak Poojari | Medium](https://deepak6446.medium.com/apriori-algorithm-in-python-recommendation-engine-5ba89bd1a6da)

Lift refers to the increase in the ratio of the sale of B when A is sold.
* Lift(A –> B) can be calculated by dividing Confidence(A -> B) divided by Support(B).
* Mathematically it can be represented as: Lift(A→B) = (Confidence (A→B))/(Support (B))

Association rule by Lift
* lift = 1 → There is no association between A and B.
* lift < 1→ A and B are unlikely to be bought together.
* lift > 1 → greater the lift greater is the likelihood of buying both products together.

# Recommender engines
* [See 2022-11-21 lecture notebook for example of a recommender engine based on Euclidean distances](https://colab.research.google.com/drive/1ko72TAgktDU_aZ4lExPnarrzkTjey3Al#scrollTo=d4uaaJ9Es8Q9)


## Cosine similarity
* [How to build a content-based movie recommender system with Natural Language Processing | by Emma Grimaldi | Towards Data Science](https://towardsdatascience.com/how-to-build-from-scratch-a-content-based-movie-recommender-with-natural-language-processing-25ad400eb243)
* [Beginner Tutorial: Recommender Systems in Python](https://www.datacamp.com/tutorial/recommender-systems-python)
* [2022-11-21 walkthrough recommender engine.ipynb - Colaboratory (google.com)](https://colab.research.google.com/drive/1pNaYefN8tfkDRB1F72ec2t2HrcrzCbhC#scrollTo=kOyRzOWbTzNi)


<img src="https://miro.medium.com/max/1100/1*r5ULMbx7ju3_Y4TU1PJIyQ.png" width="400">


### Example 1
[How to build a content-based movie recommender system with Natural Language Processing | by Emma Grimaldi | Towards Data Science](https://towardsdatascience.com/how-to-build-from-scratch-a-content-based-movie-recommender-with-natural-language-processing-25ad400eb243)

#### Data prep
```python
import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('https://query.data.world/s/uikepcpffyo2nhig52xxeevdialfl7')

df = df[['Title','Genre','Director','Actors','Plot']]

# Data cleaning: I used this Rake function to extract key words from the Plot column, so instead of using the entire sentences describing the plot, I only considered the most relevant words in the description. In order to do this, I applied this function to each row under the Plot column and assigned the list of key words to a new column, named Key_words
# initializing the new column
df['Key_words'] = ""

for index, row in df.iterrows():
    plot = row['Plot']
    
    # instantiating Rake, by default it uses english stopwords from NLTK
    # and discards all puntuation characters as well
    r = Rake()

    # extracting the words by passing the text
    r.extract_keywords_from_text(plot)

    # getting the dictionary whith key words as keys and their scores as values
    key_words_dict_scores = r.get_word_degrees()
    
    # assigning the key words to the new column for the corresponding movie
    row['Key_words'] = list(key_words_dict_scores.keys())

# dropping the Plot column
df.drop(columns = ['Plot'], inplace = True)
```
Modeling and making the recommender
```python
# instantiating and generating the count matrix
count = CountVectorizer()
count_matrix = count.fit_transform(df['bag_of_words'])

# generating the cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix, count_matrix)
# In the resulting similarity matrix, all the numbers on the diagonal are 1 because, of course, every movie is identical to itself. The matrix is also symmetrical because the similarity between A and B is the same as the similarity between B and A.

# creating a Series for the movie titles so they are associated to an ordered numerical
# list I will use in the function to match the indexes
indices = pd.Series(df.index)

#  defining the function that takes in movie title 
# as input and returns the top 10 recommended movies
def recommendations(title, cosine_sim = cosine_sim):
    
    # initializing the empty list of recommended movies
    recommended_movies = []
    
    # gettin the index of the movie that matches the title
    idx = indices[indices == title].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)
    
    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(list(df.index)[i])
        
    return recommended_movies
```
## Euclidean distance
[W08D01 lecture notebook](https://colab.research.google.com/drive/1ko72TAgktDU_aZ4lExPnarrzkTjey3Al)

```python
import pandas as pd

data_url = 'https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv'
cars = pd.read_csv(data_url)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# Step 1: define the features
from sklearn.preprocessing import StandardScaler

# Extract only some subset of columns to reduce computation time 
X = cars[['mpg', 'disp', 'hp', 'wt']].values

# Standardize the features so that no feature dominates the
# distance computations due to unit scale
scaler = StandardScaler().fit(X)
X = scaler.transform(X)

# Step 2: define a distance metric
from sklearn.metrics.pairwise import euclidean_distances

# Step 3: recommend items
# Car the user is looking at
looking_at_car = [15, 300, 160, 3.2] #mpg, disp, hp, wt
looking_at_car = scaler.transform([looking_at_car])

# Distance from all other cars
distances = euclidean_distances(X, looking_at_car) # (n_rows1, n_cols), (n_rows2, n_cols) --> (n_rows1, n_rows2)
distances_reshaped = distances.reshape(-1)   # Before it was (n_cars, 1), now just one dimension

# Find the 3 indices with the minimum distance (highest similarity) to the car we're looking at
ordered_indices = distances_reshaped.argsort() #smallest values to largest

closest_indices = ordered_indices[:3] # three closest

# Get the cars for these indices
closest_cars = cars.iloc[closest_indices]
```

## Apriori algorithm for collaborative filtering 
* [Reference: The Apriori Algorithm in Python. Expanding Thor’s fan base | by Fabio Italiano | Medium](https://medium.com/@fabio.italiano/the-apriori-algorithm-in-python-expanding-thors-fan-base-501950d55be9)
* [See A priori exercise notebook](/W10/2022-11-21-recommender_engines_exercise/apriori_exercise.ipynb)

```python
# import pandas
import pandas as pd  

# from apyori import apriori
from apyori import apriori
movie_data = pd.read_csv('https://raw.githubusercontent.com/pirandello/apriori/master/movie_dataset.csv', 
                         header = None)

# Transform dataframe to a list of lists as that is requred for apyori
records = []
for i in range(len(movie_data)):
    records.append([str(movie_data.values[i, j]) for j in range(20)])

# Instantiate
association_rules = apriori(records, min_length=2,
    min_support=40/len(records),
    min_confidence=.2,
    min_lift=3
    )
# Put results into list format
association_results = list(association_rules)

# Convert results into a dataframe
results = []
for item in association_results:
    # first index of the inner list contains base item and add item.
    # A pair may contain more than 2 items because each "item" in the pair can contain more than 1 movie.
    pair = item[0]
    items = [item for item in pair]
    title1 = str(items[0])
    title2 = str(items[1])
    # support = (item[1]).str.replace('\w+=(\d*.\d*)', '\\1', regex=True)
    support = item[1]
    #third index of the list located at 0th of the third index of the inner list
    confidence = item[2][0][2]
    lift = item[2][0][3]
    rows = (title1, title2, support, confidence, lift)
    results.append(rows)
labels = ['Title 1','Title 2','Support','Confidence','Lift']
movie_suggestion = pd.DataFrame.from_records(results, columns = labels)
```
## Memory-Based Collaborative Filtering
* [See CF_memory_based_exercise notebook](./W10/2022-11-21-recommender_engines_exercise/CF_memory_based_exercise_Colab_version.ipynb)
* [See 2022-11-22 notepad](./w10/2022-11-22%20notepad%20recommender%20engines.ipynb)

## Model-Based Collaborative Filtering
* See CF_model_based_exercise_Colab_version.ipynb: [on local machine](./w10/2022-11-21-recommender_engines_exercise/CF_model_based_exercise_Colab_version.ipynb), [on Colab for faster computation](https://colab.research.google.com/drive/1vG1YBCh0BlBUhkDqaRiPohnT3e9VPx4m#scrollTo=_iFYzBysputy)
* [Tutorial: Practical Introduction to Recommender Systems | by Cambridge Spark | Cambridge Spark](https://blog.cambridgespark.com/tutorial-practical-introduction-to-recommender-systems-dbe22848392b)
* [Scikit Surprise](https://surprise.readthedocs.io/en/stable/getting_started.html?highlight=train%20test%20split#train-test-split-and-the-fit-method)
* [2022-11-22 lecture notebook](https://colab.research.google.com/drive/11lwbpsx8Rk8xMnECmS0HaGLZBrjbe6ic)

### Example from `CF_model_based_exercise_Colab_version.ipynb`
```python
import pandas as pd
# import SVD from surprise
from surprise import SVD

# # import dataset from surprise
from surprise import Dataset
from surprise import Reader

# import accuracy from surprise
from surprise import accuracy

# import train_test_split from surprise.model_selection
from surprise.model_selection import train_test_split
# import GridSearchCV from surprise.model_selection
from surprise.model_selection import GridSearchCV
# import cross_validate from surprise.model_selection
from surprise.model_selection import cross_validate

book_ratings = pd.read_csv('/content/drive/MyDrive/data exercises/W10/BX-Book-Ratings.csv',
                           sep=";", encoding="latin").sample(frac=.05, random_state=0)

# Create data set in surprise format
reader = Reader(rating_scale=(0, 10))

# Loads Pandas dataframe
data = Dataset.load_from_df(book_ratings, reader)

# Train test split
trainset, testset = train_test_split(data, test_size=0.15) 

# Fit and predict (no grid search)
alg = SVD()
output = alg.fit(trainset)

predictions = alg.test(testset)
rmse = accuracy.rmse(predictions)
print(f'Model RMSE on test set: {rmse:.2f}')
```
#### With GridSearchCV
```python
param_grid = {
    'n_factors': [110, 120, 140, 160],
    'reg_all': [0.08, 0.1, 0.15]
}
gs = GridSearchCV(SVD, param_grid, measures={'rmse', 'mae'})
gs.fit(data)
print(gs.best_params['rmse'])

alg2 = gs.best_estimator['rmse']
alg2.fit(trainset)
predictions2 = alg2.test(testset)
rmse2 = accuracy.rmse(predictions2)
print(f'Model 2 RMSE on test set: {rmse2:.2f}')
```
<details>
<summary>Tutorial: Practical Introduction to Recommender Systems | by Cambridge Spark </summary>

```python
! pip install scikit-surprise # for Colab

import numpy as np
import pandas as pd
import surprise

dataset = load_csv('ratings.txt', r'C:\Users\silvh\OneDrive\lighthouse\W10', sep=' ')
dataset.columns= ['uid', 'iid', 'rating']
# For this dataset, the first column is the user ID, the second is the ID of the movie they’ve reviewed, and the third column is their review score
lower_rating = dataset['rating'].min()
upper_rating = dataset['rating'].max()
reader = surprise.Reader(rating_scale = (lower_rating, upper_rating))
data = surprise.Dataset.load_from_df(dataset, reader)

# We will use the method SVD++. This method extends vanilla SVD algorithms such as the one covered in the previous blog post by only optimising known terms and performing regularisation
alg = surprise.SVDpp()
output = alg.fit(data.build_full_trainset())

# Now we’ve fitted the model, we can check the predicted score of, for example, user 50 on a music artist 52 using the predict method.
pred = alg.predict(uid='50', iid='52')
score = pred.est

# Let’s make our recommendations to a particular user. Let’s focus on uid 50 and find one item to recommend them. First we need to find the movie ids that user 50 didn’t rate, since we don’t want to recommend them a movie they’ve already watched!
# Get a list of all movie ids
iids = dataset['iid'].unique()
# List of iids that uid 50 has rated
iids50 = dataset.loc[dataset['uid'] == 50, 'iid']
# Remove the iids that uid 50 had rated from the list of all movie ids
iids_to_pred = np.setdiff1d(iids, iids50)
```
### Making predictions
Next we want to predict the score of each of the movie ids that user 50 didn’t rate, and find the best one. For this we have to create another dataset with the iids we want to predict in the sparse format as before of: uid, iid, rating. We'll just arbitrarily set all the ratings of this test set to 4, as they are not needed. Let's do this, then output the first prediction.

```python
testset = [[50, iid, 4.] for iid in iids_to_pred]
predictions = alg.test(testset)

#  each prediction is a special object. In order to find the best, we’ll convert this object into an array of the predicted ratings. We’ll then use this to find the iid with the best predicted rating.
pred_ratings = np.array([pred.est for pred in predictions])

# Find index of the max predicted rating, then ind the the corresponding iid to recommend
i_max = pred_ratings.argmax()
iid = iids_to_pred[i_max]
print('Top item for user 50 has iid {0} with predicted rating {1}'.format(iid, pred_ratings[i_max]))

```
### Tuning and Evaluating the Model

The method `SVD++`, as well as most other matrix factorisation algorithms, will depend on a number of main tuning constants: the dimension DD affecting the size of UU and VV; the learning rate, which affects the performance of the optimisation step; the regularisation term affecting the overfitting of the model; and the number of epochs, which determines how many iterations of optimisation are used.

In this tutorial we’ll tune the learning rate and the regularisation term.
In surprise, tuning is performed using a function called `GridSearchCV`.
```python
param_grid = {
    'lr_all': [.11, .01],
    'reg_all': [0.1, .5]
}
gs = surprise.model_selection.GridSearchCV(surprise.SVDpp, param_grid, measures={'rmse', 'mae'}, cv=3)
gs.fit(data)
print(gs.best_params['rmse'])

# The performance of a particular model you’ve chosen can be evaluated using cross validation. This might be used to compare a number of methods for example, or just to check your method is performing reasonably. This can be done by running the following:
alg = surprise.SVDpp(lr_all= .001) # Parameter choices can be added here
output = surprise.model_selection.cross_validate(alg, data, verbose=True)
```
</details>

# Online learning

In `sklearn`, online learning can be implemented using `.partial_fit()` method on new batches of data.

# Reinforcement learning
[2022-11-23 lecture notebook](https://colab.research.google.com/drive/1FuncJ1N2GgqO45sBDgi_S_xEpquq9DzT#scrollTo=tq6C6ruilD4G)
## Markov Decision Process (MDP):
- At each time step, the agent will get some representation of the environment's state.
- Given this representation, the agent selects an action to take.
- The environment is then transitioned into a new state.
- The agent is given a reward as a consequence of the previous action.
- The agent's goal is to maximize the total amount of rewards from its actions.

## Q-Learning
**Bellman formula**:
$$ Q(s,a) = r(s,a) + \gamma \max_{a'} Q(s',a') $$
* $\gamma$ : the "discount factor" that determines to which extent you should prefer the current reward over the future reward and vice versa. 
* To summarize, the Q-Table score at state *s*, given action *a* $Q(s,a)$ is the immediate reward $r(s,a)$ plus the best possible future reward $\gamma \max_{a'} Q(s',a')$.

### Learning Algorithm

Given the equation above, we can now write pseudo-code for our learning algorithm:

1. Initialize Q-Table Q with equal numbers for all states and actions
1. Set learning rate α ← 1
1. Repeat simulation many times:
   1. Start at random position
   1. Repeat:
        1. Select an action *a* at state *s*
        1. Execute action by moving to a new state *s'*
        1. If we encounter end-of-game condition, or total reward is too small - exit simulation  
        1. Compute reward *r* at the new state
        1. Update Q-Function according to Bellman equation: *Q(s,a)* ← *(1-α)Q(s,a)+α(r+γ max<sub>a'</sub>Q(s',a'))*
        1. *s* ← *s'*
        1. Update the total reward and decrease α. 
            * *That way, you put more weight on immediate rewards and less ewight on future rewards.*

## Exploit vs. Explore
To strike a balance between exploration and exploitation, choose the action at state s with probabilities proportional to values in the Q-Table. In the beginning, when Q-Table values are all the same, it would correspond to a random selection, but as we learn more about our environment, we would be more likely to follow the optimal route, while also allowing the agent to choose the unexplored path occasionally.

[See 2022-11-23 lecture notebook for how to implement on Python](https://colab.research.google.com/drive/1FuncJ1N2GgqO45sBDgi_S_xEpquq9DzT#scrollTo=tq6C6ruilD4G)