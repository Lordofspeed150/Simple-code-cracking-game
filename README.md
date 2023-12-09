# Simple-code-cracking-game
a simple game where you have to solve a puzzle. that's it.

-SPOILERS-
PLEASE DO NOT read ahead of this message if you want a challenge without explanation of the puzzle.


In this game you are given 4 rows of numbers. the first row consists of that I call primary numbers.
Primary numbers are multiplied by the numbers below them. Let me give an example:

3 | 8 | 4 | 9
0 | 1 | 1 | 1
0 | 0 | 1 | 1
0 | 0 | 0 | 0

we have our first number, 3. since all the numbers below it are 0, it is multiplied by 0.
in our second column we have 8, the numbers below is are 1, 0 and 0. therefore 8 is multiplied by 1.
in our third column there is a 4 are two 1's below it. hence, 4 * (1+1) = 8.
lastly, in our 4th column we got 9 and two 2's below it, we do the same as previously. 9 * (1+1) = 18.
* we do not write anything for a column if it's answer is 0.

our answer should be 8818.
(0)  8   8   18
1st 2nd 3rd  4th
