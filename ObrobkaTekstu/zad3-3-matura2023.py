FILE_PATH = "liczby.txt"

m_numbers = []


def is_prime(x):
    if x <= 2:
        return True

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


with open(FILE_PATH) as file:
    lines = file.readlines()

    for line in lines:
        record = line.split(" ")
        m_number = int(record[0])
        m_numbers.append(m_number)


prime_count = 0

for m in m_numbers:
    if is_prime(m):
        prime_count += 1

print(prime_count)
