class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        n = len(s)
        # Convert string to list because Python strings are immutable
        s_list = list(s)
        conflicts = 0
        
        # Step 1: Count initial conflicts
        for i in range(n - 1):
            if s_list[i] == s_list[i+1]:
                conflicts += 1
        
        # Step 2: If no conflicts initially, return 0
        if conflicts == 0:
            return 0
        
        # Step 3: Simulate replacing characters with '?' day by day
        for i in range(n):
            idx = p[i]
            
            # Check left neighbor conflict
            # Conflict exists only if current and neighbor are same AND neither is '?'
            if idx > 0:
                if s_list[idx] != '?' and s_list[idx-1] != '?' and s_list[idx] == s_list[idx-1]:
                    conflicts -= 1
            
            # Check right neighbor conflict
            if idx < n - 1:
                if s_list[idx] != '?' and s_list[idx+1] != '?' and s_list[idx] == s_list[idx+1]:
                    conflicts -= 1
            
            # Mark the character as '?' to resolve future neighbor checks
            s_list[idx] = '?'
            
            # If all conflicts are resolved, return the number of days (1-based)
            if conflicts == 0:
                return i + 1
        
        return 0