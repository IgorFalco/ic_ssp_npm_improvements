#ifndef LOCAL_SEARCH_HPP
#define LOCAL_SEARCH_HPP

#include "global_vars.hpp"
#include "summary.hpp"

bool VNDCrit(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, const std::vector<int> &sequence, Summary &summary);
bool VNDFull(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, const std::vector<int> &sequence, Summary &summary);
bool VNDCritSim(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, const std::vector<int> &sequence, Summary &summary);
bool VNDFullSim(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, const std::vector<int> &sequence, Summary &summary);

/* Local search methods */
/* 0 */ bool jobInsertionLocalSearchCrit(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
/* 0 */ bool jobInsertionLocalSearchFull(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
/* 1 */ bool twoOptLocalSearch(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest, bool onlyCriticalMachine);
/* 2 */ bool jobExchangeLocalSearchCrit(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
/* 2 */ bool jobExchangeLocalSearchFull(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
/* 3 */ bool swapLocalSearch(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
bool oneBlockLocalSearch(std::function<int(void)> &evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
bool oneBlockLocalSearchCrit(std::function<int(void)> &evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
std::vector<std::tuple<int, int>> findOneBlocks(int machineIndex, int tool);

bool swapLocalSearchSim(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
bool twoOptLocalSearchSim(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest, bool onlyCriticalMachine);
bool jobExchangeLocalSearchFullSim(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);
bool jobExchangeLocalSearchCritSim(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, int currentBest);

#endif