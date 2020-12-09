#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>


size_t b(std::vector<int64_t> l, size_t index) {
  for(auto i = 0; i < index; i++) {
    auto sum = 0;
    std::vector<size_t> range;
    for (auto n = i; n < index; n++) {
      sum += l[n];
      range.emplace_back(l[n]);
      if (sum == l[index]) {
        auto p = std::minmax_element(range.begin(), range.end());
        return *p.first + *p.second;
      }
      if (sum > l[index]) {
        continue;
      }
    }
  }
  return -1;
}

int a(std::vector<int64_t> l, int64_t p) {
  auto k = (l.begin() + p);
  auto index = 0;
  while (k != l.end()) {
    bool found = false;
    for (auto a = index; a < index + p && !found; ++a) {
      for (auto b = a + 1; b < index + p && !found; ++b) {
        if ((l[a] + l[b]) == *k) {
          found = true;
        }
      }
    }
    if (!found) {
      auto bval = b(l, index + p);
      std::cout << "Result of b is: " << bval << std::endl;
      return *k;
    }
    ++index;
    ++k;
  }
  return -1;
}


int main() {
  std::fstream f;
  f.open("/Users/andreasvalter/xdev/other/advent/2020/9/input.txt", std::ifstream::in);
  if (!f.is_open())
    return -1;

  std::vector<int64_t> n;

  std::string line;
  while (std::getline(f, line)) {
    std::stringstream ss(line);
    int64_t x;
    ss >> x;
    n.emplace_back(x);
  }
  auto v1 = a(n, 25);
  std::cout << "Result of A is: " << v1 << std::endl;
  return 0;
}