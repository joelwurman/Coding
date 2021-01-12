GeneticCode = f'''
    UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G '''

for string in range(len(GeneticCode)):
    GeneticCode.replace('  ', '')

print(GeneticCode)

# GeneticCode.split(' ')
#
# without_empty_strings = []
# for character in GeneticCode:
#     if character != '\n':
#         without_empty_strings.append(character)
#
# GeneticCode = ' '.join(without_empty_strings)
# without_empty_strings = []
#
# for character in GeneticCode:
#     if character != ' ':
#         without_empty_strings.append(character)
# print(without_empty_strings)
#
# RNAtoProt_Dic = []
#
# # n = 0
# # RNAtoProt_Dic = GeneticCode.split(' ')
# # RNAtoProt_Dic.remove()
# # print(RNAtoProt_Dic)
