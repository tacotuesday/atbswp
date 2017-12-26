tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

for i in range(len(tableData)):
    tableData[i].sort(key=len)
    colWidths[i] = len(tableData[i][-1])
    justifyBase = int(max(colWidths)) + 1

for i in range(len(tableData)):
    print(str(tableData[i]).rjust(justifyBase))
