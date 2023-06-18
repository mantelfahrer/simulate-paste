# import
import sys


def readFilesToStringLists(file1Name: str, file2Name: str):
    # load files directly from directory
    try:
        file1 = open(file1Name)
        file2 = open(file2Name)
    except:
        raise RuntimeError("Specified file could not be found.")

    # read file content into string
    try:
        file1Content = file1.read()
        file2Content = file2.read()
    except:
        raise RuntimeError(
            "Could not read specified file. Please ensure that the file is in the correct format.")

    # close files
    file1.close()
    file2.close()

    # transfer strings to list
    file1ContentList = file1Content.splitlines()
    file2ContentList = file2Content.splitlines()

    return file1ContentList, file2ContentList


def getMaxLineWidth(string1: str, string2: str):
    if len(string1) > len(string2):
        return len(string1)
    else:
        return len(string2)


def paste(file1StringList: list, file2StringList: list):
    # check argument type
    if not isinstance(file1StringList, list) or not isinstance(file2StringList, list):
        raise TypeError("Arguments must be of type List.")

    # determine longest string
    maxStringLength = 0
    for i in range(0, len(file1StringList)):
        if len(file1StringList[i]) > maxStringLength:
            maxStringLength = len(file1StringList[i])

    # print
    for i in range(0, len(file1StringList)):
        print(f"{file1StringList[i]:{maxStringLength}}",
              f"{file2StringList[i]}")


def paste_d(file1StringList: list, file2StringList: list, separator: str):
    # check argument type
    if not isinstance(file1StringList, list) or not isinstance(file2StringList, list):
        raise TypeError("The first two arguments must be of type List.")
    if not isinstance(separator, str):
        raise TypeError("The third argument must be of type String.")

    # print
    for i in range(0, len(file1StringList)):
        print(f"{file1StringList[i]}", f"{file2StringList[i]}", sep=separator)


def paste_s(file1StringList: list, file2StringList: list):
    # check argument type
    if not isinstance(file1StringList, list) or not isinstance(file2StringList, list):
        raise TypeError("The first two arguments must be of type List.")

    # print
    for i in range(0, len(file1StringList)):
        if i < len(file1StringList) - 1:
            print(
                f"{file1StringList[i]:{getMaxLineWidth(file1StringList[i], file2StringList[i])}}", end=" ")
        else:
            print(
                f"{file1StringList[i]:{getMaxLineWidth(file1StringList[i], file2StringList[i])}}")
    for i in range(0, len(file2StringList)):
        if i < len(file1StringList) - 1:
            print(
                f"{file2StringList[i]:{getMaxLineWidth(file1StringList[i], file2StringList[i])}}", end=" ")
        else:
            print(
                f"{file2StringList[i]:{getMaxLineWidth(file1StringList[i], file2StringList[i])}}")

# main


def main():
    try:
        # determine number of arguments passed
        argumentsLength = len(sys.argv)
        optionD = False
        optionS = False

        if argumentsLength < 3:
            raise RuntimeError("At least two arguments must be passed.")

        if sys.argv[1] == "-s":
            optionS = True
        elif sys.argv[1] == "-d":
            optionD = True
            separator = sys.argv[2]

        if optionS and argumentsLength < 4:
            raise RuntimeError(
                "When using the -s option, it must be followed by two filenames.")
        elif optionD and argumentsLength < 5:
            raise RuntimeError(
                "When using the -d option, it must be followed by a seperator and two filenames.")

        # read files into string lists
        if optionD:
            file1ContentList, file2ContentList = readFilesToStringLists(
                sys.argv[3], sys.argv[4])
        elif optionS:
            file1ContentList, file2ContentList = readFilesToStringLists(
                sys.argv[2], sys.argv[3])
        else:
            file1ContentList, file2ContentList = readFilesToStringLists(
                sys.argv[1], sys.argv[2])

        # print
        if optionD:
            paste_d(file1ContentList, file2ContentList, separator)
        elif optionS:
            paste_s(file1ContentList, file2ContentList)
        else:
            paste(file1ContentList, file2ContentList)

    except RuntimeError as e:
        print("Error:", e)
    except TypeError as e:
        print("TypeError:", e)


# execute main function
if __name__ == '__main__':
    main()
