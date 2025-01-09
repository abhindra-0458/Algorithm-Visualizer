# Sorting Algorithm Visualizer

This project is a Python application that visualizes sorting algorithms using the `pygame` library. It provides an interactive interface to observe how different sorting algorithms work step-by-step, making it a great educational tool for understanding sorting techniques.

---

## Features
- Visual representation of sorting algorithms.
- Supports the following sorting algorithms:
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
- Ability to toggle between ascending and descending order.
- Option to reset the list and visualize sorting again.
- Interactive controls for easy navigation.

---

## Requirements
- Python 3.x
- `pygame` library

To install `pygame`, run:
```bash
pip install pygame
```

---

## How to Run
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the script using Python:
   ```bash
   python sorting_visualizer.py
   ```
4. The application window will open, and you can start interacting with it.

---

## Controls
- **R**: Reset the list with new random values.
- **SPACE**: Start sorting using the selected algorithm.
- **A**: Set sorting order to ascending.
- **D**: Set sorting order to descending.
- **I**: Select Insertion Sort.
- **B**: Select Bubble Sort.
- **M**: Select Merge Sort.

---

## How It Works
The application begins by creating a random list of integers. Each integer represents a value that corresponds to the height of a rectangular bar on the screen. The bars are displayed side-by-side, creating a graphical representation of the list.

As the sorting algorithm executes, the positions of these bars change in real-time. This allows users to observe how the algorithm rearranges the numbers in ascending or descending order. For example, in Bubble Sort, you will see pairs of bars being swapped repeatedly until the largest (or smallest) values "bubble" to their correct positions.

To ensure a smooth and step-by-step visualization, each sorting algorithm is implemented as a Python generator. Generators yield control back to the main application after every step in the sorting process, pausing the algorithm and allowing the screen to update. This makes the visualizer interactive and easy to follow, as users can watch how individual comparisons and swaps are made.

---

## File Structure
- `sorting_visualizer.py`: The main script containing the implementation of the visualizer and sorting algorithms.

---

## Customization
You can customize the application by:
1. Changing the number of elements (`n`), minimum value (`min_val`), and maximum value (`max_val`) in the `main()` function.
2. Modifying the colors and fonts in the `DrawInfo` class.

---

## Acknowledgments
This project was created to help visualize sorting algorithms and make learning them more intuitive. Special thanks to the `pygame` community for providing excellent resources and documentation.

