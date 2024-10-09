
func solxx() {
  let N = Int(readLine()!)!
  let ino = readLine()!.split(separator: " ").map{Int($0)!}
  let poo = readLine()!.split(separator: " ").map{Int($0)!}
  var tree: [Int: (Int?, Int?)] = [:]
  func cq(_ inoStart: Int, _ inoEnd: Int, _ pooStart: Int, _ pooEnd: Int) -> Int? {
    guard inoStart <= inoEnd, pooStart <= pooEnd else { return nil }
    if inoEnd == inoStart {
      return ino[inoStart]
    }
    let rootVal = poo[pooEnd]
    let inoRootInd = ino.firstIndex(of: rootVal)!
    
    let depth = inoRootInd - 1 - inoStart
    let pooStartInd = depth + pooStart
    
    let leftChildVal: Int? = cq(inoStart, inoRootInd - 1, pooStart, pooStartInd)
    let rightChildVal: Int? = cq(inoRootInd + 1, inoEnd,  pooStartInd + 1, pooEnd - 1)
    tree[rootVal] = (leftChildVal, rightChildVal)
    return rootVal
  }
  let root = cq(0, N - 1, 0, N - 1)!
  var res: [Int] = []
  func preOrder(_ root: Int) {
    res.append(root)
    if let (leftVal, rightVal) = tree[root] {
      if leftVal != nil {
        preOrder(leftVal!)
      }
      if rightVal != nil {
        preOrder(rightVal!)
      }
    }
  }
  preOrder(root)
  print(res.map{String($0)}.joined(separator: " "))
}
