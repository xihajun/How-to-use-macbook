A=[]
for i =0:25
    A = [A char(65+i)]
end


B = 'MY WORD!'

C =[]
for i =1:length(B)
    temp = find(A==B(i));
    if temp
        C = [C A(temp)];
    else
        C = [C ' ']
    end
end
C = []
D = []
E = []
for i =1:length(B)
    temp = find(A==B(i));
    if temp
        E = [E ' ' num2str(temp-1)]
        
        cipher = mod((temp-1)^5,26)
        C = [C A(cipher+1)];
        decode = mod(cipher^5,26)
        D = [D A(decode+1)];
    else
        C = [C ' ']
        D = [D ' ']
        E = [E ' ']
    end
end
C
D
