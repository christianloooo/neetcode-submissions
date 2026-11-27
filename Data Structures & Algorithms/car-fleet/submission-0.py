class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        slowest = 0.0
        fleets = 0

        for pos, sp in cars:
            time = (target-pos) / sp
            if time > slowest:
                fleets+=1
                slowest = time
        return fleets