//import Foundation
//
//
//let file = FileIO()
//let directions = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]
//let (R, C, M) = (file.readInt(), file.readInt(), file.readInt())
//let tr = 2 * (R - 1)
//let tc = 2 * (C - 1)
//
//struct Shark {
//  var row: Int
//  var col: Int
//  var speed: Int
//  var direction: Int
//  var curDirection: (Int, Int) { return (directions[direction][0], directions[direction][1]) }
//  var size: Int
//  init(_ r: Int, _ c: Int, _ s: Int, _ d: Int, _ z: Int) {
//    self.row = r
//    self.col = c
//    self.speed = s
//    self.direction = d
//    self.size = z
//  }
//  mutating func move() {
//    var curRow = (row + curDirection.0 * speed) % tr
//    var curCol = (col + curDirection.1 * speed) % tc
//    if (direction == 1 || direction == 2 ) {
//      if curRow < 0 {
//        curRow = abs(curRow)
//        self.direction = direction == 1 ? 2 : 1
//      }
//      
//      if curRow >= R - 1 {
//        curRow = (R - 1) - (curRow % (R - 1))
//        self.direction = direction == 1 ? 2 : 1
//      }
//      
//    }else if (direction == 3 || direction == 4 ) {
//      if curCol < 0 {
//        curCol = abs(curCol)
//        self.direction = direction == 3 ? 4 : 3
//      }
//      
//      if curCol >= C - 1 {
//        curCol = (C - 1) - (curCol % (C - 1))
//        self.direction = direction == 3 ? 4 : 3
//      }
//      
//    }
//    self.row = curRow
//    self.col = curCol
//  }
//}
//
//struct Position: Hashable {
//  var row: Int
//  var col: Int
//}
//
//struct SharkSystem {
//  var board: [Position: [Shark]] = .init()
//  var res: Int = 0
//  init() { }
//  mutating func start() {
//    addShark(M)
//    for col in 0..<C {
//      catchShark(col: col)
//      moveShark()
//      removeShark()
//    }
//  }
//  
//  mutating func addShark(_ count: Int) {
//    (0..<count).forEach { _ in
//      let curShark: Shark = .init(file.readInt() - 1, file.readInt() - 1, file.readInt(), file.readInt(), file.readInt())
//      board[.init(row: curShark.row, col: curShark.col), default: []].append(curShark)
//    }
//  }
//  
//  mutating func catchShark(col: Int) {
//    for i in 0..<R {
//      if let shark = board[.init(row: i, col: col)]?.first {
//        res += shark.size
//        board[.init(row: i, col: col)] = nil
//        return
//      }
//    }
//  }
//  mutating func moveShark() {
//    var newBoard: [Position: [Shark]] = .init()
//    board.values.flatMap{$0}.forEach{ shark in
//      var shark = shark
//      shark.move()
//      newBoard[.init(row: shark.row, col: shark.col), default: []].append(shark)
//    }
//    board = newBoard
//  }
//  
//  mutating func removeShark() {
//    var newBoard: [Position: [Shark]] = .init()
//    board.values.map { sharks -> Shark in
//      if sharks.count > 1 {
//        let curShark = sharks.max{$0.size < $1.size}!
//        return curShark
//      }
//      return sharks.first!
//    }
//    .forEach { shark in
//      newBoard[.init(row: shark.row, col: shark.col), default: []] = [shark]
//    }
//    board = newBoard
//  }
//}
//
