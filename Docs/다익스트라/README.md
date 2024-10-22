# 다익스트라 알고리즘

### 들어가면서 
어떠한 구현이든 그래프 방향의 유무는 상관 없다. 어떠한 구현이든 음수 사이클이 존재한다면 사용할 수 없다. 구현에 따라 음수 간선(幹線, Edge)이 있을 때도 정상 동작하는 구현이 있고 그렇지 않은 구현이 있다.
다익스트라 알고리즘을 확장시킨 알고리즘이 A* 알고리즘이다. 이 외에도 바로 위에서 언급한 벨만-포드 알고리즘이나 플로이드-워셜 알고리즘도 다익스트라 알고리즘에서 영향을 받았고, 경로탐색 시 가장 기초적이면서 보편적으로 쓰이는 도구인 만큼 프로그래밍을 배우는 사람이라면 반드시 이해하고 넘어가야 하는 중요 개념이다.

## 알고리즘
1. 출발점으로부터 최단거리를 저장할 배열 d[V]를 만들고, 출발 노드에는 0을 출발점을 제외한 다른 노드들에는 매우큰 값 INF를 채워 넣는다. 보통은 최단거리 저장 배열의 이론상 최대에 맞는 INF를 정한다.
2. 현재 노드를 나타내는 변수 A에 출발 노드의 번호를 저장한다.
3. A로 부터 갈 수 있는 임의의 노드 B에 대해, d[A] + p[A][B]와 d[B]의 값을 비교한다. (p[A][B]는 A와 B사의의 거리 이다.)
4. 만약 d[A] + p[A][B]의 값이 더 작다면, 즉 더 짧은 경로라면, d[B]의 값을 이 값으로 갱신시킨다.
5. A의 모든 이웃 노드B에 대해 이 작업을 수행한다.
6. A의 상태를 "방문 완료"로 바꾼다. 그러면 이제 더 이상 A는 사용하지 않는다.
7. "미방문" 상태인 모든 노드들 중, 출발점으로 부터의 거리가 제일 짧은 노드 하나를 골라서 그 노드를 A에 저장한다.
8. 도착 노드가 "방문 완료" 상태가 되거나, 혹으 더 이상 미방문 상태의 노드를 선택할 수 없을 때 까지 3~7의 과정을 반복한다.

## 구현 방법 3가지
### Version 1 
Using a nested for-loop to relax vertices. This is the easiest way to implement Dijkstra's algorithm. The time complexity is O(V^2).
▶ 중첩 반복문을 사용한 간선 업데이트 구현 방식이다. 우선순위 큐를 사용하지 않는 방식으로 가장 가까운 거리의 노드를 찾고 해당 노드와 연결된 노드들의 최단거리를 갱신한다.
 
### Version 2
Priority-queue/heap based implementation + NO re-entrance allowed, where re-entrance means a relaxed vertex can be pushed into the priority-queue again to be relaxed again later.
▶ 우선순위 큐를 사용하되 한 번 방문했던 노드는 절대 다시 방문하지 않는다. 즉 방문한 노드는 우선순위 재삽입하지 않는다. 
 
### Version 3
Priority-queue/heap based implementation + re-entrance allowed.
▶ 2번과 유사하지만 한 번 방문한 노드를 다시 우선순위 큐에 삽입하는 것이 가능하다.
 