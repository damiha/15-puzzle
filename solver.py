
import node
import statistics

goal_node = node.Node.create_goal_node()


def bfs(start_node):

    seen = set()
    queue = [start_node]

    while len(queue) > 0:

        current_node = queue.pop(0)

        if current_node == goal_node:
            return get_solution(current_node)

        seen.add(current_node)

        next_nodes = current_node.get_next_nodes()

        for next_node in next_nodes:
            if next_node not in seen:
                queue.append(next_node)

    return []


def dfs(start_node):
    seen = set()
    return dfs_helper(start_node, seen, 0)


def dfs_helper(current_node, seen, depth):

    if current_node == goal_node:
        return get_solution(current_node)

    seen.add(current_node)

    for next_node in current_node.get_next_nodes():
        if next_node not in seen:
            solution = dfs_helper(next_node, seen, depth + 1)

            if is_solution(solution):
                return solution

    return []


def dfs_depth_limited(start_node, depth_limit):
    seen = set()
    start_depth = 0

    return dfs_depth_limited_helper(start_node, seen, start_depth, depth_limit)


def dfs_depth_limited_helper(current_node, seen, current_depth, depth_limit):

    if exceeds_depth_limit(current_depth, depth_limit):
        return []

    if current_node == goal_node:
        return get_solution(current_node)

    seen.add(current_node)

    for next_node in current_node.get_next_nodes():

        if next_node not in seen:
            solution = dfs_depth_limited_helper(next_node, seen, current_depth + 1, depth_limit)

            if is_solution(solution):
                return solution

    return []


def exceeds_depth_limit(current_depth, depth_limit):
    return current_depth >= depth_limit


def dfs_iterative_deepening(start_node):

    depth_limit = 0
    found = False

    while not found:
        depth_limit += 1
        solution = dfs_depth_limited(start_node, depth_limit)

        if is_solution(solution):
            return solution


def is_solution(solution):
    return len(solution) > 0


def get_solution(end_node):

    solution = []
    current_node = end_node

    while current_node.parent is not None:
        solution.append(current_node.instruction)
        current_node = current_node.parent

    solution.reverse()
    return solution


