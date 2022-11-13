def get_list() -> list:
    return list(range(0, 1_000_000, 2))


class Solution:


    def find_target(self, list, target):
        self.list = get_list()
        low = 0
        high = len(self.list)
        mid = int(high) // 2
        while True:
            if target < high:
                if target == mid:
                    return int(mid) // 2
                elif target > mid:
                    low = mid
                    mid = (low + high) // 2
                    continue
                elif target < mid:
                    high = mid
                    mid = (low + high) // 2
                    continue
            else:
                 return f"error"



print(Solution().find_target(get_list(), 500000))
