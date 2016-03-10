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
    
    #Replace all T's with U's in the to-be RNA strands.
    RNAStrand1 = DNAStrand1.replace("T", "U")
    RNAStrand2 = DNAStrand2.replace("T", "U")
    
    #Print the results of the strands of DNA and RNA.
    print("DNA Strand 1: %s") % DNAStrand1
    print("DNA Strand 2: %s") %DNAStrand2
    print("")
    print("RNA Strand 1: %s") % RNAStrand1
    print("RNA Strand 2: %s") % RNAStrand2

def RNAtoAminoAcids(RNAStrand1):
    #Initialization of variables
    AminoAcids = []
    timesDone = 0
    codons = []
    basePairToRead = 0
    
    #Chunk the RNA into codons and save them to the
    #codons variable.
    for timesDone in range(len(RNAStrand2)):
        codons.append(RNAStrand2[basePairToRead] + RNAStrand2[basePairToRead + 1] + RNAStrand2[basePairToRead + 2])
        basePairToRead += 3
    print(codons)
    
