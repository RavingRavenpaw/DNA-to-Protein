def convert(startType, startSequence, endType, endSequence):
    #GENERAL INFO
    #------------------------------------------
    #
    #DNA Base Pairs:
    #A-T, C-G
    #Adenine and Thymine, Cytosine and Guanine
    #
    #RNA Base Pairs:
    #A-U, C-G
    #Adenine and Uracil, Cytosine and Guanine
    #I know RNA is almost always single-stranded so bonding
    #between the bases doesn't matter, but sometimes
    #it happens!
    #
    #Amino Acids & Corresponding Codons:
    #No idea. I'll look this up later.
    print("test")

def DNAtoRNA(DNAStrand1):
    #Initialization of variables
    timesDone = 0
    DNAStrand2 = []
    
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
    
    #Make the RNAStrand variable global so the RNAtoAminoAcids function
    #can utilize it.
    global RNAStrand
    
    #Print the results of the strands of DNA and RNA.
    print("DNA Strand 1: %s") % DNAStrand1
    print("DNA Strand 2: %s") %DNAStrand2
    print("")
    print("RNA Strand: %s") % RNAStrand

def RNAtoAminoAcids(RNAStrand):
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
    
    codonsStr = str(codons)
    codonsStr = codonsStr.replace(",", "")
    codonsStr = codonsStr.replace("[", "")
    codonsStr = codonsStr.replace("]", "")
    codonsStr = codonsStr.replace("\'", "")
    print("RNA Codons: %s") % codonsStr
    
def DNAtoCodons(DNAStrand1):
    DNAtoRNA(DNAStrand1)
    RNAtoAminoAcids(RNAStrand)