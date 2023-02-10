class Solution {
    public int findMinArrowShots(int[][] points) {
        int n = points.length;
        if(n < 2) return n;
        Arrays.sort(points, (a,b)-> a[1] - b[1]);
        int arrow = 1, preEndPoint = points[0][1];
        for(int i = 1; i < n; i++){
            if(points[i][0] <= preEndPoint && preEndPoint <= points[i][1]){
                continue;
            }else{
                arrow++;
                preEndPoint = points[i][1];
            }
        }
        return arrow;
    }
}

/**

[[3,4],[2,5],[1,6]]

 */