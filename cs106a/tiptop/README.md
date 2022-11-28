## Homework 7b - TipTop

This is a small project where you pull together many Python features to solve a realistic data problem. Download [tiptop.zip](https://web.stanford.edu/class/cs106a/handouts_w2021/tiptop.zip) to get started. The file "tiptop.py" is included as a starting point, but it is basically blank, so you are creating and testing your functions from scratch. This project does not require map/lambda.

## TipTop

Suppose there's this new social network called TipTop. Each poster has a handle like `'@alice'`. TipTop posts have tags like `'#watsup'` and `'#meh'`.

A "posts" text file records the statistics about a series of posts in following format: each line in the file represents one post by a poster. The first word on the line is the poster, e.g. `'@alice'`, followed by 0 or more tags, like this:

```
@alice^#meh^#wut
@rose^#woot^#bleh^#NOPE
@dude
@ALICE^#hope
...
```

The line is divided into parts by `'^'`. The poster and tags will not contain `'^'`, but may contain any other chars. Your code should identify the poster and tags by their position on the line, not by assuming that the first char is `'@'` or `'#'`.

We'll say a "tags" dict has a key for each tag, and its value is a nested list of the posters that posted with that tag. The list of posters should not have duplicates in it; a poster should be in the list at most once. The poster and tag names should be converted to lowercase form.

```
{
 ...
 '#meh': ['@juliette', '@alice', '@arun'],
 '#texas': ['@miguel', '@rose'],
 ...
}
```

## TipTop Output

The tiptop.py program takes a posts file as its one command line argument, reads it into the tags dict, and prints a report of all the tags. Print the tags in alphabetical order, one per line. For each tag, print its posters in alphabetical order, indented by 1 space, like this:

```bash
$ **python3 tiptop.py small.txt**
#bikelife
 @bfranklin
 @celine
 @tkirk
#bleh
 @at
 @celine
...
#whatevs
 @bob
 @sal
```

## TipTop Code

The starter file tiptop.py has the minimal structure of a Python program, but you need to design and type in the functions yourself. You should have a function that reads the posts text file into a tags dict. You should have another function that prints out the tags dict. The `main()` function should knit the two functions together. See [wordcount.zip](https://web.stanford.edu/class/cs106a/handouts_w2021/wordcount.zip) for an example of this pattern.

The functions other than `main()` should have 1-sentence """Pydoc""". Doctests are not required, but may be the easiest way to be confident that your code works correctly. Your program should be able to process these input files: test1.txt test2.txt small.txt big.txt

```bash
$ python3 tiptop.py test1.txt
#aaa
 @alice
 @bob
#bbb
 @alice
 @bob
$ **python3 tiptop.py big.txt**
#bestlife
 @alice
 @at
 @bfranklin
...
#zippy
 @bfranklin
 @bitso
 @eric27
 @jack
 @vputin
```

## All Done

Once your code is cleaned up and works right, creating order out of chaos, please turn in your tiptop.py and ghost.py files on [Paperless](https://paperless.stanford.edu) as usual.
