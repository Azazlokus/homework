#include "mainDll.h"
#pragma once

class SlaeFactory:public IClassFactory {
    private:
        int m_lRef;
    public:
        SlaeFactory();
        virtual ~SlaeFactory();
        HRESULT __stdcall QueryInterface(const IID& iid, void** ppv);
        virtual ULONG __stdcall AddRef();
        virtual ULONG  __stdcall Release();
        virtual HRESULT __stdcall CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv);
        virtual HRESULT __stdcall LockServer(BOOL block);
};

class SlaeModFactory: public IClassFactory {
    private:
        int m_lRef;
    public:
        SlaeModFactory();
        virtual ~SlaeModFactory();
        HRESULT __stdcall QueryInterface(const IID& iid, void** ppv);
        virtual ULONG __stdcall AddRef();
        virtual ULONG __stdcall Release();
        virtual HRESULT __stdcall CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv);
        virtual HRESULT __stdcall LockServer(BOOL block);
};
