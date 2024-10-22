import Foundation

// 오답입니다. 프로그래머스에서는 정답처리지만 백준에서는 오답입니다.
func solution(_ operations:[String]) -> [Int] {
    var ansQueue:[Int] = []
    for i in operations {
        let node = i.split(separator: " ").map{String($0)}
        if node[0] == "I"{
            ansQueue.append(Int(node[1])!)
        }
        else if !ansQueue.isEmpty{
            ansQueue = ansQueue.sorted(by: <)

            if node[1] == "-1" {
                _ = ansQueue.removeFirst()
                continue
            }
            _ = ansQueue.removeLast()
        }
    }
    ansQueue = ansQueue.sorted(by: <)

    return ansQueue.count == 0 ? [0, 0] : [ansQueue.last!, ansQueue[0]]
}

let n = Int(readLine()!)!
var res: [String] = []
for _ in 0..<n {
    var operations: [String] = [] 
    for _ in 0..<Int(readLine()!)! {
        operations.append(readLine()!)
    }
    let answer = solution(operations)
    if answer == [0, 0] {
        res.append("EMPTY")
    }else {
        res.append("\(answer[0]) \(answer[1])")
    }
    
}
print(res.joined(separator: "\n"))