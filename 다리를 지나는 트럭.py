# 다리길이만큼 0을 채운 리스트를 이용해 트럭이 건너는걸 시뮬레이션
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for c in range(bridge_length)]

    timer = 0
    while len(truck_weights) > 0:
        if sum(bridge[1:]) + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            while bridge[1] == 0:
                bridge.pop(0)
                bridge.append(0)
                timer += 1
            bridge.append(0)

        timer += 1
        bridge.pop(0)

    timer += len(bridge)
    return timer
