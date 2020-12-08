#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>


enum class T {
  NOP,
  ACC,
  JMP
};

struct OP {
  OP(const std::string& op, const std::string& n)
  {
    if (op == "nop") {
      mOp = T::NOP;
    }
    else if (op == "acc") {
      mOp = T::ACC;
    }
    else if (op == "jmp") {
      mOp = T::JMP;
    }
    mN = std::stoi(n);
  }
  T mOp;
  int mN;
};

void exec(OP op, size_t& i, size_t& acc) {
  if (op.mOp == T::NOP) {
    i += 1;
  }
  if (op.mOp == T::JMP) {
    i += op.mN;
  }
  if (op.mOp == T::ACC) {
    acc += op.mN;
    i += 1;
  }
}

std::optional<size_t>  run(std::vector<OP> sequence, std::map<size_t, bool>& visited, size_t& i, size_t& acc) {
  if (i > sequence.size()) {
    return acc;
  }
  exec(sequence[i], i, acc);
  if (visited.find(i) != std::end(visited)) {
    return std::nullopt;
  }
  else {
    visited[i] = true;
  }
  return run(sequence, visited, i, acc);
}

int main() {
  std::fstream f;
  f.open("input.txt", std::ifstream::in);
  if (!f.is_open())
    return -1;
  std::string op;
  std::string n;
  std::vector<OP> mOperations;
  std::string line;
  while (std::getline(f, line)) {
    std::stringstream ss(line);
    ss >> op >> n;
    mOperations.emplace_back(OP(op, n));
  }

  size_t acc = 0;
  size_t i = 0;
  std::map<size_t, bool> v;
  if (!run(mOperations, v, i, acc)) {
    for (auto p : v) {
      auto copy = mOperations;
      if (mOperations[p.first].mOp == T::JMP) {
        copy[p.first].mOp = T::NOP;
      }
      else if (mOperations[p.first].mOp == T::NOP) {
        copy[p.first].mOp = T::JMP;
      }
      else {
        continue;
      }
      acc = 0;
      i = 0;
      std::map<size_t, bool> ov;
      if (run(copy, ov, i, acc)) {
        break;
      }
    }
  }
  return 0;
}