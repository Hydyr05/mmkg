import matplotlib.pyplot as plt

# Define the line segments with their coordinates
line_segments = [
    [(4, 2.5), (10.4, 6.5)],
    [(-8.8, -7.6), (2.2, 1.9)],
    [(0, 0), (13, 5)],
    [(0, 0), (5, 8)]
]

# Create a new plot
plt.figure(figsize=(8, 8))

# Plot the line segments
for segment in line_segments:
    x_values, y_values = zip(*segment)
    plt.plot(x_values, y_values, marker='o')

# Set the plot limits to provide some padding around the points
plt.xlim(-10, 15)
plt.ylim(-10, 10)

# Add grid, labels, and title
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rasterized Line Segments')

# Show the plot
plt.show()
