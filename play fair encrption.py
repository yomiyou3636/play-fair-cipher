import numpy as np
###############################################################################################################

key = input("enter the key\n")# key used for encrypting 
plain_text=input("enter the plain text\n")#text that is going to be encrypted
key_list=[]#2D list used for storing the key and all the other alphabets 
text_list=[]# list of the processed plain text
position=[]# retrives and store  the position of the letters the plain text from the key_list. 
cipher_text=[] #holds the cipher text that is generated from the algorithm 
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
###############################################################################################################

for x in range(0,len(plain_text)):
    if plain_text[x]!=" " and plain_text[x]!="-" and plain_text[x]!="+"and plain_text[x]!="$"and plain_text[x]!="/""/"and plain_text[x]!="%"and plain_text[x]!="!" and plain_text[x]!="&" and plain_text[x]!="@" and plain_text[x]!="?":
        if len(text_list) %2 ==1 and plain_text[x]==text_list[len(text_list)-1]:     
            text_list.append("x")
            text_list.append(plain_text[x])
                           
        elif plain_text[x]=='j':
            text_list.append("i")
        
        else:
            text_list.append(plain_text[x])

###############################################################################################################

if len(text_list) % 2 !=0:
    text_list.append("z")
# print(text_list)

###############################################################################################################

key_array=np.array(key_list)
key_array=key_array.reshape(5,5)
print(key_array)

###############################################################################################################

def find_pos(letter):
    
    for i in range(0,5):
        for j in range(0,5):
            
            if key_array[i,j]==letter:
                lx,ly=i,j
                position.append(lx)
                position.append(ly)
                       
###############################################################################################################

for i in range(0,len(text_list)):
    letter=text_list[i]
    find_pos(letter)

###############################################################################################################

for i in range(0,len(position),4):
    # print(i)
    if position[i]==position[i+2]:
        #row###################################################################################################
        if position[i+1] ==4:
             
             cipher_text.append(key_array[position[i],0])
             cipher_text.append(key_array[position[i+2],position[i+3]+1])
        elif position[i+3] ==4:
             
             cipher_text.append(key_array[position[i],position[i+1]+1])
             cipher_text.append(key_array[position[i+2],0])
        
        else:
            cipher_text.append(key_array[position[i],position[i+1]+1])
            cipher_text.append(key_array[position[i+2],position[i+3]+1])
        #column################################################################################################
    elif position[i+1]==position[i+3]:
        if position[i] ==4:
             
             cipher_text.append(key_array[0,position[i+1]])
             cipher_text.append(key_array[position[i+2]+1, position[i+3]] )
        elif position[i+2] ==4:
             
             cipher_text.append(key_array[position[i]+1,position[i+1]])
             cipher_text.append(key_array[0,position[i+3]])
        
        else:
            cipher_text.append(key_array[position[i]+1,position[i+1]])
            
            cipher_text.append(key_array[position[i+2]+1,position[i+3]])
        #box###################################################################################################  
    else:
        
        cipher_text.append(key_array[position[i],position[i+3]])
        cipher_text.append(key_array[position[i+2],position[i+1]])
cipher_string="".join(cipher_text)

print('\ncipher text->'+cipher_string+"\n")



