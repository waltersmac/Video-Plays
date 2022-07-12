def max_concurrent(dict):

     """ Create a list of the dictionary values
          and return with the max value"""

     values = list(dict.values())

     return max(values)


def concurrent_intervals(intervals):

    """ Initially sorting the start/end dates
        and then processing the list of tuples
        to find the concurrent occurances"""

    ordered_times = sorted(intervals, key=lambda tup: tup[0])

    # Dictionary and list for tracking
    count_dict = {}
    current = []

    # Variables for tracking
    i = 0
    count = 1

    # Initialise the finish times before while loop
    current_end = ordered_times[0][1]

    # looping through the ordered times
    while i < len(ordered_times)-1:

        # Initialise the start times
        next_start = ordered_times[i+1][0]

        # Comparing the end time with start times
        # to see if they overlap
        if next_start <= current_end:

            # Incrementing the count
            count = count + 1

            # keeping the current end date
            current.append(current_end)
            current_end = current.pop()

            # Updating the count of concurrent
            count_dict[current_end] = count

        # Updating the occurance and assigning the next end time
        else:
            count_dict[current_end] = count
            current_end = ordered_times[i+1][1]

        # Updating for indexing
        i += 1

    return max_concurrent(count_dict)


if __name__ == '__main__':

    l = [(5, 7), (11, 116), (3, 4), (10, 12), (6, 12), (10,13), (11,300)]

    print("Original list of start and end times: {}".format(l))
    concurrent_dict = concurrent_intervals(l)
    print("End time dicionary: {}".format(concurrent_dict))
