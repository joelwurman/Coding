from Genetic_Code_dictionary import RNA_to_Aminoacid

RNA = """AUGUCGCGAAUUGUCGAGGGUAACGCUCGCUUACACGUCCUCCUUCAUCCGAAAUUACUCCGUGUUGCAGAUGGCCUAUUCAAGCAUAGUACGUCGGUCGUGCAGAUCGCCCACGGGCUUAGCACGUGGAAUAACAGUCGUGAUAAGUCCCGUCCGGGGGUCAGGCUAACAGCACUAAGACUUUUGUUCCGGACCCCCAGAAUAGUGCGACCCCGACGGUACCAUUCCGUUUAUGGUACGUGCCGCUCAGCGUCGUUGUCUACGCGAGGUAGCGAUGUCGUAGUAGCGGUACGGGAUGACGCACAUGCCAUUCCUCAAUGGCGAUCACCGCUGCGAUCGUAUGUGACGAUAGGGAUCUCCAUCGAAAGCCUCCUUACCCGCCAUAUCGUACGAUAUCAAAAACACCUGGCAGUGCUGUCUCAACCUUCAGCGAAGUUGAUGCAGAACCAGGGGGUCUGCUCACCGAAGCUGCGUUAUCCGAAGACCCUACGUGCGACCAGCUACAGGGAGUGUAAUUACGGGAAAAAUCCCCUUCUUAACUAUGUGCUAUCUGAGGGGUGCGGGUCAAAGGUUCCCCGAAGUGACAGCCUUGGACUCUUUAGCGAAUCUGAAAACACUGGACUCCGAGUCUCCCCUGCCCCGCAGCAGGAGAAGGUCCUUAUUCAAUACCGAUGUAAAGUUGCAAGGGAGAAUCGAGGUGCCUGCUCGGGGUACCGGCCCGACUUUAGAGCCGCGUGCAUUAACCGGUGUGAAAGCACCCAAAAGGGUGGUAUGAUCGGUGAUGACGGCGUAUACUGUAGCUCCACGGUAAGGUCUGACCCUAAAUGCCGGUUCCGCCGUUCAGCACAAGGAAAUUUGCGUCAUCGUGGAGCGACAAUCCCCGCGCUAUACAGGUUCCGAAUUCGAUUUGUCUGUAGGCGCUUCAAUACCAGCGCCGCUCGAAACCCUGGGAUUACUGAAUCACCUCUCACACCGAUCGACCUACGGGUUAAUGUGCGUGACUACCUAUAUCCGGGUUCGACGUAUUAUGCCGCGACGCGGGCCCUACACGGUCAAAGACGGAGAGGCGGAAACCGCUGUCUUACGUCUGGCAUGCAUAAAGAGGCGUUUGACGAGAUCCAGGUGUUUCGUCUACUCGUGAGCCGAAAGCGUAAUUGCAAGACGCAAAGCGCAUCCCUUGCGGACAAAUUCGAUCCGUGCAAUGACGACUGUCACGACUAUAUAGAUCGUGGCACCCUUGCUGAGACCUUUCGAUCUCGCGGUAAUGAGAGCGCGACUCCCGCCAUGGCGGGACGGCAAAUGCGCCUUAAUCAUUCCCAGCCUAGGAGGAGAGCAGGAAGCCUAGGGCGACUGCAUUGUACCUUAUACACACUACAAGCUGUGUAUAGAGAAGUGUUCUUCCGAGACCCUGUGACCGCGCACUGCUUGGACGCCGGUAAAGAGCCAGAUGAUCAGGAUUCCGGGAAGAAACGAGGGCUCCUUAAUACCCGAGGUUGGUGCUUGGACCCUACUAGGUCUCCGUUGUCUAUUGCCAUGCACAUGGCUGCGCAGCUCGGAAGUAGUCCUCUUUUCAUACCGCGUGACUUUUUAUAUCGAUCUAUUGCCUCCGCGGGUUGUUGGGCCACACAGCGGAUCCUUUUCGCCUGGAAUGUUCACUGGUCUGAAUGCUCGAUGUUUUCCACGGACCCUAGCAGCCUCCAACUGUCUAGUAUGUUGAUGGGUUCUACGAUACUGAAUGAUAGUGCUUAUCUGCACAAUGAGUCUCCCCCUCCGUCGAACGUUUUGUUCCCCCGCGAGUGUUUCAUUUCCAGCGGGAGCUUGCCCGUACGGCUGCGGGAACCUGAAUAUGUUGCUCUAUCGACGAAGGGAAAAACUAAUGACAUUCACCCGCGAGGCCGAAGAGCGAUGUGGAAGUACGCACGUGGGAGGGCGACUUAUAUAAUAAAGCCUCUUGAAGUAUCCACGGCUAUUACUGCUAGGUAUUUCCGCAGCACGUAUGAUUCCCCAAGGAAUCUCACCCAUAGGAUAGCAUGGGGGACGUUAUUGCGGAUGAUGCAAAAUCAGCGUAUAGGCCCAGGCGCAAAAGUGCCCAGCCUAACUCCUCACUUACAUCAGCUUGCCGAAGACCAUCAACUUGAAUUCAUAUCCUACUUGGCGAGCAGCGACAAGACUGCGCAGCUGGGGCAGUGGUGCGCCAUAUUCGUCUUACAUGUACGGAGAGAUUUCCAUAGACGCGCUGACAUCCGGUGUCGGUGUGUGGGAUGCAACGCCGGAAACCUAAAUGGAGCUCCCCAAUCAACGAUUUUAGCCCAUGUACCGGUUUGUGGUAUGCUUUGGAGAAUGAUUAAAAGCUUAAAGCGGAAUGCCGUUCGCCUCAUCGUUGCACGCACCGAGUGGGCUAUCGAGCACGACGUUGACCGCGAUCCUCCCCACCUCGGUUGUGAAAGUUUACACAUUCAAAUUGCCACCCUCACUCCUCAUCAUGUUCGUAAGAAGCACCCCCCCCGCUAUCGUAUACCUUGGAUGACGACUUAUUUAUCCCUCGAAGAAACUAUCGGAGUCGAGGAACUAAAUAACCCCUCAUUGCCCGAGCCUGCUUUAUGCGUAUUUUGGCCGUAUGUGGCAAAGACCCUCUUGUUUAGCUACAUAAUAGCAGGGAAUUAUUGCCGGGGCUGUGCACAGUCGAGCGGAGUCGACAACUGGCCCAUCCCCUUGACUUCUCGUGCGAAACGCAUUACGCGAAUAAGCCUCGCUAGGUGUUGCCCAGACCUAAGAUUCUCGUUUCUGGGUGGCACGGGCGGUCAAAGUAACAAAGCAGAAUCCGAGGUUAUGGAUGAUCAUCAGUUUUUCCCAGUAUAUAGCACGGGACCUGUUAUCAAGCGCUGGUACACGGGAAAUUUCGCACGUACGAAGUACAUCUACUACCCUACCUCCAUGCCCCUCUGCGUGACUGUGGGUACACUUGCUGGCGCGGGAAAACUAUCUAGGAAUAAGGCCCAUUAUUCAAUGCGCUCGCGAAGUGAAUAUCACCCGCCAGUCCCGAUAAUAAGCCUCCCUUUUUCAUUGCAAUCCCUAUUACUUCCUGAGAGCAAUUCCGUAUUUAGUAGAGUCGCUACGCUCGAAGGCUUCGAACCAAGGAUGGCCCCACAUCCAUAUUCGACAGAAAGAAGCGCAGCUAUCGCUCUCCCGGAAACCCACUUCCCACAAGACAGAGUUCUACGAAGUCUACUAUGGAAGUACUUUGCAAUCUUAUGUUCUUGGCGGACAGAAGGAAUGUCACUUAUUGACCAAGGUCGCCAGCGUGUGAGGAGAUGCUACGGCGCUGUCCAGUCGAGUACUCCGGCGGUGCAGUACUACCGACGACAGGAGCCUAGGUUCCCAGAACUCUUCUGUGUCGUCACGCUUACAACGGCCAUCUCAGGCAUGUAUGGCCAAUUCGGCGACCCAGGUUGGACUAGGUGGAUAUCGGCGCAGCCCGCUGUUGGCGCUACAACUGGAGUACCCUUAAGAUGGUGCCCCGCCUCAAGUAGGUACGUGAAUUCUUACUCCCAUAAAAUCCAUGUACCCGGACAGCACAGCCAGCGAAUGUCGGAGCGAUACAAACCGCAUUGCAAUGGUGUUUUCUGUGAAAGAUUUCCCUCCGAACGGCUAGGACCGUGUCCGAGGGCCUUCAGAAAUCGUAGAUACUAUGGCGGAAGUCUAACCGGAUGGGCGUCCAUGGAUAAGUACUUCACGUGGGCGGUGAGGUCCCUACAAGGGUGCAUACCCUACAUAAAUAAAAUAAUCGGUGCGGCGCCUAAGAAGUUUUCUCUCCUGGCCUCGCGCAUAGCGUCUUGGAUUCGGACACAGGGCAGUUAUAUACCCGGCGUAUUGUGCCGGCCACGCCAAGAAGUCCCCAAAUUGUCUCGCCUCACUAUCGGUUCCAUCUGGGCGUGCCUUCCAUCGAAUGCCCAAAUCGAAUUGACGGGCAUCUGCGCGCAAUGUAAGUUACUGAAGGCAGUAAGAUAUGCCGUCGACUCUGAUCAUUACUUAACCGUUGAGUAUGUUUACAGAUUAAUGGCUGGAUCACUUAGUGUUCGUUUAAUAUUACACGCUAACUUAACCGAAGUUGUCUUUAAUACAGACCGGCAAGUAGACUGCAUGUGCGUUUCAUUGGUUGGAAUAAACGGGAUAGACUGCGACCGCAACUACUCAGUGCGCCAGGCAGGUAAAUCGAUGAAGCGGUAUAAUUCGACGGACCAUACGGCUACAUGCUAUGAUUCCCUGACUGACCAUGACUACCUACUGGCGACUUCUAUCCGAGGCUUGGUCGACGCCAGGCAAUUUUUACUUCGCUCGUCGGCCUGCCAGAGCGAAUCGGUCGUCCGACUACCAUUGAGACCCCUUAACAUUAAGGGGCUAGCGGGAGCUAUGAAUACUGCACGCGCUAAACUUGAUCCACUGACACAGUUGAUACGAGCGGUAGUCCAAGCAGGUGAACGAACUUCCAGCGACUCUGGUAUCGUAGAAUCUAAGAGCUAUGUUCUAUUAAAGACAGUGCAGAGCGGUGAAAGAUUGUCCCCCCAGAAUGCUUCACAUCUAGUGCCGAUGUUACACCAUACCUGCGACGGCUUCAUCGCAAGACUUCUCUCAUGGUCUCCGAGGCAUCUAUCUCUUCUAGGCCUCUUCUACUCAUACUCCGGAACUAGUUAUUCGAGGGGACAACGUCAGGGAACUUGCCCUCAUAUUUUGUUCGUGUUGAGACACGUCCACCUGGAUUCACUCACCAGUGCACUGCGGGGCGCGGGCCCGUGGUUAGUAUCUAGCGGUGCCAGCAGGGGAUUAAGAGCAUCGAUAUACCAAGAACAGCGGGCUGCUUACCGCUCAAUUGGAUUUUCGGUCUCAACCCUUCGAGUAUUUUCUAUAACAUUCAUAUCAUGCAGAAUCACACUUGAAUAUAACAUCUGGGUACCUAUGAAAGUGCCUGUCUCUCCCGUAGAAUCGAUCUCGCUAGGGGCGUCGACAGACACGCCCCCCAUUUUUAAGCUAAGUACGCCUCUAGAGAGUUGCACCGCGACAUGCGUAUCACCUCAGGGGAGAGCGCAUACCGGACGACAUCGCUUCGGAAAGACCGGUAUCAAAUUUUUACUUUGUGCGUCUGUUGGACUGGUCCUUGGACCACGCUGUAUGCCCCGUGUUAAGUCAUUUCGUUUGGAAUUAGGACUUCUAUUCUUCGUGACUCAACCGAGCGAGUCGAAUCGACCGGUACUGAGGUCUGGAACAGUAUUAUCGAACCGCAGUCUCUGGGGGAUAUCAAUCUACCGGGACUGCUGUUUACGUCUAAUGAGAGUGUACAUCUGGGCGACUAUCCAGAUAUGGGCCCUCGAACGGCAACCAUGGACUGCUGACAGAUGCCUUUAUACGAAUCCGUUUUGUAUCCUUAAGGACGGGUAUACUUCCUCAGGUUGCGACUGGGGUUACGACCGACAGCUCCGAAAGCAGGCGACAUUGAAUAGUCCGCCAACACAUCAGUUACAAGUCAGCGAUUGUGGGUACGGCAGUAUAAAAUCGGCCGCCUGGGCGUUAUACACUGUCCGAUACACAGGUAUGCAAGCUGUGUUCGUUUUACUAAGUCUUUUGCCCAGGAGGGGGGCCGACAUCUCCGGCCAUGCGACCCCAUGGCCUUCAGAGCCUUCAGAUUCGUCACCGCGAGGCUACGGGCUCAAACACCGUCCGUCAUUGCAACUAUCGGUUCUGACGCACCCACUAACGUGGUCACGCCAUAAUCCAAAACAAACAGACACUAGGUGCUAUCGACAUUGCUCGUCGGUUUCGAACCGAAAUUGUGUCGCCUUCGUAAAGUCCUGCCGACAUCCUAAGCGGCCUGCGGCUUUCGACUGGUUGGAGGCGGUUAAAGCACAUCUUCGUAUUCAGCCACCCGAAGACCCUCGGACAAGACAUAUCACACGGCUUGUUUGGGCACGCUAUGCUCAAGCCACAGUUUCGGAACGAUUCGAACCAAUGAGACGGAAUCUUGAGCCCAGAGGCGUCAUAGCGAAAGGCAGCUCGAUGCAACUGGAAAAUGGGAAACUGGGGCGUCGUGUAAUUCGGGCGCCAGGCCUCCUAGAAAAUGUUAUAGAGUUAUUUAGUCUAACACUAAUGUUUCUUAUACCCCAAACCGGACAUUGCGCUGUAACGGCUGGUGGACUGUGUAUGUUUUCUAAACAUGUAUACAGCUUGUUACAACGAUGUCAUUACACCGGCAUUACCGCUGAGAUUAGCGUGUCUGUUAUAGCGAUGGUUCUCACCCCUCGCGAGACGUGUUGCAUAACCAGACGUAACGCGGCUUCGACCAUGAUUAUCAAUAACAGUGCUGUCCGUAUGGUUGAGGAUUCUGCUGUCGAUCGCGCAGUACUUAUAAGACCGCCGCAUCGUAUUCCUUCUGAGGUUUACGAAAGGCCCGACGGGAUUGUCGGAUCUUGGCGAGUUGUUCGAACAAGGACCGCCGCAGACGUCAAAGGUAUGCGCUCUCGCUUCGAAGGUCAAGCCUGUGGCUCGGGUAUUCUUGUAACAACCAUACGAUUUUGGAGACGAGUAGUCCGAGGCCGCCUUACAGCUAAUCAGAGCCUCUGCAUCCACUCGUCAGAAGCUCAUCGCGGUUACAGGAUAGAAAAUCACACGGGAAUAGAAGGAGUUGAAUAUUAUAAGAUAAACCUUAUUCGCAGCUACGUAGUGUCCAUUUCGCGGACGGAUUCAGUGGCCUCGGGCGGUUGGGACCAUGAUGCUACCAAACUGGUCGUAGGUAGGAGGCUGCAAAAUAUUGGCGGCUGCAUUCGUCUCGACAUACUGUGCGGACCCAUCGCCCACCCAGUCGUGGUAUGUGUUAACUCGAAAACAUUCGACUUCAGUCGACACGAAAUUGAGGCAGCUGUUCACAGAAUUCUUUCCUUCCUAGAGUGGCAAAUGAAACCCAGGAUGGACAGAAAGUCAACGUGUGAUACAAUGAUGUCAGAGGGGGGAGACCAUAUUGUAAGACACACACCCGUACCAGCCCCCAAUGGAGGCGUACUAGGUUACGUACAUACCAGUGGCUCCUCAAUGUUAGCCGCCCCAUGCUGUUACGAGACGCCGAAUCGAAAUAGCGUUAAAAUAAGAUGCCACUCGAGAUUGCCAGGCUACGCGUGGCCGCGCAACACCGUUACUUCUGGGUCGGGGCCUUCAUAUACGCAAGGCAUUGGCAUACUAGUGGCGUCAAGUUCUAAGACGAUCGGGGUGAUGCCGAAGGACUGUAGCCGUGCCUUUCGGAGUCAGCGUUGCCCGAUACUGGGGGUCAGCAAUUUACCGUUACUCAUGGUAGCGUCUCGACGACACGCUCACGGUGACAAAAUCUCAGGCGGGUGCGUAGAUGUUGCCUACACACUUUUCAGUGCGGAAAUGCGCGUACCCGAUCGAUGGGCAACCACUGCUCUCGAUCCUAUGUUAUGUGCUCCUCGUUUUACGGCCGUCGCUAGUUCAGGGCUACAAAAUUCGCCAGUCUCAUCGAAAACGAGACAGUAUUACACAAGCGUAGCCCUUAAUAAAGGGGGCAUAGAUCUACAAGUGAUACAACACGAAACAGAUACUGCACGUUGCUGGAAUCUAUUGGGACCCAUCACCGGUCCGCACUUCUGUCUCGGAAUGUGGUUGACGAGUGUGCUCCGUCAACCAGCUUCUCCACUAGCGAUUCUAAUAUUCCGGCCUUACGCGAUGAGAAGGUUUUUUGAGCGUACUACUUCCCUCGUCCUCAUUCCCAUAUGUAGUCCAGGGCGAUGGAGCAAGAACAAUUCGUGUCUGGAUUCGCUAACAGGGGAACGAAACGUUGUUCUGCCCGGGGUAUAUCCGUGCCCGGAAACGAGAUCGUGCGGGGAUCGUGAUAGCGAGAAUUUCAGAGAGGUGCUUAGAGAUCCGUGCAAUUUGAAUGUCACUGCAUUGCGGUGCCAACACGAGAAUCUCUGCCUUCGCUGCUCUUCCAACCCCACACCUAAUCAUGCAACAAACCCAUAUACGCUGCUUUCAGAGCCACCAGACCGUCAACACACGCGAUCGUCUGUGAGGUGUCUCGGUCCUUACGGCUAUGGUAUUAGGUUUGUUGAGCUCUUACAGAGUCAAGUUUCUAAUGAGGCUUACGGUCGCUCGCACCCAGCGCAGUUUUCAAGGAAAUACUACCGAUUGUACUACCCGGUUUUCCCCAUCCCCGGCGCCAAUGAUAUGGUGCAAUCCGCCAUCUACUUAGAACUACCCUUGCUAGACAUGAUUGCCCUAACGGUCGCCGUCCUAGAGUGCCGAUUGUCCUGCGGUAUCCAACCGCGACAUGAACGACCUCAUUAUUGGUAUUUUGUUUCGGGGGGAGCUUGGUAUCCAGGGCAAAACCUUGCGAGGCUCGCCAAUGUAAGCACAAUUUUGUCCUUACAUCGGCGCCGGGGUAUCACAACACGAGCACCGCGUUCGAGCGAGCUAUCAAUUCAGACAAGUUUGAUACAGGCGCGAAUUAGCCGAGCAGACGUCCGUUCGCCAUUUGCAGUAAUGGAAAAGGCAACAGAUCACCCUGGCUAUAAGAACGUCGGGGAGUGCUUAUCAGGGUACCCACGAGGCGUCCGAUUAGGGGCCAAUAUAAGCUGGCCUACGUCGCUGUACGCCGGCGGUUUCAUUAGCUUAGGGGUCUCAUGCUGCGUUUUAUUCGGACAAUCGUCAAGAGACCAGAUGCCAAGUACAAAACUGAUAACAGAGUGUAUGAACCUCCGUGUUCAGUGUCCUUCUUCGCUCUUCUACGAGCUGCGAACGUCAGGUUCGCACGCGAUCAAUGUAAGAGCGUUCAGGUGUCUCGCUAGCGAGCUGUUAGCCUGGAUUCAGGAGGGGCUGAACGGGACCGUCUCGCACACAGUAAUGCAGGAUGAAGACCGAACCGUGUUCCCGAUUAAUUACAAUUCGUUGCAUACCUAUUUACCACAUGGAUUUGCGGUAGAACCACAUCGUAAAAUGCGUUGGUGCACCGGCCUUGAUGAGGAUCUGGUCCAGCUAAAUUAUCGGAGCCAGCUCGCUGUGCGCCAAUCCAUGUCGUUAGGAAAUGCCCUCGACACGUCCAAUCGUACAAAUAUACGGUGGUCGCGUCUCGUCGCCGGACAAUUACUCAACCCUCUCUUAAAAACAAUGUGUUUUGUUACCAAAUGCGACCCCAAUUGGGCCGCCUCGGCUUAUACCGUCCGGGACAAGGGGCGACGUGUUGACGGCCCGAGCGCCGUUCAUCUUGUAAACUCUACCGCACCGCACCCCUUUAUUAUAGCACGAGGUAUGAAUUAA
"""

RNA_string = list((RNA[i:3 + i] for i in range(0, len(RNA), 3)))

nucleotide_string = ''
for nucl in RNA_string:
    if RNA_to_Aminoacid(nucl) == 'Stop':
        break
    nucleotide_string += RNA_to_Aminoacid(nucl)

print(nucleotide_string)

# nucl_number = 0
# for char in RNA:
#     nucl_number += 1
#
#     first
#
#     print(char)