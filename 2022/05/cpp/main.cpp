#include "main.hpp"

int main()
{
    // read input
    std::vector<std::string> lines;
    std::string filename = "../input.txt";
    bool input = readFileContent(filename, lines);
    if (!input)
    {
        return -1;
    }

    solvePart1(lines);
    solvePart2(lines);

    return 0;
}