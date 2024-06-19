def RtoA(s):
    A = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}      
    ans = 0                                                                       
    for i in range(len(s)):                                                                                                                      
        if i == 0:                                                                   
            ans += A[s[i]]                                                                   
        elif (s[i] == 'V' or s[i] == 'X') and s[i-1] == 'I' or \
             (s[i] == 'L' or s[i] == 'C') and s[i-1] == 'X' or \
             (s[i] == 'D' or s[i] == 'M') and s[i-1] == 'C':            
            ans += A[s[i]]                                   
            ans -= 2 * A[s[i-1]]                                                
        else:
            ans += A[s[i]]                                                                   
    return ans

def AtoR(n):
    A = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],                                           
         [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],                                                                                                         
         [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]                                                                                                                    
    ans = ''                                                                         
    for i in A:                                                                                                                  
        if n // i[0]:
            a, b = divmod(n, i[0])
            ans += i[1] * a                                                       
            n = b                                                                  
    return ans

def main():
    while True:
        try:
            data = input().strip()
            if data == '#':
                break
            parts = data.split()
            if len(parts) < 2:
                print("Invalid input. Please enter two Roman numerals separated by space.")
                continue
            a = parts[0]
            b = parts[1]
            if a == b:                                                                
                print('ZERO')
            else:
                print(AtoR(abs(RtoA(a) - RtoA(b))))
        except EOFError:
            break

if __name__ == '__main__':
    main()
