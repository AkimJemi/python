rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
squares = list(map(min, rectangles))
print([i for i in squares])
highest = max(squares)
squares_filtered = [i for i in squares if i >= highest]
print(len(squares_filtered))
