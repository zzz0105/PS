import heapq

def solution(operations):
    id = 0
    deleted = set()
    max_heap, min_heap = [], []
    
    for op in operations:
        o, n = op.split()
        n = int(n)
        if o == 'I':
            id += 1
            heapq.heappush(max_heap, (-n,id))
            heapq.heappush(min_heap, (n,id))
        else:
            if n == 1:
                while max_heap:
                    num, n_id = heapq.heappop(max_heap)
                    if n_id not in deleted:
                        deleted.add(n_id)
                        break
            else:
                while min_heap:
                    num, n_id = heapq.heappop(min_heap)
                    if n_id not in deleted:
                        deleted.add(n_id)
                        break
    
    answer = [0,0]
    while max_heap:
        num, n_id = heapq.heappop(max_heap)
        if n_id not in deleted:
            answer[0] = -num
            break
    while min_heap:
        num, n_id = heapq.heappop(min_heap)
        if n_id not in deleted:
            answer[1] = num
            break
    
    return answer