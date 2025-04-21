#pragma once

#include "results.hpp"
#include "global_vars.hpp"
#include <vector>
#include <tuple>

class Summary
{
public:
  std::vector<Results *> results;
  std::vector<long> localSearchImprovements;

  Summary()
  {
    localSearchImprovements = {0, 0, 0, 0, 0};
  }

  void addResults(Results *r) { results.push_back(r); }

  double getBestsMean(int objective)
  {
    long sum = 0;
    for (int i = 0; i < results.size(); i++)
    {
      sum += results[i]->getBestResult(objective);
    }

    return (double)sum / (double)results.size();
  }

  double getMeanStandardDeviation(int objective)
  {
    long sum = 0;
    for (int i = 0; i < results.size(); i++)
    {
      sum += results[i]->getStandardDeviation(objective);
    }

    return (double)sum / (double)results.size();
  }

  double getMeanExecutionTime()
  {
    long sum = 0;
    for (int i = 0; i < results.size(); i++)
    {
      sum += results[i]->getMeanExecutionTime();
    }

    return (double)sum / (double)results.size();
  }

  double getGeneralMean(int objective)
  {
    double r = 0.0;
    for (int i = 0; i < results.size(); i++)
    {
      r += results[i]->getMean(objective);
    }

    return r / (double)results.size();
  }

  double getMeanCompletedIterations()
  {
    long sum = 0;
    for (int i = 0; i < results.size(); i++)
    {
      sum += results[i]->getMeanCompletedIterations();
    }

    return (double)sum / (double)results.size();
  }

  std::vector<std::tuple<int, int>> getTrajectoryData()
  {
    std::vector<int> trajectory(iterations, 0);
    std::vector<std::tuple<int, int>> dots;

    for (int i = 0; i < results.size(); i++)
    {
      for (int j = 0; j < results[i]->solutions.size(); j++)
      {
        for (int k = 0; k < results[i]->solutions[j].improvements.size(); k++)
        {
          if (!trajectory[get<0>(results[i]->solutions[j].improvements[k])])
          {
            trajectory[get<0>(results[i]->solutions[j].improvements[k])] = get<1>(results[i]->solutions[j].improvements[k]);
          }
          else
          {
            trajectory[get<0>(results[i]->solutions[j].improvements[k])] = (get<1>(results[i]->solutions[j].improvements[k]) + trajectory[get<0>(results[i]->solutions[j].improvements[k])]) / 2;
          }
        }
      }
    }

    for (int i = 1; i < trajectory.size(); i++)
    {
      if (!trajectory[i])
        trajectory[i] = trajectory[i - 1];
      if (trajectory[i - 1] < trajectory[i])
        trajectory[i] = trajectory[i - 1];
    }

    dots.push_back(std::make_tuple(0, trajectory[0]));
    for (int i = 1; i < trajectory.size(); i++)
    {
      if (trajectory[i] != trajectory[i - 1])
        dots.push_back(std::make_tuple(i, trajectory[i]));
    }
      dots.push_back(std::make_tuple((int)getMeanCompletedIterations(), get<1>(dots[dots.size() - 1])));

    return dots;
  }
};

inline Summary summary;