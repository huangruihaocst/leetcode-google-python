class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        last_t = -1
        res = 0
        for p, s in cars:
            t = (target - p) / s
            if t > last_t:
                last_t = t
                res += 1
        return res
