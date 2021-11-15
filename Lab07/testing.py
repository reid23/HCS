#%%
class foo:
    """docstring for foo"""
    ONE=1
    TWO=2
    THREE=3
    FOUR=4
    FIVE=5
    def __init__(self, nums):
        self.nums = nums
    def getItemFromNum(self, item):
        return self.nums[item]

#%%
f=foo([1,2,3,4,5,6,7,8,9,0])

#%%
print('f.getItemFromNum()')
print(f.getItemFromNum(f.ONE))
# %%
