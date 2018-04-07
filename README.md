# CS693-metrics-project
This project is written and tested using Python 3.6.4 on Ubuntu.

## Running Tests
1. Switch to the root directory of the project.
1. `python3.6 -m unittest discover`
1. Optional: Add `-v` to the command for verbose output

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

### Lack of Cohesion Metric 4 (LCOM4)
This is an improved version of the LCOM which is introduced by Chidamber and Kemerer. In this metric,
methods ‘a’ and ‘b’ are related if they both access the same class-level variable or ‘a’ calls ‘b’ or ‘b’ calls
‘a’. After determining the related methods, the number of separate connected groups will give the
LCOM4 number of the class. The `__init__` method is not considered in calculation of this metric. 

No parameters are available for this metric.

### Coupling Between Objects (CBO)
This counts the number of connections between two classes.  Therefore it is only applicable for a pair of classes.
CBO is calculated for each pair of classes in the input.

Two classes are coupled when methods declared in one class use methods or instance variables defined by the other class.
The uses relationship can go either way: both used and used-by relationships are taken into account, but only once.
Only method class and variable references are counted.

No parameters are available for this metric.

#### Known Limitations
 - An instance varable or local variable must be instantiated using the constructor of its class for the calculation to identify it as that type.
 - Variables that change type cannot be handled.


### Depth of Inheritance Tree (DIT)
 This calculates the number of superclasses for each class. A class 'A' may be extending class 'B' and 'B' may be extending class 'C'. Assuming
 no other extends, the DITs of 'A', 'B', and 'C' are respectively 2, 1, 0. The parameter is including the object class or not, which is the base of all
 classes, sometimes omitted but sometimes included.  This increases the number of DIT by 1 if object is included and the parameter is set to On.

| Parameter name | Possible Values | Default Value | Explaination |
| -------------- | --------------- | ------------- | ------------ |
| object class      | On, Off         | Off           | The class 'object' is the root of all classes in python. |

#### Known Limitations
 - Multiple inheritance is not fully supported. If the inheritance tree includes a class with multiple base classes, DIT will be calculated for one branch 
 of the tree. There is no guarantee as to the branch that will be selected.

### Number of Children (NOC)
This is the number of immediate subclasses for each class. A class 'A' may be extended by classes 'B' and 'C'. Assuming there are no other classes extending 'A', and 'B' and 'C' are not extended by any other class, the NOCs of 'A', 'B', 'C' ar respectively 2,0,0. 

No parameters are available for this metric.

### Weighted Methods Per Class (WMC)
This is the number of methods for each class.  The parameter specifies whether to include the constructor or not.

| Parameter name | Possible Values | Default Value | Explaination |
| -------------- | --------------- | ------------- | ------------ |
| Constructor     | On, Off         | Off           | Constructor in python is used to instantiate an object and is the method with the name `__init__`. |

##Credits
* test/files/sample1.py - Adapted from SampleIncludingAll1.py provided by Dr. Huseyin Ergin