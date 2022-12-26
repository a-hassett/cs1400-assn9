# Alexandra Hassett, CS 1400

class Genome:
    # create variable for the string of letters and symbols that can be used
    def __init__(self, input):
        self.input = input

    # print the input as just uppercase letters of A, T, G, and C
    def display(self):
        sequence = ""
        self.input = self.input.upper()
        for i in range(len(self.input)):
            if self.input[i] == "A" or self.input[i] == "T" or self.input[i] == "G" or self.input[i] == "C":
                sequence = sequence + self.input[i]
        self.input = sequence
        print(self.input)

    # print genes containing three-letter codons in between ATG and one of the three: TAG, TAA, TGA
    def genes(self):
        # iterate until we run out of letters
        while len(self.input) > 3:
            # check whether there's a start codon
            j = self.input.find("ATG")

            # if there's no start codon, there's no gene
            if j == -1:
                print("no gene is found")
                self.input = ""
            # if there's a start codon
            else:
                self.input = self.input[j + 3:]  # shorten the sequence & get rid of the start codon & everything before

                # find the first stop codon in the sequence
                k = self.input.find("TAG")
                m = self.input.find("TAA")
                n = self.input.find("TGA")
                stopSpots = [k, m, n]  # position of all the stop codons in the sequence
                if k == -1:
                    del stopSpots[0]
                    if m == -1:
                        del stopSpots[0]
                        if n == -1:
                            del stopSpots[0]
                    else:
                        if n == -1:
                            del stopSpots[1]
                elif m == -1:
                    del stopSpots[1]
                    if n == -1:
                        del stopSpots[1]
                elif n == -1:
                    del stopSpots[2]
                p = min(stopSpots)

                # take the nucleotides between the start and stop codons
                gene = self.input[:p]
                # only print if it's a multiple of three
                if len(gene) % 3 == 0:
                    print(gene)
                self.input = self.input[j + p + 1:]


def main():
    s1 = Genome("..T.aA.DERRfDww..t.wwWWwwGC..")
    s2 = Genome("TTATGTTTTAAGGATGGGGCGTTAGTT")
    s3 = Genome("TGTGTGTATAT")
    s4 = Genome("TTATGTTTAAGGATGGGGCGTTAGTT")

    s1.display()

    print("---")
    s2.display()
    s2.genes()

    print("---")
    s3.display()
    s3.genes()

    print("---")
    s4.display()
    s4.genes()


main()
