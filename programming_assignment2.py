import random


class Anagram:
    num_iterations = 0

    def anagram_expand(self, state, goal):
        node_list = []

        # Create each possible state that can be created from the current one in a single step
        for pos in range(1, len(state)):
            new_state = state[1:pos + 1] + state[0] + state[pos + 1:]

            # TO DO: c. Very simple h' function - please improve!
            # if new_state == goal:
            #     score = 0
            # else:
            #     score = 1
            incorrect_element_count = 0
            if (state != goal):
                incorrect_element_count += 1
            # for i in state:
            #     for j in goal:
            #         if(i==j):
            #             incorrect_element_count+=1

            h_score = incorrect_element_count
            # combined_elements=zip(state,goal)
            # incorrect_element_count=0
            # for state,goal in combined_elements:
            #     if(state!=goal):
            #         incorrect_element_count+=1

            # h_score=incorrect_element_count

            node_list.append((new_state, h_score))

        # for x,y in node_list:
        #     print(x,y)

        return node_list

    # TO DO: b. Return either the solution as a list of states from start to goal or [] if there is no solution.
    def a_star(self, start, goal, expand):
        open_list = [(start, 190)]
        closed_list = []
        # g_score=0
        # g_score=[0]
        # temp_f_score_list=[]
        a = 2  # var for inital g_score

        while start != goal:
            closed_list.append((start, 190))  # node already visited
            child_list = self.anagram_expand(start, goal)
            g_score = a*5
            for i in child_list:
                # print(i)
                h_score = i[1]
                # print(h_score)
                f_score = g_score+h_score
                # print(f_score)
                val = i[0]
                # print(val,f_score)
                open_list.append((val, f_score))
            min_value = self.get_minimum(open_list, closed_list)
            start = min_value[0]
            self.num_iterations += 1

        visited_state = [t[0] for t in closed_list]

        return visited_state

    def get_minimum(self, open_list, closed_list):
        flag = True
        duplicate_list = open_list
        while (flag):
            # getting mim f-score from dup list
            min_f_value = min(duplicate_list, key=lambda x: x[1])
            # print(min_f_value)
            if (min_f_value in closed_list):
                duplicate_list.remove(min_f_value)
                pass
                # return duplicate_list
            else:
                closed_list.append(min_f_value)
                flag = False
                return min_f_value

    # Finds a solution, i.e., the set of steps from one word to its anagram

    def solve(self, start, goal):

        self.num_iterations = 0

        # TO DO: a. Add code below to check in advance whether the problem is solvable

        # if ...
        #    print('This is impossible to solve')
        #    return "IMPOSSIBLE"
        # we can check the parity of the string
        start_char = {}  # dictionary to count starting characters frequency
        goal_char = {}  # dictionary to count goal characters frequency
        odd_start = 0  # counting the odd parity of start value
        even_start = 0  # counting the even parity of start value
        odd_goal = 0  # counting the odd parity of goal value
        even_goal = 0  # counting the even parity of goal value

        for char in start:
            # self.num_iterations+=1
            if char in start_char:
                start_char[char] = start_char[char]+1
            else:
                start_char[char] = 1

        # print(self.num_iterations)

        for count in start_char.values():
            if (count % 2 != 0):
                odd_start = odd_start+1
            else:
                even_start = even_start+1

        if (odd_start > even_start):
            print("Start is Odd Parity")

        else:
            print("Start is Even Parity")

        for char in goal:
            # self.num_iterations+=1
            if char in goal_char:
                goal_char[char] = goal_char[char]+1
            else:
                goal_char[char] = 1

        # print(self.num_iterations)

        for count in goal_char.values():
            if count % 2 != 0:
                odd_goal = odd_goal+1
            else:
                even_goal = even_goal+1

        if (odd_goal > even_goal):
            print("Goal is Odd Parity")

        # elif()

        else:
            print("Goal is Even Parity")

        # print(start_char)
        # print(goal_char)

        if (start_char != goal_char):
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

        print(str(self.num_iterations) +
              ' A* iterations were performed to find this solution.')

        return str(self.num_iterations)


if __name__ == '__main__':
    anagram = Anagram()
    anagram.solve('TEARDROP', 'PREDATOR')
