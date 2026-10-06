import ast

# This function takes a string and counts repeating characters.
# It returns a list of tuples.

def encodeString(letters): 
    if letters == "":
        return []
    currentChar = None 
    result = []
    count = 1

    for char in letters: 
        if char != currentChar: 
            if currentChar is not None:
                result.append((currentChar, count))
            currentChar = char
            count = 1
        else:
            count = count + 1

    result.append((currentChar, count))
    return result


# This function takes tuples and rebuilds the original string.

def decodeString(decodeletters):
    result = ""

    for char in decodeletters:
        result = result + char[0] * char[1]

    return result 


# This function reads a text file, encodes the contents, and saves the encoded version to a new file.

def encodeFile(filename, newFilename):
    with open(filename, "r") as openedFile:
        content = openedFile.read()

    encoded = encodeString(content)

    with open(newFilename, "w") as newFile:
        newFile.write(str(encoded))


# This function reads an encoded file, decodes it, and returns the original text.

def decodeFile(filename): 
    with open(filename, "r") as openedFile:
        content = openedFile.read()

    real = ast.literal_eval(content)
    original = decodeString(real)

    return original


# Example tests

print("These are the encoded tuples")
print(encodeString("AAABBBdddd"))

print("These are the decoded tuples")
print(decodeString([('A', 4), ('b', 8)]))
