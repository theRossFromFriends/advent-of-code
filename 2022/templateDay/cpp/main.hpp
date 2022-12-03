#include<iostream>
#include<fstream>
#include<vector>
#include<string>

bool readFileContent(std::string fileName, std::vector<std::string> & lines);
int solvePart1(std::vector<std::string> & lines);
int solvePart2(std::vector<std::string> & lines);

bool readFileContent(std::string fileName, std::vector<std::string> & lines)
{
    lines.clear();
    std::ifstream input_file(fileName);
    std::string s;

    if(!input_file)
    {
        return false;
    }

    while (getline(input_file, s))
    {
        lines.push_back(s);
    }
    input_file.close();

    return true;
}

int solvePart1(std::vector<std::string> & lines)
{
    return 0;
}

int solvePart2(std::vector<std::string> & lines)
{
    return 0;
}