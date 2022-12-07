#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

bool readFileContent(std::string fileName, std::vector<std::string> &lines);
int solvePart1(std::vector<std::string> &lines);
int solvePart2(std::vector<std::string> &lines);
void createSet(std::string assignment, std::set<int> &set);

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
    int totalFullOverlaps = 0;
    std::vector<std::string>::iterator it;
    for (it = lines.begin(); it != lines.end(); ++it)
    {
        std::string s = *it;

        std::string assignment1 = s.substr(0, s.find(','));
        std::string assignment2 = s.substr(s.find(',') + 1, s.length());
        std::set<int> set1, set2;
        createSet(assignment1, set1);
        createSet(assignment2, set2);

        bool set1InSet2 = std::includes(set1.begin(), set1.end(), set2.begin(), set2.end());
        bool set2InSet1 = std::includes(set2.begin(), set2.end(), set1.begin(), set1.end());
        if (set1InSet2 || set2InSet1)
        {
            totalFullOverlaps++;
        }
    }

    return totalFullOverlaps;
}

int solvePart2(std::vector<std::string> &lines)
{
    int totalOverlaps = 0;
    std::vector<std::string>::iterator it;
    for (it = lines.begin(); it != lines.end(); ++it)
    {
        std::string s = *it;
        std::string assignment1 = s.substr(0, s.find(','));
        std::string assignment2 = s.substr(s.find(',') + 1, s.length());
        std::set<int> set1, set2;
        createSet(assignment1, set1);
        createSet(assignment2, set2);

        std::set<int> intersect;
        std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                              std::inserter(intersect, intersect.begin()));

        if (!intersect.empty())
        {
            totalOverlaps++;
        }
    }
    return totalOverlaps;
}

void createSet(std::string assignment, std::set<int> &set)
{
    int assignmentBegin = stoi(assignment.substr(0, assignment.find('-')));
    int assignmentEnd = stoi(assignment.substr(assignment.find('-') + 1, assignment.length()));
    for (int i = assignmentBegin; i <= assignmentEnd; i++)
    {
        set.insert(i);
    }
}