import heapq


def min_cost(cable_len):
    if not cable_len:
        return 0

    heapq.heapify(cable_len)
    total_cost = 0

    while len(cable_len) > 1:
        first = heapq.heappop(cable_len)
        second = heapq.heappop(cable_len)
        union = first + second
        total_cost += union
        heapq.heappush(cable_len, union)

    return total_cost


def merge_k_lists(lists):
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


cables = [4, 3, 2, 6]
print("Мінімальні витрати:", min_cost(cables))

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
