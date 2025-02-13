from django.shortcuts import render
from FD.forms import data
from django.http import HttpResponse  
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd 
from tabulate import tabulate
import functional_dependencies as f_d

fdset = 1
DependencyString = ""
FD = []
# Create your views here.
def index(request):
    global fdset
    global DependencyString
    global FD
    if request.method == 'POST' and 'submit' in request.POST:
        fdset = 1
        DependencyString = ""
        FD = []
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(myfile.name)
        file = myfile.name
        newData = pd.read_csv(file)
        templist =newData.values.tolist()
        col =newData.columns.values
        print(col)
        print(templist)
        jj =len(templist)
        print(col)
        Tabledict = {}
        for i in col:
            if i+".1" in col:
                context = {
                "FD": "CSV File corrupt",
                "fdset": "4"
                }
                return render(request,'index.html',context)
        for i in templist:
            for j in i:
                j = str(j)
                if j=="nan":
                    context = {
                    "FD": "CSV File corrupt",
                    "fdset": "4"
                    }
            return render(request,'index.html',context)
        for i in range(len(col)):
            Tabledict[col[i]] = [templist[j][i] for j in range(jj)]
        print(Tabledict)   
        # lst = ["A","B","C","D","E"]
        lst = col
        #Tabledict = {'A': [1, 2, 3, 4, 5, 6], 'C': [1,2,3, 4, 5, 6],'B': [1, 2, 3, 4, 5, 6], 'D': [1, 2, 3, 4, 5, 6], 'E': ['1', '2', '3', '4', '5', '6']}
        print(Tabledict)
        def concat(str1,lst):
            if str1 in Tabledict:
                return 0
            Concat = [""] * len(Tabledict[lst[0]])
            for item in lst:
                for i in range (len(Tabledict[item])):
                    Concat[i] = str(Concat[i]) + str(Tabledict[item][i])
            return Concat
        for i in range (1, ((2**len(lst)))):
            mainlst = []
            mainstr = ""
            i = format(i,"b").zfill(len(lst))
            while "1" in i:
                ind = i.index("1")
                mainlst.append(lst[ind])
                if mainstr == "":
                    mainstr = mainstr + lst[ind]
                else:
                    mainstr = mainstr + "," + lst[ind]
                i = i.replace("1","0",1)
            print(f"{mainstr} ++++ {mainlst}")
            if concat(mainstr,mainlst):
                Tabledict[mainstr] = concat(mainstr,mainlst)
        for i,num in Tabledict.items():
            print(f"{i} : {num}")
        PK = {}
        # FD = []

        def check(list1,list2):
            num = 0
            dic= {}
            for i in list1:
                if i in dic:
                    if dic[i] == list2[num]:
                        num += 1
                        continue
                    return 1
                dic[i] = list2[num]
                num +=1

        for rowName,columnVals in Tabledict.items():
            for rowName2,columnVals2 in Tabledict.items():
                if rowName == rowName2:
                    continue
                if (not check(columnVals,columnVals2)):
                    FD.append([rowName,rowName2])
        RelationString = ""
        for row in FD:
            DependencyString = DependencyString + row[0] + "->" + row[1] + " "
        print(DependencyString)

        i=0
        for listval in list(col):
            if i==0:
                RelationString = listval
                i+=1
            else:
                RelationString = RelationString + "," + listval
        print(RelationString)
        DependencyString = DependencyString.split(" ")
        print(DependencyString)

        list2 = []
        set1 = set()

        for i in FD:
            set1.add(i[0])

        # print(set1)

        FD2 = dict.fromkeys(set1, "")
        # print(FD2)
        for i in FD:
            if i[0] in FD2:
                FD2[i[0]] = FD2[i[0]] + i[1]
        for i in FD2.keys():
            FD2[i] = set(FD2[i])
            FD2[i].remove(",")
        # print(FD2)
        for i,j in FD2.items():
            print(f"{i}->{j}")
            s=','.join(j)
            list2.append([i,s])    
#     print(s)
# print(list2)
        DepStr= ""
        for row in list2:
            DepStr = DepStr + row[0] + "->" + row[1] + " "
        DepStr = DepStr.split(" ")
        #MINIMAL PATYU
        fdset = 1
        context = {
            "FD": DepStr,
            "fdset": "1"
        }
        return render(request,'index.html',context)
    elif request.method == 'POST' and 'check' in request.POST:
        if fdset == 1:
            fd = request.POST.get("fdcheck")
            print(fd)
            print(DependencyString)
            if fd in DependencyString:
                context = {
                "FD": "Dependency Is VALID!",
                "fdset": "2"
                }
            else:
                context = {
                "FD": "Dependency Is NOT VALID!",
                "fdset": "2"
                }
        else:
            context = {
                "FD": "Please Enter Data First",
                "fdset": "2"
                }
        return render(request,'index.html',context)
    elif request.method == 'POST' and 'closure' in request.POST:
        if fdset == 1:
            closureCheck = request.POST.get("closureFD")
            fds = f_d.FDSet()
            print(FD)
            for fd1 in FD:
                fdse = f_d.FD({str(fd1[0])},{str(fd1[1])})
                fds.add(fdse)
            m = fds.closure({closureCheck})
            m2 = []
            # print(m)
            for temp in m:
                if "," in temp:
                    m1 = temp.split(",")
                    for mm in m1:
                        m2.append(mm)
            if len(m2) == 0:
                m2.append(closureCheck)
            m2 = set(m2)
            print(m2)
            context = {
                "closure": m2,
                "element": closureCheck,
                "fdset": "3"
                }
        else:
            context = {
                "FD": "Please Enter Data First",
                "fdset": "3"
                }
        return render(request,'index.html',context)
    return render(request,'index.html',)
