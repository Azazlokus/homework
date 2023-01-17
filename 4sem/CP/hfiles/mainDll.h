#include <vector>
#include <string>
#include <windows.h>
using namespace std;
#pragma once

namespace global{
    extern int global_lRef;
}

namespace guid{
    const IID IID_IUnknown = {0x00000000, 0x0000, 0x0000, {0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x46}};
    const IID IID_IClassFactory = {0x00000001,0x0000,0x0000,{0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x46}};
}

    const CLSID CLSID_Slae = {0xA45E6C70, 0x1dAB, 0x4E6C, {0xBA, 0x7E, 0x51, 0xCA, 0x5F, 0x9D, 0xFB, 0xE2}};
    const CLSID CLSID_SlaeMod = {0x0EC953BB, 0x475B, 0x4C42, {0x9B, 0x1D, 0x9D, 0x49, 0x65, 0x6F, 0x9B, 0x32}};
    const IID IID_IPrint = {0x33124075, 0x7fa1, 0x495e, {0x80, 0xee, 0x5d, 0xc9, 0xe0, 0x92, 0x7b, 0x81}};
    const IID IID_IOperation = {0x693ea70b, 0x0142, 0x436b, {0x84, 0x0b, 0x67, 0x99, 0xf3, 0x3c, 0x1d, 0x0b}};
    const IID IID_IMatrProp = {0x0d76a1ea, 0xd0fd, 0x433c, {0x82, 0xf3, 0xd0, 0xab, 0x80, 0x4c, 0x3d, 0xed}};
    const IID IID_SlaeFactory = {0x8bd12ea6, 0x0d47, 0x4191, {0xa9, 0xf4, 0xaa, 0x74, 0x96, 0x6f, 0x19, 0xdb}};
    const IID IID_SlaeModFactory = {0x44f837e3, 0x94c8, 0x4eff, {0x8a, 0x59, 0x79, 0xf7, 0x9d, 0x7d, 0xad, 0x52}};

class IPrint: public IUnknown{
    public:
        virtual void __stdcall print() = 0;
};

class IOperation: public IUnknown{
    public:
        virtual void __stdcall input(string filename) = 0;
        virtual int __stdcall solve(string filename) = 0;
        virtual double __stdcall triangle(vector<vector<double>>&) = 0;
};

class IMatrProp: public IUnknown{
    public:
        virtual void __stdcall transpos() = 0;
        virtual void __stdcall det() = 0;
};

HRESULT CreateInstance(const CLSID& clsid, const IID& iid, void** ppv);
extern "C" __declspec(dllexport) HRESULT __stdcall  DllGetClassObject(const CLSID& clsid, const IID& iid, void** ppv);
extern "C" __declspec(dllexport) HRESULT __stdcall DllRegisterServer();
extern "C" __declspec(dllexport) HRESULT __stdcall DllUnregisterServer();
extern "C" __declspec(dllexport) HRESULT __stdcall DllCanUnloadNow();