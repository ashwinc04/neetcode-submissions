class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        k=[]
        for pos, spd in cars:
            time = (target - pos) / spd
            if not k or time > k[-1]:
                k.append(time)
        return len(k)