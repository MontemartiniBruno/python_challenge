def obtener_extremos(t,n:int):
    mi_list = []
    for i in t:
        mi_list.append(i)
    print(mi_list)
    
    i=0
    while i<n:
        mi_list.pop(0)
        mi_list.reverse()
        mi_list.pop(0)
        mi_list.reverse()

        i+=1 

    return mi_list

if __name__ == '__main__':

    print(obtener_extremos((1,2,3,4,5,6,7,8,9,10),1))
