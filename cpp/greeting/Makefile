# compiler options
CXX := clang++
INCLUDE := -I .
CXXFLAGS := -W -Wall -O2 $(INCLUDE)

# build
.PHONY: hello
hello: lib/hello.a
	$(CXX) $(CXXFLAGS) -o bin/hello src/hello.cpp $<

# pattern rules
lib/hello.a: lib/hello.o
	ar r $@ $^

lib/hello.o: src/greeting/hello.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# subcommands
.PHONY: clean
clean:
	$(RM) $(wildcard lib/*)

.PHONY: clean-all
clean-all: clean
	$(RM) $(wildcard bin/*)
