#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

bool readFileContent(std::string fileName, std::vector<std::string> &lines);
int solvePart1(std::vector<std::string> &lines);
int solvePart2(std::vector<std::string> &lines);
void readData(std::vector<std::string> &lines, std::vector<std::string> &instructions, std::vector<std::vector<char>> &stacksArray);
void printResult(std::vector<std::vector<char>> &stacksArray);

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
    std::vector<std::vector<char>> stacksArray;
    std::vector<std::string> instructions;
    std::vector<std::string>::iterator it;

    readData(lines, instructions, stacksArray);

    // perform instructions
    for (it = instructions.begin(); it != instructions.end(); ++it)
    {
        std::string str = *it;
        std::vector<std::string> data;
        std::stringstream ss(str);
        std::string s;
        while (std::getline(ss, s, ' '))
        {
            data.push_back(s);
        }
        int amount = stoi(data[1]);
        int fromStack = stoi(data[3]);
        int toStack = stoi(data[5]);

        // pop from 'fromStack' to 'toStack' times 'amount'
        for (int i = 0; i < amount; i++)
        {
            char val = stacksArray[fromStack - 1].back();
            stacksArray[fromStack - 1].pop_back();
            stacksArray[toStack - 1].push_back(val);
        }
    }

    std::cout << "Solution part1: " << std::endl;
    printResult(stacksArray);

    return 0;
}

int solvePart2(std::vector<std::string> &lines)
{
    std::vector<std::vector<char>> stacksArray;
    std::vector<std::string> instructions;
    std::vector<std::string>::iterator it;

    readData(lines, instructions, stacksArray);

    // perform instructions
    for (it = instructions.begin(); it != instructions.end(); ++it)
    {
        std::string str = *it;
        std::vector<std::string> data;
        std::stringstream ss(str);
        std::string s;
        while (std::getline(ss, s, ' '))
        {
            data.push_back(s);
        }
        int amount = stoi(data[1]);
        int fromStack = stoi(data[3]);
        int toStack = stoi(data[5]);

        // append
        stacksArray[toStack - 1].insert(stacksArray[toStack - 1].end(), stacksArray[fromStack - 1].end() - amount, stacksArray[fromStack - 1].end());
        // cut off
        stacksArray[fromStack - 1].resize(stacksArray[fromStack - 1].size() - amount);
    }

    std::cout << "Solution part2: " << std::endl;
    printResult(stacksArray);

    return 0;
}

void readData(std::vector<std::string> &lines, std::vector<std::string> &instructions, std::vector<std::vector<char>> &stacksArray)
{
    std::vector<std::string> stacks;
    std::vector<std::string>::iterator it;

    // split into stacks and instructions vectors;
    for (it = lines.begin(); it != lines.end(); ++it)
    {
        std::string s = *it;
        if (s.empty())
        {
            stacks.assign(lines.begin(), it);
            instructions.assign(it + 1, lines.end());
            break;
        }
    }

    // push elements into stacksArray
    std::vector<std::string>::reverse_iterator rit;
    for (rit = stacks.rbegin() + 1; rit != stacks.rend(); ++rit)
    {
        std::string str = *rit;

        int stacksCount = (str.length() + 1) / 4;
        if (stacksArray.size() == 0)
        {
            stacksArray.resize(stacksCount);
        }

        for (int i = 0; i < stacksCount; i++)
        {
            char element = str[i * 4 + 1];
            if (element != ' ')
            {
                stacksArray[i].push_back(element);
            }
        }
    }
}

void printResult(std::vector<std::vector<char>> &stacksArray)
{
    std::vector<std::vector<char>>::iterator it;
    for (it = stacksArray.begin(); it != stacksArray.end(); ++it)
    {
        std::vector<char> stack = *it;
        std::cout << stack.back() << std::endl;
    }
}