class Solution {
    public String solution(String s) {
        s = s.toLowerCase();
        var myInd = 0;
        var res = new StringBuilder();
        for (var cur: s.split("")) {
            if (cur.equals(" ")) {
                myInd = 0;
            }
            if (myInd % 2 == 0) {
                cur = cur.toUpperCase();
            }
            myInd += 1;
            res.append(cur);
        }
        return res.toString();
    }
}