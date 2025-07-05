'''
Primality Test
---------------

-> Alice and Bob are meeting after a long time. As usual they love to play some math games. 
-> This times Alice takes the call and decides the game.
-> The game is very simple, Alice says out an integer and Bob has to say whether the number is prime or not.
-> Bob as usual knows the logic but since Alice doesn't give Bob much time to think, so Bob decides to write a computer program.
-> Help Bob accomplish this task by writing a computer program which will calculate whether the number is prime or not.
-> Note that 1 is not a prime number.

Input
------
-> The first line of the input contains an integer T, the number of testcases. T lines follow.
-> Each of the next T lines contains an integer N which has to be tested for primality.

Output
-------
-> For each test case output in a separate line, "yes" if the number is prime else "no."

Sample :- 

input             output 
5
23                  yes
13                  yes
20                  no
1000                no
99991               yes
'''

# Answer 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n ** 0.5)+ 1):
        if n % i == 0:
            return False
    return True 

x = int(input())
for i in range(x):
    y = int(input())
    if is_prime(y):
        print("Yes")
    else:
        print("No")