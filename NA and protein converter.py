def DNAtoRNA(DNAStrand1):
    #Initialization of variables
    timesDone = 0
    DNAStrand2 = []
    global RNAStrand
    RNAStrand = ""
    
    #Run through the to-be second DNA Strand
    #a number of times equivalent to the number
    #of letters in it, and replace each base
    #with its complement.
    for timesDone in range(len(DNAStrand1)):
        if(DNAStrand1[timesDone] == "T"):
            DNAStrand2.append("A")
        elif(DNAStrand1[timesDone] == "A"):
            DNAStrand2.append("T")
        elif(DNAStrand1[timesDone] == "C"):
            DNAStrand2.append("G")
        elif(DNAStrand1[timesDone] == "G"):
            DNAStrand2.append("C")
        timesDone += 1
    
    #Change the DNAStrand2 list to a string and clean it up.
    DNAStrand2 = str(DNAStrand2)
    DNAStrand2 = DNAStrand2.replace(",", "")
    DNAStrand2 = DNAStrand2.replace("[", "")
    DNAStrand2 = DNAStrand2.replace("]", "")
    DNAStrand2 = DNAStrand2.replace(" ", "")
    DNAStrand2 = DNAStrand2.replace("\'", "")
    
    #Replace all T's with U's in the to-be RNA strand.
    RNAStrand = DNAStrand2.replace("T", "U")
    
    #Print the results of the strands of DNA and RNA.
    print("DNA Strand 1: %s") % DNAStrand1
    print("DNA Strand 2: %s") %DNAStrand2
    print("")
    print("RNA Strand: %s") % RNAStrand

def RNAtoProtein(RNAStrand):
    #Initialization of variables
    AminoAcids = []
    codons = []
    codonsStr = ""
    timesDone = 0
    basePairToRead = 0
    
    #Chunk the RNA into codons and save them to the
    #codons variable.
    for timesDone in range(len(RNAStrand)/3):
        codons.append(RNAStrand[basePairToRead] + RNAStrand[basePairToRead + 1] + RNAStrand[basePairToRead + 2])
        basePairToRead += 3
        timesDone += 3
    
    
    #Amino Acids
    Phe = ["UUU", "UUC"]
    Leu = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]
    Ile = ["AUU", "AUC", "AUA"]
    START = ["AUG"]
    Val = ["GUU", "GUC", "GUA", "GUG"]
    Ser = ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]
    Pro = ["CCU", "CCC", "CCA", "CCG"]
    Thr = ["ACU", "ACC", "ACA", "ACG"]
    Ala = ["GCU", "GCC", "GCA", "GCG"]
    Tyr = ["UAU", "UAC"]
    STOP = ["UAA", "UAG", "UGA"]
    His = ["CAU", "CAC"]
    Glu = ["CAA", "CAG", "GAA", "GAG"]
    Asn = ["AAU", "AAC"]
    Lys = ["AAA", "AAG"]
    Asp = ["GAU", "GAC"]
    Cys = ["UGU", "UGC"]
    Trp = ["UGG"]
    Arg = ["CGU", "CGC", "CGA", "CGC", "AGA", "AGG"]
    Gly = ["GGU", "GGC", "GGA", "GGG"]
    
    #Reset the timesDone variable.
    timesDone = 0
    
    #If the letters of the codon matches the letters of any of
    #an amino acid's possible combination of bases, add that amino acid
    #to the list of amino acids.
    for timesDone in range(len(codons)):
        if codons[timesDone] in Phe:
            AminoAcids.append("Phe")
            
        elif codons[timesDone] in Leu:
            AminoAcids.append("Leu")
            
        elif codons[timesDone] in Ile:
            AminoAcids.append("Ile")
            
        elif codons[timesDone] in START:
            AminoAcids.append("START")
            
        elif codons[timesDone] in Val:
            AminoAcids.append("Val")
            
        elif codons[timesDone] in Ser:
            AminoAcids.append("Ser")
            
        elif codons[timesDone] in Pro:
            AminoAcids.append("Pro")
            
        elif codons[timesDone] in Thr:
            AminoAcids.append("Thr")
            
        elif codons[timesDone] in Ala:
            AminoAcids.append("Ala")
            
        elif codons[timesDone] in Tyr:
            AminoAcids.append("Tyr")
            
        elif codons[timesDone] in STOP:
            AminoAcids.append("STOP")
            
        elif codons[timesDone] in His:
            AminoAcids.append("His")
            
        elif codons[timesDone] in Glu:
            AminoAcids.append("Glu")
            
        elif codons[timesDone] in Asn:
            AminoAcids.append("Asn")
            
        elif codons[timesDone] in Lys:
            AminoAcids.append("Lys")
            
        elif codons[timesDone] in Asp:
            AminoAcids.append("Asp")
            
        elif codons[timesDone] in Cys:
            AminoAcids.append("Cys")
            
        elif codons[timesDone] in Trp:
            AminoAcids.append("Trp")
            
        elif codons[timesDone] in Arg:
            AminoAcids.append("Arg")
            
        elif codons[timesDone] in Gly:
            AminoAcids.append("Gly")
            
        else:
            AminoAcids.append("INVALID")
            
        timesDone += 1
    
    #Clean up the leftover parts of the list we don't need
    #to display, and then print the codons and corresponding amino acids.
    codonsStr = str(codons)
    codonsStr = codonsStr.replace(",", "")
    codonsStr = codonsStr.replace("[", "")
    codonsStr = codonsStr.replace("]", "")
    codonsStr = codonsStr.replace("\'", "")
    
    AminoAcidsStr = str(AminoAcids)
    AminoAcidsStr = AminoAcidsStr.replace(",", "")
    AminoAcidsStr = AminoAcidsStr.replace("[", "")
    AminoAcidsStr = AminoAcidsStr.replace("]", "")
    AminoAcidsStr = AminoAcidsStr.replace("\'", "")
    
    #Display the codons and amino acid chain/protein.
    print("RNA Codons: %s") % codonsStr
    print("Protein:    %s") % AminoAcidsStr
        

def DNAtoAminoAcids(DNAStrand1):
    DNAtoRNA(DNAStrand1)
    RNAtoProtein(RNAStrand)