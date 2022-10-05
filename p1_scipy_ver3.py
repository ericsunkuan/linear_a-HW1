import scipy.sparse
import numpy as np

def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    row_n=len(sets)
    col_n=len(sets[0])
    #b = np.zeros(col_n)
    #a = np.array(sets)
    A = scipy.sparse.csr_matrix(sets)
    while (row_n>1):
      #b=np.where(a[0]==1)[0]
      B = np.where(A[0].toarray()==1)[0]
      for i in B:
          C = np.where(A[:,i].toarray()==-1)[0]
          #c=np.where(a[:,i]==-1)[0]
          for j in C:
            if np.array_equal(-1*A[0], A[j]):
              return True
              
            A = scipy.sparse.vstack((A,A[0]+A[j]))
            row_n +=1
            

              
            #a = np.vstack([a, a[0]+a[j]])
            

      A = A[1:]
      row_n -=1


    

      # '''
      #   HINT: You can `print(sets)` to show what the matrix looks like
      #     If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
      #           0  1  2  3  4  5
      #         0  0  0 -1  1  0  0
      #         1  0  1  0  0 -1  0
      #         2  0  0  0 -1  0  1
      #         3  0  0  1  0  0 -1
      #         4 -1  1  0  0  0  0
      #     The size of the matrix is (5,6)
      # '''
    
    return False