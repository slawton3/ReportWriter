import pandas as pd
from datetime import datetime
from tabulate import tabulate

"""These three libraries need to be installed/imported for the program to function"""


class ExpenseFile():

    def __init__(self, fileName):
        """Initializes an instance of the Expense File class"""
        self.fileName = fileName
        self.df = pd.read_csv(self.fileName, sep='\t')
        self.lst = []

    def getColumns(self):
        """Returns a list of column names from the expense data"""
        columnNames = self.df.columns
        for i in columnNames:
            self.lst.append(i)
        return self.lst


    def getRowCount(self):
        """Gets number of line items in the report excluding the header column"""
        return len(self.df)


    def sumExpenses(self):
        """Gets the total sum of expenses"""
        total = round(self.df['Amount'].sum(), 2)
        return total


    def paymentMethod(self):
        """Stores unique payment methods as dictionary keys with count of times used as values"""
        myDict = self.df['Institution'].value_counts().to_dict()
        return myDict


    def expenseDrillDown(self):
        """Returns an ascii table of expense descriptions and amount spent"""
        categories = self.df['Category'].unique()
        drillDownDict = self.df.groupby(['Category'])['Amount'].sum().to_dict()
        df2 = pd.Series(drillDownDict).to_frame()

        return tabulate(df2, headers=['Category', 'Amount'], tablefmt="grid")


def timeFormatting():
    """This function timestamps the report and formats it into common."""
    now = datetime.now()
    global dateFormat
    global timeFormat
    dateFormat = datetime.strftime(now, "%m/%d/%y")
    timeFormat = datetime.strftime(now, "%H:%M:%S")
    return dateFormat, timeFormat


def outputExpenseReport(dateFormat, timeFormat):
    """This function generates a human readable report from the initial expense data."""
    x = ExpenseFile('expenseData.txt')
    drillDown = x.expenseDrillDown()
    paySum = x.sumExpenses()
    totalLines = x.getRowCount()
    currency = "${:,.2f}".format(paySum)
    methods = x.paymentMethod()

    """This part of the function outputs all data to the text file and closes the file."""
    with open("../expenseReport.txt", "w") as outFile:
        # Writing data to a file
        outFile.write("Expense report generated on " + str(dateFormat) + " at " + str(timeFormat) + ". \n\n\n")
        outFile.write("The number of line items from the expense data is " + str(totalLines) + ". \n\n\n")
        outFile.write("The total sum of expenses for this period is " + str(currency) + ". \n\n\n")
        outFile.write("Expense Breakdown Table: \n")
        outFile.write(str(drillDown))
        outFile.write("\n\n\n")
        outFile.write("Payment methods ordered by times used descending: \n")
        for i, j in methods.items():
            outFile.write(str(i) + ": " + str(j) + "\n")
        outFile.close()


def main():
    """This is the main function that executes the program in order."""
    timeFormatting()
    outputExpenseReport(dateFormat, timeFormat)


main()