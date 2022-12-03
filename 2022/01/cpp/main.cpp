#include"main.hpp"

int main() 
{
    //read input
    std::vector<std::string> lines;
    std::string filename = "../input.txt";
    bool input = readFileContent(filename, lines);
    if(!input)
    {
        return -1;
    }
    
    auto result1 = solvePart1(lines);
    auto result2 = solvePart2(lines);

    std::cout<<"Solution part1: "<<result1<<'\n';
    std::cout<<"Solution part2: "<<result2<<'\n';

    return 0;
}