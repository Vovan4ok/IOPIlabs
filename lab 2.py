import matplotlib.pyplot as plt
import math

def drawline(filewithresults):
    filewithresults.write("==============================\n")

def getinformationfromfile(filename):
    with open(filename) as file:
        marks = []
        for item in file:
            item = int(item)
            marks.append(item)
        marks.pop(0)
        marks.sort()
        return marks

def quartilesandpercantile(marks, filewithresults):
    drawline(filewithresults)

    filewithresults.write("Перший квартиль вибірки: ")
    q = math.floor(1 / 4 * (len(marks) + 1))
    Q = marks[q-1] + 1 / 4 * (marks[q] - marks[q-1])
    filewithresults.write(str(Q) + "\n")

    drawline(filewithresults)
    filewithresults.write("Третій квартиль вибірки: ")
    q = math.floor(3 / 4 * (len(marks) + 1))
    Q = marks[q-1] + 3 / 4 * (marks[q] - marks[q-1])
    filewithresults.write(str(Q) + "\n")

    drawline(filewithresults)
    filewithresults.write("90-й персантиль: ")
    p90 = math.floor(90 / 100 * (len(marks) + 1))
    P90 = marks[p90 - 1]
    filewithresults.write(str(P90) + "\n")

def averagedeviationandstandartdeviation(marks, filewithresults):
    drawline(filewithresults)
    filewithresults.write("Середнє значення вибірки: ")
    sumofallelements = 0
    for i in range(len(marks)):
        sumofallelements += marks[i]
    average = sumofallelements / len(marks)
    filewithresults.write(str(average) + "\n")

    drawline(filewithresults)
    filewithresults.write("Середнє відхилення: ")
    sum = 0
    for i in range(len(marks)):
        sum += pow(marks[i], 2)
    averagedeviation = round(sum / len(marks) - pow(average, 2), 3)
    filewithresults.write(str(averagedeviation) + "\n")

    drawline(filewithresults)
    filewithresults.write("Стандартне відхилення: ")
    standartdeviation = round(math.sqrt(averagedeviation), 3)
    filewithresults.write(str(standartdeviation) + "\n")

    return average, standartdeviation

def newmarks(marks, filewithresults, averagemark, standartdeviation):
    newmarks = []
    drawline(filewithresults)
    filewithresults.write("100 = 100a + b\n")
    filewithresults.write("95 = " + str(averagemark) + "a + b\n")
    max = 100
    newaverage = 95
    a = round((max - newaverage) / (max - averagemark), 1)
    b = round((newaverage - averagemark * a), 1)
    filewithresults.write("Формула обрахунку нової оцінки: y = " + str(a) + "x + " + str(b) + "\n")

    drawline(filewithresults)
    filewithresults.write("Вибірка нових оцінок: ")
    for i in range(len(marks)):
        if(marks[i]!=100):
            newmarks.append(round(a * marks[i] + b, 1))
        else:
            newmarks.append(marks[i])
        filewithresults.write(str(newmarks[i]) + " ")
    filewithresults.write("\n")


def stefandleamdiagram(marks, filewithresults):
    drawline(filewithresults)
    arrayofunits = []
    arrayofdozens = []
    arrayofstefsandleams = []

    for currentmark in range(len(marks)):
        if(math.floor(marks[currentmark]/10) not in arrayofdozens):
            if(currentmark > 0):
                arrayofstefsandleams.append(arrayofunits)
            arrayofunits = []
            arrayofunits.append(marks[currentmark]%10)
            arrayofdozens.append(math.floor(marks[currentmark]/10))
        else:
            arrayofunits.append(marks[currentmark]%10)
    arrayofstefsandleams.append(arrayofunits)

    filewithresults.write("Діаграма дерево-листя\n")
    for dozens in range(len(arrayofdozens)):
        filewithresults.write(str(arrayofdozens[dozens]) + str(" | "))
        for units in range(len(arrayofstefsandleams[dozens])):
            filewithresults.write(str(arrayofstefsandleams[dozens][units]) + " ")
        filewithresults.write("\n")


def boxplotdiagram(marks):
    plt.boxplot(marks)
    plt.show()
def main():
    filewithresults = open("results.txt", "w")
    filename = input()
    marks = []
    marks = getinformationfromfile(filename)
    filewithresults.write("Вхідні дані: ")
    for i in range(len(marks)):
        filewithresults.write(str(marks[i]) + " ")
    filewithresults.write("\n")
    quartilesandpercantile(marks, filewithresults)
    averagemark, standartdeviation = averagedeviationandstandartdeviation(marks, filewithresults)
    newmarks(marks, filewithresults, averagemark, standartdeviation)
    stefandleamdiagram(marks, filewithresults)
    boxplotdiagram(marks)
main()