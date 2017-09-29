salesTotal = 0.0
oldKey = None

# Loop around the data
# It will be in the format key \t val as outputted from the mapper (and also sorted)
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    dataMapped = line.strip().split("\t")
    if len(dataMapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = dataMapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    # converting to float is necessary because thisSale is a string.

if oldKey != None:
    print oldKey, "\t", salesTotal

