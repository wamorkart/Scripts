import ROOT
import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import array
from prettytable import PrettyTable
plt.rcParams.update({'font.size': 10})

mass = [15,20,25]#,30,40,45,50,55,60]
year = [2016,2017,2018]

inDir = "/afs/cern.ch/work/t/twamorka/fggfinalfit_h4g_run2/CMSSW_10_2_13/src/flashggFinalFit/Signal/"
outDir = "/eos/user/t/twamorka/www/H4G_for_PreApp/InterpolationStudies/SignalModelInfo/"

Training = ["outdir_H4G_10Mar2021_Parametrized","outdir_H4G_10Mar2021_ANTrainig_1520Bins_New"]

for y in year:
    Sigma = []
    NumEntries = []
    for t in Training:
        Sigma_tmp = []
        NumEntries_tmp = []
        for m in mass:
            print "year ==> ",y, "  Training ==> ", t, "  Mass ==> ", m
            f_in = open(inDir+t+"_M"+str(m)+"_"+str(y)+"/sigplots/sigModelInfo.txt" ,"r")
            for li, ln in enumerate(f_in):
                 if ln.startswith('Sigma_Eff'):  Sigma_tmp.append(ln.split()[1])
                 if ln.startswith('NumEvents'):  NumEntries_tmp.append(round(float(ln.split()[1]),3))
        Sigma.append(Sigma_tmp)
        NumEntries.append(NumEntries_tmp)
    # print Sigma
    # print NumEntries

    plt.figure()
    plt.grid()
    plt.plot(mass,Sigma[0],lineStyle='-', marker='o',label='Parametrized Training')
    plt.plot(mass,Sigma[1],lineStyle='-', marker='o',label='AN Training')
    plt.xlabel('m(a) [GeV]')
    plt.ylabel('Sigma')
    plt.legend()
    plt.savefig(outDir+"SigResolution_"+str(y)+"_zoom.pdf")
    plt.savefig(outDir+"SigResolution_"+str(y)+"_zoom.png")

    plt.figure()
    plt.grid()
    plt.plot(mass,NumEntries[0],lineStyle='-', marker='o',label='Parametrized Training')
    plt.plot(mass,NumEntries[1],lineStyle='-', marker='o',label='AN Training')
    plt.xlabel('m(a) [GeV]')
    plt.ylabel('Number of events')
    plt.legend()
    plt.savefig(outDir+"NSig_"+str(y)+"_zoom.pdf")
    plt.savefig(outDir+"NSig_"+str(y)+"_zoom.png")
