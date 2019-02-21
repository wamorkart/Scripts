from pullClass import *
from ROOT import *
import json, os
import shutil
from configs import *
import resource

gStyle.SetOptStat(0)
TGaxis.SetMaxDigits(3)


dummyTFile = TFile("dummy.root", "RECREATE")

NiceBlue = '#51A7F9'
NiceBlueDark = '#2175E0'
NiceGreen = '#6FBF41'
NiceGreen2 = '#35DC3D'
NiceYellow = '#FBE12A'
NiceYellow2 = '#FEEA01'
NiceOrange = '#F0951A'
NiceRed = '#FA4912'
NicePurple = '#885BB2'
NicePaleYellow = '#FFFF66'
NiceMidnight = '#000080'
NiceTangerine = '#FF8000'
cNiceBlue = TColor.GetColor('#51A7F9')
cNiceBlueDark = TColor.GetColor('#2175E0')
cNiceGreen = TColor.GetColor('#6FBF41')
cNiceGreen2 = TColor.GetColor(NiceGreen2)
cNiceGreenDark = TColor.GetColor('#008040')
cNiceYellow = TColor.GetColor('#FBE12A')
cNiceYellow2 = TColor.GetColor(NiceYellow2)
cNiceOrange = TColor.GetColor('#F0951A')
cNiceRed = TColor.GetColor('#FA4912')
cNicePurple = TColor.GetColor('#885BB2')
cNicePaleYellow = TColor.GetColor('#FFFF66')
cNiceMidnight = TColor.GetColor('#000080')
cNiceTangerine = TColor.GetColor('#FF8000')

myCols = [cNiceMidnight, cNiceGreen, kRed, kMagenta+1, cNiceTangerine, cNicePaleYellow, cNiceOrange, cNiceRed, cNicePurple, cNiceGreen, cNiceGreen2]

if not os.path.exists(dirName):
        print dirName, "doesn't exist, creating it..."
        os.makedirs(dirName)
        if os.path.exists(dirName):
                print dirName, "now exists!"

datasets = json.load(data_file)

Trees = {}


# if isPhoCR == True:
# 	Cut += " && (isPhotonCR == 1)"
# 	CutSignal += " && (isPhotonCR == 1)"
# if isPhoCR == False:
# 	Cut += " && (isSignal == 1)"
# 	CutSignal += " && (isSignal == 1)"
# if doSignalRegion == True:
# 	CutSignal += " && ( leadingJet_bDis > "+ str(BTAG) + " || subleadingJet_bDis > "+str(BTAG)+" ) "
# 	Cut += " && ( leadingJet_bDis > "+ str(BTAG) + " || subleadingJet_bDis > "+ str(BTAG) + " ) "
# if doJetCR == True:
# 	Cut += " && leadingJet_bDis < "+ str(BTAG) + " && subleadingJet_bDis < "+ str(BTAG) + " "

CutKin = "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 10 && pho4_pt > 10 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5"
# CutMVA = "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
CutMVA = "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
CutPrune = "&& abs(dp1_mass-dp2_mass) < 6"
# CutnPho = " && n_pho > 3"

Cut_Signal = "1>0"
Cut_Signal += CutKin
# Cut_Signal += CutMVA
# Cut_Signal += CutPrune
# Cut_Signal += CutnPho

# Cut = "npho>3 && pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 10 && pho4_pt > 10"
Cut = "1>0"
Cut += CutKin
# Cut += CutMVA
# Cut += CutPrune
# Cut += CutnPho
if doBlind == True:
	Cut += " && !((tp_mass > 115 && tp_mass < 135))"

weightedcut = "weight"

weightedCut = TCut(weightedcut)

for plot in plots:
    Histos = []
    variable = plot[1]
    varName = plot[2]
    thisStack = 0
    thisHist = 0
    thisStack = myStack('test'+plot[0], varName, varName, dirName, lumi)
    if hideData == True:
        thisStack.hideData()
    if isPhoCR == 1:
        thisStack.makePhoCR()


    thisStack.setYear(year)

    modelHist = TH1F(plot[0]+"_hist", "", plot[3], plot[4], plot[5])

    backgroundHists = []
    background_sum = 0
    for background in datasets["background"]:
        thisName = plot[0]+"_hist"+"_"+background
        thisHist = modelHist.Clone(thisName)
        thisHist.SetLineColor(TColor.GetColor(datasets["background"][background]["color"]))
        thisHist.SetFillColor(TColor.GetColor(datasets["background"][background]["color"]))

        for i,fi in enumerate(datasets["background"][background]["files"]):
            thisTreeLoc = fi["file"]
            if thisTreeLoc not in Trees:
                Trees[thisTreeLoc] = TChain("h4gCandidateDumper/trees/"+str(fi["treeName"]))
                Trees[thisTreeLoc].AddFile(bkgLocation+thisTreeLoc)
                SetOwnership( Trees[thisTreeLoc], True )
            locName = thisName+str(i)
            print locName
            locHist = thisHist.Clone(locName)
            thisWeightedCut = weightedCut * TCut( Cut + '&&' + fi["cut"])
            # print " cut ", fi["cut"]
            # thisWeightedCut = weightedCut * TCut( Cut)
            print "Cut applied on background", thisWeightedCut
            # print "Bkg" , thisWeightedCut
            Trees[thisTreeLoc].Draw(plot[1]+">>"+locName, thisWeightedCut)
            # print locHist.Integral()
            # locHist.Scale(lumi/1.606)
            # locHist.Scale(lumi*2.2)
            locHist.Scale(lumi/20.5)
            # print locHist.Integral()
            thisHist.Add(locHist)
            # print " Background integral ", locHist.Integral()
            Histos.append(locHist)
            background_sum += thisHist.Integral()
            thisFile = TFile(plot[0]+"_"+fi["file"], "RECREATE")
            thisFile.cd()
            thisHist.Write()
            thisFile.Close()
            dummyTFile.cd()
        backgroundHists.append([thisHist, datasets["background"][background]["legend"], datasets["background"][background]["position"]])
        del thisHist
    OrderedBackgrounds = sorted(backgroundHists, key=lambda x: x[2], reverse=True)
    for background in OrderedBackgrounds: thisStack.addHist(background[0], background[1], background[2])
    # print " background sum :", background_sum


    for isi, signal in enumerate(datasets["signal"]):
        # print "isi ", isi, "signal ", signal
        thisName = plot[0]+"_Signal_"+"_"+signal['name']
        thisHist = modelHist.Clone(thisName)
        thisHist.SetLineColor(signal["color"])
        thisHist.SetLineColor(myCols[isi])
        thisHist.SetLineWidth(3)
        thisHist.SetLineStyle(signal["style"])
        thisTreeLoc = signal["file"]
        if thisTreeLoc not in Trees:
            Trees[thisTreeLoc] = TChain("h4gCandidateDumper/trees/"+str(signal["treeName"]))
            Trees[thisTreeLoc].AddFile(signalLocation+thisTreeLoc)
            SetOwnership( Trees[thisTreeLoc], True )
        locName = thisName+str(isi)
        locHist = thisHist.Clone(locName)
        thisWeightedCut = weightedCut *TCut(Cut_Signal)
        print "Cut applied on signal", thisWeightedCut
        Trees[thisTreeLoc].Draw(plot[1]+">>"+locName, thisWeightedCut )
        # print " Signal ", thisWeightedCut
        # locHist.Scale(signal["sfactor"])
        locHist.Scale(lumi*100)
        thisHist.Add(locHist)
        Histos.append(locHist)
        thisStack.addSignal(thisHist, signal["legend"], lumi*1000)
        del thisHist

    # print datasets['data']
    dataName = plot[0]+"_hist"+"_data"
    modelHist.Clear()
    dataHist = 0
    dataHist = modelHist.Clone(dataName)
# # #    dataHist.Sumw2()
    if datasets['data'] not in Trees:
        Trees[datasets['data']] = TChain("h4gCandidateDumper/trees/Data_13TeV_4photons")
        Trees[datasets['data']].AddFile(dataLocation+datasets['data'])
        SetOwnership( Trees[datasets['data']], True )
    Trees[datasets['data']].Draw(plot[1]+">>"+dataName, TCut(Cut))
    print "Data Cut", Cut
    # print " data integral ", dataHist.Integral()
    # print "bkg/data ", background_sum/dataHist.Integral()
    dataHist.SetMarkerStyle(20)
    dataHist.SetMarkerSize(0.8)
    dataHist.SetMarkerColor(1)
    dataHist.SetLineColor(1)
    dataHist.SetLineWidth(2)
    dataHist.SetBinErrorOption(TH1.kPoisson)
    thisStack.addData(dataHist, "Data")
    thisFile = TFile(plot[0]+"_data.root", "RECREATE")
    thisFile.cd()
    dataHist.Write()
    thisFile.Close()
    dummyTFile.cd()
#
    thisStack.drawStack(prefix + plot[0])

    del thisStack
#
#
dummyTFile.Close()
os.system("rm dummy.root")
