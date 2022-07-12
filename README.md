# Maximum number of video plays that were playing concurrently

### My Initial Thoughts

- My first initial question were in regards to the source data Structure
  - Would it be from a SQL database, or would it be provided in a dictionary format or tuple?
  - The data structure in question could be an array, a tuple, or a dictionary
- How could I leverage that data structure to solve the problem I have been asked?
  - This would probably be an overlap of the last question
- What procedure can I think of if I have the start and end time of each video?

### Python Script
- I decided to test with tuple dummy data for simplicity as I wasn't sure of the initial data structure
- The python script "concurrent_count.py" is made up of 2 method functions
  - The first is called "concurrent_intervals" which processes the data to find the numbers for the concurrent sessions, within this method I sorted the tuples before finding the maximum concurrent number
  - This method then calls the "max_concurrent" method to return the maximum number within the dictionary
