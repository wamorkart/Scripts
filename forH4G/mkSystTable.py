import ROOT
from ROOT import *
import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import array
from prettytable import PrettyTable
plt.rcParams.update({'font.size': 10})
gROOT.SetBatch(kTRUE)

inDir = "/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_22Dec2020/dataset_PhoMVA_manyKinVars_aMass_fullRun2_DataMix_HighStat_kinWeight_dataSBScaling_MGPodd_bkgOdd/"

year = [2016, 2017 , 2018]

# mass = [15]
mass = [15,20,25,30,40,45,50,55,60]
outDir = '/eos/user/t/twamorka/www/Training_forPreApp_HighStat_oldfggfinalfit/'

def mkPlot(nBins_val,xmin_val,xmax_val,x_array,xlabel,outPlotName):
    nBins, xmin, xmax = nBins_val, xmin_val,xmax_val
    bins = np.linspace(xmin, xmax, nBins+1)

    fig, ax = plt.subplots()
    plt.hist(x_array, bins=bins, label="")

    textstr = '\n'.join((
        r'Mean=%s' % (str(round(np.array(x_array).mean(),5))) ,
        r'RMS=%s' % (str(round(np.array(x_array).std(),5))) ,
        ))



    plt.xlabel(xlabel)
    plt.grid()

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
    verticalalignment='top', bbox=props)

    plt.savefig(outPlotName+".pdf")
    plt.savefig(outPlotName+".png")
    plt.close(fig)


systLabels = [""]
for direction in ["Up","Down"]:
           systLabels.append("MvaShift%s01sigma"%direction)
           systLabels.append("SigmaEOverEShift%s01sigma"%direction)
           systLabels.append("MaterialCentralBarrel%s01sigma"%direction)
           systLabels.append("MaterialOuterBarrel%s01sigma"%direction)
           systLabels.append("MaterialForward%s01sigma"%direction)
           systLabels.append("FNUFEB%s01sigma"%direction)
           systLabels.append("FNUFEE%s01sigma"%direction)
           systLabels.append("MCScaleGain6EB%s01sigma"%direction)
           systLabels.append("MCScaleGain1EB%s01sigma"%direction)
           systLabels.append("MCScaleGain1EB%s01sigma"%direction)

           systLabels.append("MCScaleHighR9EB%s01sigma" % direction)
           systLabels.append("MCScaleHighR9EE%s01sigma" % direction)
           systLabels.append("MCScaleLowR9EB%s01sigma" % direction)
           systLabels.append("MCScaleLowR9EE%s01sigma" % direction)
           systLabels.append("MCSmearHighR9EBPhi%s01sigma" % direction)
           systLabels.append("MCSmearHighR9EBRho%s01sigma" % direction)
           systLabels.append("MCSmearHighR9EEPhi%s01sigma" % direction)
           systLabels.append("MCSmearHighR9EERho%s01sigma" % direction)
           systLabels.append("MCSmearLowR9EBPhi%s01sigma" % direction)
           systLabels.append("MCSmearLowR9EBRho%s01sigma" % direction)
           systLabels.append("MCSmearLowR9EEPhi%s01sigma" % direction)
           systLabels.append("MCSmearLowR9EERho%s01sigma" % direction)
           systLabels.append("ShowerShapeHighR9EB%s01sigma" % direction)
           systLabels.append("ShowerShapeHighR9EE%s01sigma" % direction)
           systLabels.append("ShowerShapeLowR9EB%s01sigma" % direction)
           systLabels.append("ShowerShapeLowR9EE%s01sigma" % direction)
           systLabels.append("SigmaEOverEShift%s01sigma" % direction)

n_2016_diff_total = []
n_2017_diff_total = []
n_2018_diff_total = []

n_2016_diff_percentage_total = []
n_2017_diff_percentage_total = []
n_2018_diff_percentage_total = []
for m in mass:
    print "m(a): ", m
    n_events = []
    for sys_i,syst in enumerate(systLabels):
        systLabel = ""
        if syst != "":
            systLabel += '_' + syst

        ch_2016 = ROOT.TChain()
        # f_in_2016 = inDir+str(m)+'/Reduced_8Events_1Cats/signal_m_'+str(m)+'_2016_even_skim.root'
        # ch_2016.AddFile(f_in_2016+'/H4GTag_Cat0'+str(systLabel)+'_13TeV')
        # ch_2016.AddFile(f_in_2016+'/H4GTag_Cat0'+str(systLabel)+'_13TeV')
        # h_2016 = ROOT.TH1F('h_2016','h_2016',100, -1, 1)
        # ch_2016.Draw('bdt >> h_2016',ROOT.TCut('weight'))
        f_in_2016 = inDir+str(m)+'/signal_m_'+str(m)+'_2016_even_matched.root'
        ch_2016.AddFile(f_in_2016+'/HAHMHToAA_AToGG_MA_'+str(m)+'GeV_TuneCUETP8M1_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0'+str(systLabel))
        h_2016 = ROOT.TH1F('h_2016','h_2016',100, 0, 50000)
        ch_2016.Draw('tp_mass >> h_2016',ROOT.TCut('weight'))
        n_2016 = h_2016.Integral()

        ch_2017 = ROOT.TChain()
        # f_in_2017 = inDir+str(m)+'/Reduced_8Events_1Cats/signal_m_'+str(m)+'_2017_even_skim.root'
        # ch_2017.AddFile(f_in_2017+'/H4GTag_Cat0'+str(systLabel)+'_13TeV')
        # h_2017 = ROOT.TH1F('h_2017','h_2017',100, -1, 1)
        # ch_2017.Draw('bdt >> h_2017',ROOT.TCut('weight'))
        f_in_2017 = inDir+str(m)+'/signal_m_'+str(m)+'_2017_even_matched.root'
        ch_2017.AddFile(f_in_2017+'/HAHMHToAA_AToGG_MA_'+str(m)+'GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0'+str(systLabel))
        h_2017 = ROOT.TH1F('h_2017','h_2017',100, 0, 50000)
        ch_2017.Draw('tp_mass >> h_2017',ROOT.TCut('weight'))
        n_2017 = h_2017.Integral()

        ch_2018 = ROOT.TChain()
        # f_in_2018 = inDir+str(m)+'/Reduced_8Events_1Cats/signal_m_'+str(m)+'_2018_even_skim.root'
        # ch_2018.AddFile(f_in_2018+'/H4GTag_Cat0'+str(systLabel)+'_13TeV')
        # h_2018 = ROOT.TH1F('h_2018','h_2018',100, -1, 1)
        # ch_2018.Draw('bdt >> h_2018',ROOT.TCut('weight'))
        f_in_2018 = inDir+str(m)+'/signal_m_'+str(m)+'_2018_even_matched.root'
        ch_2018.AddFile(f_in_2018+'/HAHMHToAA_AToGG_MA_'+str(m)+'GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0'+str(systLabel))
        h_2018 = ROOT.TH1F('h_2018','h_2018',100, 0, 50000)
        ch_2018.Draw('tp_mass >> h_2018',ROOT.TCut('weight'))
        n_2018 = h_2018.Integral()

        h_2016.SetDirectory(0)
        h_2017.SetDirectory(0)
        h_2018.SetDirectory(0)
        #
        if syst == "":
            n_events.append(['Nominal', n_2016, n_2017, n_2018] )
        else:
            n_events.append([syst, n_2016, n_2017, n_2018] )


    n_2016_diff = []
    n_2017_diff = []
    n_2018_diff = []
    n_2016_diff_percentage = []
    n_2017_diff_percentage = []
    n_2018_diff_percentage = []
    for i in range(len(n_events)):
        n_2016_diff.append(n_events[i][1] - n_events[0][1])
        n_2017_diff.append(n_events[i][2] - n_events[0][2])
        n_2018_diff.append(n_events[i][3] - n_events[0][3])

        n_2016_diff_percentage.append((n_events[i][1] - n_events[0][1])*100/n_events[0][1])
        n_2017_diff_percentage.append((n_events[i][2] - n_events[0][2])*100/n_events[0][2])
        n_2018_diff_percentage.append((n_events[i][3] - n_events[0][3])*100/n_events[0][3])

    n_2016_diff_total.append(n_2016_diff)
    n_2017_diff_total.append(n_2017_diff)
    n_2018_diff_total.append(n_2018_diff)

    n_2016_diff_percentage_total.append(n_2016_diff_percentage)
    n_2017_diff_percentage_total.append(n_2017_diff_percentage)
    n_2018_diff_percentage_total.append(n_2018_diff_percentage)



    x = PrettyTable()
    x.field_names = [ "Syst. label","2016 Yield Diff (% diff)","2017 Yield Diff (% diff)","2018 Yield Diff (% diff)" ]
    for i in range(1,len(n_events)):
        x.add_row([n_events[i][0], str(round(n_2016_diff[i],3)) + " ("+str(round(n_2016_diff_percentage[i],3)) +"%)",str(round(n_2017_diff[i],3)) + " ("+str(round(n_2017_diff_percentage[i],3)) +"%)",str(round(n_2018_diff[i],3)) + " ("+str(round(n_2018_diff_percentage[i],3)) +"%)"])
    data = x.get_string()
    with open(outDir+str(m)+'/NSig_Diff_evaluated_on_matched_tree.txt', 'w') as f:
         f.write(data)

for i1 in range(0, len(n_2016_diff_total)):

    mkPlot(100,-0.02,0.02,n_2016_diff_total[i1],'(Nominal - Systematic): 2016',outDir+str(mass[i1]) +'/Plot_DiffYields_evaluated_on_matched_tree_2016')
    mkPlot(100,-0.02,0.02,n_2017_diff_total[i1],'(Nominal - Systematic): 2017',outDir+str(mass[i1]) +'/Plot_DiffYields_evaluated_on_matched_tree_2017')
    mkPlot(100,-0.02,0.02,n_2018_diff_total[i1],'(Nominal - Systematic): 2018',outDir+str(mass[i1]) +'/Plot_DiffYields_evaluated_on_matched_tree_2018')

    mkPlot(100,-100,100,n_2016_diff_percentage_total[i1],'(Nominal - Systematic)*100/Nominal : 2016',outDir+str(mass[i1]) +'/Plot_PercentageDiffYields_evaluated_on_matched_tree_2016')
    mkPlot(100,-100,100,n_2017_diff_percentage_total[i1],'(Nominal - Systematic)*100/Nominal : 2017',outDir+str(mass[i1]) +'/Plot_PercentageDiffYields_evaluated_on_matched_tree_2017')
    mkPlot(100,-100,100,n_2018_diff_percentage_total[i1],'(Nominal - Systematic)*100/Nominal : 2018',outDir+str(mass[i1]) +'/Plot_PercentageDiffYields_evaluated_on_matched_tree_2018')
