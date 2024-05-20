from itertools import combinations

def is_covering_all(implicants, minterms):
    covered = set()
    for imp in implicants:
        for minterm in minterms:
            if covers(imp, minterm):
                covered.add(minterm)
    return covered == set(minterms)

def covers(implicant, minterm):
    for imp_bit, min_bit in zip(implicant, minterm):
        if imp_bit != '-' and imp_bit != min_bit:
            return False
    return True

def find_prime_implicants(implicants, minterms):
    subsets = []
    for r in range(1, len(implicants) + 1):
        for subset in combinations(implicants, r):
            if is_covering_all(subset, minterms):
                subsets.append(subset)
    return subsets

# Пример данных
implicants = ["0-11", "-011", "01-1", "10-1", "1-01", "-10-"]
minterms = ["0011", "0100", "0101", "0111", "1001", "1011", "1100", "1101"]

# Нахождение подмножеств
prime_subsets = find_prime_implicants(implicants, minterms)
for subset in prime_subsets:
    print(subset)
