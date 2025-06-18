def canFinish(numCourses, prerequisites):
    from collections import defaultdict

    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(course):
        if visited[course] == 1:
            return False  # cycle detected
        if visited[course] == 2:
            return True   # already validated

        visited[course] = 1
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        visited[course] = 2
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False

    return True
