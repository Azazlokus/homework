#include "mainDll.h"
#pragma once

class Slae: public IPrint, IOperation{
    private:
        int m_lRef;
        vector <vector <double>> A;
        vector <double> X; 
    public:
        Slae();
        ~Slae();
         virtual HRESULT QueryInterface(const IID&, void**);
        ULONG AddRef();
        ULONG Release();
        void copy_matr(vector<vector <double>>&, int, int);
        vector<vector<double>> getA();

        virtual void print();
        virtual int solve(string filename);
        virtual void input(string filename);
        virtual double triangle(vector<vector<double>>&);
};