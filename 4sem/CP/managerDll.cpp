#include "managerDll.h"
#include "module-info.h"
#include <fstream>
using namespace std;

vector<HINSTANCE> libs(1);

HRESULT GetClassObject(const CLSID& clsid, const IID& iid, void** ppv){
    HRESULT hr;
    HINSTANCE h;
    FunctionArg DLLGetClassObject;
    bool isFind = false;
    fstream file;
    string line, num;
    const char *path;
    int pos_sep;

    file.open("reg.txt", ios::in);
    while(getline(file, line)){
        pos_sep = line.find(":");
        num = line.substr(0, pos_sep);
        if (stoi(num) == 2){
            line = line.substr(pos_sep + 1, line.length());
            path = line.c_str();
            isFind = true;
            break;
        } 
    }
    file.close();
    if (isFind){
        h = LoadLibrary(path);
        if (h){
            DLLGetClassObject = (FunctionArg) GetProcAddress(h, "DllGetClassObject");
            libs.push_back(h);
            if (DLLGetClassObject){
                hr = DLLGetClassObject(clsid, iid, ppv);
            }
        }
    }
    return hr;
}

HRESULT CreateInstance(const CLSID& clsid, const IID& iid, void** ppv){
    HRESULT hr;
    IClassFactory* factory;
    hr = GetClassObject(clsid, guid::IID_IClassFactory, (void**)&factory);
    factory->CreateInstance(NULL, iid, ppv);
    return hr;
}

HRESULT FreeUnusedLibraries(){
    HRESULT hr;
    FunctionNotArg DllCanUnloadNow;
    for (int i = 0; i < libs.size(); i++){
        DllCanUnloadNow = (FunctionNotArg) GetProcAddress(libs[i], "DllCanUnloadNow");
        if (DllCanUnloadNow){
            hr = DllCanUnloadNow();
            if (SUCCEEDED(hr)){
                FreeLibrary(libs[i]);
                libs.erase(libs.begin() + i);
                libs.resize(libs.size() - 1);
            }
        }
    }
    return hr;
}