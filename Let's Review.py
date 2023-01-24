
if __name__ == "__main__":
    T = int(input().strip())
    
    for i in range(0, T):
        S = str(input().strip())
        even = ''
        odd = ''
        for j in range(len(S)):
            if j%2 == 0 or j==0:
                even += S[j]
            else:
                odd += S[j]
        print(f'{even} {odd}')
    
