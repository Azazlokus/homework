#include "module-info.h"
#pragma once

extern "C" HRESULT __declspec(dllexport) GetClassObject(const CLSID& clsid, const IID& iid, void** ppv);
extern "C" HRESULT __declspec(dllexport) CreateInstance();
extern "C" HRESULT __declspec(dllexport) FreeUnusedLibraries();