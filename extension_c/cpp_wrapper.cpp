#include <iostream>
#include <vector>

class Wrap {
 public:
  bool check3multp(int a) {
    auto cond = (a % 3 == 0);
    if (!cond) {
      col_.emplace_back(a);
    }
    return cond;
  }

  void showRec() {
    std::cout << "Record: ";
    for (auto i : col_) {
      std::cout << i << ", ";
    }
    std::cout << "\n";
  }

 private:
  std::vector<int> col_;
};

extern "C" {
Wrap* Wrap_new() { return new Wrap(); }
bool Wrap_myFunction(Wrap* geek, int n) {
  if (!geek) {
    std::cout << "Null geek pointer, did you forget to pass the obj parameter?"
              << std::endl;
    return false;
  }

  std::cout << "Get n: " << n << std::endl;
  return geek->check3multp(n);
}

void Wrap_show(Wrap* geek) { geek->showRec(); }
}
