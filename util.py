class Node():
    def __init__(self, state, parent, action, heuristic_value):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic_value = heuristic_value

    def get_heuristic_value(self):
        return self.heuristic_value


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def get_one_and_remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def sortFn(self, node):
        return node.get_heuristic_value()

    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort(key=self.sortFn, reverse=True)


    def get_one_and_remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
