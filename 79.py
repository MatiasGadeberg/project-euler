with open("p079_keylog.txt", "r") as file:
    
    data = file.readlines()
    data = [line.rstrip() for line in data]

passdict = {}

for i in range(10):
    passdict['{}'.format(i)] = {
        "before": [],
        "after": []
    }

for line in data:
    first = str(line[0])
    mid = str(line[1])
    last = str(line[2])

    #Add mid and last number to "after" if not allready there
    if not mid in passdict[first]["after"]:
        passdict[first]["after"].append(mid)
    if not last in passdict[first]["after"]:
        passdict[first]["after"].append(last)

    #Add first number to "before" and last number to "after" if not allready there
    if not first in passdict[mid]["before"]:
        passdict[mid]["before"].append(first)
    if not last in passdict[mid]["after"]:
        passdict[mid]["after"].append(last)

    if not first in passdict[last]["before"]:
        passdict[last]["before"].append(first)
    if not mid in passdict[last]["before"]:
        passdict[last]["before"].append(mid)

noshow = []
for item in passdict:

    if passdict[item]["before"] == [] and passdict[item]["after"] == []:
        noshow.append(item)

for num in noshow:
    del passdict[num]

passkey = []

while not passdict == {}:
    for item in passdict:
        if passdict[item]["before"] == []:
            nextkey = item
    passkey.append(nextkey)
    del passdict[nextkey]

    for item in passdict:
        passdict[item]["before"].remove(nextkey)
    
print(passkey)