class Solution:

    def encode(self, strs: List[str]) -> str:
        bigstr = ""

        for s in strs:
            bigstr = bigstr + (str(len(s)) + "#" + s)
        
        return bigstr



    def decode(self, s: str) -> List[str]:
        liststr = []

        while s != "":
            slen = int(s[:s.find("#")])
            liststr.append(s[s.find("#")+1:s.find("#")+slen+1])
            s = s[s.find("#")+slen+1:]
        
        return liststr

