// ***************************************
//
// run with: root -b -q computeYields.C++
//
// ***************************************

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

#include "TFile.h"
#include "TF1.h"
#include "TH1F.h"
#include "TSystem.h"
#include "TTree.h"

// *******************************************************
// function to read Ntuples and prepare yields histograms
// *******************************************************
void doHistos()
{

  TH1::SetDefaultSumw2(true);

  // --- lumi and input file path
  float lumi = 59.7; //fb-1
  TString inFilePath = "/eos/user/m/mrkim/2021_06_28_samples2l2q/MC_2018/";
  TString dataset = "ggH750";

  // --- define input file characteristics
  TFile*  inputFile;
  TTree*  inputTree;
  TH1F*   hCounters;
  Float_t gen_sumWeights;
  Float_t partialSampleWeight;

  // --- define input file branches
  Float_t overallEventWeight;
  Float_t xsec;
  vector<short> *ZZsel  = 0;  
  vector<float> *ZZMass = 0;  


  // --- define yield histogram: 1 bin only
  TH1F* hYields = new TH1F("hYields", "", 1, 0., 1.);
  hYields->Sumw2(true);


  // --- select and open input file
  TString inputFileName = inFilePath + dataset + "/ZZ2l2qAnalysis.root";
  cout<<"Opening input file "<<inputFileName<<" ..."<<endl;
  inputFile = TFile::Open(inputFileName);

  hCounters           = (TH1F*)inputFile->Get("ZZTree/Counters");
  gen_sumWeights      = (Long64_t)hCounters->GetBinContent(40);
  partialSampleWeight = lumi * 1000 / gen_sumWeights;
  inputTree           = (TTree*)inputFile->Get("ZZTree/candTree");

  // --- set branch addresses
  inputTree->SetBranchAddress("overallEventWeight", &overallEventWeight);
  inputTree->SetBranchAddress("xsec",               &xsec);  
  inputTree->SetBranchAddress("ZZsel",              &ZZsel);
  inputTree->SetBranchAddress("ZZMass",             &ZZMass);

 
  // --- loop over input tree
  Long64_t entries = inputTree->GetEntries(); 
  for(Long64_t z=0; z<entries; z++){

    inputTree->GetEntry(z);


    if(ZZMass->size() == 0) continue; // temporary solution to skip empty events
    if(ZZsel->at(0) < 0.) continue;


    // compute event weights
    Double_t eventWeight = partialSampleWeight *xsec *overallEventWeight;


    // --- fill histogram for yields
    hYields->Fill(0.5, eventWeight); 


  }// end loop over tree events


  // --- save yields in a root file
  TFile* fout_yields = new TFile("f_yields.root", "recreate"); 
  fout_yields->cd();
  hYields->Write();
  fout_yields->Close();


} // end of doHistos function



// ***********************************
// function to read yields histograms
// *********************************** 
void readYields()
{

  TString inFileName = "f_yields.root";
  TFile*  fInYields  = TFile::Open(inFileName);

  TH1F*   htemp;
  Float_t yields;
  Float_t yields_err;

  htemp      = (TH1F*)fInYields->Get("hYields");
  yields     = htemp->GetBinContent(1); // the yield is the content of the first (and only) bin of this histo
  yields_err = htemp->GetBinError(1);   // uncertainty over the yield is the error of the bin content

 
  // print yield on screen as an example (not very elegant)
  cout<<"Yields: "<<yields<<" +- "<<yields_err<<endl;


}


// **************
// main function
// **************
void computeYields()
{

  doHistos();
  readYields();

}



