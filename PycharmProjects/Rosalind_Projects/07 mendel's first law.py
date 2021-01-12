# k = homozygous dominant
# m = heterozygous
# n = homozygygous recessive

k, m, n = 27, 22, 30
p = k + m + n

ProbOfHavingOnlyRecAlleles = ((n / p) * ((n - 1) / (p - 1))) + ((n / p) * (m / (p - 1)) * 0.5) + (
        (m / p) * (n / (p - 1)) * 0.5) + (m / p * ((m - 1) / (p - 1) * 0.25))

ProbOfHavingOneDomAllele = 1 - ProbOfHavingOnlyRecAlleles
print(ProbOfHavingOneDomAllele)
