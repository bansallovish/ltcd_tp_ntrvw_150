class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        final = ''
        i = len(a)
        j = len(b)
        carry = 0
        id = 0
        while(id<=i-1 and id<=j-1):
            if a[id] == '1' and b[id]=='1' and carry:
                carry = 1
                final+='1'
            elif a[id] == '1' and b[id]=='1':
                carry = 1
                final+='0'
            elif a[id] == '1' or b[id]=='1' :
                carry = 0
                final+='1'
            else:
                carry = 0
                final+='0'
            id+=1

        if i>j:
            for k in range(id,i):
                if carry ==1:
                    if a[k]=='1':
                        final+='0'
                        carry = 1
                    else:
                        final+='1'
                        carry = 0
                else:
                    final+=a[k]
        else:
            for k in range(id,j):
                if carry ==1:
                    if b[k]=='1':
                        final+='0'
                        carry = 1
                    else:
                        final+='1'
                        carry = 0
                else:
                    final+=b[k]

        if carry == 0:
            return final
        else:
            return final+str(carry)


        
obj1=Solution()
print("100",obj1.addBinary("11","1"))
print("10101",obj1.addBinary("1010","1011"))
# print("",obj1.addBinary("",""))
# print("",obj1.addBinary("",""))
# print("",obj1.addBinary("",""))