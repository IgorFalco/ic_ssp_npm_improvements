SRC_DIR := src
INCLUDE_DIR := include
BUILD_DIR := build
BIN_DIR := bin
BIN := $(BIN_DIR)/ssp_npm_solver.out

CXX := g++
CXXFLAGS := -std=c++17 -Wall -I$(INCLUDE_DIR) -I$(SRC_DIR)

RELEASE_FLAGS := -O3 -march=native
DEBUG_FLAGS := -g -O0

MODE ?= release

ifeq ($(MODE),release)
	CXXFLAGS += $(RELEASE_FLAGS)
else ifeq ($(MODE),debug)
	CXXFLAGS += $(DEBUG_FLAGS)
else
	$(error Unknown MODE: $(MODE). Use 'release' or 'debug')
endif

SRCS := $(shell find $(SRC_DIR) -name '*.cpp')
OBJS := $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(SRCS))

all: $(BIN)

$(BIN): $(OBJS)
	@mkdir -p $(BIN_DIR)
	$(CXX) $^ -o $@

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(BUILD_DIR) $(BIN_DIR)

debug:
	$(MAKE) MODE=debug

release:
	$(MAKE) MODE=release