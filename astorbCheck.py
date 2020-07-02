import re

# open all the files, and pull the content from the pho file
astorb = open("astorb.txt")
pho = open("pho.txt")
phoContent = pho.read()
results = open("phoResult.txt", 'w+')

# generate a regex to find the 6-digit bracketed ID number of the pho
phoRegex = re.compile(r'\(\d{6}\)')
# find all matches for the regex and place them in a list using the findall method
phoMatch = phoRegex.findall(phoContent)

print(phoMatch) # debug

# generate a blank list, split the brackets off, and fill the list with the raw ID numbers
phoList = []
for asteroid in phoMatch:
    asteroid = asteroid[1:-1]
    phoList.append(asteroid)

print(phoList) # debug

# truncate the astorb list to something more useful


# generate a blank list for the phos found in the astorb list, and a "fail" list
astorbList = []
failList = []



for asteroid in phoList:
    astorbRegex = re.compile(asteroid)
    astorbMatch = astorbRegex.search(astorbContent)
    if astorbMatch is not None:
        print(f"Found {asteroid} in the astorb")
        astorbList.append(asteroid)
    else:
        print(f"{asteroid} was not found.")
        failList.append(asteroid)

results.write(str(astorbList))
results.close()
print(failList)
