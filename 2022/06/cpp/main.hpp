#include <iostream>
#include <fstream>
#include <vector>
#include <string>

bool readFileContent(std::string fileName, std::vector<std::string> &lines);
int solvePart1(std::vector<std::string> &lines);
int solvePart2(std::vector<std::string> &lines);
bool hasUniqueCharacters(std::string str);

bool readFileContent(std::string fileName, std::vector<std::string> &lines)
{
    lines.clear();
    std::ifstream input_file(fileName);
    std::string s;

    if (!input_file)
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

int solvePart1(std::vector<std::string> &lines)
{
    std::string str = lines[0];
    for (int i = 4; i < str.length(); i++)
    {
        std::string substring = str.substr(i - 4, 4);
        if (hasUniqueCharacters(substring))
        {
            return i;
        }
    }

    return 0;
}

int solvePart2(std::vector<std::string> &lines)
{
    std::string str = lines[0];
    for (int i = 14; i < str.length(); i++)
    {
        std::string substring = str.substr(i - 14, 14);
        if (hasUniqueCharacters(substring))
        {
            return i;
        }
    }

    return 0;
}

bool hasUniqueCharacters(std::string str)
{
    for (int i = 0; i < str.length() - 1; i++)
    {
        for (int j = i + 1; j < str.length(); j++)
        {
            if (str[i] == str[j])
            {
                return false;
            }
        }
    }

    return true;
}