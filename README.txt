# Final Project Description

This project is designed to take an expense file (.txt) and output a text file report.

The expenseData.txt is a text file, tab delimited. This file contains raw data to be parsed by the program.

The ExpenseFile class has multiple methods that can be called to extract data from the report and
return meaningful analysis for decision makers in an organization.

One of the functions also outputs a tabulated table of data that groups by the expense categories
and sums the amount for each.

There are two other functions in the program.  One of the functions timestamps when the program was run
and the other writes human readable analysis output to a text file.

## Requirements

In order to run this program, one must have Python 3.8+ installed.

The Python libraries of datetime, Pandas and Tabulate must also be installed to your environment.
Pip is the package installer for Python so I highly recommend using this tool.
I use a pipenv virtual environment and run the 

[python3]

[pip3]

## Installation

[pip3 install -r requirements.txt]

## Running the program

Make sure that you have saved the supplied expenseData.txt file saved in your working directory.
The program checks the directory for a specific file name so it is imperative to have both the 
final.py file and expenseData.txt file saved in the same directory.

When you are ready to execute the program, open the command line and navigate to the directory and run:

[python3 final.py]