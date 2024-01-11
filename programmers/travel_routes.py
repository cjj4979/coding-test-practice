def solution(tickets):
    routes = []
    def dfs(idx, vlist, vset, count):
        if count == len(tickets):
            route = []
            for i in vlist:
                route.append(tickets[i][0])
            route.append(tickets[vlist[len(vlist)-1]][1])
            routes.append(route)
            return
        
        for i in range(len(tickets)):
            if i not in vset and tickets[idx][1] == tickets[i][0]:
                dfs(i, vlist + [i], vset | {i}, count+1)
            
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            dfs(i, [i], set([i]), 1)
    
    answer = routes[0]
    for i in range(1, len(routes)):
         if routes[i] < answer:
                answer = routes[i]
                
    return answer
