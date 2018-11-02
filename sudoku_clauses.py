import sys

def S(x,y,z):
    return 81 * (x-1) + 9 * (y-1) + z

def sudoku_clauses(file):
    
    count = 0
    
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                file.write('{} '.format(S(x,y,z)))
            file.write('0\n')
            count += 1
                
                
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1,9):
                for i in range(x+1, 10):
                    file.write('{} {} {}\n'.format(-S(x,y,z), -S(i,y,z),0))
                    count += 1
                    
                    
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 9):
                for i in range(y+1, 10):
                    file.write('{} {} {}\n'.format(-S(x,y,z), -S(x,i,z),0))
                    count += 1
                    
                    
                    
    for z in range(1, 10):
        for i in range(0, 3):
            for j in range(0,3):
                for x in range(1,4):
                    for y in range(1,4):
                        for k in range(y+1,4):
                            file.write('{} {} {}\n'.format(-S((3*i+x),(3*j+y),z), -S((3*i+x),(3*j+k),z),0))
                            count += 1
                            
    
    
    for z in range(1,10):
        for i in range(0,3):
            for j in range(0,3):
                for x in range(1,4):
                    for y in range(1,4):
                        for k in range(x+1, 4):
                            for l in range(1,4):
                                file.write('{} {} {}\n'.format(-S((3*i+x),(3*j+y),z), -S((3*i+k),(3*j+l),z),0))
                                count += 1
    return count

def main(): 
    myfile = open('sudoku.txt')#sys.argv[1])
    outfile = open('sudoku.dimacs', 'w')
    outfile.write('p cnf 81 729\n') 
    
    row = 0 
    column = 0
    for line in myfile:
        row+= 1
        line = line.split()
        for item in line:
            column += 1
            if item != 'x':
                outfile.write('{} {}\n'.format(S(row, column, int(item)),0))
        column = 0
            
            
            
                
    sudoku_clauses(outfile)
    print(sudoku_clauses(outfile))
    
    # Close files.
    outfile.close()
    myfile.close()

if __name__ == '__main__':   
    main()