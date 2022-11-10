## Homework 6a - Baby Names

This project use the Social Security Administration's (SSA) [baby names](https://www.ssa.gov/oact/babynames/) data set of babies born in the US going back more than 100 years. This part of the project will load and organize the data. The second part of the project will build out interactive code that displays the data. Background reading: [Where Have All The Lisas Gone](https://www.nytimes.com/2003/07/06/magazine/where-have-all-the-lisas-gone.html). This is the article that gave Nick the idea to create this assignment way back when.

All parts of HW6 are due Wed Nov 16th at 11:55pm. The file [babynames.zip](babynames.zip) contains a "babynames" folder to get started.

## Warmups

Here are some warmup problems to get started. The first couple are just regular list problems. Then dict-count and nested dict problems. The "previous" pattern on the last problem will be in Fri lecture.

\> [dict3hw](https://wopr-service-qbrbcbuzwa-uw.a.run.app/#dict3hw)

**Turn In** [Turn In Warmups](https://wopr-service-qbrbcbuzwa-uw.a.run.app/turnin?hw=6.1&path=dict3hw) to Paperless

## Baby Data

Let's see what form the data is in to start with. At the Social Security [baby names](https://www.ssa.gov/oact/babynames/) site, you can visit a different web page for each year. Here's what the data looks like in a web page (indeed, this is pretty close to the birth year for many students in CS106A - hey there Emily and Jacob!)

**Popularity in 2000**

| Rank | Male name   | Female name |
| ---- | ----------- | ----------- |
| 1    | Jacob       | Emily       |
| 2    | Michael     | Hannah      |
| 3    | Matthew     | Madison     |
| 4    | Joshua      | Ashley      |
| 5    | Christopher | Sarah       |
| ...  | ...         | ...         |

In this data set, rank 1 means the most popular name, rank 2 means next most popular, and so on down through rank 1000. The data is divided into "male" and "female" columns. (To be strictly accurate, at birth when this data is collected, not all babies are categorized as male or female. That's rare enough to not affect the numbers at this level.)

## baby-2000.txt

A web page is encoded as - you guessed it! - plain text in a format called HTML. For your project, we have done a superficial clean up of the HTML text and stored it in files "baby-2000.txt", which look like:

```csv
2000
1,Jacob,Emily
2,Michael,Hannah
3,Matthew,Madison
4,Joshua,Ashley
5,Christopher,Sarah
6,Nicholas,Alexis
7,Andrew,Samantha
...
997,Vincenzo,Maiya
998,Dayne,Melisa
999,Francesco,Adrian
1000,Isaak,Marlen
```

## Data Organization

> A door is what a dog is perpetually on the wrong side of. - Ogden Nash

Data in the real world is very often not in the form you need. Reasonably for the Social Security Administration, their data is organized by **year**. Each year they get all those forms filled out by parents, they crunch it all together, and eventually publish the data for that year, such as we have as baby-2000.txt.

However, the most interesting analysis of the data requires organizing it by **name**, across many years. This real-world mismatch is part of the challenge for this project.

## Names Data Structure

We'll say that the "names" dict structure for this program has a key for every name. The value for each name is a nested dict, mapping int year to int rank:

```json
{
'Aaden': {2010: 560},
'Aaliyah': {2000: 211, 2010: 56},
...
}
```

Each name has data for 1 or more years, but which years have data for each name jumps around. In the above data, 'Aaliyah' jumped from rank 211 in 2000 to 56 in 2010 (these names are alphabetically first in the 2000 + 2010 data set). An empty dict is a valid names data structure - it just has zero names in it.

Functions below will work on this "names" data structure.

## a. Add Name

The `add_name()` function takes in a single year+rank+name, e.g. 2000, 10, 'abe', and adds that data into the names dict. Later phases can call this function in a loop to build up the whole data set.

The dict is passed in as a parameter. Python **never** passes a copy, but instead passes a reference to the one dict in memory. In this way, if `add_name()` modifies the passed in "names" dict, that's the same dict being used by the caller. The function also returns the names dict to facilitate writing Doctests. The starter code includes a single Doctest as an example (below).

```python
def add_name(names, year, rank, name):
"""
Add the given data: int year, int rank, str name
to the given names dict and return it.
(1 test provided, more tests TBD) >>> add_name({}, 2000, 10, 'abe')
{'abe': {2000: 10}}
"""
```

The provided 'abe' test hits the case where the passed in dict is empty, so both the name and the year are new. Write at least 2 additional tests where the name is not-new: test year-new and test year-not-new. The add_name() function is short but dense. Doctests are a good fit for this situation, letting you explicitly identify and work out the various cases.

## Issue: Name Appears Twice

In rare cases a name, e.g. 'Christian', appears twice in the data: once as a male name and once as a female name. We need a policy for how to handle that case. Our policy will be to keep whatever rank number for that name/year is read first (in effect the smaller number). For example for the baby-2000.txt data 'Christian' comes in as a male name at rank 22. Then it comes in as a female name at rank 576. We will disregard the 576. Your tests should include this case. This sort of rare case in the data is more likely to cause bugs; it doesn't fit the common data pattern you have in mind as you write the code.

CS Observation — if 99% of the data is one way, and 1% is some other way .. that doesn't mean the 1% is going to require less work just because it's rare. A hallmark of computer code is that it forces you to handle 100% of the cases.

## b. Add File

The simple baby text format for this data looks like:

```csv
2000
1,Jacob,Emily
2,Michael,Hannah
3,Matthew,Madison
4,Joshua,Ashley
5,Christopher,Sarah
6,Nicholas,Alexis
7,Andrew,Samantha
...
997,Vincenzo,Maiya
998,Dayne,Melisa
999,Francesco,Adrian
1000,Isaak,Marlen
```

The year is on the first line. The later lines each have the rank, male name, female name separated from each other by commas. Don't assume the data runs to exactly 1000, which would make the function too single-purpose. Just process all the lines there are.

Write the code to add the contents of one file.txt to the names dict parameter, which is returned. Tests are provided for this function, using the feature that a Doctest can refer to a file in the same directory. Here the tests use the relatively small test files "small-2000.txt" and "small-2010.txt" to build a names dict.

For reference, here is the contents of the small files:

**small-2000.txt**:

```
2000
1,Bob,Alice
2,Alice,Cindy
```

**small-2010.txt**:

```csv
2010
1,Yot,Zena
2,Bob,Alice
```

Each line from the text file ends with a '\\n', so we typically remove that with `line = line.strip()`. Use split() to separate the words from the commas.

For this data set, you need to treat the first line of the file differently than all the other lines. The standard for-line-in-file does not work well for that pattern, but there are other ways to get the lines of a text file. Here is a friendly reminder of three ways in Python to read a file. In this case, the `f.readlines()` function is a good fit.

```python
# Always open the file first
with open(filename) as f:

# 1. Go through all the lines, the super common pattern

for line in f:
line = line.strip()
...

# 2. Alternative: read the entire file contents in as a list of strings,
# one string for each line. Similar to #1, but a list that can be
# processed with a later foreach loop, you can grab a subset of the lines
# with a slice, etc.
lines = f.readlines()

# 3. Alternative: read the entire file contents into 1 text string
text = f.read()

# Reading data out a file works once per file-open. So calling f.read() or
# f.readlines() a second time does not read the data in again. You could open the
# file a second time to read the lines in a second time.

```

## c. read_files()

Write code for `read_files()` which takes a list of filenames, building and returning a names dict of all their data. This function is called by `main()` to build up the names dict from all the files mentioned on the command line. We are not testing this short function.

## d. search_names()

Write code for `search_names()` which searches for a target string and returns a sorted list of all the name strings that match the target (no year or rank data). In this case, the target matches a name, not-case sensitive, if the target appears anywhere in the name. (Sorting is in the Friday lecture.) For example the target strings 'aa' and 'AA' both match 'Aaliyah' and 'Ayaan'. Return the empty list if no names match the target string. This function is called by main() for the -search command line argument.

Write at least 3 Doctests for `search_names()` which is the most algorithmic. You can make up a tiny names dict just for the tests.

## Provided: main() and print_names()

We've provided the main() function. Given 1 or more baby data file arguments, main() reads them in with your read_files() function, and then calls the provided print_names() function (2 lines long!) to print all the data out.

The files small-2000.txt small-2010.txt have just a few test names, so they are good to hand-check that your output is correct, and of course your Doctests are working on your decomposed functions to check them individually. The output should be the same if small-2010.txt is loaded before small-2000.txt.

Running your code to load multiple files:

```bash
$ python3 babynames.py small-2000.txt small-2010.txt
Alice \[(2000, 1), (2010, 2)\]
Bob \[(2000, 1), (2010, 2)\]
Cindy \[(2000, 2)\]
Yot \[(2010, 1)\]
Zena \[(2010, 1)\]
```

## Try It With Real Data

I believe this is the [correct meme](https://cheezburger.com/3914695680) for this part of the homework.

The small files test that the code is working correctly, but are no fun. The provided main() function looks at all the files listed on the command line, and loads them all by calling your read_files() function in a loop. You can take a look at 4 decades of data with the following command in the terminal (use the tab-key, to complete file names without all the typing).

```bash
$ **python3 babynames.py baby-1980.txt baby-1990.txt baby-2000.txt baby-2010.txt**
...tons of output!...
```

## Filename \*

A handy feature of the terminal is that you can enter baby-\*.txt to mean all the filenames with that pattern: baby-1900.txt baby-1910.txt ... baby-2020.txt. This is an incredibly handy shorthand when you are working through a big-data problem with many files. This may also explain why CS and data-science people tend to use patterns to name their data files, so the filenames work with this \* feature. You can demonstrate this with the "ls" command, which prints out filenames (this form works in Windows PowerShell too):

```bash
$ **ls baby-\*.txt**
baby-1900.txt baby-1930.txt baby-1960.txt baby-1990.txt
baby-1910.txt baby-1940.txt baby-1970.txt baby-2000.txt
baby-1920.txt baby-1950.txt baby-1980.txt baby-2010.txt
baby-2020.txt
```

This \* feature fits perfectly with babynames.py. The following terminal command loads all 13 baby-xxx.txt files without typing in anything else:

```bash
$ **python3 babynames.py baby-\*.txt**
```

In the Windows PowerShell, the command line is slightly different, using the "get-item" command:

```bash
$ **py babynames.py (get-item baby-\*.txt)**
```

With the baby-\*.txt technique, the command line loads all the files, running the 24,000 odd data points through your functions to get it all organized in the blink of an eye .. that's how the data scientists to it.

## Search

Organizing all the data and dumping it out is impressive, but it is a blunt instrument. Main() connects to your search function like this: if the first 2 command line args are "-search _target_", then main() reads in all the data and calls your search_names() function to find matching names and print them. Here is an example with the search target "aa":

```bash
$ **python3 babynames.py -search aa baby-2000.txt baby-2010.txt**
Aaden
Aaliyah
Aarav
Aaron
Aarush
Ayaan
Isaac
Isaak
Ishaan
Sanaa
```

Once that's working, you are done with the first part, getting the data organized in memory and searchable.

## Whole File Doctests

Right click in your Python code on a line that is not inside of a function. You should see an option to run all of the Doctests in the whole file. This is a satisfying final step once all the bugs are worked out.

Once the data loading and searching are working, you are ready for part-b, bringing the data to life on screen.
