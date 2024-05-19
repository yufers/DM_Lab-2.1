def clearCallinMatrix(quineMatrix, row):
    for col in range(2, len(quineMatrix[0])):
        quineMatrix[row][col] = ''

def getConjunctiveMatrixRepresentation(quineMatrix):
    res = []
    # Обход по колонкам
    for col in range(2, len(resQuineMatrix[0])):
        counter = 0
        firstResRow = 0

        # Обход по строкам
        for row in range(1, len(resQuineMatrix) - 1):
            if (resQuineMatrix[row][col] == '+'):
                if counter == 0:
                    firstResRow = resQuineMatrix[row][0]
                else:
                    res.append({firstResRow, resQuineMatrix[row][0]})
                counter += 1

    return res

def exludeQuineCore(quineMatrix):
    resQuineMatrix = quineMatrix.copy()

    # Append additional row to store row for remove
    resQuineMatrix.append([0 for x in range (len(resQuineMatrix[0]))])

    # Обход по колонкам
    for col in range(2, len(resQuineMatrix[0])):
        counter = 0
        tmpRow = 0

        # Обход по строкам
        for row in range(1, len(resQuineMatrix) - 1):
            if (resQuineMatrix[row][col] == '+'):
                counter += 1
                tmpRow = row

        # Если в колонке всего один +, то сохраним номер строки для удаления
        if (counter == 1):
            resQuineMatrix[-1][col] = tmpRow

    for col in range(2, len(resQuineMatrix[0])):
        if (resQuineMatrix[-1][col] > 0):
            clearCallinMatrix(resQuineMatrix, resQuineMatrix[-1][col])

    return resQuineMatrix

if __name__ == "__main__":
    quineMatrix1 = [["", "", "0011", "0100", "0101", "0111", "1001", "1011", "1100", "1101"],
                   ["x1", "0-11", '+', '', '', '+', '', '', '', ''],
                   ["x2", "-011", '+', '', '', '', '', '+', '', ''],
                   ["x3", "01-1", '', '', '+', '+', '', '', '', ''],
                   ["x4", "10-1", '', '', '', '', '+', '+', '', ''],
                   ["x5", "1-01", '', '', '', '', '+', '', '', '+'],
                   ["x6", "-10-", '', '+', '+', '', '', '', '+', '+']]


    resQuineMatrix = exludeQuineCore(quineMatrix1)
    conjunctiveMatrixRepresentation = getConjunctiveMatrixRepresentation(resQuineMatrix)
    print(conjunctiveMatrixRepresentation)