dict_var = { 'csev' : 2, 'cwen' : 2, 'zqian' : 1}

for out, out2 in dict_var.items() : 
    print('item() : ' + out)

for out in dict_var.values() :
    print(out)

for out in dict_var : 
    print("just dictionary : " +out)

for out in dict_var.keys() :
    print('keys() : ' + out)

for out, out2 in dict_var.items() :
    print(out2)