#include "global_vars.hpp"
#include "results.hpp"
#include "summary.hpp"
#include "io.hpp"

using namespace std;

int main(int argc, char *argv[])
{
  vector<string> arguments(argv + 1, argv + argc);

  srand(time(NULL));
  parseArguments(arguments);

  Summary summary;

  cout << "Sequence: " << sequence << endl;

  if (fpIndex.is_open())
  {
    while (fpIndex >> inputFileName)
    {
      Results *results = new Results();
      for (int i = 1; i <= runs; i++)
      {
        results->addSolution(singleRun(inputFileName, outputFile, i, objective, sequence, summary));
        termination();
      }
      summary.addResults(results);
    }
  }
  else if (fileExists(instance))
  {
    Results *results = new Results();
    for (int i = 1; i <= runs; i++)
    {
      results->addSolution(singleRun(instance, outputFile, i, objective, sequence, summary));
      termination();
    }
    summary.addResults(results);
  }
  else
    throw invalid_argument("ERROR : Input file not well informed");

  printSummary(fpIndex.is_open() ? inputFileName : instance, summary);
}