import matplotlib.pyplot as plt
import math

def drawline(filewithresults):
    filewithresults.write("====================================================\n")

def getinformationfromfile(filename, numberoffilms):
    with open(filename) as file:
        array = []
        for item in file:
            item = int(item)
            array.append(item)
        numberoffilms = array.pop(0)
        array.sort()
        return array, numberoffilms

def moda(array, arrayoffrequencies, arraywithuniqueelements):
    moda = []
    maxfrequency = max(arrayoffrequencies)
    newmax = maxfrequency
    copyarray = []

    for i in range(len(arrayoffrequencies)):
        copyarray.append(arrayoffrequencies[i])

    i = 0
    while(newmax == maxfrequency):
        if(i>0):
            moda.append(arraywithuniqueelements[copyarray.index(newmax) + i])
        else:
            moda.append(arraywithuniqueelements[copyarray.index(newmax)])
        copyarray.pop(copyarray.index(newmax))
        newmax = max(copyarray)
        i += 1
    return moda

def frequencies(filewithresults, array):
    arraywithuniqueelements = []
    arrayoffrequencies = []
    quantity = 0
    cumulativefrequency = 0
    filewithresults.write("Завдання 1\n")
    filewithresults.write("Фільм\tЧастота\tСукупна частота\n")
    for i in range(len(array)):
        if array[i] not in arraywithuniqueelements:
            arrayoffrequencies.append(quantity)
            quantity = 1
            arraywithuniqueelements.append(array[i])
        else:
            quantity += 1
    arrayoffrequencies.append(quantity)
    arrayoffrequencies.pop(0)

    for i in range(len(arraywithuniqueelements)):
        cumulativefrequency += arrayoffrequencies[i]
        filewithresults.write(str(arraywithuniqueelements[i]) + "\t" + str(arrayoffrequencies[i]/len(array)*100)+"%" + "\t" + str(cumulativefrequency) + "\n")

    maximum = moda(array, arrayoffrequencies, arraywithuniqueelements)

    filewithresults.write("Фільм(и) з найбільшою кількістю переглядів: ")
    for i in range(len(maximum)):
        filewithresults.write(str(maximum[i]) + " ")
    filewithresults.write("\n")
    drawline(filewithresults)
    return arraywithuniqueelements, arrayoffrequencies, maximum

def modaandmediana(array, moda, arraywithuniqueelements, filewithresults):
    filewithresults.write("Завдання 2\n")
    filewithresults.write("Мода вибірки: ")

    if(len(moda) == len(arraywithuniqueelements)):
        filewithresults.write("немає\n")
    else:
        for i in range(len(moda)):
            filewithresults.write(str(moda[i])+" ")
    filewithresults.write('\n')
    filewithresults.write("Медіана: ")
    if(len(array)/2==0):
        mediana = (array[len(array)/2]+array[len(array)/2-1])/2
    else:
        mediana = array[round(len(array)/2) - 1]
    filewithresults.write(str(mediana) + "\n")
    drawline(filewithresults)
def dispersionanddeviation(array, arraywithuniqueelements, arrayoffrequencies, filewithresults):
    filewithresults.write("Завдання 3\n")
    sumofallelements = 0
    for i in range(len(arraywithuniqueelements)):
        sumofallelements += arraywithuniqueelements[i] * arrayoffrequencies[i]
    average = sumofallelements/len(array)
    filewithresults.write("Середнє значення вибірки: " + str(average) + "\n")

    sum = 0
    for i in range(len(arraywithuniqueelements)):
        sum += arrayoffrequencies[i] * pow(arraywithuniqueelements[i], 2)
    dispersion = round(sum / len(array) - pow(average, 2), 3)
    deviation = round(math.sqrt(dispersion), 3)
    filewithresults.write("Дисперсія: " + str(dispersion) + "\nСтандартне квадратичне відхилення: " + str(deviation) + "\n")
    drawline(filewithresults)
def gistograma(array, numberoffilms):
    plt.figure()
    range1 = []
    for i in range(numberoffilms * 10):
        range1.append(i)
    plt.hist(array, range1)
    plt.title("Гістограма частот")
    plt.show()
def main():
    filewithresults = open("results.txt", "w")
    filename = input()
    numberoffilms = 0
    array, numberoffilms = getinformationfromfile(filename, numberoffilms)
    filewithresults.write("Вхідні дані: ")
    for i in range(len(array)):
        filewithresults.write(str(array[i]) + " ")
    filewithresults.write("\n")
    arraywithuniqueelements, arrayoffrequencies, moda = frequencies(filewithresults, array)
    modaandmediana(array, moda, arrayoffrequencies, filewithresults)
    dispersionanddeviation(array, arraywithuniqueelements, arrayoffrequencies, filewithresults)
    gistograma(array, numberoffilms)
main()