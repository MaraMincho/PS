////
////  Heap.swift
////  codingTest
////
////  Created by MaraMincho on 3/15/24.
////
//
//import Foundation
//
//struct FirstMakeHeap<T> where T: Comparable {
//  var elements: [T] = []
//  var isMaxHeap: Bool
//  init(isMaxHeap: Bool) { self.isMaxHeap = isMaxHeap}
//  var count: Int { return elements.count - 1}
//  
//  mutating func append(_ element: T) {
//    if count == -1 { elements.append(element) }
//    elements.append(element)
//    push(count)
//  }
//  
//  func last() -> T? {
//    if !elements.indices.contains(1) {
//      return nil
//    }
//    return elements[1]
//  }
//  
//  mutating func push(_ ind: Int) {
//    let pInd = ind / 2
//    if pInd == 0 {
//      return
//    }
//    let p = elements[pInd]
//    let cur = elements[ind]
//    if (isMaxHeap && p < cur) || (!isMaxHeap && p > cur) {
//      elements.swapAt(ind, pInd)
//      push(pInd)
//    }
//  }
//  
//  mutating func delete() -> T?{
//    guard count >= 1 else {
//      return nil
//    }
//    
//    let ind = count
//    elements.swapAt(ind, 1)
//    let deleteVal = elements.popLast()
//    if isMaxHeap {
//      moveDownWithAscending(1)
//    }
//    else {
//      moveDownWithDescending(1)
//    }
//    
//    return deleteVal
//  }
//  
//  mutating private func moveDownWithAscending(_ ind: Int) {
//    let leftInd = ind * 2
//    let rightInd = leftInd + 1
//    
//    let sortedInd = [ind, leftInd, rightInd].filter{ elements.indices.contains($0) }.map{ ($0, elements[$0]) }.sorted{$0.1 > $1.1}.map{$0.0}
//    
//    if ind == sortedInd.first {
//      return
//    }else if let firstInd = sortedInd.first {
//      elements.swapAt(ind, firstInd)
//      moveDownWithAscending(firstInd)
//    }
//  }
//  
//  mutating private func moveDownWithDescending(_ ind: Int) {
//    let leftInd = ind * 2
//    let rightInd = leftInd + 1
//    let sortedInd = [ind, leftInd, rightInd].filter{elements.indices.contains($0)}.map{($0, elements[$0])}.sorted{$0.1 < $1.1}.map{$0.0}
//    
//    if ind == sortedInd.first {
//      return
//    }else if let firstInd = sortedInd.first {
//      elements.swapAt(ind, firstInd)
//      moveDownWithDescending(firstInd)
//    }
//  }
//}
//
//struct MaxHeap<T> where T: Comparable {
//  var count: Int { elements.count - 1}
//  var peak: T? { elements.indices.contains(1) ? elements[1] : nil }
//  var isEmpty: Bool { !elements.indices.contains(1) }
//  var elements: [T] = []
//  
//  mutating func append(_ element: T) {
//    if isEmpty {
//      elements.append(element)
//    }
//    elements.append(element)
//    push(count)
//  }
//  
//  private mutating func push(_ ind: Int) {
//    let pInd = ind / 2
//    if pInd == 0 {
//      return
//    }
//    if elements[pInd] < elements[ind] {
//      elements.swapAt(pInd, ind)
//      push(pInd)
//    }
//  }
//  
//  mutating func delete() -> T? {
//    guard elements.indices.contains(1) else {
//      return nil
//    }
//    
//    let ind = count
//    elements.swapAt(ind, 1)
//    let deleteVal = elements.popLast()
//    shift(1)
//    
//    return deleteVal
//  }
//  
//  private mutating func shift(_ ind: Int) {
//    let leftInd = ind * 2
//    let rightInd = ind * 2 - 1
//    var targetInd = ind
//    
//    if elements.indices.contains(leftInd) && elements[leftInd] > elements[targetInd] {
//      targetInd = leftInd
//    }
//    
//    if elements.indices.contains(rightInd) && elements[rightInd] > elements[targetInd] {
//      targetInd = rightInd
//    }
//    
//    if targetInd != ind {
//      elements.swapAt(ind, targetInd)
//      shift(targetInd)
//    }
//  }
//  
//}
//
//struct MinHeap<T> where T: Comparable {
//  var count: Int { elements.count - 1}
//  var peak: T? { elements.indices.contains(1) ? elements[1] : nil }
//  var isEmpty: Bool { !elements.indices.contains(1) }
//  var elements: [T] = []
//  
//  init() {}
//  
//  mutating func append(_ element: T) {
//    if isEmpty { elements.append(element) }
//    elements.append(element)
//    push(count)
//  }
//  
//  private mutating func push(_ ind: Int) {
//    let pInd = ind / 2
//    if pInd == 0 {
//      return
//    }
//    if elements[pInd] > elements[ind] {
//      elements.swapAt(ind, pInd)
//      push(pInd)
//    }
//  }
//  
//  mutating func delete() -> T?{
//    let ind = count
//    guard ind >= 1 else {
//      return nil
//    }
//    
//    elements.swapAt(ind, 1)
//    let deleteVal = elements.popLast()
//    shiftDown(1)
//    
//    return deleteVal
//  }
//
//  private mutating func shiftDown(_ ind: Int) {
//    let leftInd = ind * 2
//    let rightInd = leftInd + 1
//    var targetInd = ind
//    let count = count
//    
//    if leftInd < count && elements[leftInd] < elements[targetInd] {
//      targetInd = leftInd
//    }
//    
//    if leftInd < count && elements[rightInd] < elements[targetInd] {
//      targetInd = rightInd
//    }
//    
//    if targetInd == ind {
//      return
//    }
//    
//    elements.swapAt(ind, targetInd)
//    shiftDown(targetInd)
//  }
//}
