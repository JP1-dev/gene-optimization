
# Codon-optimization tool

## Background

Proteins are the most essential building blocks of any kind of life, 
they basically are the tools of nature which form life itself. 

They are defined by a specific concatenation of amino acids and a 3D structure.
The information, in which sequence the amino acids should be concatenated,
is stored in the DNA. 
A protein "blueprint" in the DNA is encoded by the base-letters (A, T, C, G) with 3 digits (codon). 

### Simple example:

   *DNA-sequence:*  ATGGTGCAT

   *codons:*
   1. ATG    (encodes Methionine)
   2. GTG    (encodes Valine)
   3. CAT    (encodes Histidine)

   In this example Methionine, Valine and Histidine would be strung together in the Ribosome (place of protein manufacturing).

![image](https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20170202084949/ri/590/picture/Ribosome%20during%20protein%20synthesis.%20The%20Interaction%20of%20a%20Ribosome%20with%20mRNA.%20Process%20of%20initiation%20of%20translation-Designua_thumb.jpg)



DNA can encode 64 different amino acids (4 base-letters to the
power of 3 digits = 64), but there are only 21 amino acids which are used 
by living organisms. The way nature handles this is simply by encoding
amino acids by multiple codons. So different codons can stand for the 
same amino acid. But, as one might have falsely imagined, it's not 
irrelevant which codon encodes an amino acid at a specific position. 
Two codons might represent the same amino acid, but they definitely 
won't have the same production speed. Every codon means a different 
production speed in the ribosome. That's because every codon needs
a different amino acid transporter (tRNA) and there are not equally
many of them available. If there are many tRNA's for a certain codon 
available, it will take less time to find the matching tRNA to the codon.

---

### Idea
As explained above, speed differs from codon to codon and the codon 
usage isn't the same everywhere, it differs in each organism. This
is called codon bias. 

When proteins are to be produced artificially with bacteria
(E. coli K12 is often used), that's a big problem. The amino acids 
would be strung together in the correct sequence, but would likely
misfold because of the wrong speed at each production step. 

Codon optimization aims to correct this error by exchanging some codons
with other codons, which are better suited considering the speed. 

---

### Usage
1. [Open this](https://jojotech.one:4000)
2. Enter a human DNA sequence in the left text-box (doesn't matter if it represents a real
protein or not). In case of pure testing, the example button can be clicked
and the DNA-sequence of Hemoglobin (iron transporter) will be shown in the box.
3. Choose a destination organism, meanwhile only Escherichia coli K12 
is supported, because it's mostly used for protein production.
4. Click on optimize. The DNA-sequence will be sent to the server which will
try to change some codons to make the speeds at every production step in 
E. coli K12 as close as possible to the speeds of the host organism 
Homo sapiens. 

---


