#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <array>
#include <deque>
#include <
using namespace std;

std::vector<std::pair<int64_t, int64_t>> parsePairFile(const std::string& filename) {
    std::vector<std::pair<int64_t, int64_t>> pairs;
    std::ifstream file(filename);
    
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filename << std::endl;
        return pairs;
    }
    
    std::string line;
    while (std::getline(file, line)) {
        size_t start = line.find_first_not_of(" \t\n\r");
        size_t end = line.find_last_not_of(" \t\n\r");
        
        if (start == std::string::npos) continue; // Empty line
        
        line = line.substr(start, end - start + 1);
        
        size_t commaPos = line.find(',');
        if (commaPos != std::string::npos) {
            try {
                int64_t first = std::stoll(line.substr(0, commaPos));
                int64_t second = std::stoll(line.substr(commaPos + 1));
                pairs.push_back(std::make_pair(first, second));
            } catch (const std::exception& e) {
                std::cerr << "Error parsing line: " << line << std::endl;
            }
        }
    }
    
    file.close();
    return pairs;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <input_file>" << std::endl;
        return 1;
    }
    auto pairs = parsePairFile(argv[1]);



    int64_t res1 = 0;
    for (int i = 0; i + 1< pairs.size(); ++i) {
        for (int j = i + 1; j + 1 < pairs.size(); ++j) {
            const auto& p1 = pairs[i];
            const auto& p2 = pairs[j];

            pair<int64_t, int64_t> tl = {std::min(p1.first, p2.first), std::min(p1.second, p2.second)};
            pair<int64_t, int64_t> br = {std::max(p1.first, p2.first), std::max(p1.second, p2.second)};

            int64_t area = (br.first - tl.first + 1) * (br.second - tl.second + 1);
            res1 = max(res1, area); 
        }
    }

    std::cout << "Max area: " << res1 << std::endl;

    pair<int64_t, int64_t> br = {0ll, 0ll};
    for (auto& p : pairs) {
        p.first += 1; 
        p.second += 1;
        br = {max(br.first, p.first), max(br.second, p.second)};
    }

    br.first += 2;
    br.second += 2;

    vector<vector<uint8_t>> grid(br.first, vector<uint8_t>(br.second, 1));

    for(int i = 0; i < pairs.size(); ++i) {
        auto& p1 = pairs[i];
        auto& p2 = pairs[(i + 1) % pairs.size()];

        pair<int64_t, int64_t> tl2 = {std::min(p1.first, p2.first), std::min(p1.second, p2.second)};
        pair<int64_t, int64_t> br2 = {std::max(p1.first, p2.first), std::max(p1.second, p2.second)};

        for(int x = tl2.first; x <= br2.first; ++x) {
            for(int y = tl2.second; y <= br2.second; ++y) {
                grid[x][y] = 2;
            }
        }
    }

    std::deque<pair<int64_t, int64_t>> q;
    q.push_back({0,0});
    grid[0][0] = 0;
    int64_t count = 0;
    int64_t print_next = 1;

    while(q.size()) {

        ++count;
        if (count == print_next) {
            std::cout << "flooded " << count << " fields" << std::endl;
            print_next *= 2;
        }

        auto [x, y] = q.front();
        q.pop_front();

        array<pair<int64_t, int64_t>, 4> neigs = {{
                  {x + 1, y},
                    {x - 1, y},
                    {x, y + 1},
                    {x, y - 1}       
        }};

        for (const auto& neig : neigs) {
            auto [nx, ny] = neig;
            if (nx < 0 || ny < 0 || nx >= br.first || ny >= br.second) {
                continue;
            }

            if (grid[nx][ny] != 1) {
                continue;
            }

            grid[nx][ny] = 0;
            q.push_back({nx, ny});
        }
    }

    auto check_no_zero = [&](pair<int64_t, int64_t> p1, pair<int64_t, int64_t> p2) {
        for(int x = p1.first; x <= p2.first; ++x) {
            for(int y = p1.second; y <= p2.second; ++y) {
                if (grid[x][y] == 0) {
                    return false;
                }
            }
        }
        return true;
    };

    int64_t res2 = 0;

    count = 0;
    print_next = 1;
    for (int i = 0; i + 1< pairs.size(); ++i) {
        for (int j = i + 1; j + 1 < pairs.size(); ++j) {
            ++count;
            if (count == print_next) {
                std::cout << "Checked " << count << " pairs" << std::endl;
                print_next *= 2;
            }
            const auto& p1 = pairs[i];
            const auto& p2 = pairs[j];


            pair<int64_t, int64_t> tl = {std::min(p1.first, p2.first), std::min(p1.second, p2.second)};
            pair<int64_t, int64_t> br = {std::max(p1.first, p2.first), std::max(p1.second, p2.second)};

            if (!check_no_zero({tl.first, tl.second}, {br.first, tl.second})
                || !check_no_zero({tl.first, tl.second}, {tl.first, br.second})
                || !check_no_zero({br.first, tl.second}, {br.first, br.second})
                || !check_no_zero({tl.first, br.second}, {br.first, br.second})) {
                continue;
            }
            int64_t area = (br.first - tl.first + 1) * (br.second - tl.second + 1);
            res2 = max(res2, area); 
        }
    }

    cout << "Max area no flood: " << res2 << endl;
    
    return 0;
}