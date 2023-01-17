#include "hfiles/ClassFactory.h"
#include "hfiles/mainDll.h"
#include "hfiles/Slae.h"
#include <windows.h>
#include <iostream>
#pragma once

typedef HRESULT (*FunctionArg) (CLSID, IID, void**);
typedef HRESULT (*FunctionNotArg) ();
