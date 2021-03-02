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
from scipy import stats


plt.rcParams.update({'font.size': 10})
gROOT.SetBatch(kTRUE)

def mkPlot(nBins_val,xmin_val,xmax_val,x_array,p,f,e,xlabel,outPlotName):
    nBins, xmin, xmax = nBins_val, xmin_val,xmax_val
    bins = np.linspace(xmin, xmax, nBins+1)

    fig, ax = plt.subplots()
    plt.hist(x_array, bins=bins, label="")
    # pdfIndexMap = {0:'1st Order Bernstein',1:'1st Order Exponential',2:'1st Order Power Law', 3: '1st Order Laurent', 4: '2nd Order Laurent',5:'Envelope'}

    # pdfIndexMap = {0:'1st Order Bernstein',1:'1st Order Exponential',2:'1st Order Power Law', 3: '1st Order Laurent', 4: 'Envelope'}

    pdfIndexMap = {0:'1st Order Bernstein', 1:'2nd Order Bernstein',2:'1st Order Exponential',3:'1st Order Power Law', 4: '1sr Order Laurent', 5: 'Envelope'}
    # pdfIndexMap = {0:'1st Order Bernstein', 1:'1st Order Exponential',2:'1st Order Laurent', 3:'2nd Order Laurent',4:'2nd Order Laurent?',5: '1st Order Power Law',6: 'Envelope'}

    textstr = '\n'.join((
        r'$r_{Truth}$=%s' % (str(e) ),
        r'Mean=%s' % (str(round(np.array(x_array).mean(),3))) ,
        # r'Mode=%s' % (str(round(np.array(x_array).mode(),3))) ,
        r'RMS=%s' % (str(round(np.array(x_array).std(),3))) ,
        r'PDF Generated=%s' % (pdfIndexMap[p] ),
        r'PDF Fit=%s' % (pdfIndexMap[f] )
        ))

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


    plt.savefig(outPlotName+".pdf")
    plt.savefig(outPlotName+".png")
    plt.close(fig)


def mk_mu(r_array,e):
    r_mean = []
    r_down01sigma = []
    r_up01sigma = []

    r_mean_0 = []
    r_down01sigma_0 = []
    r_up01sigma_0 = []
    for index in range(0,len(r_array)):
        if ((index+2*index)<len(r_array) ):
            r_mean.append(r_array[index+2*index])
        if (index+1+(2*index) < len(r_array) ):
            r_down01sigma.append(r_array [index+1+(2*index)])
        if (index+2+(2*index) < len(r_array) ):
            r_up01sigma.append(r_array[index+2+(2*index)])

    if (e==0):
        for i1 in range (0, len(r_mean)):
            if (r_mean[i1]>-0.99):
            # if (1>0):
                # print r_mean[i1],"  ",   r_down01sigma[i1],"  ", r_up01sigma[i1]
                r_mean_0.append(r_mean[i1])
                r_down01sigma_0.append(r_down01sigma[i1])
                r_up01sigma_0.append(r_up01sigma[i1])

    if (e==0):
        return r_mean_0,r_down01sigma_0,r_up01sigma_0
    else: return r_mean,r_down01sigma,r_up01sigma

# expectSignal = [0.3,1]
pdfIndex = [0,1,2,3,4]
# mass = [60,55,50,45,40,25,20,15]#,40]
mass = [30]
# pdfIndex = [1]
# mass = [60,55,45,25,20,15]
# mass = [60, 55, 50, 45, 40, 30, 25,20,15]
# mass = [55,50,45,40,30,25,20,15]
treeName = "limit"
branchName = "r"

inDir = "/afs/cern.ch/work/t/twamorka/fggfinalfit_h4g_run2/CMSSW_10_2_13/src/flashggFinalFit/Datacard/"
outDir = "/eos/user/t/twamorka/www/H4G_for_PreApp/BiasPlots_6Feb2021/"
#outDir = "/eos/user/t/twamorka/www/H4G_for_PreApp/BiasStudyPlots_AltDefinition/"
# pdfIndexMap = {0:'1st Order Bernstein',1:'1st Order Exponential',2:'1st Order Power Law', 3: '1st Order Laurent', 4: 'Envelope'}
# pdfIndexMap = {0:'1st Order Bernstein',1:'1st Order Exponential',2:'1st Order Power Law', 3: '1st Order Laurent', 4: '2nd Order Laurent',5:'Envelope'}

pdfIndexMap = {0:'1st Order Bernstein', 1:'2nd Order Bernstein',2:'1st Order Exponential',3:'1st Order Power Law', 4: '1sr Order Laurent', 5: 'Envelope'}
# pdfIndexMap = {0:'1st Order Bernstein', 1:'1st Order Exponential',2:'1st Order Power Law', 3: '1st Order Laurent'}
# pdfIndexMap = {0:'1st Order Bernstein', 1:'1st Order Exponential',2:'1st Order Laurent', 3:'2nd Order Laurent',4:'2nd Order Laurent?',5: '1st Order Power Law'}
for m in mass: ## Loop over m(a)
    if (m==60): expectSignal=["0.3"]#,1]
    elif (m==55): expectSignal=["0.41"]#,1]
    elif (m==50): expectSignal=["0.53"]#,1]
    elif (m==45): expectSignal=["0.70"]#,1]
    elif (m==40): expectSignal=["0.73"]#,1]
    elif (m==30): expectSignal=["0.87"]#,1]
    elif (m==25): expectSignal=["0.88"]#,1]
    elif (m==20): expectSignal=["0.74"]#,1]
    elif (m==15): expectSignal=["0.99"]#,1]
    envelope_bias = []
    for p in pdfIndex: ## Loop over toy function
        mean_list = []
        for e in expectSignal: ## Loop for different r_truth values
            # mean_list = []
            stddev_list = []
            print "m: ", m, " p: ", p , " e: ", e
            if (e!=1):
                fileName = inDir+"BiasStudies_M"+str(m)+"_2000Toys_23Jan2021/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin-2_rmax10.MultiDimFit.mH125.123456.root"
                fileName_Envelope = inDir+"BiasStudies_M"+str(m)+"_2000Toys_23Jan2021/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin-2_rmax10_Envelope.MultiDimFit.mH125.123456.root"
            elif (e==1):
                fileName = inDir+"BiasStudies_M"+str(m)+"_2000Toys_noSyst/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin0_rmax10.MultiDimFit.mH125.123456.root"
                fileName_Envelope = inDir+"BiasStudies_M"+str(m)+"_2000Toys_noSyst/higgsCombine_M"+str(m)+"_pdfindex"+str(p)+"_signal"+str(e)+"_2000Toys_rmin0_rmax10_Envelope.MultiDimFit.mH125.123456.root"

            file = ROOT.TFile(fileName)
            tree = file.Get(treeName)

            file_Envelope = ROOT.TFile(fileName_Envelope)
            tree_Envelope = file_Envelope.Get(treeName)

            r_array_pdf0 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==0")
            r_array_pdf1 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==1")
            r_array_pdf2 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==2")
            r_array_pdf3 = tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV==3")

            r_array_Envelope = tree2array(tree_Envelope,branches=branchName)

            # array_pdfindex_0 = mk_mu(tree2array(tree,branches="pdfindex_H4GTag_Cat0_13TeV"),e)[0]
            # mkPlot_nominal(10,0,4,array_pdfindex_0,'PDF index',outDir+"M"+str(m)+"_nFit_pdfGen_"+str(p)+"_expectSignal_"+str(e)+"_1000Toys")

            r_mean = []
            r_sigma = []
            mean_list_tmp = []
            up01sigma = []
            down01sigma = []
            r_mean_cleaned = []

            for pdf in [0,1,2,3,4]:#,5]:
            #for pdf in [3]:
                r_mean_tmp = mk_mu(tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV=="+str(pdf)),e)[0] ## r central value
                r_down01sigma = mk_mu(tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV=="+str(pdf)),e)[1] ## r-1 sigma
                r_up01sigma = mk_mu(tree2array(tree,branches=branchName,selection="pdfindex_H4GTag_Cat0_13TeV=="+str(pdf)),e)[2] ## r+1 sigma
                r_sigma_tmp = 0.5*np.subtract(r_up01sigma,r_down01sigma) ##( (r+1sigma) - (r-1sigma) )/2

                up01sigma_tmp = np.abs(np.subtract(r_mean_tmp,r_up01sigma)) ## abs(r_central-r_up01sigma)
                down01sigma_tmp = np.abs(np.subtract(r_mean_tmp,r_down01sigma))## abs(r_central-r_down01sigma)

                r_mean.append(r_mean_tmp)
                r_sigma.append(r_sigma_tmp)

                up01sigma.append(up01sigma_tmp)
                down01sigma.append(down01sigma_tmp)

            r_mean_Envelope = mk_mu(tree2array(tree_Envelope,branches=branchName),e)[0]
            r_down01sigma_Envelope = mk_mu(tree2array(tree_Envelope,branches=branchName),e)[1]
            r_up01sigma_Envelope = mk_mu(tree2array(tree_Envelope,branches=branchName),e)[2]
            r_sigma_Envelope = 0.5*np.subtract(r_up01sigma_Envelope,r_down01sigma_Envelope)

            up01sigma.append(np.abs(np.subtract(r_mean_Envelope,r_up01sigma_Envelope)))
            down01sigma.append(np.abs(np.subtract(r_mean_Envelope,r_down01sigma_Envelope)))

            r_mean.append(r_mean_Envelope)
            r_sigma.append(r_sigma_Envelope)

            for i1 in range(0,len(r_mean)):
                # if (r_mean[i1]==0):
                    # print (r_mean[i1])
                # pull = []
                r_truth = np.ones(len(r_mean[i1]))*float(e)

                pull_num =  np.subtract(r_truth, r_mean[i1])
                #pull_denom = r_sigma[i1]
                for i2 in range(0,len(r_mean[i1])):
                    if (r_mean[i1][i2] > float(e) and up01sigma[i1][i2]!=0):
                       pull_denom = down01sigma[i1]
                       pull = (np.divide(pull_num,up01sigma[i1] ))
                       #pull_denom = up01sigma[i1]
                    elif(r_mean[i1][i2] < float(e)and down01sigma[i1][i2]!=0):
                       pull = (np.divide(pull_num,down01sigma[i1] ))
                       pull_denom = up01sigma[i1]
                #print (len(pull_num), " " , len(pull_denom))
                #print pull_denom
                #pull = np.divide(pull_num,pull_denom)
                # if (e==0):
                   # pull = np.divide(np.subtract(r_truth, r_mean[i1]),up01sigma[i1] )

                # elif (e==1):
                    # pull = np.divide(pull_num, pull_denom )
                # print pull_denom
                #pull_num_cleaned = []
                #pull_denom_cleaned = []
                pull_cleaned = []
                for p1 in range(0,len(pull)):
                    if (pull_denom[p1]!=0 and abs(pull[p1]) < 10):
                       #print "not defined pull"
                    #print math.isnan(pull_denom[p1])
                    #if (math.isnan(pull[p1]) == False):
                    #if ( pull[p1] !=0 ):
                        pull_cleaned.append(pull[p1])
                #        pull_denom_cleaned.append(pull_denom[p1])
                #        pull_num_cleaned.append(pull_num[p1])

                #pull_cleaned = np.divide(pull_num_cleaned,pull_denom_cleaned)
                #print len(pull_denom_cleaned)
                #print len(pull_denom)
                #print len(pull)
                #print len(pull_cleaned)
                #print np.array(pull_cleaned).mean()
                mkPlot(100,-1,10,r_mean[i1],p,i1,e,'r(fit)',outDir+"M"+str(m)+"_rFit_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                mkPlot(100,0,2,r_truth,p,i1,e,'r(truth)',outDir+"M"+str(m)+"_rTruth_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                #mkPlot(100,-2.5,2.5,pull_num,p,i1,e,'r(truth)-r(fit)',outDir+"M"+str(m)+"_PullNum_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                #mkPlot(100,-2.5,2.5,pull_denom,p,i1,e,'Sigma(r)',outDir+"M"+str(m)+"_PullDenom_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                #mkPlot(100,-2.5,2.5,pull_num_cleaned,p,i1,e,'r(truth)-r(fit)',outDir+"M"+str(m)+"_PullNum_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                #mkPlot(100,-2.5,2.5,pull_denom_cleaned,p,i1,e,'Sigma(r)',outDir+"M"+str(m)+"_PullDenom_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                mkPlot(100,-2.5,2.5,down01sigma[i1],p,i1,e,'Down 1 sigma',outDir+"M"+str(m)+"_Down01Sigma_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                mkPlot(100,-2.5,2.5,up01sigma[i1],p,i1,e,'Up 1 sigma',outDir+"M"+str(m)+"_Up01Sigma_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))
                # mkPlot(100,-10,10,pull,p,i1,e,'pull',outDir+"M"+str(m)+"_Pull_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e)+"r_-1to2_greaterthan_m0p99")
                # mean_list_tmp.append(mkPlot(100,-10,10,pull,p,i1,e,'pull',outDir+"M"+str(m)+"_Pull_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))[0])
                mean_list_tmp.append(mkPlot(100,-10,10,pull_cleaned,p,i1,e,'pull',outDir+"M"+str(m)+"_Pull_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))[0])
                # print mkPlot(100,-10,10,pull_cleaned,p,i1,e,'pull',outDir+"M"+str(m)+"_Pull_pdfGen_"+str(p)+"_pdfFit_"+str(i1)+"_expectSignal_"+str(e))[0]

            mean_list.append(mean_list_tmp)

        #print mean_list
        pdf0_list = [ mean_list[0][0]]#,mean_list[1][0] ]
        pdf1_list = [ mean_list[0][1]]#,mean_list[1][1] ]
        pdf2_list = [ mean_list[0][2]]#,mean_list[1][2] ]
        pdf3_list = [ mean_list[0][3]]#,mean_list[1][3] ]
        pdf4_list = [mean_list[0][4]]
        # pdf5_list = [mean_list[0][5]]
        envelope_list = [ mean_list[0][5]]#,mean_list[1][4]]
        # print envelope_list
        envelope_bias.append(mean_list[0][5])
        # # x_arr = ['0.3','1']
        x_arr = expectSignal
        plt.figure()

        plt.title("Toy Function: "+str(pdfIndexMap[p]))
        # plt.plot(array(pdf0_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Bernstein',color='red')
        # plt.plot(array(pdf1_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Exponential',color='orange')
        # plt.plot(array(pdf2_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Power Law ',color='blue')
        # plt.plot(array(pdf3_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Laurent ',color='purple')
        # plt.plot(array(pdf4_list,dtype=float),x_arr,marker='o',linestyle='none',label='2nd Order Laurent ',color='pink')
        # plt.plot(array(envelope_list,dtype=float),x_arr,marker='o',linestyle='none',label='Envelope')
        plt.plot(array(pdf0_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Bernstein',color='red')
        plt.plot(array(pdf1_list,dtype=float),x_arr,marker='o',linestyle='none',label='2nd Order Bernstein',color='green')
        plt.plot(array(pdf2_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Exponential ',color='orange')
        plt.plot(array(pdf3_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Power Law ',color='blue')
        plt.plot(array(pdf4_list,dtype=float),x_arr,marker='o',linestyle='none',label='1st Order Laurent ',color='purple')
        plt.plot(array(envelope_list,dtype=float),x_arr,marker='o',linestyle='none',label='Envelope',color='black')
        plt.axvline(-0.14,color='black',linestyle='--')
        plt.axvline(0.14,color='black',linestyle='--')
        plt.legend()
        plt.xlabel(r'$\frac{(\mu-\tilde{\mu})}{\sigma_{\mu}}$')
        plt.ylabel(r'$\tilde{\mu}$')
        plt.grid()
        plt.xlim(-0.5,0.5)
        plt.savefig(outDir+"M"+str(m)+"PullVsTruthSignalStrength_pdfGen_"+str(p)+".pdf")
        plt.savefig(outDir+"M"+str(m)+"PullVsTruthSignalStrength_pdfGen_"+str(p)+".png")

    print envelope_bias
    plt.figure()
    plt.grid()
    color_list = ['red','green','orange','blue','purple']
    legend_list = ['1st Order Bernstein','2nd Order Bernstein','1st Order Exponential','1st Order Power Law','1st Order Laurent']
    for evi, ev in enumerate(envelope_bias):

        # plt.title("Toy Function: "+str(pdfIndexMap[p]))
        plt.plot(array(ev,dtype=float),x_arr,marker='o',linestyle='none',color=color_list[evi],label=legend_list[evi])
        plt.axvline(-0.14,color='black',linestyle='--')
        plt.axvline(0.14,color='black',linestyle='--')
        plt.legend()
        plt.xlabel(r'$\frac{(\mu-\tilde{\mu})}{\sigma_{\mu}}$')
        plt.ylabel(r'$\tilde{\mu}$')

        plt.xlim(-0.5,0.5)
        plt.savefig(outDir+"M"+str(m)+"_EnvelopeBias.pdf")
        plt.savefig(outDir+"M"+str(m)+"_EnvelopeBias.png")
