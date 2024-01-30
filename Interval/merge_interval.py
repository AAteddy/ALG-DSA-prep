def is_overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


def merge_overlap(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        merge = [intervals[0]]

        for i in intervals[1:]:
            if is_overlap(merge[-1], i):
                merge[-1] = merge_overlap(merge[-1], i)
            else:
                merge.append(i)
        return merge
