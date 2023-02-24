#### Approach 1: Schoolbook Addition

**Intuition**

Let's add numbers in a schoolbook way, column by column. For example, to add $123$ and $912$, we add $3+2$, then $2+1$, then $1+9$. Whenever our addition result is more than $10$, we carry the $1$ into the next column. The result is $1035$.

**Algorithm**

We can do a variant of the above idea that is easier to implement - we put the entire addend in the first column from the right.

Continuing the example of `123` + `912`, we start with `[1, 2, 3+912]`. Then we perform the addition `3+912`, leaving `915`. The `5` stays as the digit, while we 'carry' `910` into the next column which becomes `91`.

We repeat this process with `[1, 2+91, 5]`. We have `93`, where `3` stays and `90` is carried over as `9`. Again, we have `[1+9, 3, 5]` which transforms into `[1, 0, 3, 5]`.

**Implementation**

<details>
  <summary><b>Java</b></summary>

``` java
class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
        int N = A.length;
        int cur = K;
        List<Integer> ans = new ArrayList();

        int i = N;
        while (--i >= 0 || cur > 0) {
            if (i >= 0)
                cur += A[i];
            ans.add(cur % 10);
            cur /= 10;
        }

        Collections.reverse(ans);
        return ans;
    }
}
```
</details>
<details>
  <summary><b>Python</b></summary>

``` python
class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A
```
</details>

**Complexity Analysis**

- Time Complexity: $O(max⁡(N,log⁡K))$ where $N$ is the length of `A`.
- Space Complexity: $O(max⁡(N,log⁡K))$.