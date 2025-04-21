#ifndef CONSTRUCTIVE_HEURISTICS_HPP
#define CONSTRUCTIVE_HEURISTICS_HPP

#include "global_vars.hpp"
#include "settings.hpp"

/* Constructive Heuristics */
void constructInitialSolution();
int minTSJ();
int calcJobDifferences(int j1, int j2);
int mostSimilarJob(std::vector<int> &rj, int machineIndex);
void constructSimilarityMatrix(Settings &settings);

#endif