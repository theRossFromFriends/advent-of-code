#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

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
    int totalScore = 0;
    std::vector<std::string>::iterator it;
    for(it = lines.begin(); it != lines.end(); ++it)
    {
        std::string s = *it;
        char opponentChoice = s[0];
        char myChoice = s[2];

        std::map<char, int> itemPoints;
        itemPoints['X'] = 1;
        itemPoints['Y'] = 2;
        itemPoints['Z'] = 3;

        std::map<std::pair<char,char>, int> roundPoints;
        roundPoints[std::make_pair('A', 'X')] = 3;
        roundPoints[std::make_pair('A', 'Y')] = 6;
        roundPoints[std::make_pair('A', 'Z')] = 0;
        roundPoints[std::make_pair('B', 'X')] = 0;
        roundPoints[std::make_pair('B', 'Y')] = 3;
        roundPoints[std::make_pair('B', 'Z')] = 6;
        roundPoints[std::make_pair('C', 'X')] = 6;
        roundPoints[std::make_pair('C', 'Y')] = 0;
        roundPoints[std::make_pair('C', 'Z')] = 3;

        totalScore += itemPoints[myChoice];
        totalScore += roundPoints[std::make_pair(opponentChoice,myChoice)];
    }

    return totalScore;
}

int solvePart2(std::vector<std::string> & lines)
{
    int totalScore = 0;
    std::vector<std::string>::iterator it;
    for(it = lines.begin(); it != lines.end(); ++it)
    {
        std::string s = *it;
        char opponentChoice = s[0];
        char myStrategy = s[2];

        std::map<char, int> itemPoints;
        itemPoints['A'] = 1;
        itemPoints['B'] = 2;
        itemPoints['C'] = 3;

        std::map<std::pair<char,char>, char> choiceStrategy;
        choiceStrategy[std::make_pair('A', 'X')] = 'C';
        choiceStrategy[std::make_pair('A', 'Y')] = 'A';
        choiceStrategy[std::make_pair('A', 'Z')] = 'B';
        choiceStrategy[std::make_pair('B', 'X')] = 'A';
        choiceStrategy[std::make_pair('B', 'Y')] = 'B';
        choiceStrategy[std::make_pair('B', 'Z')] = 'C';
        choiceStrategy[std::make_pair('C', 'X')] = 'B';
        choiceStrategy[std::make_pair('C', 'Y')] = 'C';
        choiceStrategy[std::make_pair('C', 'Z')] = 'A';

        std::map<std::pair<char,char>, int> roundPoints;
        roundPoints[std::make_pair('A', 'A')] = 3;
        roundPoints[std::make_pair('A', 'B')] = 6;
        roundPoints[std::make_pair('A', 'C')] = 0;
        roundPoints[std::make_pair('B', 'A')] = 0;
        roundPoints[std::make_pair('B', 'B')] = 3;
        roundPoints[std::make_pair('B', 'C')] = 6;
        roundPoints[std::make_pair('C', 'A')] = 6;
        roundPoints[std::make_pair('C', 'B')] = 0;
        roundPoints[std::make_pair('C', 'C')] = 3;

        char myChoice = choiceStrategy[std::make_pair(opponentChoice,myStrategy)];

        totalScore += itemPoints[myChoice];
        totalScore += roundPoints[std::make_pair(opponentChoice,myChoice)];
    }

    return totalScore;
}