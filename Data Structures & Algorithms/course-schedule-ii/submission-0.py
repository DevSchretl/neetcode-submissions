class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #Get all the courses each course points to in array[numCourses]
        #Get number of prereqs for each course in array[numCourses]

        numPre = [0] * numCourses
        prereqs = {i:[] for i in range(numCourses)}

        for dst, src in prerequisites:
            prereqs[src].append(dst)
            numPre[dst] += 1
        
        #Find all courses where num prereqs is 0, add to ouptut array

        worklist = deque()
        output = []

        for i in range(numCourses):
            if numPre[i] == 0:
                worklist.append(i)
                output.append(i)

        #Reduce num prereqs for all outbound courses, add courses with 0 prereqs to queue

        while len(worklist) != 0:

            c = worklist.popleft()

            for i in prereqs[c]:
                numPre[i] = numPre[i] - 1
                if numPre[i] == 0:
                    worklist.append(i)
                    output.append(i)
        
        if len(output) != numCourses:
            return []

        return output


#Goal: Return list where any prereqs for a course come before it



#Find all courses where num prereqs is 0, add to ouptut array
#Reduce num prereqs for all outbound courses, add courses with 0 prereqs to queue
# Repeat until queue is empty, 
# if any course still has prereqs: impossible
        