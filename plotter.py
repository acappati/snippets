#!/usr/bin/env python

import ROOT

inFile         = ROOT.TFile.Open('/eos/user/m/mrkim/2021_06_28_samples2l2q/MC_2018/ggH750/ZZ2l2qAnalysis.root')
inHisto        = inFile.Get('ZZTree/Counters')
gen_sumWeights = inHisto.GetBinContent(40)     # sum of all PUWeight*genHEPMCweight, for normalization
inTree         = inFile.Get('ZZTree/candTree')

lumi = 59.7 #fb-1
partialSampleWeight = (lumi * 1000.) / gen_sumWeights # compute weights normalization (*1000 necessary because xsec value is in pb)

h_ZZMass   = ROOT.TH1F('ZZMass',  ';ZZMass (GeV); Events', 30, 70.,1500.) # non-weighted histo
h_ZZMass_w = ROOT.TH1F('ZZMass_w',';ZZMass (GeV); Events', 30, 70.,1500.) # weighted histo


print 'tree entries: ', inTree.GetEntries()
for event in inTree:
   
    if event.ZZMass.size() == 0 : # temporary solution to skip empty events
        continue

    weight = partialSampleWeight * event.xsec * event.overallEventWeight # per-event weight; overallEventWeight = PUWeight * genHEPMCweight * dataMCWeight * trigEffWeight 
        
    h_ZZMass.Fill(event.ZZMass[0])          # temporary solution for double counting: take only first component of ZZMass vector 
    h_ZZMass_w.Fill(event.ZZMass[0],weight) 



c1 = ROOT.TCanvas('c1','c1',800,600)
c1.cd()
h_ZZMass.Draw('histo') 
c1.SaveAs('ZZMass.png')

c2 = ROOT.TCanvas('c2','c2',800,600)
c2.cd()
h_ZZMass_w.Draw('histo') 
c2.SaveAs('ZZMass_w.png')
