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
| ...  |

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

```python
{
    "Aaden": { 2010: 560 },
    "Aaliyah": { 2000: 211, 2010: 56 }
    # ...
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

The provided 'abe' test hits the case where the passed in dict is empty, so both the name and the year are new. Write at least 2 additional tests where the name is not-new: test year-new and test year-not-new. The `add_name()` function is short but dense. Doctests are a good fit for this situation, letting you explicitly identify and work out the various cases.

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

Each line from the text file ends with a `\n`, so we typically remove that with `line = line.strip()`. Use `split()` to separate the words from the commas.

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

Write code for `search_names()` which searches for a target string and returns a sorted list of all the name strings that match the target (no year or rank data). In this case, the target matches a name, not-case sensitive, if the target appears anywhere in the name. (Sorting is in the Friday lecture.) For example the target strings 'aa' and 'AA' both match 'Aaliyah' and 'Ayaan'. Return the empty list if no names match the target string. This function is called by `main()` for the -search command line argument.

Write at least 3 Doctests for `search_names()` which is the most algorithmic. You can make up a tiny names dict just for the tests.

## Provided: main() and print_names()

We've provided the `main()` function. Given 1 or more baby data file arguments, `main()` reads them in with your `read_files()` function, and then calls the provided `print_names()` function (2 lines long!) to print all the data out.

The files small-2000.txt small-2010.txt have just a few test names, so they are good to hand-check that your output is correct, and of course your Doctests are working on your decomposed functions to check them individually. The output should be the same if small-2010.txt is loaded before small-2000.txt.

Running your code to load multiple files:

```bash
$ python3 babynames.py small-2000.txt small-2010.txt
Alice [(2000, 1), (2010, 2)]
Bob [(2000, 1), (2010, 2)]
Cindy [(2000, 2)]
Yot [(2010, 1)]
Zena [(2010, 1)]
```

## Try It With Real Data

I believe this is the [correct meme](https://cheezburger.com/3914695680) for this part of the homework.

The small files test that the code is working correctly, but are no fun. The provided `main()` function looks at all the files listed on the command line, and loads them all by calling your `read_files()` function in a loop. You can take a look at 4 decades of data with the following command in the terminal (use the tab-key, to complete file names without all the typing).

```bash
$ **python3 babynames.py baby-1980.txt baby-1990.txt baby-2000.txt baby-2010.txt**
...tons of output!...
```

## Filename \*

A handy feature of the terminal is that you can enter baby-\*.txt to mean all the filenames with that pattern: baby-1900.txt baby-1910.txt ... baby-2020.txt. This is an incredibly handy shorthand when you are working through a big-data problem with many files. This may also explain why CS and data-science people tend to use patterns to name their data files, so the filenames work with this \* feature. You can demonstrate this with the "ls" command, which prints out filenames (this form works in Windows PowerShell too):

```bash
$ **ls baby-*.txt**
baby-1900.txt baby-1930.txt baby-1960.txt baby-1990.txt
baby-1910.txt baby-1940.txt baby-1970.txt baby-2000.txt
baby-1920.txt baby-1950.txt baby-1980.txt baby-2010.txt
baby-2020.txt
```

This \* feature fits perfectly with babynames.py. The following terminal command loads all 13 baby-xxx.txt files without typing in anything else:

```bash
$ python3 babynames.py baby-*.txt
```

In the Windows PowerShell, the command line is slightly different, using the "get-item" command:

```bash
$ py babynames.py (get-item baby-*.txt)
```

With the baby-\*.txt technique, the command line loads all the files, running the 24,000 odd data points through your functions to get it all organized in the blink of an eye .. that's how the data scientists to it.

## Search

Organizing all the data and dumping it out is impressive, but it is a blunt instrument. `main()` connects to your search function like this: if the first 2 command line args are "-search _target_", then main() reads in all the data and calls your `search_names()` function to find matching names and print them. Here is an example with the search target "aa":

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

## Homework 6b - Baby Graphics

For this project, you will bring the Baby Names data to life.

## TK GUI

When Python is installed on a machine, it includes the venerable "TK" graphics systems via the "tkinter" module. It can create graphical windows, buttons etc. on screen - the graphical user interface (GUI). We provide the code that sets up the GUI. That code is not very interesting. TK is a very old system, so the code to set it up is kind of archaic too, but it works fine for our purposes. To learn modern GUI techniques, you could take CS108 or CS142. In this case, the functions you need to write are at the top of the file, and the provided TK functions are below.

## a. main() / Search

The main() code is provided in babygraphics.py. The main() function calls your babynames.read_files() function to read in the names data. The challenge on this assignment is providing an interactive GUI for the baby data. Run the program from the command line in the usual way.

```bash
$ python3 babygraphics.py
```

Without adding any code, running babygraphics.py should load the baby data, and display a largely empty window which waits for you to type something. The provided code takes care of setting up the GUI elements, and detecting when the return-key is typed to call your search and draw functions. Click in the search field, type "arg" or "aa" and hit return. The provided handle_search() functions calls your babynames.search_names() function, and pastes the result into the window. Those functions were called to print output in the terminal for HW 6a. Here, the GUI code calls the exact same functions, but puts the output in the GUI.

Syntax: here is the key line in the provided handle_search() where it calls your search_names() function from HW6a:

```
 ...
 # Call the search_names function in babynames.py
 result = babynames.search_names(names, target)
 ...
```

Milestone search: you can run babygraphics and see the results of searches like "aa" and "arg" in the GUI.

## Constants

Here are constants for the use in the babygraphics algorithms. The number of years of data is given by `len(YEARS)`.

```
# Provided constants to load and draw the baby data
FILENAMES = ['baby-1900.txt', 'baby-1910.txt', 'baby-1920.txt', 'baby-1930.txt',
             'baby-1940.txt', 'baby-1950.txt', 'baby-1960.txt', 'baby-1970.txt',
             'baby-1980.txt', 'baby-1990.txt', 'baby-2000.txt', 'baby-2010.txt',
             'baby-2020.txt']

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000,
         2010, 2020]
SPACE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
```

Look at the YEARS constant above. For each year there are actually two values your code might use - the int year itself, e.g. 1900 or 1910. For each of those years, there is also the **index**, indicating where that year is in the YEARS list, e.g. 0 or 1. It's easy to get those two related quantities mixed up in your code — a good place to use good variables names to keep things straight.

## b. draw_fixed()

The draw_fixed() function draws the fixed lines and text behind the data lines. It is called once from main() to set up the window initially, and then again whenever the graph is re-drawn. When draw_fixed() runs, the canvas is some width/height in the window. The provided code retrieves those numbers from the canvas for use by the subsequent lines.

Draw the year grid as follows. All of these drawings are in black: The provided constant SPACE=20 defines an empty space which should be reserved at the 4 edges of the canvas. Draw a top horizontal line, SPACE pixels from the top, and starting SPACE pixels from the left edge and ending SPACE pixels before the right edge. Draw a bottom horizontal line SPACE pixels from the bottom edge, and SPACE from the left and right edges. For this project, we will not be picky about +/- 1 pixel coordinates in the drawing.

Here is a diagram of the line spacing for draw_fixed(). The outer edge of the canvas is shown as a rectangle, with the various lines drawn within it. Each double-arrow marks a distance of SPACE pixels.

![](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-baby-diagram.png)

In the GUI, the text field takes up the top of the window, and the canvas is a big rectangle below it. Then the search text field is at the bottom of the window below the canvas.

![](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-baby-lines1.png)

## Year Lines

The provided constant YEARS lists the int years to draw. In draw_fixed(), draw a vertical "year" line for each year in YEARS. The first year line should be SPACE pixels from the left canvas edge. The year lines should touch the 2 horizontal lines, spaced out proportionately so each year line gets a roughly equal amount of empty space to its right on the horizontal lines. Vertically, the year lines should extend all the way from the top of the canvas to its bottom.

The trickiest math here is computing the x value for each year index. Decompose out a short helper function index_to_x() to compute the x coordinate in the canvas for each year index: 0 (the first year), 1 (the second year), 2, .... len(YEARS)-1 (the last year). No loops are required for this function.

The two functions draw_fixed() and draw_name() need to agree exactly on the x coordinate for each year. By calling index_to_x() to figure the needed x value, they are perfectly in sync. Doctests are not required. The vertical lines should be spread evenly across the width (vs. the strategy where all the years have the same int sub_width).

For drawing, we will use Python's built in "TK" drawing functions which are similar but not identical to the DrawCanvas functions we used earlier. The drawing functions truncate coordinates from float to int internally, so you can do your computations as float. The function to draw a black line in TK is:

```python
canvas.create_line(_x1_, _y1_, _x2_, _y2_)
```

![alt:draw a vertical line and year label for every year](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-baby-lines2.png)

At a point TEXT_DX pixels to the right of the intersection of each vertical line with the lower horizontal line, draw the year string. The TK create_text() function shown below will draw the `'hi'` string with its upper left corner at the given x/y. The constant `tkinter.NW` indicates that the x,y point is at the north-west corner relative to the text.

```python
canvas.create_text(_x_, _y_ , text=_'hi'_, anchor=tkinter.NW, fill='red')
```

The optional parameter `fill='red'` specifies a color other than the default black for the TK functions like create_line() and create_text().

By default, main() creates a window with a 1000 x 600 canvas in it. Try running main() like this to try different width/height numbers:

```bash
$ python3 babygraphics.py 800 400
```

Your line-drawing math should still look right for different width and height values. Note that if you specify a width of, say, 400, that will be the size of the canvas, but the window may be a wider number since it also needs space to the right of the search text field to display the search results. You should also be able to change temporarily, say, the SPACE constant to a value like 100, and your drawing should use the new value. (SPACE is a good example of a constant - a value which is used in several places. Defining it as a constant makes it easy to change, and the lines of code that use it remain consistent with each other.)

Milestone draw-fixed: your code can create all the fixed straight lines and year strings and works for various window widths and heights.

## draw_names() - Jennifer Mode

Ultimately, the draw_names() function should take in any number of names and draw all their data. The starter code for draw_names() works in a special "Jennifer" mode where it always draws the name "Jennifer" when you hit the return key with the cursor in the input field (or some other single name you typed in there). This is handy way to work on the draw_name() function without having to type a lot in the GUI. In a later step, you will upgrade draw_names() out of its always-Jennifer mode.

The names in the SSA data set all have an upper case character as their first character, e.g. `'Emily'`. To shield the user from that detail, the provided code converts what the user types in, e.g. `'emily'`, to the SSA `'Emily'` form before draw_names() is called. In this way, the user can type the names in without worrying about capitalization.

## c. best_rank()

This is a helper function for the main drawing function. There is a problem when trying to draw the data for a name and year: some years have data and some do not. For example, in the Jennifer data, there's nothing in the years before 1940.

```python
{1940: 690, 1950: 118, "..."}
```

The drawing code is most straightforward if every year has a rank number to draw, without worrying about the details that yielded that rank number. Our solution is this: if a name does not have data for a particular year (e.g. `'Jennifer'` in 1900), or if the name itself does not appear in the name dict at all, e.g. the name `'Xyz'`, then we'll say that the best rank number to use is `MAX_RANK`. Given a complication like this, the CS strategy is to wrap it up in a function. Write code for the best_rank() function which isolates this issue — if a name and year have a rank number, return that number. Otherwise, return `MAX_RANK`. Doctests are provided.

```python
def best_rank(names, name, year):
    """
    Given names dict, name string, and int year.
    Return the best rank to use: the actual rank if
    that name+year exists in the data, or MAX_RANK
    if the name or year is not present.
    >>> # Tests provided, code TBD
    ...
```

Milestone best-rank: best_rank() passes its tests.

## d. draw_name() Part 1

def draw_name(canvas, names, name, color):

The draw_name() function is the heart of the program, drawing all the lines for one name. The draw_name() function has parameters for the names dict, name string, and color to use for the drawing. The function also accesses the YEARS constant for the series of years to draw.

![alt: data coming in to draw_name](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-baby1.svg)

Suppose the passed in name is "Jennifer". For every year, the code looks up the Jennifer rank for that year, and works out the y value in the graph for each year's rank. The x value for each year is already solved by the helper function index_to_x().

To compute the y, first get a rank number using your best_rank() helper. If the rank is 1 (the best possible rank), the y should be at the very top (covering the top horizontal line). If rank is MAX_RANK, the y should be at the very bottom (covering the bottom horizontal line).

As a milestone, figure out the x,y for each year for the given name, and as a temporary measure, draw a horizontal line starting at that x,y and extending rightwards 40 pixels (each x,y is a little dot in the drawing below). As mentioned above "Jennifer" is a nice example here, as the name hits both the min and the max possible ranks, something of an achievement for a single name.

![alt: figure x,y for each year](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-babydraw.svg)

The default TK create_line() draws a 1-pixel-wide line. For draw_name(), it looks better to draw the lines with a little more thickness. Use the constant LINE_WIDTH and the color parameter as shown below to draw a thick, colored line. The parameters to create_line() don't have great names in this context: "width" is the thickness of the line, and "fill" is its color. The line below draws in red, and you can fix it later to use the right color.

```python
canvas.create_line(_x1_, _y1_, _x2_, _y2_, width=LINE_WIDTH, fill='red')
```

Here's a picture of the Jennifer data with the 40-pixel lines. Hitting the return key with the cursor in the input field should call draw_name() this way. Jennifer has no data in 1900, and is #1 in 1970. You can scroll down to the later stages to see the full Jennifer data curve.  
![alt: draw short lines for each jennifer x,y](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-baby-name1.png)

You can type a different name in the input field, and draw_name() will be called with that name, so you can try different names to see your x,y code at work.

Milestone draw-name-1: for a name, your code can loop over all the years, figuring out the right x,y, for every year and draw the 40 pixel line.

## e. draw_name() Part 2

With the x,y working for every year, there are two more challenges for draw_name().

Draw the name/rank as a string, e.g. `'Jennifer 690'`, TEXT_DX pixels to the right of each year/rank point. The call to canvas.create_text(..) is the same as before, except using the constant `tkinter.SW` to position the text above and to the right of the year/rank point.

Drawing in all the lines is an algorithmic puzzle. For N years of data, there are N-1 lines to draw, connecting the x,y of one year to the x,y of the next year. There are several approaches that can work here. One approach uses the "previous" pattern to remember the x,y point from the previous iteration in the loop. For each point except the first, draw a line from the current point back to the previous point.

![alt: draw a line back to the previous point](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-babydraw2.svg)

Here is the Jennifer output with all the text and lines working:  
![alt: draw all lines and text for jennifer](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-baby-name2.png)

Milestone draw-name-2: for one name, the code loops over all the years, drawing in all the lines and text labels.

## f. draw_names()

The last step is fixing draw_names() to get out of its "Jennifer" dev mode. Delete the Jennifer dev-mode code from draw_names().

The "lookups" parameter is a list of name strings to process, e.g. `['Jennifer', 'Miguel', 'Anna']`. The provided code builds the lookups from whatever the user types in the text field, converting the first char of each word to uppercase. At the your-code-here mark, write code to draw all of the name strings in the lookups list, calling your draw_name() function once for each name.

The provided constant COLORS is a list of 4 color names. Draw the name at index 0 with the color at index 0. Draw name at index 1 with color 1, and so on. When the number of names is greater than the number of colors, wrap around to use the first color again (use the % "mod" operator).

Get your code working for multiple lookup names, looping to draw them all. That is the last challenge, and now this thing is really working.

"Jennifer" is a good test of course, but now we can layer on the data for Lucy and Jorge.  
![](https://web.stanford.edu/class/cs106a/handouts_w2021/homework-baby-name3.png)

Isn't "Chad" like some internet insult for something? Well check out Chad's graph. Compare it to Hazel. I don't think Madge is coming back either. Use your search feature to find more names. What names can you think of that have "haz" in them? Try it in the search field to see. Search for "marg" to see the many variations on Margaret. Try the names of your parents and grandparents and their friends. Many will be out of fashion, but some, like Emily, have come back.

Once it's drawing everything nicely - congratulations - you've built a complete end-to-end program: parsing the raw data, organizing it in a dict, and presenting it in an interactive GUI. With your code cleaned up, please turn in the two files babynames.py and babygraphics.py on [Paperless](https://paperless.stanford.edu).

## Background and Acknowledgements

Nick Parlante created the Baby Names assignment around 2004 for the then new Java version of CS106A and later brought it over to Python/TK. The original inspiration came from the article [Where Have All The Lisas Gone](https://www.nytimes.com/2003/07/06/magazine/where-have-all-the-lisas-gone.html) about how parents choose baby names, often wanting a name that is rare but not _too_ rare.

The data has been organized in a few different ways over the years, but it's always combined the algorithmic challenge of complex name/year data at one level, and then the loop/drawing logic above it to bring the data to the screen. The data set is large and fun, and that helps make the assignment fun too. The assignment was subsequently selected for the [Nifty Assignments](http://nifty.stanford.edu) archive and has been adopted by many schools.
