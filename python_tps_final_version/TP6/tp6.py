'''
========================================
TP6_numpy YAN Wenli & PENG Hanyuan
========================================
'''
import numpy as np

#a = np.random.randint((4,3,2))
#a1 = np.empty((2,3,4))


def creationA():
    #Créer un tableau de dimension 3 avec un shape de (4, 3, 2) remplit avec des nombres aléatoires.
    # a1 = np.random.empty(0,10,size=[4,3,2])
    a1 = np.random.randint((4,3,2))
    # a1 = np.empty((2,3,4))

    #Vous afficherez les attributs du tableau : ndim, shape, size, dtype, itemsize, data.
    print(a1)
    print("ArrayType: ",type(a1))
    print("DataType: ",a1.dtype)
    print("ArraySize: ",a1.size)
    print("ItemSize: ",a1.itemsize)
    print("ArrayShape: ",a1.shape)
    print("data: ",a1.data)
    print("ArrayDimension: ",a1.ndim)



def creationB():
    #Créer 2 matrices 3x3 initialisées avec les entiers de 0 à 8 pour la 1e et de 2 à 10 pour la 2e puis
    #calculer le produit des 2 (différence entre * et dot). Transposer une matrice

    #b1 = np.random.randint(0,8,size=[3,3])
    b1_arr = np.arange(0,9).reshape(3,3)   # ne contient pas 9  (0-8)
    b2_arr = np.arange(2,11).reshape(3,3)   # ne contient pas 11  (2-10)
    b1_mat = np.mat(b1_arr)
    b2_mat = np.mat(b2_arr)

    print("----------------- array ---------------------------")

    print("b1_mat\n",b1_arr)
    print("b2_mat\n",b2_arr)

    print("+\n", b1_arr + b2_arr)
    print("dot\n", np.dot(b1_arr, b2_arr))
    print("*\n", (b1_arr) * (b2_arr))
    print("multiply\n", np.multiply(b1_arr, b2_arr))
    print("transposer\n", np.transpose(b1_arr))

    print("----------------- matrice ---------------------------")
    print("b1_mat\n",b1_mat)
    print("b2_mat\n",b2_mat)

    print("+\n", b1_mat + b2_mat)

    print("dot\n", np.dot(b1_mat, b2_mat))
    # print("dot :Pour un tableau de rang 1, effectuez la multiplication de position correspondante puis faire la somme；")
    # print("Pour un tableau à deux dimensions dont le rang n'est pas égal à 1, effectuez la multiplication matricielle.")

    print("*\n", (b1_mat) * (b2_mat))
    # print("(*:  Effectuer la multiplication de position correspondante sur le tableau;\
        # Effectuer une multiplication matricielle sur des matrices)")

    print("multiply\n", np.multiply(b1_mat, b2_mat))
    print("transposer of b1_mat: \n", np.transpose(b1_mat))

    #Calculer le déterminant et l’inverse d’une matrice.
    print("det of b1_mat: \n", np.linalg.det(b1_mat)) #le déterminant égale à 0, ce matrice est invertible
    try:
        inverse = np.linalg.inv(b2_mat)
        print("inverse of b2_mat: \n", inverse)
    except np.linalg.LinAlgError:
        print("Not invertible. Skip this one.") #Si non invertible. Passer à la suite
        pass
    else:
        print("ok")
    eig1,eig2 = np.linalg.eig(b1_mat)
    print("the eig of mat is:\n",eig1)
    print("the feature vector of mat is:\n",eig2)

creationB()
