#ifndef GLOBAL_VARS_HPP
#define GLOBAL_VARS_HPP

#include <sys/stat.h>
#include <random>
#include <algorithm>
#include <iostream>
#include <string>
#include <fstream>
#include <climits>
#include <vector>
#include <chrono>
#include <cstdio>
#include <numeric>
#include <tuple>
#include <functional>
#include <set>
#include <cstdlib>
#include <cmath>
#include <iomanip>

#define PRINT_MATRIX false

inline int flowtimeSum, flowtimeAux, iterations, objectives[] = {1 /*TS*/, 2 /*Makespan*/, 3 /*Flowtime*/};
inline int machineCount, toolCount, jobCount, currentBest, best, beforeSwap1, beforeSwap2, maxTime = 3600;
inline float lowestMakespanPercentage = 0.5;
inline std::chrono::duration<double> time_span;
inline std::string ans;
inline std::vector<int> npmMagazineCapacity, npmSwitchCost, npmCurrentToolSwitches, npmCurrentMakespan, npmCurrentFlowTime, mI, randomTools, localSearchImprovements, timeTracking, sequence;
inline std::vector<std::set<int>> jobSets, magazines;
inline std::set<std::tuple<int, int>> dist;
inline std::vector<std::tuple<int, int>> oneBlocks, improvements;
inline std::vector<std::vector<int>> npmJobAssignement, bestSolution, toolsRequirements, npmJobTime, npmCurrentMagazines, npmToolsNeedDistance;
inline std::vector<std::vector<int>> toolsDistancesGPCA, jobEligibility;
inline std::vector<std::vector<bool>> similarityMatrix;
inline std::chrono::high_resolution_clock::time_point t1, t2;

#endif