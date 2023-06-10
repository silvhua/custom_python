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