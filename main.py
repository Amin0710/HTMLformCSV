import csv
import pandas as pd

csvFileName = "340104.csv"


def GeneratePage(pName):
    ##open new HTML file
    myfile = open(pName + ".html", "w")
    myfile.write("<html>\n")
    myfile.write("<head><title>" + pName + "</title></head>\n")
    myfile.write("<body>")
    ##read the csv file
    df = pd.read_csv(csvFileName)

    ##get the country names
    country_names = list(df.columns.values)
    ##calculate teh total movments by country
    for country in country_names[1:]:
        myfile.write("<p>Country Name: " + country + "</br>")
        myfile.write("Total number of Movnement: " + str(df[country].sum()))
        myfile.write("</p><hr>")

    myfile.write("</body>\n")
    myfile.write("</html>")
    myfile.close()


#################Main########
file = open("PageLists.csv", "r")
reader = csv.reader(file)

myfile = open("index.html", "w")

myfile.write("<html>\n")
myfile.write("<head><title><My first html page</title></head>\n")
myfile.write("<body style='background-color: #dOe4fe;'>\n")
myfile.write("<h1>Welcome</h1></br>\n")

for row in reader:
    myfile.write("<a style='font-family:arial;font-size:18pt;font-weight:bold'"
                 "onmouseout='this.style.color=\"OOOOOO\"'"
                 "onmouseover='this.style.color=\"#ffOOOO\"'"
                 "href='" + row[1] + ".html'>" + row[0] + "</a></br>\n")
    GeneratePage(row[1])

##with open('PageLists.csv') as csv_file:
##    csv_reader = csv.reader(csv_file)
##    rows = list(csv_reader)

##GeneratePage(rows[0][1])


myfile.write("</body>\n")
myfile.write("</html>")
myfile.close()