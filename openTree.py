#!/usr/bin/env python

import ROOT


inFile = ROOT.TFile.Open('ZZ2l2qAnalysis.root')
inTree = inFile.Get('ZZTree/candTree')


print 'tree entries: ', inTree.GetEntries()

idx = 0
for event in inTree:

    print 'event n. ', idx
   
    for j in range(0,event.LepPt.size()):

        print event.LepPt[j]
    
    idx += 1
