#include <vector>
#include <iostream>
#include "global_vars.hpp"
#include "results.hpp"
#include "summary.hpp"
#include "settings.hpp"
#include "io.hpp"

using namespace std;

int main(int argc, char *argv[])
{
  vector<string> arguments(argv + 1, argv + argc);

  srand(time(NULL));
  Settings::init(arguments);

  Settings &settings = Settings::getInstance();

  Summary summary;

  cout << "Sequence: " << settings.sequence << endl;

  if (settings.fpIndex.is_open())
  {
    while (settings.fpIndex >> settings.inputFileName)
    {
      Results *results = new Results();
      for (int i = 1; i <= settings.runs; i++)
      {
        results->addSolution(singleRun(settings.inputFileName, settings.outputFile, i, settings.objective, sequence, summary, settings));
        termination();
      }
      summary.addResults(results);
    }
  }
  else if (fileExists(settings.instance))
  {
    Results *results = new Results();
    for (int i = 1; i <= settings.runs; i++)
    {
      results->addSolution(singleRun(settings.instance, settings.outputFile, i, settings.objective, sequence, summary, settings));
      termination();
    }
    summary.addResults(results);
  }
  else
    throw invalid_argument("ERROR : Input file not well informed");

  string input = settings.fpIndex.is_open() ? settings.inputFileName : settings.instance;
  printSummary(input, summary, Settings::getInstance());
}