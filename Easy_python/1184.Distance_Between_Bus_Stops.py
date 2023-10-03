def distance_between_bus_stops(distance: list[int], start: int, destination: int) -> int:
    min_distance = sum(distance[start: destination])
    min_distance_ = sum(distance[:start]) + sum(distance[destination:])
    return min(min_distance_, min_distance)


if __name__ == '__main__':
    distance = [7,10,1,12,11,14,5,0]
    start = 7
    destination = 2
    print(f'Ans: {distance_between_bus_stops(distance, start, destination)}')
