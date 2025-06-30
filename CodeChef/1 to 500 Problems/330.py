'''
Bidding
-------
-> Alice, Bob and Charlie are bidding for an artifact at an auction.
-> Alice bids A rupees, Bob bids B rupees, and Charlie bids C rupees (where A, B, and C are distinct).
-> According to the rules of the auction, the person who bids the highest amount will win the auction.
-> Determine who will win the auction.

Input Format
-------------
-> The first line contains a single integer T — the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains three integers A, B, and C, — the amount bid by Alice, Bob, and Charlie respectively.

Output Format
--------------
-> For each test case, output who (out of Alice, Bob, and Charlie) will win the auction.
-> You may print each character of Alice, Bob, and Charlie in uppercase or lowercase (for example, ALICE, aliCe, aLIcE will be considered identical).


Sample 

input               output 
4
200 100 400         Charlie
155 1000 566        Bob
736 234 470         Alice
124 67 2            Alice
'''

# Answer
 
N = int(input())
for i in range(N):
    X, Y , Z = map(int, input().split())
    if X > Y and X > Z:
        print("Alice")
    elif Y > X and Y > Z:
        print("Bob")
    else:
        print("Charlie")