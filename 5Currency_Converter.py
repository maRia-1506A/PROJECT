with open("5Currency_Converter.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parts = line.split("\t")

    currencyDict[parts[0]] = parts[1]

amount = int(input("Enter the amount: "))
print("Available options:\n")
for item in currencyDict.keys():
    print(item)

target = input("Target currencry: ")
rate = float(currencyDict.values)
result = target*rate
print(f"{amount} is equal to {result}")
