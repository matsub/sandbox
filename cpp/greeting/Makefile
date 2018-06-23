# compiler options
CXX := clang++
INCLUDE := -I .
CXXFLAGS := -W -Wall -O2 $(INCLUDE)

TARGETS := $(wildcard src/*.cpp)
TARGETS := $(notdir $(TARGETS))
TARGETS := $(basename $(TARGETS))

LIB_DIR := src/greeting
LIB_TARGETS := $(wildcard $(LIB_DIR)/*.cpp)
LIB_TARGETS := $(notdir $(LIB_TARGETS:.cpp=.o))
LIB_TARGETS := $(addprefix lib/, $(LIB_TARGETS))


# build
.PHONY: all
all: $(TARGETS)
$(TARGETS): %: lib/greeting.a
	$(CXX) $(CXXFLAGS) -o bin/$@ src/$@.cpp $<

# pattern rules
lib/greeting.a: $(LIB_TARGETS)
	ar r $@ $^

lib/%.o: $(LIB_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<


# subcommands
.PHONY: clean
clean:
	$(RM) $(wildcard lib/*)

.PHONY: clean-all
clean-all: clean
	$(RM) $(wildcard bin/*)
