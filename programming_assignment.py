class Anagram:
    num_iterations = 0
    def anagram_expand(self, state, goal):
        node_list = []
        # combined_elements=zip(state,goal)
        # incorrect_element_count=0
        # for state,goal in combined_elements:
        #     if(state!=goal):
        #         incorrect_element_count+=1
        
        # score=incorrect_element_count
        
        for pos in range(1, len(state)):  # Create each possible state that can be created from the current one in a single step
            new_state = state[1:pos + 1] + state[0] + state[pos + 1:]

            # TO DO: c. Very simple h' function - please improve!
            # if new_state == goal:
            #     score = 0
            # else:
            #     score = 1
            combined_elements=zip(state,goal)
            incorrect_element_count=0
            for start,end in combined_elements:
                if(start!=end):
                    incorrect_element_count+=1
        
        score=incorrect_element_count

        node_list.append((new_state, score))
        
        # for x,y in node_list:
        #     print(x,y)

        return node_list

    # TO DO: b. Return either the solution as a list of states from start to goal or [] if there is no solution.
    def a_star(self, start, goal, expand):
        g_score = {start: 0}#g_score of initial node is usually 0 
        open=[(start,0)]#dictionary to keep tuple elements that are nodes yet to be explored with f value as 0
        closed={}#dictionary to keep tuple elements that are nodes already explored
        # path=[]

        while len(open)>0:#while open list not empty
            sorted_list = sorted(open, key=lambda x: x[1]) #sorting list based on the f-scores in ascending order
            curr, _ = sorted_list.pop(0)#popping the first element of the list with lowest f-score

            if curr == goal:#checking if the current node is the goal node
                path = [curr]#path to the current node 
                while curr in closed:
                    curr = closed[curr]
                    path.insert(0, curr)
                return path#returns the optimal path to the goal node

            for new_node, h_score in expand(curr, goal):
                g_temp = g_score[curr] + 1
                if  g_temp < g_score[new_node] or new_node not in g_score:
                    g_score[new_node] = g_temp
                    f_score = g_temp + h_score
                    sorted_list.append((new_node, f_score))
                    closed[new_node] = curr
                    self.num_iterations += 1

        return []


    # Finds a solution, i.e., the set of steps from one word to its anagram
    def solve(self,start, goal):

        self.num_iterations = 0

        # TO DO: a. Add code below to check in advance whether the problem is solvable

        # if ...
        #    print('This is impossible to solve')
        #    return "IMPOSSIBLE"
        # we can check the parity of the string 
        start_char={}# dictionary to count starting characters frequency
        goal_char={}#dictionary to count goal characters frequency
        odd_start=0#counting the odd parity of start value
        even_start=0#counting the even parity of start value
        odd_goal=0#counting the odd parity of goal value
        even_goal=0#counting the even parity of goal value
        
        for char in start:
            # self.num_iterations+=1
            if char in start_char:
                start_char[char]= start_char[char]+1
            else:
                start_char[char]=1

        # print(self.num_iterations)

        for count in start_char.values():
            if (count%2!=0):
                odd_start=odd_start+1
            else:
                even_start=even_start+1
        
        if(odd_start>even_start):
            print("Start is Odd Parity")

        else:
            print("Start is Even Parity")

        for char in goal:
            # self.num_iterations+=1
            if char in goal_char:
                goal_char[char]= goal_char[char]+1
            else:
                goal_char[char]=1

        # print(self.num_iterations)

        for count in goal_char.values():
            if count%2!=0:
                odd_goal=odd_goal+1
            else:
                even_goal=even_goal+1

        
        if(odd_goal>even_goal):
            print("Goal is Odd Parity")

        # elif()

        else:
            print("Goal is Even Parity")

        print(start_char)
        print(goal_char)

        if (start_char!=goal_char):
            print("Problem cannot be solved")
            return
        else:
            pass

        # for char in start_char.keys():
        #     if char in goal_char.keys():
        #         if(goal_char[char]!=start_char[char]):
        #            return "Problem cannot be solved"
        #         else:
        #             pass
        
        self.solution = self.a_star(start, goal, self.anagram_expand)

        if not self.solution:
            print('No solution found')
            return "NONE"

        print(str(len(self.solution) - 1) + ' steps from start to goal:')

        for step in self.solution:
            print(step)

        print(str(self.num_iterations) + ' A* iterations were performed to find this solution.')

        return str(self.num_iterations)


if __name__ == '__main__':
    anagram = Anagram()
    anagram.solve('CAR', 'ARC')
