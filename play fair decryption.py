import numpy as np
###############################################################################################################

key = input("enter the key\n")
cipher_text=input("enter the cipher text\n")
key_list=[]
text_list=[]
position=[]
plain_text=[]
alphabet=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

################################################################################################################

for x in range(0,len(key)):
    if key[x] not in key_list:
        if key[x]=="i" or key[x]=="j":
             key_list.append("i")

        else:
            key_list.append(key[x])
for y in range(0,25):
    if alphabet[y] not in key_list:
        key_list.append(alphabet[y])
############################################################################################################

for x in range(0,len(cipher_text)):
    if cipher_text[x]!=" " and cipher_text[x]!="-" and cipher_text[x]!="+"and cipher_text[x]!="$"and cipher_text[x]!="/""/"and cipher_text[x]!="%"and cipher_text[x]!="!" and cipher_text[x]!="&" and cipher_text[x]!="@" and cipher_text[x]!="?":
        
            text_list.append(cipher_text[x])

############################################################################################################


key_array=np.array(key_list)
key_array=key_array.reshape(5,5)
print(key_array)

############################################################################################################

def find_pos(letter):
    
    for i in range(0,5):
        for j in range(0,5):
            
            if key_array[i,j]==letter:
                lx,ly=i,j
                position.append(lx)
                position.append(ly)
                       
############################################################################################################

for i in range(0,len(text_list)):
    letter=text_list[i]
    find_pos(letter)

#############################################################################################################

for i in range(0,len(position),4):
    # print(i)
    if position[i]==position[i+2]:
        #row################################################################################################
        if position[i+1] ==0:
             
             plain_text.append(key_array[position[i],4])
             plain_text.append(key_array[position[i+2],position[i+3]-1])
        elif position[i+3] ==0:
             
             plain_text.append(key_array[position[i],position[i+1]-1])
             plain_text.append(key_array[position[i+2],4])
        
        else:
            plain_text.append(key_array[position[i],position[i+1]-1])
            plain_text.append(key_array[position[i+2],position[i+3]-1])
        #column##############################################################################################
    elif position[i+1]==position[i+3]:
        if position[i] ==0:
             
             plain_text.append(key_array[4,position[i+1]])
             plain_text.append(key_array[position[i+2]-1, position[i+3]] )
        elif position[i+2] ==0:
             
             plain_text.append(key_array[position[i]-1,position[i+1]])
             plain_text.append(key_array[4,position[i+3]])
        
        else:
            plain_text.append(key_array[position[i]-1,position[i+1]])
            
            plain_text.append(key_array[position[i+2]-1,position[i+3]])
        #box#####################################################################################   
    else:
        
        plain_text.append(key_array[position[i],position[i+3]])
        plain_text.append(key_array[position[i+2],position[i+1]])
cipher_string="".join(plain_text)

print('\ncipher text->'+cipher_string+"\n")



