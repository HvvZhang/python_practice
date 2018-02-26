# -*- coding: utf-8 -*-
#很多收费软件都需要用激活码来注册，限时促销活动也需要填写激活码来进行。
#用Python语言生成常见的激活码。
#一个激活码里的字符是可以重复的，而激活码是不能重复的。
#放在字典中，通过字典来判断是否有重复的激活码。
import random  
import string
import uuid
  
def gene_activation_key1(number,length):  
    """
    gene the activation key

    :param number: number of activation key
    :param length: length of activation key
    :returns: activation key
    """
    keys = {}  
    source = list(string.ascii_uppercase + string.digits)  #大写26个字母和10个数字
            
    while len(keys) < number:  
        key= ''  
        for index in range(length):  
            key += random.choice(source)  #得到key
        if key in keys:  
            pass  
        else:  
            keys[key] = True
    return list(keys.keys())
        
def gene_activation_key2(number,length):  
    """
    gene the activation key

    :param number: number of activation key
    :param length: length of activation key
    :returns: activation key
    """
    keys = []
    for i in range(number):
        key = str(uuid.uuid1()).replace('-','').upper()
        keys.append(key)
    return keys

def print_key(keys):
    for key in keys:
        print(key)

keys1 = gene_activation_key1(20,32)
keys2 = gene_activation_key2(20,32)
    
if __name__ == "__main__":  

    print_key(keys1)
    print('-'*32)
    print_key(keys2)
