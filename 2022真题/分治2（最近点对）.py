'''
在《三体》中，人类舰队中的万有引力号和蓝色空间号进入到了四维世界。在三维世界中，一个坐标可以视作(c,y,z的三元组，进入四维世界后，则需要四元组(ac,y,z,w)才能唯一定位了。

在三维世界中建造出的导航系统因为缺乏高维感知能力，无法继续使用，舰长找到了你希望你能开发一个程序，辅助飞船运行。因为不知道四维空间内是否可能通往更高维
的空间，舰长需要你开发一个适配各个维度的程序。为了验证你的程序是否正确，舰长会给你n个k维空间的点，你需要回报这些点中，最近的点对的距离是多少。在这里定
义两个k维点(21,t2...tk)和(y1,y...yk)的距离S =  (1 - 1)2 +(22 - 22 + ... + (ak - yk)2

输入格式:
输入的第一行是两个整数n,k(2 < n < 5000,1 <  < 10)，分别代表点的个数和维度
接下来n行包含k个整数，每个数的绝对值小于105，按顺序标识一个k维点的坐标。

输出格式:
为了避免误差，假设所有点对的最小距离为ans,请你输出ans?的值.
题目数据保证答案在64位整数范围内

输入样例:
5 2
1 1
1 9
9 1
9 9
0 10
输出样例:
2
'''

import sys
import math


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a.coordinates, b.coordinates)))


def closest_pair_distance(points, left, right):
    if right - left <= 3:
        min_dist = sys.maxsize
        for i in range(left, right + 1):
            for j in range(i + 1, right + 1):
                min_dist = min(min_dist, distance(points[i], points[j]))
        return min_dist

    mid = (left + right) // 2
    left_dist = closest_pair_distance(points, left, mid)
    right_dist = closest_pair_distance(points, mid + 1, right)
    min_dist = min(left_dist, right_dist)

    strip = [point for point in points[left:right + 1] if
             abs(point.coordinates[0] - points[mid].coordinates[0]) < min_dist]
    strip.sort(key=lambda point: point.coordinates[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j].coordinates[1] - strip[i].coordinates[1] < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))

    return min_dist


def main():
    n, dimensions = map(int, input("").split())
    points = []

    print("")
    for _ in range(n):
        coordinates = tuple(map(int, input().split()))
        points.append(Point(coordinates))

    points.sort(key=lambda point: point.coordinates[0])
    result = closest_pair_distance(points, 0, n - 1)

    print(int(result**2))


if __name__ == "__main__":
    main()