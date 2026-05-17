class Solution:
    def replaceElements(self, arr):
        rightmax = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = rightmax
            rightmax = max(rightmax, temp)

        return arr