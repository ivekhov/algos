# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = [big, 0]         # 1 0
        self.medium = [medium, 0]   # 1 0
        self.small = [small, 0]     # 0 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big[0] > self.big[1]:
                self.big[1] += 1
                return True
            else:
                return False

        elif carType == 2:
            if self.medium[0] > self.medium[1]:
                self.medium[1] += 1
                return True
            else:
                return False

        elif carType == 3:
            if self.small[0] > self.small[1]:
                self.small[1] += 1
                return True
            else:
                return False


if __name__ == '__main__':
    tests = [
        [
            [1, 1, 0], [1], [2], [3], [1], [None, True, True, False, False],
        ],
    ]
    s = ParkingSystem(0, 0, 2)
    # print(s)
    print(s.addCar(1))
    print(s.addCar(2))
    print(s.addCar(3))
    # print(s.addCar(1))


