class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        t_sum=sum(nums)
        rem=t_sum%p
        if rem==0:
            return 0
        if t_sum <p:
            return -1
        p_sum=0
        min_len=len(nums)
        prefixxmap={0:-1}
        for i ,num in enumerate(nums):
            p_sum=(p_sum+num)%p
            req_mod=(p_sum - rem) %p 
            if req_mod in prefixxmap:
                min_len=min(min_len,i-prefixxmap[req_mod])
            prefixxmap[p_sum]=i
        if min_len<len(nums):
            return min_len 
        else:
            return -1