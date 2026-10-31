class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "lebronjames"
        
        encoded_string = "A$,s$c*&".join(strs)
        return encoded_string        

    def decode(self, s: str) -> List[str]:
        if s == "lebronjames":
            return []
            
        if not s:
            return [""]
            
        decoded_string = s.split("A$,s$c*&")
        return decoded_string
