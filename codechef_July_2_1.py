'''
Relativity:

In Chefland, the speed of light is c m/s, and acceleration due to gravity is g m/s^2.

Find the smallest height (in meters) from which Chef should jump such that during his journey down
only under the effect of gravity and independent of any air resistance, he achieves the speed of light
and verifies Einstein's theory of special relativity.

Assume he jumps at zero velocity and at any time, his velocity (v) and depth of descent (H) are related as
v^2=2⋅g⋅H.

Input:
The first line contains an integer T, the number of test cases.
Then the test cases follow.
Each test case contains a single line of input, two integers g, c.

Output:
For each test case, output in a single line the answer to the problem.
We can show that under the constraints, the answer is an integer.

Constraints:
1≤T≤5⋅10^3
1≤g≤10
1000≤c≤3000
2⋅g divides c^2.

Sample Input:
3
7 1400
5 1000
10 1000

Sample Output:
140000
100000
50000
'''
T=int(input())
G=[]
C=[]
for i in range(0,T):
    g,c=input().split()
    G.append(int(g))
    C.append(int(c))
for i in range(0,T):
    H=(C[i])**2/(2*G[i])
    print(int(H))
