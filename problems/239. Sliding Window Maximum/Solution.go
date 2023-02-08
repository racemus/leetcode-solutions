func maxSlidingWindow(nums []int, k int) []int {
    if len(nums) == 0 || k == 0 {
        return []int{}
    }

    n := len(nums)
    result := make([]int, n-k+1)
    q := make([]int, 0, n)

    for i := 0; i < n; i++ {
        if i >= k && q[0] <= i-k {
            q = q[1:]
        }

        for len(q) > 0 && nums[q[len(q)-1]] <= nums[i] {
            q = q[:len(q)-1]
        }

        q = append(q, i)
        if i >= k-1 {
            result[i-k+1] = nums[q[0]]
        }
    }

    return result
}
