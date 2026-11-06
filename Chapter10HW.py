#problem1 
def amortization():
    p0 = float(input("Enter the amount financed: "))
    r = float(input("Enter the annual interest rate as a decimal: "))
    n = int(input("Enter the number of years: "))

    k = 12
    rate = r / k
    total_payments = n * k

    payment = p0 * rate / (1 - (1 + rate) ** (-total_payments))
    balance = p0

    filename = input("Enter the output filename: ")

    with open(filename, "w") as outfile:
        print("Payment\tPayment Amount\tInterest\tPrincipal\tBalance",
              file=outfile)

        for number in range(1, total_payments + 1):
            interest = balance * rate
            principal = payment - interest
            balance = balance - principal

            if balance < 0:
                balance = 0

            print(number,
                  f"${payment:.2f}",
                  f"${interest:.2f}",
                  f"${principal:.2f}",
                  f"${balance:.2f}",
                  sep="\t",
                  file=outfile)

    print("Amortization report saved to", filename)

def main():
    amortization()

if __name__ == "__main__":
    main()

#problem 2
def readPath(filename):
    path = []

    with open(filename, "r") as infile:
        dimensions = infile.readline().split()
        rows = int(dimensions[0])
        columns = int(dimensions[1])

        for line in infile:
            values = line.split()

            if len(values) == 2:
                row = int(values[0])
                col = int(values[1])
                path.append((row, col))

    return rows, columns, path

def createGrid(message, rows, columns):
    message = message.upper().replace(" ", "")
    message = message.ljust(rows * columns, "X")

    grid = []
    position = 0

    for row in range(rows):
        current_row = []

        for col in range(columns):
            current_row.append(message[position])
            position = position + 1

        grid.append(current_row)

    return grid

def encrypt(message, rows, columns, path):
    grid = createGrid(message, rows, columns)
    ciphertext = ""

    for row, col in path:
        ciphertext = ciphertext + grid[row][col]

    return ciphertext

def decrypt(ciphertext, rows, columns, path):
    grid = [[""] * columns for row in range(rows)]

    position = 0

    for row, col in path:
        grid[row][col] = ciphertext[position]
        position = position + 1

    message = ""

    for row in range(rows):
        for col in range(columns):
            message = message + grid[row][col]

    return message.rstrip("X")

def main():
    filename = input("Enter the path filename: ")

    rows, columns, path = readPath(filename)

    message = input("Enter the message: ")

    encrypted = encrypt(message, rows, columns, path)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, rows, columns, path)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()

#problem 3
from graphics import *

def getFrequencies(text):
    counts = [0] * 26
    total = 0

    text = text.lower()

    for char in text:
        if char >= "a" and char <= "z":
            position = ord(char) - ord("a")
            counts[position] = counts[position] + 1
            total = total + 1

    frequencies = []

    for count in counts:
        if total > 0:
            frequencies.append(count / total)
        else:
            frequencies.append(0)

    return frequencies

def drawGraph(frequencies):
    win = GraphWin("Letter Frequency Analysis", 700, 500)

    highest = max(frequencies)

    if highest == 0:
        highest = 1

    win.setCoords(0, 0, 27, highest * 1.2)

    for i in range(26):
        x = i + 0.5
        bar_height = frequencies[i]

        bar = Rectangle(Point(x, 0), Point(x + 0.7, bar_height))
        bar.setFill("blue")
        bar.draw(win)

        label = Text(Point(x + 0.35, -0.02 * highest), chr(i + 97))
        label.draw(win)

    win.getMouse()
    win.close()

def main():
    filename = input("Enter the text filename: ")

    with open(filename, "r") as infile:
        text = infile.read()

    frequencies = getFrequencies(text)

    for i in range(26):
        print(chr(i + 97), ":", frequencies[i])

    drawGraph(frequencies)

if __name__ == "__main__":
    main()


#problem 4
from graphics import *
from pathlib import Path

def getFrequencies(text):
    counts = [0] * 26
    total = 0

    text = text.lower()

    for char in text:
        if char >= "a" and char <= "z":
            position = ord(char) - ord("a")
            counts[position] = counts[position] + 1
            total = total + 1

    frequencies = []

    for count in counts:
        if total > 0:
            frequencies.append(count / total)
        else:
            frequencies.append(0)

    return frequencies

def readPythonFiles(directory):
    path = Path(directory)
    text = ""

    for filename in path.glob("*.py"):
        if filename.is_file():
            with open(filename, "r") as infile:
                text = text + infile.read()

    return text

def drawGraph(frequencies):
    win = GraphWin("Python Code Frequency", 700, 500)

    highest = max(frequencies)

    if highest == 0:
        highest = 1

    win.setCoords(0, 0, 27, highest * 1.2)

    for i in range(26):
        x = i + 0.5

        bar = Rectangle(
            Point(x, 0),
            Point(x + 0.7, frequencies[i])
        )

        bar.setFill("blue")
        bar.draw(win)

        Text(Point(x + 0.35, -0.02 * highest),
             chr(i + 97)).draw(win)

    win.getMouse()
    win.close()

def main():
    directory = input("Enter the directory containing Python files: ")

    text = readPythonFiles(directory)
    frequencies = getFrequencies(text)

    for i in range(26):
        print(chr(i + 97), ":", frequencies[i])

    drawGraph(frequencies)

if __name__ == "__main__":
    main()

#problem 5
from graphics import *
from urllib.request import urlopen

def getFrequencies(url):
    counts = [0] * 256
    total = 0

    with urlopen(url) as infile:
        text = infile.read().decode("utf-8")

    text = text.lower()

    for char in text:
        value = ord(char)

        if value < 256:
            counts[value] += 1
            total += 1

    frequencies = []

    for i in range(26):
        letter_count = counts[ord("a") + i]

        if total > 0:
            frequencies.append(letter_count / total)
        else:
            frequencies.append(0)

    return counts, frequencies


def drawGraph(frequencies):
    win = GraphWin("Internet Text Frequency", 700, 500)

    highest = max(frequencies)

    if highest == 0:
        highest = 1

    win.setCoords(0, -highest * 0.05, 27, highest * 1.2)

    for i in range(26):
        x = i + 0.5

        bar = Rectangle(Point(x, 0), Point(x + 0.7, frequencies[i]))
        bar.setFill("blue")
        bar.draw(win)

        label = Text(Point(x + 0.35, -highest * 0.02), chr(i + 97))
        label.draw(win)

    win.getMouse()
    win.close()


def saveFrequencies(counts, filename):
    with open(filename, "w") as outfile:
        for i in range(26):
            letter = chr(ord("a") + i)
            count = counts[ord(letter)]
            print(letter, count, file=outfile)


def main():
    url = input("Enter the URL of the text file: ")

    counts, frequencies = getFrequencies(url)

    filename = input("Enter the output filename: ")

    saveFrequencies(counts, filename)

    print("Frequency data saved to", filename)

    drawGraph(frequencies)


if __name__ == "__main__":
    main()