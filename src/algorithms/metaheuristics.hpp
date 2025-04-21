#ifndef METAHEURISTICS_HPP
#define METAHEURISTICS_HPP

#include "global_vars.hpp"
#include "summary.hpp"

/* Metaheuristics */
void ILSCrit(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, const std::vector<int> &sequence, Summary &summary);
void ILSFull(std::function<int(void)> evaluationFunction, std::vector<int> &evaluationVector, const std::vector<int> &sequence, Summary &summary);

void jobInsertionDisturb();
void jobExchangeDisturb();
void twoOptDisturb();
void swapDisturb();
bool criticJobDisturb();

void updateBestSolution(std::function<int(void)> evaluationFunction);

#endif