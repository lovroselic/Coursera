# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:50:17 2020

@author: SELICLO1
"""

# Efficient Python 3 program 
# to find length of 
# the longest prefix 
# which is also suffix 

# Returns length of the longest prefix 
# which is also suffix and the two do 
# not overlap. This function mainly is 
# copy computeLPSArray() of in below post 
# https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/ 
def longestPrefixSuffix(s) : 
	n = len(s) 
	lps = [0] * n # lps[0] is always 0 

	# length of the previous 
	# longest prefix suffix 
	l = 0
	
	# the loop calculates lps[i] 
	# for i = 1 to n-1 
	i = 1
	while (i < n) : 
		if (s[i] == s[l]) : 
			l = l + 1
			lps[i] = l 
			i = i + 1
		
		else : 

			# (pat[i] != pat[len]) 
			# This is tricky. Consider 
			# the example. AAACAAAA 
			# and i = 7. The idea is 
			# similar to search step. 
			if (l != 0) : 
				l = lps[l-1] 

				# Also, note that we do 
				# not increment i here 
			
			else : 

				# if (len == 0) 
				lps[i] = 0
				i = i + 1

	res = lps[n-1] 

	# Since we are looking for 
	# non overlapping parts. 
	if(res > n/2) : 
		return n//2
	else : 
		return res 
		

# Driver program to test above function 
s = "CLOVROSELICLO"
print(longestPrefixSuffix(s)) 


# This code is contributed 
# by Nikita Tiwari. 
