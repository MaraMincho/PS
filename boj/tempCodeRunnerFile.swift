import Foundation

func sol() {
  let NK = readLine()!.split(separator: " ").map{Int($0)!}
  let N = NK[0]
  let K = NK[1]
  let arr = readLine()!.split(separator: " ").map{Int($0)!}

  var left = 0
  var right = 0
  var res = arr[0] % 2 == 0 ? 1 : 0
  var prev = K - (arr[0] % 2 == 0 ? 0 : 1)
  while right + 1 < N {
    if arr[right + 1] % 2 == 1 {
      if prev == 0 {
        while left < right && arr[left] % 2 != 1 {
          left += 1
        }
        left += 1
        prev += 1
      }
      prev -= 1
    }
    right += 1
    res = max(res, right - left + 1 - (K - prev))
  }
  print(res)
}
sol()

// 8 4
// 1 3 5 7 9 12 14 26
