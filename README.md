# Lexicographic Word Ladders

An **edit step** is a transformation from one word $x$ to another word $y$ such that $x$ and $y$ are words in the dictionary, and $x$ can be transformed to $y$ by **adding**, **deleting**, or **changing** one letter. So the transformation from `dig` to `dog` or from `dog` to `do`are both edit steps. A **lexicographic word ladder** is a *lexicographically ordered sequence* of words $w_1, ~w_2, \ldots, ~w_n$ such that the transformation from $w_i$ to $w_{i+1}$ is an edit step for all $i$ from 1 to $n−1$.

For a given dictionary, you are to compute the length of the longest lexicographic word ladder, along with a sequence of words that make up such a ladder. 


## Input

The input to your program consists of an ordered word dictionary – a set of lower case words in **lexicographic order** – one per line. No word exceeds 6 letters and there are no more than 1000 words in the dictionary.


### Sample Input

    cat
    dig
    dog
    fig
    fin
    fine
    fog
    log
    wine


### Sample Output

    5: dig, fig, fin, fine, wine



# Cube Towers

You are given $n$ colorful cubes each having a distinct weight. Each face of a cube is colored with one color. Your job is to build a tower using the cubes you have subject to the following restrictions:

- Never put a heavier cube on a lighter one.

- The bottom face of every cube (except the bottom cube, which is lying on the floor) must have the same color as the top face of the cube below it.

Construct the tallest tower possible.

## Input

The input may contain multiple test cases. The first line of each test case contains an integer $n$, $1 \leq n \leq 50$ indicating the number of cubes you are given. The $i^{th}$ ($1 \leq i \leq n$) line in the next $n$ lines contains the description of the $i^{th}$ cube (assume the cubes are numbered from 1).

A cube is described by giving the colors of its faces in the following order: front, back, left, right, top and bottom face. For your convenience colors are identified by integers in the range 1 to 100. You may assume that cubes are given in the increasing order of their weights, that is, cube 1 is the lightest and cube $n$ is the heaviest.

The input terminates with a value $0$ for $n$.

## Output

For each test case in the input, first print the test case number (starting from 1) on a separate line as shown in the sample output. On the next line print the number of cubes in the tallest tower you have built. From the next line describe the cubes in your tower from top to bottom with one description per line. Each description contains an integer (giving the serial number of this cube in the input) followed by a single whitespace character and then the identification string (front, back, left, right, top or bottom) of the top face of the cube in the tower. 

Note that there may be multiple solutions and any one of them is acceptable.
Print a blank line between two successive test cases.

### Sample Input

    3 
    1 2 2 2 1 2 
    3 3 3 3 3 3 
    3 2 1 1 1 1 
    10
    0

### Sample Output

    Case 1
    2
    2 front
    3 front

