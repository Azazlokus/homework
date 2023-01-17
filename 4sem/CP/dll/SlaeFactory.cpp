#include "../hfiles/Slae.h"
#include "../hfiles/ClassFactory.h"
#include <iostream>
#define NULL __null

namespace global{
    int global_lRef = 0;
}

SlaeFactory::SlaeFactory(){
    m_lRef = 0;
}

SlaeFactory::~SlaeFactory(){}

HRESULT SlaeFactory::QueryInterface(const IID& iid, void** ppv){
    if (iid == guid::IID_IUnknown || iid == guid::IID_IClassFactory){
        *ppv = (IClassFactory*)this;
    } else if (iid == IID_SlaeFactory){
        *ppv = (SlaeFactory*)this;
    } else {
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}

HRESULT SlaeFactory::CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv){
    HRESULT hr;
    Slae *pSlae;
    *ppv = NULL;
    pSlae = new Slae();
    if (pSlae == 0){
        return E_OUTOFMEMORY;
    }
    hr = pSlae->QueryInterface(iid, ppv);  
    if (FAILED(hr)){ 
        delete pSlae;
    } 
    return hr;
}

ULONG SlaeFactory::AddRef(){
    m_lRef++;
    global::global_lRef++;
    return m_lRef;
}

ULONG SlaeFactory::Release(){
    m_lRef--;
    global::global_lRef--;
    if (m_lRef == 0){
        delete this;
        return 0;
    }
    return m_lRef;
}

HRESULT SlaeFactory::LockServer(BOOL block){return S_OK;}