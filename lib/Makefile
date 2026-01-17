cc = gcc
CFLAGS = -O3 -fPIC -Wall
TARGET = fastConnect.so

all: $(TARGET)

$(TARGET): fastConnect.c
	$(CC) $(CFLAGS) -shared -o $(TARGET) fastConnect.c

clean:
	rm -rf $(TARGET)
