"""
Knight movement on a chess board

Given any source point and destination point on a chess board, we need to find whether Knight can move to the destination or not.

Knight's movements on a chess board

The above figure details the movements for a knight ( 8 possibilities ). Note that a knight cannot go out of the board.

If yes, then what would be the minimum number of steps for the knight to move to the said point.
If knight can not move from the source point to the destination point, then return -1

Input:

N, M, x1, y1, x2, y2
where N and M are size of chess board
x1, y1  coordinates of source point
x2, y2  coordinates of destination point
Output:

return Minimum moves or -1
Example

Input : 8 8 1 1 8 8
Output :  6
"""

bool valid(int x, int y, int n , int m ){
    if(x>=0 && x<n && y>=0 && y<m)return true;
    else return false;
}
int Solution::knight(int N, int M, int x1, int y1, int x2, int y2) {
    // Do not write main() function.
    //Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    int xcord[] = {2,1,-1,-2};
    int ycord[] = {1,2,2,1};

    vector< vector<int> > board(N, vector<int>(M, -1) );
    queue< pair<int,int> >  q;

    q.push(make_pair(x1-1,y1-1));
    board[x1-1][y1-1] ++;
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        if(x==(x2-1) && y == (y2-1) ){
            return board[x][y];
        }

        for(int i=0; i<4; i++){
            int xnew = x + xcord[i];
            int ynew = y + ycord[i];
            if(valid(xnew, ynew, N, M) && board[xnew][ynew]==-1){
                board[xnew][ynew] = board[x][y] + 1;
                q.push(make_pair(xnew, ynew));
            }

            ynew = y - ycord[i];
            if(valid(xnew, ynew, N, M) && board[xnew][ynew]==-1){
                board[xnew][ynew] = board[x][y] + 1;
                q.push(make_pair(xnew, ynew));
            }
        }

    }
    return -1;
}
