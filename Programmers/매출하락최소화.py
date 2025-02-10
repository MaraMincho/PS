import collections
def solution(sales, links):
    answer = 0
    tree = {}
    # key: 팀원 value: 팀번호
    pu = {}
    for (parent, child) in links:
        tree[parent] = tree.get(parent, []) + [child]
    
    # parent, child ....
    teams = {}
    teamIndex = 0
    def make(parent, depth):
        nonlocal teamIndex, tree, teams, pu
        cur = [parent]
        pl = []
        for member in tree[parent]:
            cur.append(member)
            
            if tree.get(member) :
                make(member, depth + 1)
                pl.append(member)
        teams[teamIndex] = cur
        for cpl in pl :
            pu[cpl] = teamIndex
        teamIndex += 1
    make(1, 0)
    
    q = collections.deque()
    
    answer = 100_000_000_000
    visited = list(map(lambda _: False, range(teamIndex)))
    tempAnswer = 0
    def go(nextTeamIndex) :
        nonlocal teamIndex, teams, answer, tempAnswer
        
        if nextTeamIndex == teamIndex:
            answer = min(answer, tempAnswer)
            return
        
        if visited[nextTeamIndex] :
            go(nextTeamIndex + 1)
            return
        
        myTeams = teams[nextTeamIndex]
        
        for index in range(len(myTeams)):
            member = myTeams[index]
            tempAnswer += sales[member - 1]
            visited[nextTeamIndex] = True
            if index == 0 and member != 1:
                visited[pu[member]] = True
            go(nextTeamIndex + 1)
            tempAnswer -= sales[member - 1]
            visited[nextTeamIndex] = False
            if index == 0 and member != 1:
                visited[pu[member]] = False
            
    go(0) 
    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],	[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))