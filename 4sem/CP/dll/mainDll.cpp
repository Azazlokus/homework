#include "../hfiles/mainDll.h"
#include "../hfiles/Slae.h"
#include "../hfiles/ClassFactory.h"
#include <windows.h>
#include <iostream>
#include <fstream>
#define NULL __null
using namespace std;

char module_name[MAX_PATH];

HRESULT CreateInstance(const CLSID& clsid, const IID& iid, void** ppv){
    HRESULT hr;
    IClassFactory *pClassFactory = NULL;
    if(clsid == CLSID_Slae){
        SlaeFactory *comFact = new SlaeFactory();
        comFact->QueryInterface(IID_SlaeFactory, (void**)&pClassFactory);
        hr = pClassFactory->CreateInstance(NULL, iid, ppv);
    }
    else if (clsid == CLSID_SlaeMod){
        SlaeModFactory *comFact = new SlaeModFactory();
        comFact->QueryInterface(IID_SlaeModFactory, (void**)&pClassFactory);
        hr = pClassFactory->CreateInstance(NULL, iid, ppv);
    }
    return hr;
}

HRESULT DllGetClassObject(const CLSID& clsid, const IID& iid, void** ppv){
    HRESULT hr;
    if (clsid == CLSID_Slae){
        SlaeFactory *pClassFactory = new SlaeFactory();
        hr = pClassFactory->QueryInterface(iid, ppv);
    } else if (clsid == CLSID_SlaeMod) {
        SlaeModFactory* pClassFactory = new SlaeModFactory();
        hr = pClassFactory->QueryInterface(iid, ppv);
    }
    return hr;
}

HRESULT DllRegisterServer(){
    fstream file;
    int pos_sep;
    string line, num;
    vector<string> lines;
    file.open("C:\\Studies\\prog_labs\\CP\\reg.txt", ios::in);
    while(!file.eof()){
        if (getline(file, line)){
            lines.push_back(line);
        }
    }
    file.close();
    for(int i = 0; i<lines.size(); i++){
        pos_sep = lines[i].find(":");
        num = line.substr(0, pos_sep);
        if (stoi(num) == 1 || stoi(num) == 2){
            lines[i] = num + ":" + (string)module_name + "\n";
        } 
    }
    file.open("C:\\Studies\\prog_labs\\CP\\reg.txt", ios::out);
    if (lines.empty()){
        file << "1:" + (string)module_name + "\n";
        file << "2:" + (string)module_name;
    } else{
        for(int i = 0; i<lines.size(); i++){
            file << lines[i];
        }
    }
    file.close();
    return S_OK;
}

HRESULT DllUnregisterServer(){
    fstream file;
    int pos_sep;
    string line, num;
    vector<string> lines;
    file.open("reg.txt", ios::in);
    while(!file.eof()){
        getline(file, line);
        lines.push_back(line);
    }
    file.close();
    for(int i = 0; i<lines.size(); i++){
        pos_sep = lines[i].find(":");
        if (pos_sep > -1){
            num = line.substr(0, pos_sep);
            if (stoi(num) == 1 or stoi(num) == 2){
                lines[i].erase();
                lines.resize(lines.size() - 1);
                break;
            }
        } 
    }

    file.open("reg.txt", ios::out);
    for(int i = 0; i<lines.size(); i++){
        file << lines[i];
    }
    
    file.close();
    return S_OK;
}

HRESULT DllCanUnloadNow(){
    return (global::global_lRef == 0) ?  S_OK : S_FALSE;
}

BOOL APIENTRY DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved){
    GetModuleFileName(hinstDLL, module_name, sizeof module_name);
    return TRUE;
}