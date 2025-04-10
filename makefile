# Diretórios
SRC_DIR := src
INCLUDE_DIR := include
BUILD_DIR := build
BIN_DIR := bin
BIN := $(BIN_DIR)/ssp_npm_solver.out

# Compiler
CXX := g++
CXXFLAGS := -std=c++17 -Wall -I$(INCLUDE_DIR)

# Flags para modos
RELEASE_FLAGS := -O3 -march=native
DEBUG_FLAGS := -g -O0

# Modo padrão
MODE ?= release

ifeq ($(MODE),release)
	CXXFLAGS += $(RELEASE_FLAGS)
else ifeq ($(MODE),debug)
	CXXFLAGS += $(DEBUG_FLAGS)
else
	$(error Unknown MODE: $(MODE). Use 'release' or 'debug')
endif

# Fontes e objetos
SRCS := $(wildcard $(SRC_DIR)/*.cpp)
OBJS := $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(SRCS))

# Target principal
all: $(BIN)

# Linkagem final
$(BIN): $(OBJS)
	@mkdir -p $(BIN_DIR)
	$(CXX) $^ -o $@

# Compilação dos .cpp em .o
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Limpeza dos arquivos gerados
clean:
	rm -rf $(BUILD_DIR) $(BIN_DIR)

# Debug específico
debug:
	$(MAKE) MODE=debug

# Release explícito
release:
	$(MAKE) MODE=release