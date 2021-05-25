// **************************
//
// run with: 
//       root -l -b -q esempio_grafico.C++
//
// **************************

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <iomanip>

#include "TString.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TMath.h"
#include "TStyle.h"
#include "TSystem.h"
#include "TTree.h"
#include "TAxis.h"
#include "TF1.h"
#include "TGraph.h"
#include "TLine.h"
#include "TPaveText.h"
#include "TRandom3.h"
#include "TPaveText.h"
#include "TGraphErrors.h"


void esempio_grafico(){


  const int n_ = 7;
  float x_[n_]    = {-20., -10., -5., 0., 5., 10., 20.}; 
  float x_err[n_] = {0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001};
  float y_[n_]    = {0.0001024, 0.0001025, 0.0001021, 0.0001011, 0.000101,  0.0001025, 0.0001035}; 
  float y_err[n_] = {8.847e-07, 1.187e-06, 1.107e-06, 6.381e-07, 4.814e-07, 8.436e-07, 4.224e-07}; 
  TString xAxisLabel = "x_ax_label";
  TString label      = "graph_with_fit";
  float x_min = -20.;
  float x_max = 20.;



  // plot and fit 
  TCanvas* c = new TCanvas("c","c", 800, 600);
  c->cd();
  TGraphErrors* g = new TGraphErrors(n_, x_, y_, x_err, y_err); 
  g->SetMarkerStyle(20);
  g->SetTitle("");
  g->GetXaxis()->SetTitle(xAxisLabel);
  g->GetYaxis()->SetTitle("xsec [pb]");
  TF1 *f1 = new TF1("f1","pol2",x_min,x_max);
  g->Fit("f1","R");
  gStyle->SetOptFit(1111);
  g->Draw("APE");
  c->SaveAs(label + "_" + xAxisLabel + ".png");


}
