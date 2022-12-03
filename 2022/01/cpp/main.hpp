#include<iostream>
#include<fstream>
#include<vector>
#include<string>

bool readFileContent(std::string fileName, std::vector<std::string> & lines);
int solvePart1();
int solvePart2();
void getAllLoads(std::vector<std::string> & lines, std::vector<int> & loads);

void getAllLoads(std::vector<std::string> & lines, std::vector<int> & loads)
{
    loads.clear();
    int elfLoad = 0;
    std::vector<std::string>::iterator it;
    for(it = lines.begin(); it != lines.end(); ++it)
        {
            if(*it == "")
            {
                loads.push_back(elfLoad);
                elfLoad = 0;
            }
            else{
                elfLoad += stoi(*it);
            }
        }
    
    sort(loads.begin(), loads.end());
}

int solvePart1(std::vector<std::string> & lines)
{
    std::vector<int> loads;
    getAllLoads(lines, loads);
    int maxTotalCalories = loads[loads.size() - 1];

    return maxTotalCalories;
}

int solvePart2(std::vector<std::string> & lines)
{
    std::vector<int> loads;
    getAllLoads(lines, loads);

    int maxTotalCaloriesTop3=0;
    for(std::vector<int>::iterator it = loads.end()-3; it != loads.end(); ++it)
        maxTotalCaloriesTop3 += *it;

    return maxTotalCaloriesTop3;
}

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