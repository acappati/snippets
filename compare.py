#!/usr/bin/env python

import ROOT 
from ROOT import TFile, TH1, TH1F, TCanvas, TLegend, gSystem, gStyle
from ROOT import kBlue, kRed, kBlack, kWhite




lumi = 59.7 #fb-1


# file 1
inputFile_1 = TFile.Open('/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200205_CutBased/MC_2018/ggH125/ZZ4lAnalysis.root') #ggH125 2018 HIG-19-001

h_m4l_1          = TH1F('h_m4l_1',         ';m_{4l} (GeV); events/2 GeV', 45, 70., 160.)
h_m4l_noWeight_1 = TH1F('h_m4l_noWeight_1',';m_{4l} (GeV); a.u./2 GeV',   45, 70., 160.)
h_mZ1_1          = TH1F('h_mZ1_1',         ';m_{Z1} (GeV); events/2 GeV', 30, 60., 120.)
h_mZ1_noWeight_1 = TH1F('h_mZ1_noWeight_1',';m_{Z1} (GeV); a.u./2 GeV',   30, 60., 120.)
h_mZ2_1          = TH1F('h_mZ2_1',         ';m_{Z2} (GeV); events/2 GeV', 25, 10., 60. )
h_mZ2_noWeight_1 = TH1F('h_mZ2_noWeight_1',';m_{Z2} (GeV); a.u./2 GeV',   25, 10., 60. )

hcounters_1           = inputFile_1.Get('ZZTree/Counters')
gen_sumWeights_1      = hcounters_1.GetBinContent(40)
partialSampleWeight_1 = lumi * 1000 / gen_sumWeights_1
inputTree_1           = inputFile_1.Get('ZZTree/candTree');

yield_1 = 0.

print "reading tree", inputFile_1.GetName(),inputTree_1.GetName()  ,"..."
for event_1 in inputTree_1 :

    weight_1 = partialSampleWeight_1*event_1.xsec*event_1.overallEventWeight*event_1.ggH_NNLOPS_weight

    h_m4l_1         .Fill(event_1.ZZMass, weight_1)
    h_m4l_noWeight_1.Fill(event_1.ZZMass)
    h_mZ1_1         .Fill(event_1.Z1Mass, weight_1)
    h_mZ1_noWeight_1.Fill(event_1.Z1Mass)
    h_mZ2_1         .Fill(event_1.Z2Mass, weight_1)
    h_mZ2_noWeight_1.Fill(event_1.Z2Mass)

    yield_1 += weight_1

# print "saving histograms into root file ..."
# outFile_1 = TFile.Open("out_1.root", "RECREATE")
# outFile_1.cd()
# h_m4l_1         .Write()
# h_m4l_noWeight_1.Write()
# h_mZ1_1         .Write()
# h_mZ1_noWeight_1.Write()
# h_mZ2_1         .Write()
# h_mZ2_noWeight_1.Write()
# outFile_1.Close()



# file 2
inputFile_2 = TFile.Open('prod/PROD_samples_2018_MC_UL_4b644dc6/AAAOK/ggH125/ZZ4lAnalysis.root') #ggH125 UL

h_m4l_2          = TH1F('h_m4l_2',         ';m_{4l} (GeV); events/2 GeV', 45, 70., 160.)
h_m4l_noWeight_2 = TH1F('h_m4l_noWeight_2',';m_{4l} (GeV); a.u./2 GeV',   45, 70., 160.)
h_mZ1_2          = TH1F('h_mZ1_2',         ';m_{Z1} (GeV); events/2 GeV', 30, 60., 120.)
h_mZ1_noWeight_2 = TH1F('h_mZ1_noWeight_2',';m_{Z1} (GeV); a.u./2 GeV',   30, 60., 120.)
h_mZ2_2          = TH1F('h_mZ2_2',         ';m_{Z2} (GeV); events/2 GeV', 25, 10., 60. )
h_mZ2_noWeight_2 = TH1F('h_mZ2_noWeight_2',';m_{Z2} (GeV); a.u./2 GeV',   25, 10., 60. )

hcounters_2           = inputFile_2.Get('ZZTree/Counters')
gen_sumWeights_2      = hcounters_2.GetBinContent(40)
partialSampleWeight_2 = lumi * 1000 / gen_sumWeights_2
inputTree_2           = inputFile_2.Get('ZZTree/candTree');

yield_2 = 0.

print "reading tree", inputFile_2.GetName(),inputTree_2.GetName()  ,"..."
for event_2 in inputTree_2 :

    weight_2 = partialSampleWeight_2*event_2.xsec*event_2.overallEventWeight*event_2.ggH_NNLOPS_weight

    h_m4l_2         .Fill(event_2.ZZMass, weight_2)
    h_m4l_noWeight_2.Fill(event_2.ZZMass)
    h_mZ1_2         .Fill(event_2.Z1Mass, weight_2)
    h_mZ1_noWeight_2.Fill(event_2.Z1Mass)
    h_mZ2_2         .Fill(event_2.Z2Mass, weight_2)
    h_mZ2_noWeight_2.Fill(event_2.Z2Mass)

    yield_2 += weight_2; 

# print "saving histograms into root file ..."
# outFile_2 = TFile.Open("out_2.root", "RECREATE")
# outFile_2.cd()
# h_m4l_2         .Write()
# h_m4l_noWeight_2.Write()
# h_mZ1_2         .Write()
# h_mZ1_noWeight_2.Write()
# h_mZ2_2         .Write()
# h_mZ2_noWeight_2.Write()
# outFile_2.Close()

    
print 'yield HIG-19-001: ',yield_1, '  yield UL: ', yield_2


gStyle.SetOptStat(0)

#plot

#---
c_m4l = TCanvas('c_m4l','m4l',800,600)
c_m4l.cd()
h_m4l_1.SetLineColor(kBlack)
h_m4l_2.SetLineColor(kRed)
h_m4l_1.Draw('hist')
h_m4l_2.Draw('hist same')

# l_m4l = TLegend(0.74,0.68,0.94,0.87)
# l_m4l.AddEntry(h_m4l_1,"HIG-19-001", "l")
# l_m4l.AddEntry(h_m4l_2,"UL","l")
# l_m4l.SetFillColor(kWhite)
# l_m4l.SetLineColor(kBlack)
# l_m4l.SetTextFont(43)
# l_m4l.SetTextSize(20)
# l.Draw()

c_m4l.SaveAs('c_m4l.png')


#---
c_m4l_noWeight = TCanvas('c_m4l_noWeight','m4l_noWeight',800,600)
c_m4l_noWeight.cd()
h_m4l_noWeight_1.SetLineColor(kBlack)
h_m4l_noWeight_2.SetLineColor(kRed)
h_m4l_noWeight_1.Scale(1./h_m4l_noWeight_1.Integral())
h_m4l_noWeight_2.Scale(1./h_m4l_noWeight_2.Integral())
h_m4l_noWeight_1.Draw('hist')
h_m4l_noWeight_2.Draw('hist same')

c_m4l_noWeight.SaveAs('c_m4l_noWeight.png')


#---
c_mZ1 = TCanvas('c_mZ1','mZ1',800,600)
c_mZ1.cd()
h_mZ1_1.SetLineColor(kBlack)
h_mZ1_2.SetLineColor(kRed)
h_mZ1_1.Draw('hist')
h_mZ1_2.Draw('hist same')

c_mZ1.SaveAs('c_mZ1.png')


#---
c_mZ1_noWeight = TCanvas('c_mZ1_noWeight','mZ1_noWeight',800,600)
c_mZ1_noWeight.cd()
h_mZ1_noWeight_1.SetLineColor(kBlack)
h_mZ1_noWeight_2.SetLineColor(kRed)
h_mZ1_noWeight_1.Scale(1./h_mZ1_noWeight_1.Integral())
h_mZ1_noWeight_2.Scale(1./h_mZ1_noWeight_2.Integral())
h_mZ1_noWeight_1.Draw('hist')
h_mZ1_noWeight_2.Draw('hist same')

c_mZ1_noWeight.SaveAs('c_mZ1_noWeight.png')


#---
c_mZ2 = TCanvas('c_mZ2','mZ2',800,600)
c_mZ2.cd()
h_mZ2_1.SetLineColor(kBlack)
h_mZ2_2.SetLineColor(kRed)
h_mZ2_1.Draw('hist')
h_mZ2_2.Draw('hist same')

c_mZ2.SaveAs('c_mZ2.png')


#---
c_mZ2_noWeight = TCanvas('c_mZ2_noWeight','mZ2_noWeight',800,600)
c_mZ2_noWeight.cd()
h_mZ2_noWeight_1.SetLineColor(kBlack)
h_mZ2_noWeight_2.SetLineColor(kRed)
h_mZ2_noWeight_1.Scale(1./h_mZ2_noWeight_1.Integral())
h_mZ2_noWeight_2.Scale(1./h_mZ2_noWeight_2.Integral())
h_mZ2_noWeight_1.Draw('hist')
h_mZ2_noWeight_2.Draw('hist same')

c_mZ2_noWeight.SaveAs('c_mZ2_noWeight.png')



















