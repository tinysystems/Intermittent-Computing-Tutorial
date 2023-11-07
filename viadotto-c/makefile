CC=gcc
CFLAGS=-I.

viadotto: main.o fixed.o viadotto.o
	$(CC) -o viadotto main.o fixed.o viadotto.o

.PHONY: clean

clean:
		rm -f *.o *.exe $(objects) viadotto