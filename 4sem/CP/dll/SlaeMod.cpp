#include "../hfiles/SlaeMod.h"
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

SlaeMod::SlaeMod(){
    m_lRef = 0;
    CreateInstance(CLSID_Slae, guid::IID_IUnknown, (void**)&this->Slae_base);
}

SlaeMod::~SlaeMod(){}

HRESULT SlaeMod::QueryInterface(const IID& iid, void** ppv){
    if (iid == guid::IID_IUnknown){
        *ppv = (IUnknown*)((IMatrProp*)this);
    } else if (iid == IID_IOperation){
        *ppv = (IOperation*)this;
    } else if (iid == IID_IMatrProp){
        *ppv = (IMatrProp*)this;
    } else {
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}

ULONG SlaeMod::AddRef(){
    m_lRef++;
    Slae_base->AddRef();
    global::global_lRef++;
    return m_lRef;
}

ULONG SlaeMod::Release(){
    m_lRef--;
    Slae_base->Release();
    global::global_lRef--;
    if (m_lRef == 0){
        delete this;
        return 0;
    }
    return m_lRef;
}

void SlaeMod::input(string filename){
    Slae_base->input(filename);
    this->A = Slae_base->getA();
}

int SlaeMod::solve(string filename){
    return Slae_base->solve(filename);
}

double SlaeMod::triangle(vector<vector<double>>&temp){
    double res = Slae_base->triangle(temp);
    this->A = Slae_base->getA();
    return res;
}

void SlaeMod::transpos(){
    fstream file;
    double temp;
    vector<vector<double>> tempA;
    Slae_base->copy_matr(tempA, this->A.size(), this->A[0].size() - 1);
    int size = tempA.size();
    for (int i = 0; i < size; i++){
        for (int j = i + 1; j < size; j++){
            temp = tempA[i][j];
            tempA[i][j] = tempA[j][i];
            tempA[j][i] = temp;
        }
    }
    file.open("input.txt", ios::app);
    file << "\nTransposed matrix\n";
    for (int i = 0; i<tempA.size(); i++){
        for (int j = 0; j < tempA.size(); j++){
            file << tempA[i][j] << " ";
        }
        if (i != tempA.size() - 1) file << "\n";
    }
    file.close();
}

void SlaeMod::det(){
    double determ = 1, max = 0;
    int i_index;
    std::vector<std::vector<double>> tempA;
    Slae_base->copy_matr(tempA, A.size(), A[0].size() - 1);
    int size = tempA.size();
    if (tempA.size() == 0) determ = 0;
    if (tempA.size() == 1) determ = tempA[0][0];
    if (tempA.size() == 2) determ =  tempA[0][0] * tempA[1][1] - tempA[0][1] * tempA[1][0];

    for(int i=0; i<size; i++){
        max = fabs(tempA[i][i]);
        for(int j=i; j<size; j++){
            if (fabs(tempA[j][i])>max){
                max = tempA[j][i];
                i_index = j;
            }
        }

        if (max != fabs(tempA[i][i])){
            for(int j = 0; j<size; j++){
                double temp = tempA[i][j];
                tempA[i][j] = tempA[i_index][j];
                tempA[i_index][j] = temp; 
            }
            determ *= -1;
        }


        double temp = tempA[i][i];
        for(int j = size - 1; j>=i; j--){
            tempA[i][j] /= temp;
        }
        determ *= temp;

        for(int j = i+1; j<size; j++){
            temp = tempA[j][i];
            for(int k = size - 1; k>=i; k--){
                tempA[j][k] -= temp*tempA[i][k]; 
            }
        }
    }
    
    for (int i = 0; i < size; i++){
        determ *= tempA[i][i];
    }

    fstream file;
    file.open("input.txt", ios::app);
    file << "\nDeterminant\n" << determ;
    file.close();
}

