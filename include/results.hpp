#pragma once
#include <vector>
#include <cmath>
#include "instance.hpp"

class Results
{
public:
  std::vector<Instance> solutions;

  void addSolution(Instance s) { solutions.push_back(s); }

  int getBestResult(int objective)
  {
    int best = INT_MAX;
    switch (objective)
    {
    case 1:
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        if (solutions[i].toolSwitches < best)
          best = solutions[i].toolSwitches;
      }
      break;
    case 2:
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        if (solutions[i].makespan < best)
          best = solutions[i].makespan;
      }
      break;
    case 3:
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        if (solutions[i].flowtime < best)
          best = solutions[i].flowtime;
      }
      break;
    }

    return best;
  }

  double getMean(int objective)
  {
    int sum = 0;
    switch (objective)
    {
    case 1:
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        sum += solutions[i].toolSwitches;
      }
      break;
    case 2:
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        sum += solutions[i].makespan;
      }
      break;
    case 3:
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        sum += solutions[i].flowtime;
      }
      break;
    }

    return (double)sum / (double)solutions.size();
  }

  double getStandardDeviation(int objective)
  {
    double standardDeviation = 0, mean;
    switch (objective)
    {
    case 1:
      mean = this->getMean(1);
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        standardDeviation += pow(solutions[i].toolSwitches - mean, 2);
      }
      break;
    case 2:
      mean = this->getMean(2);
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        standardDeviation += pow(solutions[i].makespan - mean, 2);
      }
      break;
    case 3:
      mean = this->getMean(3);
      for (int i = 0; i < (int)solutions.size(); i++)
      {
        standardDeviation += pow(solutions[i].flowtime - mean, 2);
      }
      break;
    }

    return sqrt(standardDeviation / (double)solutions.size());
  }

  double getMeanExecutionTime()
  {
    double sum = 0;
    for (int i = 0; i < solutions.size(); i++)
    {
      sum += solutions[i].runningTime;
    }

    return sum / (double)solutions.size();
  }

  double getMeanCompletedIterations()
  {
    double sum = 0;
    for (int i = 0; i < solutions.size(); i++)
    {
      sum += solutions[i].completedIterations;
    }

    return sum / (double)solutions.size();
  }
};