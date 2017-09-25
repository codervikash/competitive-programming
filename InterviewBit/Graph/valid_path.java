"""
There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle. Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.
Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.

Constraints
 0 <= x , y , R <= 100
 1 <= N <= 1000
Center of each circle would lie within the grid

Input
Input contains x, y , N , R  and two array of size N containing centers of circles.
The ith index of first array contains x co-ordinate of the ith circle and ith index of second array contains the y co-ordinate of the ith circle.

Output
YES or NO depending on weather it is possible to reach cell  (x,y) or not starting from (0,0).

  Sample Input
  2 3 1 1
  2
  3
  Sample Output
  NO
"""

public class Solution {
private class Pair
{
    int x ; int y ;
}
ArrayList<Integer> xindex ; ArrayList<Integer> yindex ; int R ;int len ;
public String solve(int x, int y, int n, int r, ArrayList<Integer> xi, ArrayList<Integer> yi) {
    int dp[][] = new int[x+1][y+1] ;
    len = xi.size() ;
    for(int i=0;i<=x;i++)
    {
        for(int j=0;j<=y;j++)
        dp[i][j] = -1 ;
    }

    xindex = xi ; yindex = yi ;
    dp[0][0] = 1 ; R = r*r ;
    LinkedList<Pair> q = new LinkedList<Pair>() ;
    Pair obj = new Pair() ;
    obj.x = 0 ; obj.y = 0 ;
    q.add(obj) ;
    int arr1[] = {1,1,1,0,-1,-1,-1,0} ;
    int arr2[] = {-1,0,1,1,1,0,-1,-1} ;

    while(q.size()!=0)
    {
        Pair temp = q.poll() ;
        int x1 = temp.x ;
        int x2 = temp.y ;

        for(int i=0;i<8;i++)
        {
            int t1 = x1+arr1[i] ; int t2 = x2+arr2[i] ;

            if((t1>=0)&&(t1<=x)&&(t2>=0)&&(t2<=y))
            {
                if(dp[t1][t2]==-1)
                {
                    boolean res = isValidIndex(t1,t2) ;
                    if(res==false)
                    dp[t1][t2] = 2 ;
                    else
                    {
                        dp[t1][t2] = 1 ;
                        Pair t = new Pair() ;
                        t.x = t1 ;
                        t.y = t2 ;
                        q.add(t) ;
                    }
                }
            }
        }

        if(dp[x][y]!=-1)
        break ;
    }

    if(dp[x][y]==1)
    return "YES" ;

    return "NO" ;

}

public boolean isValidIndex(int x,int y)
{
    for(int i=0;i<len;i++)
    {
        int x1 = xindex.get(i) ; int x2 = yindex.get(i) ;
        if((x==x1)&&(y==x2))
        return false ;

        int n = (x1-x)*(x1-x) + (x2-y)*(x2-y) ;

        if(n<=R)
        return false ;
    }
    return true ;
}
}
