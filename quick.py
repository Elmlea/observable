# A quick attempt to search a known file, without functionalisation or any inputs

import re

targetList = targets = [5335, 15504, 45802, 54520, 88268, 88269, 91133, 118379, 119066, 119067,
                        119068, 119069, 119070, 134568, 135571, 144908, 149560, 160148, 380751,
                        413837, 415788, 420062, 427446, 428282, 458152, 461203, 466096, 467777,
                        469922, 475707, 476348, 476743, 477976, 478116, 481443, 481448, 489604,
                        496826, 496827, 497295, 497299, 497346, 498088, 498127, 498957, 499161,
                        499233, 499551, 500942, 501043, 504036, 504054, 504290, 504713, 504764,
                        505407, 506480, 506566, 506570, 506574, 506580, 506592, 506848, 507114,
                        507126, 507198, 507702, 508781, 509943, 509959, 510727, 511134, 512701,
                        513148, 513360, 513439, 515375, 519665, 524654, 526549, 526598, 526630,
                        526644, 526674, 526697, 526711, 526746, 526747, 526752, 526778, 526806,
                        526916, 527452, 528423, 528567, 528612, 528762, 528824, 529847, 529869,
                        529899, 529908, 530037, 530131, 530203, 530213, 530236, 530267, 530317,
                        530374, 531550, 531664, 532105, 532870, 533198, 533267, 533631, 534268,
                        534455, 534499, 534531, 534742, 534794, 534933, 535429, 535443, 535626,
                        535905, 536049, 536643, 540834, 541101]

observableFile = open("observable.txt", 'r')
observableContent = observableFile.read()
resultFile = open("results.txt", "w+")
resultList =[]

for asteroid in targetList:
    regexObject = re.compile(str(asteroid)) # Need to add \s to either side
    matchObject = regexObject.search(observableContent)
    if matchObject is not None:
        print(f"{asteroid} was found in the list")
        resultList.append(asteroid)
    else:
        print(f"{asteroid} fard & shid pant")

print(f"\nWe found {str(len(resultList))} asteroids from your data set on the observable list.")
resultFile.write(str(resultList))
resultFile.close()


