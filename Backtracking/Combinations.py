class Solution:

    def combine(self, n: int, k: int):
        nums = list(range(1, n + 1))
        combinations = []

        def backtracking(results, path, depth, options):
            if depth == 0:
                results.append(path[:])
                return
            else:
                for index, num in enumerate(options):
                    path.append(num)
                    backtracking(results, path, depth - 1, options[index + 1:])
                    path.pop()

        backtracking(combinations, [], k, nums)

        return combinations

obj= Solution()
print (obj.combine(4,3))