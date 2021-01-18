import ROOT
from ROOT import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# matplotlib.use('Agg')
import math
import numpy as np
from numpy import array
from prettytable import PrettyTable
from root_numpy import root2array, tree2array

plt.rcParams.update({'font.size': 10})
gROOT.SetBatch(kTRUE)

def mkPlot(nBins_val,xmin_val,xmax_val,x_array,p,f,e,xlabel,outPlotName):
    nBins, xmin, xmax = nBins_val, xmin_val,xmax_val
    bins = np.linspace(xmin, xmax, nBins+1)

    fig, ax = plt.subplots()
    plt.hist(x_array, bins=bins, label="")

    pdfIndexMap = {0:'Bernstein_1', 1:'Exponential_1',2:'Laurent_1', 3: 'Power Law_1', 4: 'Envelope'}


    textstr = '\n'.join((
        r'Mean=%s' % (str(round(np.array(x_array).mean(),3))) ,
        r'RMS=%s' % (str(round(np.array(x_array).std(),3))) ,
        # r'PDF Index (generated)=%s' % (str(p) ),
        #   r'PDF Index (fit)=%s' % (str(f) ),
        r'PDF Generated=%s' % (pdfIndexMap[p] ),
        r'PDF Fit=%s' % (pdfIndexMap[f] ),
       r'$r_{Truth}$=%s' % (str(e) )))



    plt.xlabel(xlabel)
    plt.grid()

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
    verticalalignment='top', bbox=props)

    plt.savefig(outPlotName+".pdf")
    plt.savefig(outPlotName+".png")
    plt.close(fig)

    output_list = []
    output_list.append(np.array(x_array).mean())
    output_list.append(np.array(x_array).std())
    return output_list


def mkPlot_nominal(nBins_val,xmin_val,xmax_val,x_array,xlabel,outPlotName):
    nBins, xmin, xmax = nBins_val, xmin_val,xmax_val
    bins = np.linspace(xmin, xmax, nBins+1)

    fig, ax = plt.subplots()
    plt.hist(x_array, bins=bins, label="")

    plt.xlabel(xlabel)
    plt.grid()


    # props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    # plt.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
    # verticalalignment='top', bbox=props)

    plt.savefig(outPlotName+".pdf")
    plt.savefig(outPlotName+".png")
    plt.close(fig)


def mk_mu(r_array):
    r_mean = []
    r_down01sigma = []
    r_up01sigma = []
    for index in range(0,len(r_array)):
        if ((index+2*index)<len(r_array) ):
            r_mean.append(r_array[index+2*index])
        if (index+1+(2*index) < len(r_array)):
            r_down01sigma.append(r_array [index+1+(2*index)])
        if (index+2+(2*index) < len(r_array)):
            r_up01sigma.append(r_array[index+2+(2*index)])

    return r_mean,r_down01sigma,r_up01sigma

expectSignal = [1]
pdfIndex = [0,1,2,3]
# mass = [60]
mass = [60,55,50,45,40,30,25,20,15]
treeName = "limit"
branchName = "r"

inDir = "/afs/cern.ch/work/t/twamorka/fggfinalfit_h4g_run2/CMSSW_10_2_13/src/flashggFinalFit/Datacard/"
outDir = "/eos/user/t/twamorka/www/BiasStudies_16Jan2021_AlternatePullDefinition/"
pdfIndexMap = {0:'1st Order Bernstein', 1:'1st Order Exponential',2:'1st Order Laurent', 3: '1st Order Power Law'}

for m in mass: ## Loop over m(a)
    for p in pdfIndex: ## Loop over toy function
        mean_list = []
        for e in expectSignal: ## Loop for different r_truth values
            # mean_list = []
            stddev_list = []
            print "m: ", m, " p: ", p , " e: ", e
            if (e==0):
                fileName = inDir+"BiasStudies_M"+str(m)+"_2000Toys_noSyst/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin0_rmax2.MultiDimFit.mH125.123456.root"
                fileName_Envelope = inDir+"BiasStudies_M"+str(m)+"_2000Toys_noSyst/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin0_rmax2_Envelope.MultiDimFit.mH125.123456.root"
            elif (e==1):
                fileName = inDir+"BiasStudies_M"+str(m)+"_2000Toys_noSyst/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin0_rmax10.MultiDimFit.mH125.123456.root"
                fileName_Envelope = inDir+"BiasStudies_M"+str(m)+"_2000Toys_noSyst/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin0_rmax10_Envelope.MultiDimFit.mH125.123456.root"

            file = ROOT.TFile(fileName)
            tree = file.Get(treeName)

            file_Envelope = ROOT.TFile(fileName_Envelope)
            tree_Envelope = file.Get(treeName)

            r_array_pdf0 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==0")
            r_array_pdf1 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==1")
            r_array_pdf2 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==2")
            r_array_pdf3 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==3")

            r_array_Envelope = tree2array(tree_Envelope,branches=branchName)


            array_pdfindex_0 = mk_mu(tree2array(tree,branches="pdfindex_H4GTag_Cat0_13TeV"))[0]


            mkPlot_nominal(10,0,4,array_pdfindex_0,'PDF index',outDir+"M"+str(m)+"_nFit_pdfGen_"+str(p)+"_expectSignal_"+str(e)+"_1000Toys")



            r_mean = []
            r_sigma = []
            mean_list_tmp = []
            up01sigma = []
            down01sigma = []
            for pdf in [0,1,2,3]:
                r_mean_tmp = mk_mu(tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV=="+str(pdf)))[0]
                r_down01sigma = mk_mu(tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV=="+str(pdf)))[1]
                r_up01sigma = mk_mu(tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV=="+str(pdf)))[2]
                r_sigma_tmp = 0.5*np.subtract(r_up01sigma,r_down01sigma)

                up01sigma_tmp = np.abs(np.subtract(r_mean_tmp,r_up01sigma))
                down01sigma_tmp = np.abs(np.subtract(r_mean_tmp,r_down01sigma))

                r_mean.append(r_mean_tmp)
                r_sigma.append(r_sigma_tmp)

                up01sigma.append(up01sigma_tmp)
                down01sigma.append(down01sigma_tmp)

            r_mean_Envelope = mk_mu(tree2array(tree_Envelope,branches=branchName))[0]
            r_down01sigma_Envelope = mk_mu(tree2array(tree_Envelope,branches=branchName))[1]
            r_up01sigma_Envelope = mk_mu(tree2array(tree_Envelope,branches=branchName))[2]
            r_sigma_Envelope = 0.5*np.subtract(r_up01sigma_Envelope,r_down01sigma_Envelope)

            up01sigma.append(np.abs(np.subtract(r_mean_Envelope,r_up01sigma_Envelope)))
            down01sigma.append(np.abs(np.subtract(r_mean_Envelope,r_down01sigma_Envelope)))

            r_mean.append(r_mean_Envelope)
            r_sigma.append(r_sigma_Envelope)


            # print len(r_mean)



            for i1 in range(0,len(r_mean)):
                # pull = []
                r_truth = np.ones(len(r_mean[i1]))*e

                pull_num =  np.subtract(r_truth, r_mean[i1])
                pull_denom = r_sigma[i1]
                # pull = np.divide(pull_num,up01sigma[i1])
                if (e==0):
                   pull = np.divide(np.subtract(r_truth, r_mean[i1]),up01sigma[i1] )

                elif (e==1):
                    pull = np.divide(pull_num, pull_denom )
                   # if (r_mean[i1] < e):
                   #     pull = (np.divide(np.subtract(r_truth, r_mean[i1]),down01sigma[i1] ))
                   # elif (r_mean[i1] > e):
                   #     pull = (np.divide(np.subtract(r_truth, r_mean[i1]),up01sigma[i1] ))

                # print len(pull)



                mkPlot(100,-1,3,r_mean[i1],p,i1,e,'r(fit)',outDir+"M"+str(m)+"_rFit_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))

                mkPlot(100,-2.5,2.5,pull_num,p,i1,e,'r(truth)-r(fit)',outDir+"M"+str(m)+"_PullNum_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                mkPlot(100,-2.5,2.5,pull_denom,p,i1,e,'Sigma(r)',outDir+"M"+str(m)+"_PullDenom_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                # mkPlot(100,-2.5,2.5,down01sigma,p,i1,e,'Down 1 sigma',outDir+"M"+str(m)+"_Down01Sigma_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                # mkPlot(100,-2.5,2.5,up01sigma,p,i1,e,'Up 1 sigma',outDir+"M"+str(m)+"_Up01Sigma_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                mean_list_tmp.append(mkPlot(100,-10,10,pull,p,i1,e,'pull',outDir+"M"+str(m)+"_Pull_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))[0])
        #
        #         mean_list_tmp.append(mkPlot(100,-10,10,pull,p,i1,e,'pull',outDir+"M"+str(m)+"_Pull_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))[0])
        # #          # stddev_list.append(mkPlot(100,-2,1,pull,p,i1,e,'pull',outDir+"M"+str(m)+"_Pull_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e)+"_1000Toys")[1])
        # #
            mean_list.append(mean_list_tmp)
        #
        #
        pdf0_list = [ mean_list[0][0]]#,mean_list[1][0] ]
        pdf1_list = [ mean_list[0][1]]#,mean_list[1][1] ]
        pdf2_list = [ mean_list[0][2]]#,mean_list[1][2] ]
        pdf3_list = [ mean_list[0][3]]#,mean_list[1][3] ]
        envelope_list = [ mean_list[0][4]]#,mean_list[1][4]]
        # mean_down = [-0.14]
        # mean_up = [0.14]
        # x_arr = ['0','1']
        x_arr = ['1']
        plt.figure()
        #
        plt.title("Toy Function: "+str(pdfIndexMap[p]))
        plt.plot(array(pdf0_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Bernstein')
        plt.plot(array(pdf1_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Exponential')
        plt.plot(array(pdf2_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Laurent ')
        plt.plot(array(pdf3_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Power Law')
        plt.plot(array(envelope_list,dtype=float),x_arr,marker='o',linestyle='none',label='Envelope')
        plt.axvline(-0.14,color='black',linestyle='--')
        plt.axvline(0.14,color='black',linestyle='--')
        plt.legend()
        plt.xlabel(r'$\frac{(\mu-\tilde{\mu})}{\sigma_{\mu}}$')
        plt.ylabel(r'$\tilde{\mu}$')
        plt.grid()
        plt.xlim(-0.5,0.5)
        plt.savefig(outDir+"M"+str(m)+"PullVsTruthSignalStrength_pdfGen_"+str(p)+".pdf")
        plt.savefig(outDir+"M"+str(m)+"PullVsTruthSignalStrength_pdfGen_"+str(p)+".png")
