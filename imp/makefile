all: testManager clean

testManager: testManager.o metaheuristics.o local_search.o io.o evaluation.o eligibility.o constructive_heuristics.o
	g++ testManager.o metaheuristics.o local_search.o io.o evaluation.o eligibility.o constructive_heuristics.o -o testManager -std=c++17 -O3 -march=native -g

testManager.o: src/testManager.cpp
	g++ src/testManager.cpp -c -std=c++17 -O3 -march=native -g

metaheuristics.o: src/metaheuristics.cpp src/metaheuristics.hpp
	g++ src/metaheuristics.cpp -c -std=c++17 -O3 -march=native -g

local_search.o: src/local_search.cpp src/local_search.hpp
	g++ src/local_search.cpp -c -std=c++17 -O3 -march=native -g

io.o: src/io.cpp src/io.hpp
	g++ src/io.cpp -c -std=c++17 -O3 -march=native -g

evaluation.o: src/evaluation.cpp src/evaluation.hpp
	g++ src/evaluation.cpp -c -std=c++17 -O3 -march=native -g

eligibility.o: src/eligibility.cpp src/eligibility.hpp
	g++ src/eligibility.cpp -c -std=c++17 -O3 -march=native -g

constructive_heuristics.o: src/constructive_heuristics.cpp src/constructive_heuristics.hpp
	g++ src/constructive_heuristics.cpp -c -std=c++17 -O3 -march=native -g

clean:
	rm *.o
