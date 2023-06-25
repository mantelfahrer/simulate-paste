# Simulate paste (Unix)

## Description

This is a small repository that was created in the course of my studies at the university. It is aimed at simulating or recreating the features of the Unix paste tool with Python, to merge corresponding or subsequent lines of files.

## How it works
Suppose we have a file "names.txt" with the following content:

```
Mark Smith
Bobby Brown
Sue Miller
Jenny Igotit
```

and a file "numbers.txt" with the following content:

```
555-1234
555-9876
555-6743
876-5309
```
The call
```
$ python paste.py names.txt numbers.txt
```
returns the formatted output
```
Mark Smith   555-1234
Bobby Brown  555-9876
Sue Miller   555-6743
Jenny Igotit 867-5309
```

## How to use
`python paste.py [-s] [-d list] file1 file2`

### Options
The options are as follows:

Option | Description
--- | ----
-s | (serialize) presents the information in a horizontal fashion
-d *character/string* | (delimiter) Uses the character or string following the `-d` as delimiter

### Examples
The following example shows the output of paste with the option ```-s``` presententing the information in a horizontal fashion:
```
$ python paste.py -s names.txt numbers.txt
Mark Smith Bobby Brown Sue Miller Jenny Igotit
555-1234   555-9876    555-6743   867-5309
```

The following example shows the output of paste with the option ```-d``` which uses the character `:` as delimiter:
```
$ python paste.py -d : names.txt numbers.txt
Mark Smith:555-1234
Bobby Brown:555-9876
Sue Miller:555-6743
Jenny Igotit:867-5309
```