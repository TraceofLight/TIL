### 문제의 정의

- 현재의 상태 변화로 인하여 목표 상태가 생기는 것
- 복잡도, 해결가부, 반복성 등으로 구분

### 문제의 해결

- 해결을 위해 시간, 노력, 사고의 투입
- 투입 정도에 따른 결과물의 질적 차이

### 문제의 해결 과정

- 문제에서 문제해결 상태에 도달하기 위한 일련의 처리 및 사고 과정을 순차적으로 나열한 것

### 문제 유형

- 일반적 문제
- 컴퓨팅 기반 문제

#### 컴퓨팅 기반 문제 유형

- 결정 문제
- 탐색 문제
- 연산 가능한 문제
- 최적화 문제

### 일반적인 문제 해결 과정

- 문제 이해 > 해결방안 고안 > 해결책 선택 > 실행 및 평가
  
  - 문제 이해 : 조건과 정보에 대한 바른 이해, 논리적 사고 & 통합적 사고의 필요
  
  - 해결방안 고안 : 문제를 해결할 당사자의 경험 및 지식에 따른 다양한 아이디어 존재, 확장된 사고 필요, 다양한 자료의 수집과 탐색이 기반이 되어 다양한 해결방안을 도출 가능
  
  - 해결책 선택 : 해결책 선택을 위한 수렴적 사고의 필요성 (수렴적 사고 : 다양한 해결 방안 중에서 더 유용하고 효율적이며 가치 있는 것을 선택하기 위한 사고)
  
  - 실행 및 평가 : 과정 중 문제가 발생할 경우 되돌아가 해결책의 문제, 이해 착오 등을 확인해야 함, 목표치에 도달하지 못한 경우도 문제를 확인, 실행 이후 평가는 다음 문제해결의 실행을 위한 중요한 자료

### 컴퓨팅 기반 문제 해결 과정

- 문제 이해 > 해결과정 설계 > 프로그래밍 구현 > 결과물 확인
  
  - 문제 이해 : 문제의 요구 상황에 대한 정확한 파악, 자료의 수집, 문제의 재정의
  - 해결과정 설계 : 알고리즘, 명확한 의미를 갖는 용어로 기술, 절차간 효율적 처리가 가능하도록 기술, 시작과 끝이 반드시 포함, 표현 방식으로는 자연어, 의사코드, 순서도 등이 존재
  - 프로그래밍 구현 : 컴퓨터를 사용하여 결과를 만들어내는 과정 '자동화'
  - 결과물 확인 : 작성한 프로그램에 실제 데이터값을 입력, 처리하여 원하는 결과가 도출되었는지 확인, 실행결과에 대한 검토 및 보안, 효율성에 대한 검토

---

### 선택정렬

가장 작은 것을 선택해서 제일 앞으로 보내는 알고리즘
시간복잡도 O(N^2) << 연산 횟수의 최고차항

---

### 버블정렬

옆에 있는 값과 비교할 때 더 작은 값을 앞으로 보내는 알고리즘
시간복잡도 O(N^2)

---

### 삽입정렬

각 숫자를 적절한 위치에 삽입하는 방법, 정렬된 상태의 경우 매우 빠름
시간복잡도 O(N^2)

---

### 퀵정렬

시간복잡도 O(N\*logN) 이나 이미 정렬이 된 케이스일 경우 O(N^2) 에 수렴한다.

1. Pivot값을 설정
2. 왼쪽에서부터 해당 값보다 큰 숫자 서치, 오른쪽에서부터 해당 값보다 작은 값 서치
3. 두 값을 교체
4. 반복하다가 큰 값이 작은 값보다 오른쪽에 위치할 경우, Pivot값과 작은 값의 위치를 교환
5. Pivot값을 기준으로 좌우 크기 갈리며 다시 퀵정렬 반복

---

### 병합정렬

큰 문제를 작은 문제 2개로 분할하고 이후 정렬하는 방식
일단 최소단위까지 계속 반으로 쪼갠 이후 결합하면서 정렬
시간복잡도 O(N\*logN)

---

### 힙정렬

힙 트리 구조를 이용하는 정렬 방법  
이진 트리 : 모든 노드의 자식 노드가 2개 이하인 트리 구조  
완전 이진 트리 : 자식 노드가 차근차근 들어가서 순서대로 차는 2진 트리 구조
최대 힙 구조 : 이진 트리 기반 부모 노드가 자식 노드보다 큰 힙  
힙 생성 알고리즘 : 특정 노드의 두 자식 중 더 큰 자식과 자신의 위치를 바꾸는 알고리즘

최대 힙 구성을 한 이후 Root 값을 맨 뒤의 값과 교체하면서 트리의 크기를 줄여나가는 과정

시간 복잡도 O(N\*logN)
속도 자체는 퀵정렬이 평균적으로 우위

---

### 카운팅 정렬 (계수 정렬)

시간복잡도 O(N)  
범위 조건이 있는 경우에 한하여 매우 빠른 알고리즘  
숫자를 하나하나 범위 조건과 대조하면서 체크 후 갯수대로 순서 출력

---

### 다익스트라 알고리즘

최단거리 구하는 알고리즘으로 많이 사용
가중치 배치
갈 수 있는 모든 목적지에 대하여 리스트 제작
이후 주변에 갈 수 있는 통로에 대해서 점수 합산
그 점에 도착했을 때 나올 수 있는 점수 중 가중치 최고 혹은 최저만 남기도록 갱신
이후 다른 점들에 대해서도 시행

기초 시간복잡도 O(V^2) 를 가지는 코드는 아래와 같은 과정을 통해 경로를 탐색한다.

```python
# 다음 이동할 정점 변수 선언
next_start_idx = None

# 모든 정점들 중 방문하지 않았고 가장 최단 거리에 있는 지점에 대해서 조사
for idx in range(N):
    if not visited[idx] and min_distance > distance[idx]:
        next_start_idx = idx

# 방문 처리
visited[next_start_idx] = True

# 다음 노드에 대해서 현 시작 지점을 경유하는 것이 더 짧을 경우 갱신
for next_node, next_dist in graph[next_start_idx]:
    distance[next_node] = min(distance[next_node], distance[next_start_idx] + next_dist)
```

다만 가장 최단 거리에 있는 지점 탐색을 우선순위 큐의 사용을 통해 해결한다면 O(E * log V) 의 시간 복잡도를 가지도록 단축할 수 있다.

---

### 다이나믹 프로그래밍

분할정복 기법을 사용할 때 기존에 사용했던 값이 나오면 재사용할 수 있도록 값을 저장

필요할 때 꺼내서 쓸 수 있도록 하는 기법

Top - Down 기법 : 메모이제이션 (최고값부터) > 보통 재귀의 방식으로 사용

Bottom - Up 기법 : 타뷸레이션 (1부터) > 리스트에 값 저장, 반복문 방식으로 사용

해당 방식 사용 시 시간 복잡도 O(n^2)을 O(n)으로 줄일 수 있다

---

## 자식 노드의 갯수를 반환하는 함수

```python
# 자식 노드를 찾고 갯수를 카운팅하는 함수 선언
def find_child(graph_dict: dict, parent_node: int, now_node: int, result_dict: dict) -> None:

    # 현재 노드를 포함하여 기본값 1 설정
    result_dict[now_node] = 1

    # 해당 노드에 연결된 노드들 전수 조사
    for next_node in graph_dict[now_node]:

        # 부모 노드가 아닌 경우에 이어서 조사
        if next_node != parent_node:

            # 다음 노드들에 대해서도 확인
            find_child(graph_dict, now_node, next_node, result_dict)

            # 다음 노드들 값을 현재 노드에 합산
            result_dict[now_node] += result_dict[next_node]

    # 결과 반환
    return result_dict[now_node]
```

트리의 자식 노드를 찾는 방식에 더하여 재귀 형태로 구현

---

## 세그먼트 트리

유한한 일차원 구조가 있을 때 해당 구조에 대해서 모든 구간을 효율적으로 찾기 위해 구성하는 구조

완전 이진 트리의 형태를 갖추고 있다.

```python
def make_seg_tree(result_list: list, target_list: list, start: int, end: int, node: int) -> int:
    '''
    주어진 리스트를 기반으로 구간합 세그먼트 트리를 만들어주는 함수
    '''

    # 커서가 1개로 조여진 경우
    if start == end:

        # 리스트의 값을 노드값으로 지정
        result_list[node] = target_list[start]

    # 커서가 범위를 나타내는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2
        
        # 자식 노드들의 합을 해당 노드의 값으로 지정
        result_list[node] = (
            make_seg_tree(result_list, target_list, start, mid, node * 2)
            + make_seg_tree(result_list, target_list, mid + 1, end, node * 2 + 1)
        )

    # 노드의 값을 반환하여 재귀에 활용
    return result_list[node]

def sum_seg_tree(tree_info: list, start: int, end: int, left: int, right: int, node: int) -> int:
    '''
    구간 범위와 세그먼트 트리가 주어졌을 때 구간합을 반환하는 함수
    '''

    # 찾는 구간이 범위에 없는 경우
    if left > end or right < start:

        # 0을 반환
        return 0

    # 전 구간이 범위에 들어온 경우
    elif left <= start and end <= right:

        # 해당 값을 그대로 반환
        return tree_info[node]

    # 일부 구간만 범위에 존재하는 경우
    else:

        # 이분 탐색 알고리즘을 사용
        mid = (start + end) // 2

        # 구간을 세분화하여 합산
        result = (
            sum_seg_tree(tree_info, start, mid, left, right, 2 * node)
            + sum_seg_tree(tree_info, mid + 1, end, left, right, 2 * node + 1)
        )

        # 합산값을 반환
        return result

def mod_seg_tree(tree_info: list, start: int, end: int, index: int, val: int, node: int) -> None:
    '''
    세그먼트 트리의 값을 변경하는 함수
    '''

    # 찾는 인덱스가 범위에 없는 경우
    if index < start or end < index:

        # 그대로 종료
        return

    # 찾는 인덱스가 구간에 존재하는 경우
    else:

        # 해당 노드에 변경값을 반영
        tree_info[node] += val

        # 커서가 1개로 조여지지 않은 경우
        if start != end:

            # 이분 탐색 알고리즘을 사용
            mid = (start + end) // 2

            # 자식 노드들에 대해서 재귀 함수를 호출하여 조사
            mod_seg_tree(tree_info, start, mid, index, val, node * 2)
            mod_seg_tree(tree_info, mid + 1, end, index, val, node * 2 + 1)
```

기본적으로 모든 구간값에 대해서 세그먼트 트리에 구분이 되어 있는 상태에서 해당 로그에 따라서 움직임을 동일하게 취할 수 있는 후속함수들이 값을 빠르게 확인할 수 있도록 하는 모습을 보이고 있다.
