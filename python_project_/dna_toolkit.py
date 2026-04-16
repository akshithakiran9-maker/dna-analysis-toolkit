"""
DNA Analysis Toolkit
A simple Python-based tool for DNA sequence analysis.
Author: Akshitha Kiran

Features:
- DNA validation
- Base counting & GC content
- Reverse complement
- DNA → Protein translation
- Motif finding
- Mutation detection
...
"""
# SEQUENCE INPUT
dna = input("enter the dna sequence :  ")   # Take DNA input from user
dna = dna.upper()                           # Convert to uppercase
dna = dna.replace(" ", " ")                 # (This line doesn't change anything)
print(" processed dna sequence :  ", dna)   # Print processed DNA


# VALIDATION OF THE SEQUENCE
dna = dna.upper()                           # Ensure uppercase again
dna = dna.replace(" ", "")                  # Remove spaces from sequence
valid_bases = {"A", "T", "G", "C"}          # Valid DNA bases

is_valid = True                             # Assume sequence is valid initially

# Check each base in DNA
for base in dna:
    if base not in valid_bases:             # If invalid base found
        is_valid = False
        break                               # Stop checking further

# Print validation result
if is_valid:
    print("processed dna sequence :", dna)
    print("DNA sequence is valid")
else:
    print("Invalid DNA sequence detected")


# CALCULATING GC CONTENT AND COUNTING BASES
length = len(dna)                           # Length of DNA sequence
print("length of dna sequence : ", length)

# Count each nucleotide
A_count = dna.count("A")
print("Total count of A : ", A_count)

T_count = dna.count("T")
print("Total count of T : ", T_count)

G_count = dna.count("G")
print("Total count  of G : ", G_count)

C_count = dna.count("C")
print("Total count of C: ", C_count)

# Calculate GC content percentage
gc_content = ((G_count + C_count)) / len(dna) * 100
print("gc  content", gc_content)


# REVERSE COMPLEMENT
complement = ""                             # Empty string to store complement

# Loop through each base
for base in dna:
    if base == "A":
        complement += "T"                   # A pairs with T
    elif base == "T":
        complement += "A"                   # T pairs with A
    elif base == "G":
        complement += "C"                   # G pairs with C
    elif base == "C":
        complement += "G"                   # C pairs with G

# Reverse the complement sequence
reverse_complement = complement[::-1]
print("Reverse Complement:", reverse_complement)


# DNA TO PROTEIN TRANSLATION
# Codon table (DNA → Amino Acid)
codon_table = {
    "ATA":"I","ATC":"I","ATT":"I","ATG":"M",
    "ACA":"T","ACC":"T","ACG":"T","ACT":"T",
    "AAC":"N","AAT":"N","AAA":"K","AAG":"K",
    "AGC":"S","AGT":"S","AGA":"R","AGG":"R",
    "CTA":"L","CTC":"L","CTG":"L","CTT":"L",
    "CCA":"P","CCC":"P","CCG":"P","CCT":"P",
    "CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
    "CGA":"R","CGC":"R","CGG":"R","CGT":"R",
    "GTA":"V","GTC":"V","GTG":"V","GTT":"V",
    "GCA":"A","GCC":"A","GCG":"A","GCT":"A",
    "GAC":"D","GAT":"D","GAA":"E","GAG":"E",
    "GGA":"G","GGC":"G","GGG":"G","GGT":"G",
    "TCA":"S","TCC":"S","TCG":"S","TCT":"S",
    "TTC":"F","TTT":"F","TTA":"L","TTG":"L",
    "TAC":"Y","TAT":"Y","TAA":"_","TAG":"_",
    "TGC":"C","TGT":"C","TGA":"_","TGG":"W",
}

protein = ""                                # Empty protein sequence

# Read DNA in codons (3 bases at a time)
for i in range(0, len(dna) - 2, 3):
    codon = dna[i:i+3]  

    if codon in codon_table:
        amino_acid = codon_table[codon]

        if amino_acid == "_":              # Stop codon
            break

        protein += amino_acid              # Add amino acid

print("Protein Sequence:", protein)


# SIMPLE MOTIF FINDING (length = 3)
motifs = {}                                # Dictionary to store motif counts

# Loop through DNA
for i in range(len(dna) - 2):
    motif = dna[i:i+3]                     # Extract 3-base motif
    
    if motif in motifs:
        motifs[motif] += 1                 # Increase count
    else:
        motifs[motif] = 1                  # Add new motif

# Print repeated motifs only
for m in motifs:
    if motifs[m] > 1:
        print(m, ":", motifs[m])


# MUTATION DETECTION
original = input("Enter original DNA: ")    # Original sequence
mutated = input("Enter mutatated dna : ")  # Mutated sequence
    
# Check if lengths are equal
if len(original) != len(mutated):
    print("Length mismatch")
else:
    # Compare each position
    for i in range(len(original)):
        if original[i] != mutated[i]:
            print("Position", i+1, ":", original[i], "→", mutated[i])

            


   
