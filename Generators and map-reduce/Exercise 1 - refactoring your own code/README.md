# This architecture has some problems of its own. Can you see where this goes wrong and how you can solve them?

The AverageYear and AverageMonth are responsible for two functions: getting the average and plotting. To adhere to seperation of concerns, it would be better to split these functions up into seperate classes. 

The way these classes are set up, they are inefficient for handling larger files. There are also some hard coded elements in the code that could be changed to command line elements to make it more easily applicable to other datasets. 

