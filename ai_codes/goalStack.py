class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def execute(self):
        print(f"Executing action: {self.name}")

class Goal:
    def __init__(self, name):
        self.name = name

class GoalStackPlanner:
    def __init__(self):
        self.stack = []

    def push_goal(self, goal):
        self.stack.append(goal)

    def pop_goal(self):
        return self.stack.pop()

    def plan(self):
        while self.stack:
            current_goal = self.stack[-1]

            if isinstance(current_goal, Goal):
                print(f"Attempting to achieve goal: {current_goal.name}")
                # Add your goal decomposition logic here
                # For simplicity, we assume each goal is an action
                action = current_goal
                self.stack.pop()  # Remove the goal
                self.stack.extend(action.preconditions[::-1])  # Add preconditions to the stack
            elif isinstance(current_goal, Action):
                if all(goal.name in current_goal.effects for goal in self.stack[:-1]):
                    print(f"Executing action: {current_goal.name}")
                    current_goal.execute()
                    self.stack.pop()  # Remove the achieved action
                else:
                    print(f"Failed to achieve action: {current_goal.name}")
                    break

if __name__ == "__main__":
    # Define actions
    action1 = Action("MoveToA", [], ["AtA"])
    action2 = Action("MoveToB", [], ["AtB"])
    action3 = Action("PickUp", ["AtA"], ["Holding"])
    action4 = Action("PutDown", ["Holding"], ["OnTable"])

    # Define goals
    goal1 = Goal("AtA")
    goal2 = Goal("AtB")
    goal3 = Goal("OnTable")

    planner = GoalStackPlanner()

    # Example plan: Move to A, Pick up, Move to B, Put down
    planner.push_goal(goal1)
    planner.push_goal(action1)
    planner.push_goal(goal3)
    planner.push_goal(action3)
    planner.push_goal(goal2)
    planner.push_goal(action2)
    planner.push_goal(goal3)
    planner.push_goal(action4)

    planner.plan()
