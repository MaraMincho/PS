import Foundation

func sol() -> String {
    let n = Int(readLine()!)!
    let arrs = readLine()!.split(separator: " ").map{Int($0)! - 1}
    var prev: [Int] = []
    var visited = Array(repeating: false, count: n)
    var res = 0

    func dfs(_ cur: Int) {
        if visited[cur] == true {
            if prev.contains(cur) {
                res += prev[prev.firstIndex(of: cur)!...].count
            }
            return 
        }

        visited[cur] = true
        prev.append(cur)
        dfs(arrs[cur])
    }

    for i in 0..<n {
        if visited[i] == false {
            prev = []
            dfs(i)
        }
    }
    return "\(n - res)"
}

let result = (0..<Int(readLine()!)!).map{ _ in
    return sol()
}
print(result.joined(separator: "\n"))