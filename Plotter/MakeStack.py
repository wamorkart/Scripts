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

myCols = [cNiceMidnight, cNicePurple,  kMagenta+1, cNiceTangerine, cNiceTangerine, cNicePaleYellow, cNiceOrange, cNiceRed, cNicePurple, cNiceGreen, cNiceGreen2]

if not os.path.exists(dirName):
        print dirName, "doesn't exist, creating it..."
        os.makedirs(dirName)
        if os.path.exists(dirName):
                print dirName, "now exists!"

datasets = json.load(data_file)

Trees = {}

# if doKinCut == True:
#     Cut += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0"
#     Cut_Signal += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0"
if doKinCut == True:
    Cut += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"
    Cut_Signal += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"

if doHggMVALoose == True:
    Cut += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
    Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"

if doHggMVATight == True:
   Cut += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75"
   Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75"

if doEGMVA == True:
   Cut += "&& pho1_EGMVA > 0.2 && pho2_EGMVA > 0.2 && pho3_EGMVA > 0.2 && pho4_EGMVA > 0.2 && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"
   Cut_Signal += "&& pho1_EGMVA > 0.2 && pho2_EGMVA > 0.2 && pho3_EGMVA > 0.2 && pho4_EGMVA > 0.2 && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"

if doHiggsWindow ==  True:
   Cut += "&& tp_mass > 110 && tp_mass < 180"
   Cut_Signal += "&& tp_mass > 110 && tp_mass < 180"

if doBlind == True:
	Cut += " && !((tp_mass > 115 && tp_mass < 135))"

if (mvaWP == 'veryLoose'):
    Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.9 && pho2_MVA_mix > -0.9 && pho3_MVA_mix > -0.9 && pho4_MVA_mix > -0.9'
    Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
elif (mvaWP == 'Loose'):
    Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.9 && pho2_MVA_mix > -0.9 && pho3_MVA_mix > -0.75 && pho4_MVA_mix > -0.75'
    Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75"
elif (mvaWP == 'Medium'):
    Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.75 && pho4_MVA > -0.75'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.2 && pho2_MVA_mix > -0.4 && pho3_MVA_mix > -0.75 && pho4_MVA_mix > -0.75'
    Cut_Signal += "&& pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.75 && pho4_MVA > -0.75"
else:
    Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.5 && pho4_MVA > -0.5'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.2 && pho2_MVA_mix > -0.4 && pho3_MVA_mix > -0.5 && pho4_MVA_mix > -0.5'
    Cut_Signal += "&& pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.5 && pho4_MVA > -0.5"


print "Cut_signal ", Cut_Signal
Cut_DataDriven = "pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass < 180 &&  !((tp_mass > 115 && tp_mass < 135))"
weightedcut = "weight"

weightedCut = TCut(weightedcut)

for plot in plots:
    Histos = []
    variable = plot[1]
    varName = plot[2]
    thisStack = 0
    thisHist = 0
    # thisStack = myStack('test'+plot[0], varName, varName, dirName, lumi)
    thisStack = myStack('test'+plot[0], plot[6], plot[6], dirName, lumi)
    dataintegral = 0
    if hideData == True:
        thisStack.hideData()

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
                # Trees[thisTreeLoc] = TChain("h4gCandidateDumper/trees/"+str(fi["treeName"]))
                Trees[thisTreeLoc] = TChain(str(fi["treeName"]))
                Trees[thisTreeLoc].AddFile(bkgLocation+thisTreeLoc)
                SetOwnership( Trees[thisTreeLoc], True )
            locName = thisName+str(i)
            print "name ", locName
            locHist = thisHist.Clone(locName)
            thisWeightedCut =  "(" +Cut + "&& "+fi["cut"] + "&&" + Cut_MVA  + ")"

            # thisWeightedCut =  "weight* (" +Cut + "&& "+fi["cut"] + "&&" + Cut_MVA  + ")"
            print "Background cut: ", thisWeightedCut
            # print fi["cut"]
            # thisWeightedCut = weightedCut * TCut( fi["cut"])

            # thisWeightedCut = weightedCut * TCut( Cut + '&&' + fi["cut"] + '&&' +Cut_MVA)

            # print "Cut on background: ", thisWeightedCut
            # if 'DataDriven' in locName:
                # thisWeightedCut = weightedCut * TCut( Cut_DataDriven + '&&' + fi["cut"])
            # print "cut on background = ", thisWeightedCut
            # Cut_mix = " pho1_pt_mix > 30 && pho2_pt_mix > 18 && pho3_pt_mix > 15 && pho4_pt_mix > 15 && abs(pho1_eta_mix) < 2.5 && abs(pho2_eta_mix) < 2.5 && abs(pho3_eta_mix) < 2.5 && abs(pho4_eta_mix) < 2.5 && (abs(pho1_eta_mix) < 1.4442 || abs(pho1_eta_mix) > 1.566) && (abs(pho2_eta_mix) < 1.4442 || abs(pho2_eta_mix) > 1.566) && (abs(pho3_eta_mix) < 1.4442 || abs(pho3_eta_mix) > 1.566) && (abs(pho4_eta_mix) < 1.4442 || abs(pho4_eta_mix) > 1.566) && pho1_electronveto_mix==1 && pho2_electronveto_mix==1 && pho3_electronveto_mix==1 && pho4_electronveto_mix==1  && tp_mass_mix > 110 && tp_mass_mix < 180  && (isPresel==1) && !((tp_mass_mix > 115 && tp_mass_mix < 135)) && " + str(Cut_MVA_mix)
            # print "Cut_mix: ", Cut_mix
            # Cut_mix = " pho1_pt_mix > 30 && pho2_pt_mix > 18 && pho3_pt_mix > 15 && pho4_pt_mix > 15 && abs(pho1_eta_mix) < 2.5 && abs(pho2_eta_mix) < 2.5 && abs(pho3_eta_mix) < 2.5 && abs(pho4_eta_mix) < 2.5 && (abs(pho1_eta_mix) < 1.4442 || abs(pho1_eta_mix) > 1.566) && (abs(pho2_eta_mix) < 1.4442 || abs(pho2_eta_mix) > 1.566) && (abs(pho3_eta_mix) < 1.4442 || abs(pho3_eta_mix) > 1.566) && (abs(pho4_eta_mix) < 1.4442 || abs(pho4_eta_mix) > 1.566) && pho1_electronveto_mix==1 && pho2_electronveto_mix==1 && pho3_electronveto_mix==1 && pho4_electronveto_mix==1 && pho1_MVA_mix > -0.2 && pho2_MVA_mix > -0.2 && pho3_MVA_mix > -0.75 && pho4_MVA_mix > -0.75 && tp_mass_mix > 110 && tp_mass_mix < 180  && (isPresel==1) "

            # # Cut_sculpt = "&&  (pho4_pt_mix+pho3_pt_mix+pho2_pt_mix+pho1_pt_mix)/(tp_mass_mix) > 0.75"
            Trees[thisTreeLoc].Draw(plot[1]+">>"+locName, thisWeightedCut)
            # print "Cut_mix + Cut_sculpt : ", Cut_mix + Cut_sculpt
            # Cut_VBF = ""
            # if 'DataDriven' in locName:
            #     print "Data driven background"
            #     Cut_VBF = "weight_VBF"
            # else:
            #     Cut_VBF =  "weight*(" + str(Cut_Signal) + "&& !((tp_mass > 115 && tp_mass < 135)))"
            # print "Cut_VBF: ", Cut_VBF
            # Trees[thisTreeLoc].Draw(plot[6]+">>"+locName, Cut_VBF)
            # locHist.Scale(lumi)
            # if 'DataDriven' in locName:
            #     locHist.Scale(1)
            # else:
            #     locHist.Scale(lumi)
            # locHist.Scale(lumi)
            #if 'DiPhoJets0' in locName:
                #print "DiPhoJets0"
                #locHist.Scale(363.614829153/locHist.Integral())
            #else:
                #print "MC BACKGROUND"
                #locHist.Scale(lumi)
            # locHist.Scale(lumi)
            locHist.Scale(467/locHist.Integral())
            # locHist.Scale(91/locHist.Integral()) ## -0.2,-0.4,-0.75,-0.75
            #locHist.Scale(195/locHist.Integral()) ## -0.9,-0.9,-0.75,-0.75
            # locHist.Scale(291/locHist.Integral())
            # if 'DataDriven' in locName:
            #      print "DATA DRIVEN BACKGROUND"
            #      locHist.Scale(159.94566/locHist.Integral())
            #      # locHist.Scale(322.878526241/locHist.Integral())
            #      # print "Scale factor ", 322.878526241/locHist.Integral()
            # else:
            #      print "MC BACKGROUND"
            #      locHist.Scale(lumi)
            # print "cut on background = ", thisWeightedCut
            print locHist.Integral()
            thisHist.Add(locHist)
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
    for background in OrderedBackgrounds:
        thisStack.addHist(background[0], background[1], background[2])  ##--add all background histograms to "myHistograms" in "thisStack"

    for isi, signal in enumerate(datasets["signal"]):
        thisName = plot[0]+"_Signal_"+"_"+signal['name']
        thisHist = modelHist.Clone(thisName)
        thisHist.SetLineColor(signal["color"])
        thisHist.SetLineColor(myCols[isi])
        thisHist.SetLineWidth(3)
        thisHist.SetLineStyle(signal["style"])
        thisTreeLoc = signal["file"]
        if thisTreeLoc not in Trees:
            # Trees[thisTreeLoc] = TChain("h4gCandidateDumper/trees/"+str(signal["treeName"]))
            Trees[thisTreeLoc] = TChain(str(signal["treeName"]))
            Trees[thisTreeLoc].AddFile(signalLocation+thisTreeLoc)
            SetOwnership( Trees[thisTreeLoc], True )
        locName = thisName+str(isi)
        locHist = thisHist.Clone(locName)
        # thisWeightedCut = weightedCut*TCut(Cut)
        # weightedCut += TCut(Cut_Signal)
        # thisWeightedCut = weightedCut * TCut( Cut_Signal)
        # thisWeightedCut = TCut(Cut_Signal)
        # print "cut on Signal = ", thisWeightedCut
        weightedCut = "weight* (" + str(Cut_Signal) +")"
        print "Signal weightedCut ", weightedCut
        Trees[thisTreeLoc].Draw(plot[1]+">>"+locName,weightedCut )

        # Trees[thisTreeLoc].Draw(plot[1]+">>"+locName,thisWeightedCut )
        # locHist.Scale(lumi)
        locHist.Scale(467/locHist.Integral())
        # print "Signal before scale: ", locHist.Integral()
        # locHist.Scale(lumi)
        print "Signal : ", locHist.Integral()
        thisHist.Add(locHist)
        Histos.append(locHist)
        thisStack.addSignal(thisHist, signal["legend"], lumi)   ##-- add all signals to "mySignals " in "thisStack"
        del thisHist

    dataName = plot[0]+"_hist"+"_data"
    modelHist.Clear()
    dataHist = 0
    dataHist = modelHist.Clone(dataName)
# # #    dataHist.Sumw2()
    if datasets['data'] not in Trees:
        Trees[datasets['data']] = TChain("Data_13TeV_4photons")
        Trees[datasets['data']].AddFile(dataLocation+datasets['data'])
        SetOwnership( Trees[datasets['data']], True )
    h = TH1F('h','h',100,30,120)
    # Cut_data = "1>0"
    Cut_data = "pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1  && tp_mass > 110 && tp_mass < 180 && !((tp_mass > 115 && tp_mass < 135)) && " + str(Cut_MVA)

    print "Cut_data: ", Cut_data
    # Cut_sculpt_data = "&& (pho4_pt+pho3_pt+pho2_pt+pho1_pt)/(tp_mass) > 0.75"
    # Trees[datasets['data']].Draw(plot[1]+">>"+dataName, Cut_data+Cut_sculpt_data)
    Trees[datasets['data']].Draw(plot[1]+">>"+dataName, TCut(Cut_data))
    #Trees[datasets['data']].Draw("pho1_pt >> h",TCut(Cut))
    # print "cut on data ", Cut
    dataintegral = h.Integral()
    print h.Integral()
    print "dataHist : ", dataHist
    # for b in range(0,dataHist.GetNbinsX()):
        # print "bin#", b , "  binContent :", dataHist.GetBinContent(b+1)
    dataHist.SetMarkerStyle(20)
    dataHist.SetMarkerSize(0.8)
    dataHist.SetMarkerColor(1)
    dataHist.SetLineColor(1)
    dataHist.SetLineWidth(2)

    # dataHist.Scale(lumi)
    dataHist.SetBinErrorOption(TH1.kPoisson)
    thisStack.addData(dataHist, "Data") ##--add data to "thisStack"
    thisFile = TFile(plot[0]+"_data.root", "RECREATE")
    thisFile.cd()
    dataHist.Write()
    thisFile.Close()
    dummyTFile.cd()

    thisStack.drawStack(prefix + plot[0])

    del thisStack

dummyTFile.Close()
os.system("rm dummy.root")
