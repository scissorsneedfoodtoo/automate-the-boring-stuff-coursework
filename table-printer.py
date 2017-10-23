tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],]

# def printTable(userTables):
#     colWidths = [0] * len(userTables) # list containing inner list for each found in tableData
#     output = ''
#
#     for i in range(len(userTables[0])):
#         for n in range(len(userTables)):
#             colWidths[n] = len(max(userTables[n], key=len))
#             output = userTables[n][i]
#             print(output.rjust(colWidths[n]), end=" ")
#         print("\n")

def printTable(userTables):
    colWidths = [0] * len(userTables)
    output = ''

    for i, record in enumerate(userTables):
        for item in record:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)

    for i in range(len(userTables[0])):
        for n in range(len(userTables)):
            print(userTables[n][i].rjust(colWidths[n]), end=" ")
        print("\n")

printTable(tableData)
