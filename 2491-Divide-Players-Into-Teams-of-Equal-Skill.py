class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        total_sum=skill[0]+skill[-1]
        chem_sum=0
        for i in range(n//2):
            if skill[i]+skill[n-i-1] != total_sum:
                return -1
            else:
                chem_sum+=skill[i]*skill[n-i-1]
        return chem_sum