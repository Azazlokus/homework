g++ -c dll/mainDll.cpp -o ofiles/mainDll.o
g++ -c dll/Slae.cpp -o ofiles/Slae.o
g++ -c dll/SlaeFactory.cpp -o ofiles/SlaeFactory.o
g++ -c dll/SlaeMod.cpp -o ofiles/SlaeMod.o
g++ -c dll/SlaeModFactory.cpp -o ofiles/SlaeModFactory.o
g++ -c managerDll.cpp -o ofiles/managerDll.o

g++ -shared ./ofiles/Slae.o ./ofiles/mainDll.o ./ofiles/SlaeFactory.o ./ofiles/SlaeMod.o ./ofiles/SlaeModFactory.o -o Slae.dll -lole32 -loleaut32 -luser32 -Wl,--kill-at
g++ -shared ./ofiles/managerDll.o -o managerDll.dll -Wl,--kill-at