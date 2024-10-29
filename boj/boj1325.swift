import Foundation

func sol() {
    let NM = readLine()!.split(separator: " ").map{Int($0)!}
    let (N, M) = (NM[0], NM[1])
    
    var graph: [[Int]] = Array(repeating: [] , count : N  + 1)
    for _ in 0..<M {
        let endAndStart = readLine()!.split(separator: " ").map{Int($0)!}
        graph[endAndStart[1]].append(endAndStart[0])
    }

    var visited = Array(repeating: false, count: N + 1)
    func dfs(_ root: Int) -> Int {
        
        var currentDepth = 1
        for next in graph[root] {
            if visited[next] == false {
                visited[next] = true
                currentDepth += dfs(next)
            }
        }
        return currentDepth
    }

    var res: [Int] = [-1]
    for ind in 1...N {
        visited = Array(repeating: false, count: N + 1)
        visited[ind] = true
        res.append(dfs(ind))
    }
    let maxVal = res.max()!
    print(res.enumerated().filter{$0.1 == maxVal}.map{ String($0.0) }.joined(separator: " "))
}
sol()