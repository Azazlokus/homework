g++ -c main.cpp -o ofiles/main.o
g++ ./ofiles/main.o -o main.exe -lole32 -loleaut32 -luser32 -luuid