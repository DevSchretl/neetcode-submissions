class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqs = {i: [] for i in range(numCourses)}

        for p in prerequisites:
            prereqs[p[0]].append(p[1])
        
        visited = set()
        
        def dfs(course) -> bool:

            if course in visited:
                return False
            
            visited.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            prereqs[course] = []
            return True


        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True


        






#[0, 1]:   0 -> 1

#[0, 1], [1, 2], [2, 0]     0 -> 1 -> 2
#                           ^---------

#[0, 1], [1, 2]    0 -> 1 -> 2    3
                        

#array of all prereqs each course gives (outbound arrow)
# index is array position

# Check for cycles
# DFS: Hold path, check for duplicates


        