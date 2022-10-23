
def main():
    key = ''
    file = open("salida_ia.txt")
    PTDicc = {}
    PCDicc = {}
    TCDicc = {}
    for l in file:
        if l.__contains__(','):
            l = l.removesuffix('\n')
            key = [int(x) for x in l.split(', ')]
        if l.__contains__('V'):
            aux = l.split('  ')
            value = int(aux[0])
            ptk = key[0]/key[1]
            pck = key[0]/key[2]
            tck = key[1]/key[2]
            if not ptk in PTDicc.keys():
                PTDicc[ptk] = []
            PTDicc[ptk].append(value)
            if not pck in PCDicc.keys():
                PCDicc[pck] = []
            PCDicc[pck].append(value)
            if not tck in TCDicc.keys():
                TCDicc[tck] = []
            TCDicc[tck].append(value)

    for i in PTDicc.keys():
        PTDicc[i] = sum(PTDicc[i]) / len(PTDicc[i])
    for i in PCDicc.keys():
        PCDicc[i] = sum(PCDicc[i]) / len(PCDicc[i])
    for i in TCDicc.keys():
        TCDicc[i] = sum(TCDicc[i]) / len(TCDicc[i])

    PTDiccc = {}
    PCDiccc = {}
    TCDiccc = {}

    for i in sorted(PTDicc.keys()):
        PTDiccc[i] = PTDicc[i]
    for i in sorted(PCDicc.keys()):
        PCDiccc[i] = PCDicc[i]
    for i in sorted(TCDicc.keys()):
        TCDiccc[i] = TCDicc[i]



    ptl = []
    for i in range(1, 11):
        ii = i/10
        aux = []
        for iii in PTDiccc.keys():
            if ii - 0.1 < iii < ii:
                aux.append(PTDiccc[iii])
        if len(aux) != 0:
            x = sum(aux) / len(aux)
            ptl.append(x)
            print(ii, ' - ', x)
    print()
    tcl = []
    for i in range(1, 11):
        ii = i / 10
        aux = []
        for iii in TCDiccc.keys():
            if ii - 0.1 < iii < ii:
                aux.append(TCDiccc[iii])
        if len(aux) != 0:
            x = sum(aux) / len(aux)
            tcl.append(x)
            print(ii, ' - ', x)
    print()
    pcl = []
    for i in range(1, 11):
        ii = i / 10
        aux = []
        for iii in PCDiccc.keys():
            if ii - 0.1 < iii < ii:
                aux.append(PCDiccc[iii])
        if len(aux) != 0:
            x = sum(aux) / len(aux)
            pcl.append(x)
            print(ii, ' - ', x)

if __name__ == "__main__":
    main()
