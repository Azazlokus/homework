#include "../hfiles/SlaeMod.h"
#include "../hfiles/ClassFactory.h"
#include <iostream>
#define NULL __null

SlaeModFactory::SlaeModFactory(){
    m_lRef = 0;
}

SlaeModFactory::~SlaeModFactory(){}

HRESULT SlaeModFactory::QueryInterface(const IID& iid, void** ppv){
    if (iid == guid::IID_IUnknown || iid == guid::IID_IClassFactory){
        *ppv = (IClassFactory*)this;
    } else if (iid == IID_SlaeModFactory){
        *ppv = (SlaeModFactory*)this;
    } else {
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}

HRESULT SlaeModFactory::CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv){
    HRESULT hr;
    SlaeMod* pSlaeMod;
    *ppv = NULL;
    pSlaeMod = new SlaeMod();
    if (pSlaeMod == 0){
        return (E_OUTOFMEMORY);
    }
    hr = pSlaeMod->QueryInterface(iid, ppv);   
    if (FAILED(hr)){
        delete pSlaeMod;
    }
    return hr;
}

ULONG SlaeModFactory::AddRef(){
    m_lRef++;
    global::global_lRef++;
    return m_lRef;
}

ULONG SlaeModFactory::Release(){
    m_lRef--;
    global::global_lRef--;
    if (m_lRef == 0){
        delete this;
        return 0;
    }
    return m_lRef;
}

HRESULT SlaeModFactory::LockServer(BOOL block){return S_OK;}