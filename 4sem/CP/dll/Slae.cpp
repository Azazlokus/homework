#include "../hfiles/Slae.h"
#include <cmath>
#include <iostream>
#include <fstream>

Slae::Slae(){
    m_lRef = 0;
}

Slae::~Slae(){}

HRESULT Slae::QueryInterface(const IID& iid, void** ppv){
    if (iid == guid::IID_IUnknown){
        *ppv = (IUnknown*)((IPrint*)this);
    } else if (iid == IID_IPrint){
        *ppv = (IPrint*)this;
    } else if (iid == IID_IOperation){
        *ppv = (IOperation*)this;
    } else {
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}

ULONG Slae::AddRef(){
    m_lRef++;
    global::global_lRef++;
    return m_lRef;
}

ULONG Slae::Release(){
    m_lRef--;
    global::global_lRef--;
    if (m_lRef == 0){
        delete this;
        return 0;
    }
    return m_lRef;
}

vector<vector<double>> Slae::getA(){
    return this->A;
}

void Slae::copy_matr(vector<vector<double>>&temp, int n, int m){
    if (n > this->A.size() || m > this->A[0].size()) return;
    temp.resize(n);
    for(int i = 0; i<n; i++){
        temp[i].resize(m);
    }

    for(int i = 0; i<n; i++){
        for(int j = 0; j<m; j++){
            temp[i][j] = A[i][j];
        }
    }
}

void Slae::print(){
    cout << "Extended matrix\n";
    for(int i = 0; i<this->A.size(); i++){
        for(int j = 0; j<this->A[i].size() - 1; j++){
            cout << this->A[i][j] << " ";
        }
        cout << "| " << this->A[i][this->A[i].size() - 1];
        cout << std::endl;
    }
    for(int i = 0; i<this->A.size(); i++){
        cout << X[i] << " ";
    }
}

void Slae::input(string filename){
    int n, m;
    double num;
    ifstream file(filename);
    
    if (file){
        file >> n;
        m = n + 1;
        this->A.resize(n);
        this->X.resize(n);
        for (int i = 0; i < n; i++){
            this->A[i].resize(m);
            for (int j = 0; j < m; j++){
                file >> this->A[i][j];
            }
        }
    }
    file.close();
}

double Slae::triangle(vector<vector<double>>&tempA){
    double max = 0;
    int i_index, columnsize = tempA.size() , linesize = tempA[0].size() - 1;
    for(int i=0; i<columnsize; i++){
        max = fabs(tempA[i][i]);
        for(int j=i; j<columnsize; j++){
            if (fabs(tempA[j][i])>max){
                max = tempA[j][i];
                i_index = j;
            }
        }

        if (max != fabs(tempA[i][i])){
            for(int j = 0; j<columnsize; j++){
                double temp = tempA[i][j];
                tempA[i][j] = tempA[i_index][j];
                tempA[i_index][j] = temp; 
            }
            double temp = tempA[i][linesize];
            tempA[i][linesize] = tempA[i_index][linesize];
            tempA[i_index][linesize] = temp;
        }


        double temp = tempA[i][i];
        for(int j = linesize; j>=i; j--){
            tempA[i][j] /= temp;
        }

        for(int j = i+1; j<columnsize; j++){
            temp = tempA[j][i];
            for(int k = linesize; k>=i; k--){
                tempA[j][k] -= temp*tempA[i][k]; 
            }
        }
    }
    return max;
}

int Slae::solve(string filename){
    const double eps = 1e-6;
    std::vector<std::vector<double>> tempA;
    fstream file;
    int columnsize = this->A.size(), linesize = this->A[0].size() - 1;
    
    copy_matr(tempA, columnsize, linesize + 1);
    if(triangle(tempA) == 0){
        return 1;
    }

    this->X[columnsize - 1] = tempA[columnsize - 1][linesize];
    for(int i = columnsize - 2; i>=0; i--){
        for(int j = i + 1; j<columnsize; j++){
            tempA[i][linesize] -= tempA[i][j]*X[j];
        }
        this->X[i] = tempA[i][linesize];
        if (fabs(this->X[i]) < eps) X[i] = 0;
    }

    file.open("input.txt", ios::app);
    file << "\nX = [ ";
    for (int i = 0; i<this->X.size(); i++){
        file << this->X[i] << " ";
    }
    file << "]";
    file.close();
    return 0;
}