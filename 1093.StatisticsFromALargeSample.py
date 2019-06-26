class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        num_count = sum(count)
        
        def cal_median():
            if num_count % 2 == 1:
                mid = num_count // 2 + 1
                s = 0
                for i, v in enumerate(count):
                    s += v
                    if s >= mid:
                        return i
            else:
                small, big = num_count // 2, num_count // 2 + 1
                small_i, big_i = None, None
                s = 0
                for i, v in enumerate(count):
                    s += v
                    if s >= small and small_i is None:
                        small_i = i
                    if s >= big and big_i is None:
                        big_i = i
                return (small_i + big_i) / 2
        
        minimum = next(i for i, v in enumerate(count) if v != 0)
        maximum = next(255 - i for i, v in enumerate(reversed(count)) if v != 0)
        mean = sum(i * v for i, v in enumerate(count)) / num_count
        median = cal_median()
        mode = max((i for i in range(255)), key=lambda i: count[i])
        
        return [float(minimum), float(maximum), float(mean), float(median), float(mode)]

