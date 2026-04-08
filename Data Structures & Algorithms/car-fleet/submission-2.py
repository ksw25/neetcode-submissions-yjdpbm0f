class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeedDesc = sorted(list(zip(position, speed)), reverse=True)
        fleets =0
        lastTime =0

        for pos, speed in posSpeedDesc:
            timeTaken = (target-pos)/speed
            if timeTaken>lastTime:
                fleets+=1
                lastTime=timeTaken

        return fleets