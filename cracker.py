#!/usr/bin/env python3

import binascii
import argparse

SPACE = ord(' ')


def main():
    parser = argparse.ArgumentParser(description="Many-time Pad Cracker")
    parser.add_argument("--filename", type=str,
                        help="Name of the file containing the ciphertexts (default: ciphertexts.txt)",
                        default="ciphertexts.txt")
    args = parser.parse_args()
    try:
        with open(args.filename) as f:
            ciphertexts = [binascii.unhexlify(line.rstrip()) for line in f]
        cleartexts = [bytearray(b'?' * len(c)) for c in ciphertexts]
    except Exception as e:
        print("Cannot crack {} --- {}".format(args.filename, e))
        raise SystemExit(-1)
    for k in range(max(len(c) for c in ciphertexts)):
        cts = [c for c in ciphertexts if len(c) > k]

	# TODO

    list_of_list = list() #creo lista di liste (senza elem)
    max_line_length = 0
    for line_of_ciphertexts in ciphertexts: #per ogni linea nel ciphertexts
        if (len(line_of_ciphertexts) > max_line_length):
            max_line_length = len(line_of_ciphertexts) #mi salvo valore linea piu lunga
        line_aux = list() #creo lista per ogni linea
        for c in line_of_ciphertexts:
            line_aux.append(c) #creo liste con tutti i bytes
        list_of_list.append(line_aux) #inserisco lista in lista di liste

    zero_to_max_line_length = range(0,max_line_length) #creo range da 0 a 64


    list_of_columns = list() #costruisco lista
    for step in zero_to_max_line_length:
        list_of_columns.insert(step,list()) #metto 64 liste vuote nella lista di liste

    for line in list_of_list:
        for index, item in enumerate(line,0):
            aux_for_columns = list_of_columns.pop(index)
            aux_for_columns.append(item)
            list_of_columns.insert(index,aux_for_columns)

    spaces = list() #lista di caratteri spazio
    pad = list()

    
    for column in list_of_columns:
        mydict = {}
        #print("---------COLONNA----------")
        for i in column:
            for j in column:
                result = i ^ j
                if (result >= 65):
                    #print(str(i) + ' XOR ' + str(j) + " -> " +  str(result))
                    if i not in mydict:
                        mydict[i] = 1
                    else:
                        mydict[i] = mydict.get(i) + 1
                    if j not in mydict:
                        mydict[j] = 1
                    else:
                        mydict[j] = mydict.get(j) + 1
                    maximum = max(mydict, key=mydict.get)
        spaces.append(maximum)

    for space in spaces:
        pad.append(space ^ 32)

    for index_row, row in enumerate(ciphertexts,0):
        for index_column, column in enumerate(row,0):
            cleartexts[index_row][index_column] = ciphertexts[index_row][index_column] ^ pad[index_column]


    #print(spaces)
    #print(pad)


    print("\n".join(c.decode('ascii') for c in cleartexts))

if __name__ == "__main__":
    main()

