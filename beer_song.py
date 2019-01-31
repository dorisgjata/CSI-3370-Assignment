def main():
    ninety_nine_bottles_of_beer()
def ninety_nine_bottles_of_beer():
  for bottles in range(99, 1, -1):
        if bottles == 1:
            print( "1 bottle of	beer on the wall, 1 bottle of beer")
	        print(bootles-1, "take one down, pass it around, no more bottles of beer on the	wall")

        else:
            print(bootles, "%d bottles of beer on the wall, %d bottles of beer")
            print(bootles-1, "take one down, pass it around, %d bottles of beer on the wall")

if __name__ == "__main__":
    main()