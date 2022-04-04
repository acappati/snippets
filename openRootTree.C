// ***************************************
//
// run with: root -l -b -q openRootTree.C++
//
// ***************************************

#include <iostream>
#include <fstream>

#include "TFile.h"
#include "TTree.h"



void openRootTree(){

  // --- define input file characteristics
  TString rootInFile   = "/afs/cern.ch/user/f/fmonti/public/4alessandra/pedestal_scan/pedestal_scan0.root";
  TString rootDirName  = "runsummary";
  TString rootTreeName = "summary";

  TFile* inputFile;
  TTree* inputTree;

  // --- define input file branches
  UInt_t   chip;
  UShort_t channel;
  UShort_t channeltype;
  Float_t  adc_mean;

  // --- open input file
  cout<<"Opening input file "<<rootInFile<<" ..."<<endl;
  inputFile = TFile::Open(rootInFile);
  inputTree = (TTree*)inputFile->Get(rootDirName +"/"+ rootTreeName);

  // --- set branch addresses
  inputTree->SetBranchAddress("chip",        &chip);
  inputTree->SetBranchAddress("channel",     &channel);
  inputTree->SetBranchAddress("channeltype", &channeltype);
  inputTree->SetBranchAddress("adc_mean",    &adc_mean);
 
  // --- loop over input tree entries
  Long64_t entries = inputTree->GetEntries(); 
  for(Long64_t z=0; z<entries; z++){

    inputTree->GetEntry(z);


    cout<<"Chip: "<<chip<<" Channel: "<<channel<<" ChannelType: "<<channeltype<<" adc mean:  "<<adc_mean<<endl;


  }// end loop over tree events




}



