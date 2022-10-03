FILE_PATH = "liczby.txt"

data = []


def nwd(a, b):
    if a < b:
        bufor = a
        a = b
        b = bufor

    last_nwd = b
    remainder = a % b

    while remainder > 0:
        last_nwd = remainder
        a = b
        b = remainder

        remainder = a % b

        if remainder == 0:
            last_nwd = b
            break

    return last_nwd


with open(FILE_PATH) as file:
    lines = file.readlines()

    for line in lines:
        line = line.replace("\n", "")
        line = line.split(" ")
        data.append(line)


count = 0
for record in data:
    m = int(record[0])
    a = int(record[1])

    if nwd(m, a) == 1:
        count += 1

print(count)
