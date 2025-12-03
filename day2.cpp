#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <array>

std::vector<std::pair<int64_t, int64_t>> parseRangeFile(const std::string& filename) {
    std::vector<std::pair<int64_t, int64_t>> ranges;
    std::ifstream file(filename);
    
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filename << std::endl;
        return ranges;
    }
    
    std::string line;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string token;
        
        // Parse comma-separated ranges
        while (std::getline(ss, token, ',')) {
            // Remove leading/trailing whitespace
            size_t start = token.find_first_not_of(" \t\n\r");
            size_t end = token.find_last_not_of(" \t\n\r");
            
            if (start == std::string::npos) continue; // Empty token
            
            token = token.substr(start, end - start + 1);
            
            // Find the dash separator
            size_t dashPos = token.find('-');
            if (dashPos != std::string::npos && dashPos > 0) {
                try {
                    int64_t first = std::stoll(token.substr(0, dashPos));
                    int64_t second = std::stoll(token.substr(dashPos + 1));
                    ranges.push_back(std::make_pair(first, second));
                } catch (const std::exception& e) {
                    std::cerr << "Error parsing range: " << token << std::endl;
                }
            }
        }
    }
    
    file.close();
    return ranges;
}

using std::int64_t;

int64_t dc(int64_t x) {
    int64_t res = 0;
    while (x > 0) {
        res += 1;
        x /= 10;
    }
    return res;
}

bool is_bad(int64_t x) {
    constexpr std::array<int64_t, 9> pows = {1,10,100,1000,10000,100000,1000000,10000000,100000000};
    auto l = dc(x);
    if (l % 2 != 0) {
        return false;
    }

    int64_t ps = pows[l / 2];
    return x == (x % ps) + (x % ps) * ps;
}

bool is_bad2(int64_t x) {
    constexpr std::array<int64_t, 9> pows = {1,10,100,1000,10000,100000,1000000,10000000,100000000};
    auto l = dc(x);

    for (int64_t i = 2; i <= l; ++i) {
        if (l % i == 0) {
            int64_t ps = pows[l / i];
            auto sec = x % ps;
            auto res = 0ll;
            for(int j = 0; j < i; ++j) {
                res *= ps;
                res += sec;
            }

            if (x == res) {
                return true;
            }
        }
    }

    if (l % 2 != 0) {
        return false;
    }

    int64_t ps = pows[l / 2];
    return x == (x % ps) + (x % ps) * ps;
}

int main() {
    // Example usage:
    auto ranges = parseRangeFile("input/2/real");

    int64_t res = 0;
    int64_t res2 = 0;
    std::cout << "Parsed " << ranges.size() << " ranges:" << std::endl;
    for (const auto& range : ranges) {
        std::cout << range.first << "-" << range.second << std::endl;
        for (int64_t i = range.first; i <= range.second; ++i) {
            if (is_bad(i)) {
                std::cout << "  Bad number: " << i << std::endl;
                res += i;
            }
            if (is_bad2(i)) {
                std::cout << "  Bad number2: " << i << std::endl;
                res2 += i;
            }
        }
    }
    std::cout << "Total bad numbers: " << res << std::endl;
    std::cout << "Total bad numbers2: " << res2 << std::endl; 
    return 0;
}