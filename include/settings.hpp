#pragma once
#include <string>
#include <vector>
#include <fstream>
#include <stdexcept>
#include <iostream>

class Settings
{
public:
  static void init(const std::vector<std::string> &arguments)
  {
    if (!_instance)
      _instance = new Settings(arguments);
  }

  static Settings &getInstance()
  {
    if (!_instance)
      throw std::logic_error("Settings not initialized. Call Settings::init(arguments) first.");
    return *_instance;
  }

  // Parâmetros públicos acessáveis globalmente
  int objective;
  int runs = 1;
  int maxIterations = 1000;
  std::string instance;
  float similarityPercentage = 0.7f;
  float criticJobPercentage = 0.65f;
  float disturbSize = 0.085f;
  float oneBlockPercentage = 0.25f;
  std::string inputFileName;
  std::ifstream fpIndex;
  std::ofstream outputFile;
  std::vector<int> sequence;

private:
  static Settings *_instance;

  Settings(const std::vector<std::string> &arguments)
  {
    parseArguments(arguments);
  }

  void parseArguments(const std::vector<std::string> &arguments)
  {
    for (size_t i = 0; i < arguments.size(); ++i)
    {
      const std::string &arg = arguments[i];
      if (arg == "--objective")
      {
        objective = std::stoi(arguments[++i]);
        if (objective < 1 || objective > 3)
          throw std::invalid_argument("ERROR : Objective must be 1 (TS), 2 (makespan), or 3 (flowtime)");
      }
      else if (arg == "--runs")
      {
        runs = std::stoi(arguments[++i]);
      }
      else if (arg == "--iterations")
      {
        maxIterations = std::stoi(arguments[++i]);
      }
      else if (arg == "--instance")
      {
        instance = arguments[++i];
      }
      else if (arg == "--similarity_percentage")
      {
        similarityPercentage = std::stof(arguments[++i]);
      }
      else if (arg == "--critic_job_percentage")
      {
        criticJobPercentage = std::stof(arguments[++i]);
      }
      else if (arg == "--disturb_size")
      {
        disturbSize = std::stof(arguments[++i]);
      }
      else if (arg == "--one_block_percentage")
      {
        oneBlockPercentage = std::stof(arguments[++i]);
      }
      else if (arg == "--input")
      {
        inputFileName = arguments[++i];
        fpIndex.open(inputFileName);
        if (!fpIndex.is_open())
          throw std::invalid_argument("ERROR : Input file doesn't exist");
      }
      else if (arg == "--output")
      {
        outputFile.open(arguments[++i]);
      }
      else if (arg == "--sequence")
      {
        sequence.clear();
        for (char ch : arguments[++i])
        {
          if (isdigit(ch))
            sequence.push_back(ch - '0');
          else
            throw std::invalid_argument("ERROR: Sequence must contain only digits.");
        }
      }
    }
  }

  // Impede cópias
  Settings(const Settings &) = delete;
  Settings &operator=(const Settings &) = delete;
};
inline Settings *Settings::_instance = nullptr;
