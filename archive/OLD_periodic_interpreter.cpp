#include <iostream>
#include <sstream>
#include <unordered_set>
#include <string>
#include <vector>

const std::string version = "1.0";

std::unordered_set<std::string> periodicTable = {
    "h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca",
    "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr",
    "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd",
    "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg",
    "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm",
    "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc", "lv", "ts", "og"
};

int main()
{
    std::cout << "Periodic Interpreter v" << version << "\n------\n";
    while (true)
    {
        std::string sentence, word;
        std::vector<std::string> words;
        std::cout << ">";
        std::getline(std::cin, sentence);
        std::istringstream iss(sentence);
        while (iss >> word)
        {
            words.push_back(word);
        }
        for (const auto& w : words)
        {
            for (std::size_t i = 0; i < w.size(); i += 2)
            {
                std::string pair = w.substr(i, 2);
                std::cout << pair << "\n";
            }
        }
    }
    return 0;
}