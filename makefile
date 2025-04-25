# Diretórios
SRC_DIR := src
INCLUDE_DIR := include
BUILD_DIR := build
BIN_DIR := bin

# Detectar sistema operacional
ifeq ($(OS),Windows_NT)
    EXE := .out
    DEL_FILE := del /Q
    RMDIR := rmdir /S /Q
    MKDIR = if not exist "$(subst /,\,$(1))" mkdir "$(subst /,\,$(1))"
else
    EXE :=
    DEL_FILE := rm -f
    RMDIR := rm -rf
    MKDIR = mkdir -p $(1)
endif

# Nome final do binário
BIN := $(BIN_DIR)/ssp_npm_solver$(EXE)

# Compilador e flags
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

# Busca todos os arquivos .cpp dentro de src/
SRCS := $(wildcard $(SRC_DIR)/**/*.cpp) $(wildcard $(SRC_DIR)/*.cpp)
# Gera os .o correspondentes, mantendo a estrutura de diretórios
OBJS := $(patsubst $(SRC_DIR)/%.cpp, $(BUILD_DIR)/%.o, $(SRCS))

# Target padrão
all: $(BIN)

# Linkagem final
$(BIN): $(OBJS)
	@$(call MKDIR,$(BIN_DIR))
	$(CXX) $^ -o $@

# Compilação dos .cpp para .o
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	@$(call MKDIR,$(dir $@))
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Limpeza
clean:
	$(RMDIR) $(BUILD_DIR) $(BIN_DIR)

# Modos
debug:
	$(MAKE) MODE=debug

release:
	$(MAKE) MODE=release