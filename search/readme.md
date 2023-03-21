# guy pridan's Maman 11 solution

### Question 1
for the _DFS_ graph search algorithm, I've used a stack
to keep track of the unvisited successors of the current state
and unvisited successors of previously visited states.
by using a stack data structure (with a LIFO accounting)
I guarantee that the next successor to be visited is a successor of the last visited state.

with a _DFS_ graph search the solution isn't allways optimal, 
the algorithm opens the successors of a given state
according to the order given by the getSuccessors function,
and without taking into account the distance of the successors from the goal state.

### Question 2
for the _BFS_ graph search algorithm, I've used a Queue
to keep track of the unvisited successors of the current state
and unvisited successors of previously visited states.
by using a Queue data structure (with a FIFO accounting)
I guarantee that the successors will be visited "level by level"

with _BFS_ graph search algorithm, the returned solution is allways optimal

### Question 3
for the _UFC_ graph search algorithm, I've used a Priority Queue
to keep track of the unvisited successors of the current state
and unvisited successors of previously visited states.
by using a Priority Queue data structure
I guarantee that the next successor to be visited has the path with the minimum cost.

### Question 4
for the _aStar_ graph search algorithm, I've used a Priority Queue
to keep track of the unvisited successors of the current state
and unvisited successors of previously visited states.
if G(x) is the cost function for the path, and H(x) is the heuristic
then the total cost used in the Priority Queue is F(x) = G(x) + H(x), as should be in an _aStar_ algorithm

### Question 6 - Proof that the heuristic is consistent
my heuristic returns the state's manhattan distance from the farthest not visited corner.

let's assume that 
* y is a state
* x is y's a successor
* S(x) is the cost to get from x to the closest goal state
* G(x) is the cost to visit x
* MD(x) is the successor's heuristic.
* manhattan path is a path from y to the farthest not visited corner with the cost of MD(y)

because the manhattan distance is the distance from a to b while ignoring the walls between them,
if x is not on any of y's manhattan paths then MD(x) 
# #TODO - finnish proof
then MD(y) - G(x) <= MD(x) and the heuristic is consistent.


