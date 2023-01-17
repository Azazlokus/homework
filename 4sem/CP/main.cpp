#include "module-info.h"
#include "managerDll.h"
using namespace std;

int main()
{

	/* USING WINDOWS MANAGER */
	CoInitialize(NULL);
	CLSID CLSID_SlaeMod_ProgID;
	const wchar_t *progID = L"VMV.Application.2";
	HRESULT resCLSID_ProgID = CLSIDFromProgID(progID, &CLSID_SlaeMod_ProgID);
	IOperation *op = NULL;
	IClassFactory *factory = NULL;
	HRESULT resFactory;
	resFactory = CoGetClassObject(CLSID_SlaeMod_ProgID, CLSCTX_INPROC_SERVER, NULL, guid::IID_IClassFactory, (void **)&factory);
	if (SUCCEEDED(resFactory))
	{
		HRESULT res;
		IOperation *op = NULL;
		res = factory->CreateInstance(NULL, IID_IOperation, (void **)&op);
		if (SUCCEEDED(res))
		{
			op->input("input.txt");
			op->solve("input.txt");
		}
		IMatrProp *mp = NULL;
		res = op->QueryInterface(IID_IMatrProp, (void **)&mp);
		if (SUCCEEDED(res))
		{
			mp->transpos();
			mp->det();
		}
		op->Release();
		mp->Release();
		factory->Release();
	}
	else
	{
		cout << "NO FACTORY";
	}
	CoUninitialize();

	/* USING OWN MANAGER */
	/*HINSTANCE h;
	HRESULT res;
	FunctionArg GetClassObject, CreateInstance;
	FunctionNotArg FreeUnusedLibraries;
	SlaeModFactory* factory;
	h = LoadLibrary("managerDll.dll");
	GetClassObject = (FunctionArg) GetProcAddress(h, "GetClassObject");
	FreeUnusedLibraries = (FunctionNotArg) GetProcAddress(h, "FreeUnusedLibraries");
	CreateInstance = (FunctionArg) GetProcAddress(h, "CreateInstance");

	res = GetClassObject(CLSID_SlaeMod, IID_SlaeModFactory, (void**)&factory);
	if (SUCCEEDED(res)){
		IOperation* op = NULL;
		res = factory->CreateInstance(NULL, IID_IOperation, (void**)&op);
		if (SUCCEEDED(res)){
			op->input("input.txt");
			op->solve("input.txt");
		}
		IMatrProp* mp = NULL;
		res = op->QueryInterface(IID_IMatrProp, (void**)&mp);
		if (SUCCEEDED(res)){
			mp->transpos();
			mp->det();
		}
		op->Release();
		mp->Release();
		factory->Release();
	}
	FreeUnusedLibraries();
	FreeLibrary(h);*/
}