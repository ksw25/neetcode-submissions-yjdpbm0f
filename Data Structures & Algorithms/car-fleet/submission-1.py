class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeedDesc = sorted(list(zip(position, speed)), reverse=True)
        stack= []

        for pos, speed in posSpeedDesc:
            timeTaken = (target-pos)/speed
            if stack and stack[-1]>=timeTaken:
                continue
            stack.append(timeTaken)

        return len(stack)