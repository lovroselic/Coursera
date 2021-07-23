def Correct_overlap_all_pairs(reads, min_length = 30):
    
    kmer_dict = createKmersFromReadS(reads, min_length) 
    #create dict with kmer key/and set of reads with that kmer value. 
    #User has to create this function
    
    
    overlap_graph = defaultdict(set) #read is key, set of overlapping reads are value
    
    
    for read in reads:
        #create suffix for this read
        read_suffix = read[-min_length: ]
        
        
        #extract set of all reads containing this kmer/suffix
        read_set = kmer_dict[read_suffix]
        
        assert(len(read_set) > 0) # check that the set isnt empty
        
        read_set.remove(read) #remove the read so we dont compare it with itself
        

        #THIS WORKS
        for compar_read in read_set:
            if overlap(read, compar_read, 30):
                overlap_graph[read].add(compar_read)
        #####################################
        
  
        
def Incorrect_overlap_all_pairs(reads, min_length = 30):
    
    kmer_dict = createKmersFromReadS(reads, min_length) #create dict with kmer key/and set of reads with that kmer value. User has to create this function
    
    
    overlap_graph = defaultdict(set)
    
    
    for read in reads:
        #create suffix for this read
        read_suffix = read[-min_length: ]
        
        
        #extract set of all reads containing this kmer/suffix
        read_set = kmer_dict[read_suffix]
        
        
        assert(len(read_set) > 0)
        
        read_set.remove(read) #remove the read so we dont compare it with itself
        
        #THIS DOESNT WORK. IT TRIPS THE ASSERT STATEMENT ABOVE. BUT HOW?
        while len(read_set) != 0:
            compar_read = read_set.pop()
            
            if overlap(read, compar_read, 30):
                overlap_graph[read].add(compar_read)
          ################################################ 