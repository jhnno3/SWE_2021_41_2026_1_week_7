from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    ans = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                ans.append(i)
                ans.append(j)
                return ans
            
def main():
    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3, 3], 6))
    
main()