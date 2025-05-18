'''
Complementary Strand in a DNA
------------------------------
-> You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. 
-> S contains the character T,C,A,T,C, and G only.
Chef knows that:
     A is complementary to T.T is complementary to A.C is complementary to G.G is complementary to C.Using the string 
     S, determine the sequence of the complementary strand of the DNA.

Input Format
----------------
-> First line will contain T, number of test cases. Then the test cases follow.
-> First line of each test case contains an integer N - denoting the length of string S.
-> Second line contains N characters denoting the string S.

Output Format
--------------------
-> For each test case, output the string containing N characters - sequence of nucleotides of the complementary strand.

sample :-

input                   output

4
4
ATCG                    TAGC
4
GTCC                    CAGG
5
AAAAA                   TTTTT
3
TAC                     ATG

'''

# Answer 
n = int(input())
for i in range(n):
    a = int(input())
    b = input()
    res = ""
    for j in b:
        if j == "A":
            res += "T"
        if j == "T":
            res += "A"
        if j == "C":
            res += "G"
        if j == "G":
            res += "C"
    print(res)
