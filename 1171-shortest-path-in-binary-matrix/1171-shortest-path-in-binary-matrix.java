class pair{
    int first,second,third;
    pair(int first,int second,int third)
    {
        this.first=first;
        this.second=second;
        this.third=third;
    }
}
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n=grid.length;
        if(grid[0][0]!=0 || grid[n-1][n-1]!=0){
            return -1;
        }
        if(n-1==0)return 1;
        Queue<pair> q =new LinkedList<>();
        int dis[][]=new int[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                dis[i][j]=Integer.MAX_VALUE;
            }
        }
        dis[0][0]=0;
        q.add(new pair(0,0,0));
        int dr[] = {0, -1, -1, -1, 0, 1, 1, 1};
        int[] dc = {-1, -1, 0, 1, 1, 1, 0, -1};
        while(!q.isEmpty()){
            pair p=q.peek();
            q.poll();
            int k=p.first;
            int y=p.second;
            int z=p.third;
            for(int i=0;i<8;i++)
            {
                int nr=y+dr[i];
                int nc=z+dc[i];
                if(nr>=0 && nr<n && nc>=0 && nc<n && grid[nr][nc]==0 && k+1<dis[nr][nc]){
                    dis[nr][nc]=k+1;
                    if(nr==n-1 && nc==n-1){
                        return k+2;
                    }
                    q.add(new pair(k+1,nr,nc));
                }
            }
        }
        return -1;     
    }
}