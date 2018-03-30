# CS693-metrics-project
This project is written and tested using Python 3.6.4 on Ubuntu.

## Running Tests
Currently, Tests can only be run for one test file at a time. 

Example: `python TestLOC.py`

A -v flag may be added for verbose output.

## Metrics
### Lines of Code (LOC)
This is a count of the lines in the given source code. All lines inside of a block comment are counted as comments even if they would be counted as a blank line or import statement outside of the comment block. Accurate calculation of this metric is subject to the following limitations:

* The """ starting a block comment must be the first thing other than whitespace on the line
* The """ ending a block comment must be the last thing other than whitespace on the line

| Parameter name | Possible Values | Default Value | Explaination |
| -------------- | --------------- | ------------- | ------------ |
| Comments       | On, Off         | Off           | Should comments be counted? This includes single line comments starting with # (with no preceeding code) and block comments surrounded by """. |
| Empty Lines    | On, Off         | Off           | Should lines containing only whitespace be counted? |
| Import Statements | On, Off      | On            | Should import statements such as `import FOO` or  `from FOO import BAR` be counted? |


##Credits
* test/files/sample1.py - Adapted from SampleIncludingAll1.py provided by Dr. Huseyin Ergin