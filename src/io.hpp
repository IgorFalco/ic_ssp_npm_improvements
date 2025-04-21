#ifndef IO_HPP
#define IO_HPP

#include "global_vars.hpp"
#include "summary.hpp"
#include "results.hpp"
#include "settings.hpp"
#include "utils/eligibility.hpp"
#include "utils/evaluation.hpp"
#include "algorithms/metaheuristics.hpp"

/* I/O */
Instance singleRun(std::string inputFileName, std::ofstream &outputFile, int run, int objective, const std::vector<int> &sequence, Summary &summary, Settings &settings);
void readProblem(std::string fileName, Settings &settings);
bool fileExists(const std::string &filename);
template <typename S>
void printSolution(std::string inputFileName, double runningTime, int objective, int run, S &s);
void printSummary(std::string input, Summary &summary, Settings &settings);
template <typename T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &v);
template <typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<std::vector<T>> &matrix);
template <typename T>
std::ostream &operator<<(std::ostream &out, const std::set<T> &m);
template <typename T>
std::ostream &operator<<(std::ostream &os, const std::vector<std::tuple<T, T>> &vector);

/* Initializes and terminates all data structures */
void initialization(Settings &settings);
void termination();
void registerTimeTracking();

#endif