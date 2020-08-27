# 중복을 없앤것의 길이와 전체 길이의 반 중에 작은걸 고른다.

def solution(nums):
    return min(len(set(nums)), len(nums)//2)
