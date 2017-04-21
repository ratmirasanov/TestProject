#Reading CSV-file to list of lists.
import csv
exampleFile = open('Sacramentorealestatetransactions.csv', 'rU')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


#Declaration of variables.
i = 0
listWithPrices = []
listWithSquareFootage = []


#Creation of two lists.
for row in exampleData:
        listWithPrices.append(exampleData[i][9])
        listWithSquareFootage.append(exampleData[i][6])
        i += 1


#Remove the first element of the each list.
listWithPrices.remove('price')
listWithSquareFootage.remove('sq__ft')


#Converting string-list to int-list.
for index, elem in enumerate(listWithPrices):
                listWithPrices[index] = int(elem)

for index, elem in enumerate(listWithSquareFootage):
                listWithSquareFootage[index] = int(elem)


#Calculations.
maxPriceOfRealEstate = max(listWithPrices)
minPriceOfRealEstate = min(listWithPrices)
averageSquareFootage = sum(listWithSquareFootage) / len(listWithSquareFootage)
averagePrice = sum(listWithPrices) / len(listWithPrices)


#Printing results.
print('Max price of real estate -- ' + str(exampleData[listWithPrices.index(maxPriceOfRealEstate)+1])
      + ' is: ' + str(maxPriceOfRealEstate) + '$.')
print('Min price of real estate -- ' + str(exampleData[listWithPrices.index(minPriceOfRealEstate)+1])
      + ' is: ' + str(minPriceOfRealEstate) + '$.')
print('Average square footage is -- ' + str(averageSquareFootage) + ' square foots.')
print('Average price is -- ' + str(averagePrice) + '$.')