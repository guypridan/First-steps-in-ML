# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    start = problem.getStartState()
    stack = util.Stack()
    stack.push(((start, None, 0), []))
    visited = set()

    while not stack.isEmpty():
        state = stack.pop()
        if problem.isGoalState(state[0][0]):
            return state[1]
        if state[0][0] not in visited:
            visited.add(state[0][0])
            for successor in problem.getSuccessors(state[0][0]):
                stack.push((successor, state[1]+[successor[1]]))

    print("ERR: didn't find any solution while searching")


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start = problem.getStartState()
    q = util.Queue()
    q.push(((start, None, 0), []))
    visited = set()

    while not q.isEmpty():
        state = q.pop()
        if problem.isGoalState(state[0][0]):
            return state[1]
        if state[0][0] not in visited:
            visited.add(state[0][0])
            for successor in problem.getSuccessors(state[0][0]):
                q.push((successor, state[1]+[successor[1]]))

    print("ERR: didn't find any solution while searching")
def uniformCostSearch(problem):
    """Search the node of the least total cost first."""
    start = problem.getStartState()
    pq = util.PriorityQueue()
    pq.push(((start, None, 0), []),0)
    visited = set()

    while not pq.isEmpty():
        (state, direction, price), way = pq.pop()
        if problem.isGoalState(state):
            return way
        if state not in visited:
            visited.add(state)
            for suc_state, suc_direction, suc_price in problem.getSuccessors(state):
                pq.push(((suc_state, suc_direction, price+suc_price), way+[suc_direction]), price+suc_price)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    pq = util.PriorityQueue()
    pq.push(((start, None, 0), []), 0)
    visited = set()

    while not pq.isEmpty():
        (state, direction, price), way = pq.pop()
        if problem.isGoalState(state):
            return way
        if state not in visited:
            visited.add(state)
            for suc_state, suc_direction, suc_price in problem.getSuccessors(state):
                pq.push(((suc_state, suc_direction, price+suc_price), way+[suc_direction]), price+suc_price+heuristic(suc_state, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
