#include "Slae.h"
#pragma once

class SlaeMod: public IOperation, IMatrProp{
    private:
        int m_lRef;
        Slae* Slae_base;
        vector <vector <double>> A;
        vector <double> X; 
    public:
        SlaeMod();
        ~SlaeMod();
        HRESULT virtual QueryInterface(const IID&, void**);
        ULONG AddRef();
        ULONG Release();

        virtual void input(string filename);
        virtual int solve(string filename);
        virtual double triangle(vector<vector<double>>&);
        virtual void transpos();
        virtual void det();
};