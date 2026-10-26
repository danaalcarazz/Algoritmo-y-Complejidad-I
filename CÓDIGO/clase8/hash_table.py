class Solution:
    def twoSum(self, nums, target):
        vistos = {}

        for i, numero in enumerate(nums):
            complemento = target - numero

            if complemento in vistos:
                return [vistos[complemento], i]

            vistos[numero] = i

        return []