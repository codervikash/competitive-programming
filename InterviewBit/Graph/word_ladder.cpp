"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

You must change exactly one character in every transformation
Each intermediate word must exist in the dictionary
Example :

Given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note that we account for the length of the transformation path instead of the number of transformation itself.

 Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

map<string,bool>mapa;
map<string,bool>memo;
map<string,int>DP;
bool ok;
string fin;
int dp(string v){
    if(v==fin){
        ok=true;
        return 0;
    }
    if(DP[v])return DP[v];
    int mini=(1<<30);
    for(int i=0;i<v.size();i++){
        char uso=v[i];
        for(int j='a';j<='z';j++){
            if(j!=uso){
            	v[i]=j;
            	if(mapa[v]&&!memo[v]||v==fin){
            		memo[v]=true;
            		mini=min(mini,1+dp(v));
            		memo[v]=false;
				}
			}
        }
        v[i]=uso;
    }
    return DP[v]=mini;
}
int Solution::ladderLength(string start, string end, vector<string> &dictV) {
    fin=end;
    ok=false;
    DP.clear();
    mapa.clear();
    memo.clear();
    for(int i=0;i<dictV.size();i++){
        mapa[dictV[i]]=true;
    }
    int r=1+dp(start);
    if(!ok)r=0;
    return r;
}
