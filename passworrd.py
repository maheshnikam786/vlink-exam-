def minChar(n,passwrd):
    if(len(password)< 8):
           res = 8-n
    return res
n=int(input())
password = input()


cap,small,digit,spec=0,0,0,0
for i in range(0,len(password)):
    if(ord(password[i]) >= 65 and ord(password[i])<=90):
        cap+=1
    elif(ord(password[i]) >= 97 and ord(password[i])<=122):
        small+=1
    elif(ord(password[i])>= 48 and ord(password[i])<= 57):
        digit+=1
    else:
        spec+=1
print("Password contains:")
print()
print("Special Character - ",spec)
print()
print("Digits - ",digit)
print()
print("Upeercase Alphabet - ",cap)
print()
print("Lowercase Alphabet - ",small)
print()
        
if(len(password)< 8):
    print(minChar(n,password),"more characters should be added") 

else:
    print("Strong Password good to go")