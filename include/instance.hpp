#pragma once

#include <iostream>
#include <string>
#include <vector>

class Instance
{
public:
  std::vector<std::vector<int>> assignement;
  int toolSwitches;
  int makespan;
  int flowtime;
  int completedIterations;
  double runningTime;
  std::vector<int> timeTracking;
  std::vector<std::tuple<int, int>> improvements;

  Instance(std::vector<std::vector<int>> _assignement, int _toolSwitches,
           int _makespan, int _flowtime, std::vector<std::tuple<int, int>> _improvements,
           double _runningTime, int _completedIterations, std::vector<int> _timeTracking)
  {
    assignement = _assignement;
    toolSwitches = _toolSwitches;
    makespan = _makespan;
    flowtime = _flowtime;
    improvements = _improvements;
    runningTime = _runningTime;
    completedIterations = _completedIterations;
    timeTracking = _timeTracking;
  }
};