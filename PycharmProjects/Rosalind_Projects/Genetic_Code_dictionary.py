def RNA_to_Aminoacid(codon):
    genetic_code_table = """
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
        UGG W      CGG R      AGG R      GGG G """

    Genetic_Code_table_NoNewLine = genetic_code_table.replace('\n', ' ')
    Genetic_Code_string = Genetic_Code_table_NoNewLine.split(' ')

    codon_list, aminoacid_list = [], []
    iterator = 1
    for item in Genetic_Code_string:
        if item != '' and item != 'V\n':
            iterator += 1
            if iterator % 2 == 0:
                codon_list.append(item)
            if iterator % 2 == 1:
                aminoacid_list.append(item)
    genetic_code_dictionary = dict(zip(codon_list, aminoacid_list))
    return genetic_code_dictionary[codon]


