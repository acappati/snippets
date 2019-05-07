#!/usr/bin/env python

# --------------------------
# check if there are events with same lumiNumber and eventNumber
# using python dictionary
# -------------------------


from ROOT import TFile, TH1, TH1F, TCanvas, gSystem, TTree
import numpy as np


inputTree = TFile.Open("/data3/Higgs/190316/ggH125/ZZ4lAnalysis.root")
tree      = inputTree.Get("ZZTree/candTree") 
treeText  = "ZZTree"


# declare dictionary
map = dict()


# read TTree 
print "reading tree", inputTree.GetName(),treeText,tree.GetName()  ,"..."
for event in tree:
    if ( event.ZZsel < 0 ) : continue # skip events that do not pass the trigger 


    if not event.LumiNumber in map :
        map[event.LumiNumber] = []
        print event.LumiNumber, event.EventNumber
    if(event.EventNumber in map[event.LumiNumber]) :
        print "AAAAAAAAAA", event.ZZMass
    else :
        map[event.LumiNumber].append(event.EventNumber)
