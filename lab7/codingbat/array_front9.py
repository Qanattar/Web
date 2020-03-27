def array_front9(nums):
  for i in range(0,4):  
    if nums[i] == 9:
      return True
  return False

print(array_front9([1,2,3,4,3]))