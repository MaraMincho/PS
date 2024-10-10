
## 이분탐색 햇갈리는거 정리

1. while문 조건
   - mid값이 최소 한개 이상 있을 때 이분탐색을 진행할 수 있습니다.
   - while문 돌아갈 때 조건은 `lo + 1 < hi`로 설정합니다.

2. lo = mid, hi = mid로 값을 업데이트 합니다.

3. Check(mid)의 return값이 Bool
   - 이분 탐색 이후 True, False값을 통해 이분탐색을 결정할 때, lo를 리턴합니다. 

4. Check(mid)의 return값이 Val이라 LowerBound, UpperBound가 된다면?
   - 탐색이후 lowerBound, uppberBound가 결정 함수라면 hi를 리턴합니다. 

5. UpperBound, LowerBound를 좀 더 직관적으로 이해하기
   - lowerBound는 v[i - 1] < k <= v[i]인 i를 찾아주는 함수로, v[i] >= k인 i의 최솟값을 반환합니다. `(등호는 <)`
     - `if calculate(mid) < taret` 
   - upper_bound는 v[i - 1] <= k < v[i]인 i를 찾아주는 함수로 v[i] > k인 i의 최솟값을 반환합니다. `(등호는 <=)`
     - `if calculate(mid) <= taret`