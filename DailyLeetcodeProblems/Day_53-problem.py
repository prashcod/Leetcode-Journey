
# 3505. Minimum Operations to Make Elements Within K Subarrays Equal


# # You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):

# # Increase or decrease any element of nums by 1.
# # Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.

 

# # Example 1:

# # Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

# # Output: 8

# # Explanation:

# # Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
# # Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
# # Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.
# # Example 2:

# # Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2

# # Output: 3

# # Explanation:

# # Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
# # Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.


def minOperations(nums , k , x): 
        n = len(nums)

        # Two heaps:
        # low  = max heap (lower half)
        # high = min heap (upper half)

        low = []
        high = []

        low_size = 0
        high_size = 0

        low_sum = 0
        high_sum = 0

        active = [False] * n
        side = [0] * n  # 0 = low, 1 = high

        def prune(heap):
            while heap and not active[heap[0][1]]:
                heapq.heappop(heap)

        def rebalance(total):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low)
            prune(high)

            target = (total + 1) // 2

            # Move elements from low to high
            while low_size > target:
                prune(low)
                neg_val, idx = heapq.heappop(low)
                val = -neg_val

                heapq.heappush(high, (val, idx))

                side[idx] = 1
                low_size -= 1
                high_size += 1

                low_sum -= val
                high_sum += val

            # Move elements from high to low
            while low_size < target:
                prune(high)
                val, idx = heapq.heappop(high)

                heapq.heappush(low, (-val, idx))

                side[idx] = 0
                high_size -= 1
                low_size += 1

                high_sum -= val
                low_sum += val

        def add(idx, total):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            val = nums[idx]

            prune(low)

            active[idx] = True

            if not low or val <= -low[0][0]:
                heapq.heappush(low, (-val, idx))
                side[idx] = 0
                low_size += 1
                low_sum += val
            else:
                heapq.heappush(high, (val, idx))
                side[idx] = 1
                high_size += 1
                high_sum += val

            rebalance(total)

        def remove(idx, total):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            val = nums[idx]
            active[idx] = False

            if side[idx] == 0:
                low_size -= 1
                low_sum -= val
            else:
                high_size -= 1
                high_sum -= val

            rebalance(total)

        # Step 1: Calculate the cost of every window
        costs = []

        for i in range(x):
            add(i, i + 1)

        def get_cost():
            median = -low[0][0]

            left_cost = median * low_size - low_sum
            right_cost = high_sum - median * high_size

            return left_cost + right_cost

        costs.append(get_cost())

        for i in range(x, n):
            remove(i - x, x - 1)
            add(i, x)

            costs.append(get_cost())

        # Step 2: Dynamic Programming
        # prev[i] = minimum cost using exactly j-1
        # subarrays within the first i elements.

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Option 1: Skip current element
                curr[i] = curr[i - 1]

                # Option 2: Select a window ending at i-1
                if i >= x:
                    pick = prev[i - x] + costs[i - x]

                    curr[i] = min(curr[i], pick)

            prev = curr

        return prev[n]




nums = [5,-2,1,3,7,3,6,4,-1]
x = 3
k = 2
ans = minOperations(nums , k , x)
print(ans)
