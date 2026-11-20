class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stackTimes = []
        cars = [(pos,speed) for pos,speed in zip(position,speed)]
        cars.sort(reverse = True)

        for pos, speed in cars:
            time = (target - pos) / speed
            if not stackTimes:
                stackTimes.append(time)
                continue
            
            if time < stackTimes[-1]:
                time = stackTimes[-1]
                stackTimes.append(time)

            if time >= stackTimes[-1]:
                stackTimes.append(time)

        stackTimes = set(stackTimes)

        return len(stackTimes)