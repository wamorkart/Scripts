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

myCols = [cNiceMidnight, cNicePurple,  cNiceRed, cNiceGreen2, cNiceTangerine, cNicePaleYellow, cNiceOrange, cNiceRed, cNicePurple, cNiceGreen, cNiceGreen2]

if not os.path.exists(dirName):
        print dirName, "doesn't exist, creating it..."
        os.makedirs(dirName)
        if os.path.exists(dirName):
                print dirName, "now exists!"

datasets = json.load(data_file)

Trees = {}

# if doKinCut == True:
    # Cut += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0"
#     Cut_Signal += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0"
if doKinCut == True:
    Cut += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"
    Cut_Signal += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"
    Cut_Bkg += "&& pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"
# if doHggMVALoose == True:
#     Cut += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
#     Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
#
# if doHggMVATight == True:
#    Cut += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75"
#    Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75"
#
# if doEGMVA == True:
#    Cut += "&& pho1_EGMVA > 0.2 && pho2_EGMVA > 0.2 && pho3_EGMVA > 0.2 && pho4_EGMVA > 0.2 && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"
#    Cut_Signal += "&& pho1_EGMVA > 0.2 && pho2_EGMVA > 0.2 && pho3_EGMVA > 0.2 && pho4_EGMVA > 0.2 && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1"
#
if doHiggsWindow ==  True:
   Cut += "&& tp_mass > 110 && tp_mass < 180"
   Cut_Signal += "&& tp_mass > 110 && tp_mass < 180"
   Cut_Bkg += "&& tp_mass > 110 && tp_mass < 180"

if doBlind == True:
	Cut += " && !((tp_mass > 115 && tp_mass < 135))"

if (mvaWP == 'veryLoose'):
    Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.9 && pho2_MVA_mix > -0.9 && pho3_MVA_mix > -0.9 && pho4_MVA_mix > -0.9'
    Cut_Signal += "&&pho1_MVA > -999. && pho2_MVA > -999. && pho3_MVA > -999. && pho4_MVA > -999"
    # Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
    # Cut_Bkg += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9"
elif (mvaWP == 'Loose'):
    Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.9 && pho2_MVA_mix > -0.9 && pho3_MVA_mix > -0.75 && pho4_MVA_mix > -0.75'
    # Cut_Signal += "&& pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75"
elif (mvaWP == 'Medium'):
    Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.75 && pho4_MVA > -0.75'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.2 && pho2_MVA_mix > -0.4 && pho3_MVA_mix > -0.75 && pho4_MVA_mix > -0.75'
    # Cut_Signal += "&& pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.75 && pho4_MVA > -0.75"
else:
    Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.5 && pho4_MVA > -0.5'
    Cut_MVA_mix = 'pho1_MVA_mix > -0.2 && pho2_MVA_mix > -0.4 && pho3_MVA_mix > -0.5 && pho4_MVA_mix > -0.5'
    # Cut_Signal += "&& pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.5 && pho4_MVA > -0.5"


print "Cut_signal ", Cut_Signal
Cut_DataDriven = "pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass < 180 &&  !((tp_mass > 115 && tp_mass < 135))"
weightedcut = "weight"

weightedCut = TCut(weightedcut)

# lumi = lumi_2016+lumi_2017+lumi_2018
# lumi = lumi_2016
for plot in plots:
    Histos = []
    variable = plot[1]
    varName = plot[2]
    thisStack = 0
    thisHist = 0
    thisStack = myStack('test'+plot[0], varName, varName, dirName, lumi)
    dataintegral = 0
    if hideData == True:
        thisStack.hideData()

    # thisStack.setYear(year)

    modelHist = TH1F(plot[0]+"_hist", "", plot[3], plot[4], plot[5])

    backgroundHists = []
    background_sum = 0

    for isi, signal in enumerate(datasets["signal"]):
        thisName = plot[0]+"_Signal_"+"_"+signal['name']
        thisHist = modelHist.Clone(thisName)
        thisHist.SetLineColor(signal["color"])
        thisHist.SetLineColor(myCols[isi])
        thisHist.SetLineWidth(3)
        thisHist.SetLineStyle(signal["style"])
        weightedCut = "weight* (" + str(Cut_Signal) + ")"
        print "Signal weightedCut ", weightedCut
        if (year==2016):
           thisTreeLoc_2016 = signal["file_2016"]
           if thisTreeLoc_2016 not in Trees:
               Trees[thisTreeLoc_2016] = TChain(str(signal["treeName_2016"]))
               Trees[thisTreeLoc_2016].AddFile(SignalLocation+thisTreeLoc_2016)
               SetOwnership( Trees[thisTreeLoc_2016], True )
           locName_2016 = thisName+str(isi)+'_2016'
           locHist_2016 = thisHist.Clone(locName_2016)
           Trees[thisTreeLoc_2016].Draw(plot[1]+">>"+locName_2016,weightedCut )
           locHist_2016.Scale(lumi)
           thisHist.Add(locHist_2016)
           Histos.append(locHist_2016)
        elif (year==2017):
             thisTreeLoc_2017 = signal["file_2017"]
             if thisTreeLoc_2017 not in Trees:
                 Trees[thisTreeLoc_2017] = TChain(str(signal["treeName_2017"]))
                 Trees[thisTreeLoc_2017].AddFile(SignalLocation+thisTreeLoc_2017)
                 SetOwnership( Trees[thisTreeLoc_2017], True )
             locName_2017 = thisName+str(isi)+'_2017'
             locHist_2017 = thisHist.Clone(locName_2017)
             Trees[thisTreeLoc_2017].Draw(plot[1]+">>"+locName_2017,weightedCut )
             locHist_2017.Scale(lumi)
             thisHist.Add(locHist_2017)
             Histos.append(locHist_2017)
        elif (year==2018):
             thisTreeLoc_2018 = signal["file_2018"]
             if thisTreeLoc_2018 not in Trees:
                 Trees[thisTreeLoc_2018] = TChain(str(signal["treeName_2018"]))
                 Trees[thisTreeLoc_2018].AddFile(SignalLocation+thisTreeLoc_2018)
                 SetOwnership( Trees[thisTreeLoc_2018], True )
             locName_2018 = thisName+str(isi)+'_2018'
             locHist_2018 = thisHist.Clone(locName_2018)
             Trees[thisTreeLoc_2018].Draw(plot[1]+">>"+locName_2018,weightedCut )
             locHist_2018.Scale(lumi)
             thisHist.Add(locHist_2018)
             Histos.append(locHist_2018)
        elif (year==1):
             thisTreeLoc_2016 = signal["file_2016"]
             thisTreeLoc_2017 = signal["file_2017"]
             thisTreeLoc_2018 = signal["file_2018"]
             if thisTreeLoc_2016 not in Trees:
                 Trees[thisTreeLoc_2016] = TChain(str(signal["treeName_2016"]))
                 Trees[thisTreeLoc_2016].AddFile(SignalLocation+thisTreeLoc_2016)
                 SetOwnership( Trees[thisTreeLoc_2016], True )

             if thisTreeLoc_2017 not in Trees:
                 Trees[thisTreeLoc_2017] = TChain(str(signal["treeName_2017"]))
                 Trees[thisTreeLoc_2017].AddFile(SignalLocation+thisTreeLoc_2017)
                 SetOwnership( Trees[thisTreeLoc_2017], True )


             if thisTreeLoc_2018 not in Trees:
                 Trees[thisTreeLoc_2018] = TChain(str(signal["treeName_2018"]))
                 Trees[thisTreeLoc_2018].AddFile(SignalLocation+thisTreeLoc_2018)
                 SetOwnership( Trees[thisTreeLoc_2018], True )

             locName_2016 = thisName+str(isi)+'_2016'
             locHist_2016 = thisHist.Clone(locName_2016)

             locName_2017 = thisName+str(isi)+'_2017'
             locHist_2017 = thisHist.Clone(locName_2017)

             locName_2018 = thisName+str(isi)+'_2018'
             locHist_2018 = thisHist.Clone(locName_2018)

             Trees[thisTreeLoc_2016].Draw(plot[1]+">>"+locName_2016,weightedCut )
             Trees[thisTreeLoc_2017].Draw(plot[1]+">>"+locName_2017,weightedCut )
             Trees[thisTreeLoc_2018].Draw(plot[1]+">>"+locName_2018,weightedCut )
             locHist_2016.Add(locHist_2017)
             locHist_2016.Add(locHist_2018)
             locHist_2016.Scale(lumi)

             thisHist.Add(locHist_2016)
             Histos.append(locHist_2016)
        # locHist.Scale(195/locHist.Integral())

        # locHist_2016.Scale(lumi)
        # locHist_2017.Scale(lumi)
        # print "Signal 2016: ", locHist_2016.Integral(), "Signal 2017: ", locHist_2017.Integral(), "Signal 2018: ", locHist_2018.Integral()

        # locHist_2016.Add(locHist_2017)
        # locHist_2016.Add(locHist_2018)
        # locHist_2018.Scale(lumi)
        # print "All Signal : ", locHist_2018.Integral()
        # thisHist.Add(locHist_2016)
        # Histos.append(locHist_2016)
        thisStack.addSignal(thisHist, signal["legend"], lumi)   ##-- add all signals to "mySignals " in "thisStack"
        del thisHist

    dataName = plot[0]+"_hist"+"_data"
    modelHist.Clear()
    dataHist = 0
    dataHist = modelHist.Clone(dataName)
# # #    dataHist.Sumw2()
    data_integral = 1
    if datasets['data'] not in Trees:
        # Trees[datasets['data']] = TChain("tagsDumper/trees/Data_13TeV_H4GTag_0")
        Trees[datasets['data']] = TChain("Data_13TeV_H4GTag_0")
        Trees[datasets['data']].AddFile(DataLocation+datasets['data'])
        # Trees[datasets['data']].AddFile(DataLocation+datasets['data'])
        # Trees[datasets['data']].AddFile(DataLocation+datasets['data'])
        SetOwnership( Trees[datasets['data']], True )
    h = TH1F('h','h',100,30,120)

    Cut_data = Cut
    # Cut_data = Cut
    print "Cut_data: ", Cut_data

    Trees[datasets['data']].Draw(plot[1]+">>"+dataName, TCut(Cut_data))

    data_integral = dataHist.Integral()


    dataHist.SetMarkerStyle(20)
    dataHist.SetMarkerSize(0.8)
    dataHist.SetMarkerColor(1)
    dataHist.SetLineColor(1)
    dataHist.SetLineWidth(2)

    # dataHist.Scale(lumi)
    dataHist.SetBinErrorOption(TH1.kPoisson)
    thisStack.addData(dataHist, "Data") ##--add data to "thisStack"
    # thisFile = TFile(plot[0]+"_data.root", "RECREATE")
    # thisFile.cd()
    # dataHist.Write()
    # thisFile.Close()
    dummyTFile.cd()

    for background in datasets["background"]:
        thisName = plot[0]+"_hist"+"_"+background
        thisHist = modelHist.Clone(thisName)
        thisHist.SetLineColor(TColor.GetColor(datasets["background"][background]["color"]))
        thisHist.SetFillColor(TColor.GetColor(datasets["background"][background]["color"]))
        for i,fi in enumerate(datasets["background"][background]["files"]):
            thisTreeLoc = fi["file"]
            if thisTreeLoc not in Trees:
                Trees[thisTreeLoc] = TChain(str(fi["treeName"]))
                Trees[thisTreeLoc].AddFile(BkgLocation+thisTreeLoc)
                # Trees[thisTreeLoc_2016].AddFile(BkgLocation_2016+thisTreeLoc)
                # Trees[thisTreeLoc_2016].AddFile(BkgLocation_2017+thisTreeLoc)
                # Trees[thisTreeLoc_2018].AddFile(BkgLocation_2018+thisTreeLoc)

                SetOwnership( Trees[thisTreeLoc], True )

            locName = thisName+str(i)
            print "name ", locName
            locHist = thisHist.Clone(locName)
            thisWeightedCut = ""
            if (bkgtype == 'mix'):
               if (doreweight):
                   thisWeightedCut = "(weight)*(" +Cut_Bkg + "&& "+fi["cut"]  +" && !(tp_mass > 115 && tp_mass < 135))"
               else:
                   thisWeightedCut = "(1)*(" +Cut_Bkg + "&& "+fi["cut"]  +" && (tp_mass > 115 && tp_mass < 135))"
            elif (bkgtype == 'vbf'):
                if 'DataDriven' in locName:
                    print 'Data driven background'
                    thisWeightedCut = "(weight_VBF)*( !(tp_mass > 115 && tp_mass < 135))"
                else:
                    thisWeightedCut =  "(weight_VBF*weight)*(" +Cut + "&& "+fi["cut"] + "&&" + Cut_MVA  + ")"
            elif (bkgtype == 'MC'):
                thisWeightedCut = "(weight) * (" + Cut + "&&" + fi["cut"] + ")"

            print "Background Cut: ", thisWeightedCut
            Trees[thisTreeLoc].Draw(plot[1]+">>"+locName, thisWeightedCut)

            # print data_integral
            locHist.Scale(data_integral/locHist.Integral())


            print locHist.Integral()
            thisHist.Add(locHist)
            Histos.append(locHist)
            background_sum += thisHist.Integral()
            # thisFile = TFile(plot[0]+"_"+fi["file"], "RECREATE")
            # thisFile.cd()
            # thisHist.Write()
            # thisFile.Close()
            # dummyTFile.cd()
        backgroundHists.append([thisHist, datasets["background"][background]["legend"], datasets["background"][background]["position"]])
        del thisHist
    OrderedBackgrounds = sorted(backgroundHists, key=lambda x: x[2], reverse=True)
    for background in OrderedBackgrounds:
        thisStack.addHist(background[0], background[1], background[2])  ##--add all background histograms to "myHistograms" in "thisStack"

    thisStack.drawStack(prefix + plot[0])

    del thisStack

dummyTFile.Close()
os.system("rm dummy.root")
                                                                                                                                                                                                                                                                 
       
