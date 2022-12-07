#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

bool readFileContent(std::string fileName, std::vector<std::string> &lines);
int solvePart1(std::vector<std::string> &lines);
int solvePart2(std::vector<std::string> &lines);
int getItemPriority(char element);
void findIntersectionOf3(std::string string1, std::string string2, std::string string3, std::string &intersection);

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
    int totalPriority = 0;
    std::vector<std::string>::iterator it;
    for (it = lines.begin(); it != lines.end(); ++it)
    {
        std::string s = *it;
        std::string commonElements;
        std::string firstCompartment = s.substr(0, s.length() / 2);
        std::string secondCompartment = s.substr(s.length() / 2);

        std::sort(firstCompartment.begin(), firstCompartment.end());
        std::sort(secondCompartment.begin(), secondCompartment.end());
        std::set_intersection(firstCompartment.begin(), firstCompartment.end(), secondCompartment.begin(), secondCompartment.end(), std::back_inserter(commonElements));

        int itemPriority = getItemPriority(commonElements[0]);
        totalPriority += itemPriority;
    }

    return totalPriority;
}

int solvePart2(std::vector<std::string> &lines)
{
    int totalGroupPriority = 0;
    std::vector<std::string>::iterator it;
    for (it = lines.begin(); it != lines.end(); it += 3)
    {
        std::string commonElements;
        std::string firstElf = *it;
        std::string secondElf = *(it + 1);
        std::string thirdElf = *(it + 2);

        findIntersectionOf3(firstElf, secondElf, thirdElf, commonElements);
        int groupPriority = getItemPriority(commonElements[0]);
        totalGroupPriority += groupPriority;
    }

    return totalGroupPriority;
}

int getItemPriority(char element)
{
    int priority = 0;
    if (isupper(element))
    {
        priority += 26;
        element = tolower(element);
    }
    priority += element - 96;

    return priority;
}

void findIntersectionOf3(std::string string1, std::string string2, std::string string3, std::string &intersection)
{
    std::sort(string1.begin(), string1.end());
    std::sort(string2.begin(), string2.end());
    std::sort(string3.begin(), string3.end());

    std::string midIntersection1;
    std::string midIntersection2;
    std::set_intersection(string1.begin(), string1.end(), string2.begin(), string2.end(), std::back_inserter(midIntersection1));
    std::set_intersection(string1.begin(), string1.end(), string3.begin(), string3.end(), std::back_inserter(midIntersection2));

    std::set_intersection(midIntersection1.begin(), midIntersection1.end(), midIntersection2.begin(), midIntersection2.end(), std::back_inserter(intersection));
}