import java.util.Scanner;

/**
 * Michael Palmer
 * CSCI 3230 A
 * Project 1 - Bags Implementation
 * February 5, 2015
 * To test this program, run it in the
 * command line and follow the prompts
 */

public class Project1 {
	
	private static final int BAG_SMALL = 20, BAG_LARGE = 100000;

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Do you want to test a small or large bag?");
		System.out.println("[1] Small Bag (20 elements)");
		System.out.println("[2] Large Bag (100,000 elements)");
		int size = scan.nextInt();
		scan.close();
		
		if(size == 1) {
			System.out.println("----- TESTING SMALL BAG -----");
			testSmall();
		} else if(size == 2) {
			System.out.println("\n----- TESTING LARGE BAG -----");
			testLarge();
		} else {
			System.err.println("Invalid option");
			System.exit(0);
		}
	}
	
	/**
	 * Test all methods for a small bag (20 elements)
	 */
	public static void testSmall() {
		// Create instance
		Bag b1 = new Bag(BAG_SMALL);
		
		// Print if the bag is empty
		System.out.printf("Bag is empty: %s\n", b1.isEmpty());
		
		// Add BAG_SMALL items
		System.out.println("Populating bag...");
		for(int i = 0; i < BAG_SMALL; i++) {
			b1.add("test" + i);
		}
		
		// Print if the bag is empty
		System.out.printf("Bag is empty: %s\n", b1.isEmpty());
		
		// Check if bag contains an item
		String randElement = "test" + (int)(Math.random() * BAG_SMALL);
		System.out.printf("Checking if bag contains \"%s\"\n", randElement);
		if( b1.contains(randElement) ) {
			System.out.printf("Bag contains \"%s\"\n", randElement);
			
			// Remove the item
			System.out.printf("Removing \"%s\" from the bag...\n", randElement);
			b1.remove(randElement);
		} else {
			System.out.printf("Bag does not contain \"%s\"\n", randElement);
		}
		
		// Remove a random item
		System.out.println("Removing a random element...");
		b1.removeRandom();
		
		// Print the size
		System.out.printf("Bag Size: %d\n", b1.size());
		
		// Create duplicate bag
		Bag b2 = new Bag(BAG_SMALL);
		
		// Add all elements
		System.out.println("Adding all elements of bag 1 to bag 2");
		b2.addAll(b1);
		
		// Make them unequal
		System.out.println("Removing a random element from bag 2");
		b2.removeRandom();
		System.out.printf("Bags are equal: %s\n", b1.equals(b2));
		
		// Compute the union of the two bags
		System.out.printf("Computing the union of bag 1 (%d elements) and bag 2 (%d elements)\n", b1.size(), b2.size());
		Bag b3 = b1.union(b2);
		System.out.printf("Bag 3 now contains %d elements\n", b3.size());
	}
	
	/**
	 * Test all methods for a large bag (100,000 elements)
	 */
	public static void testLarge() {
		// Create instance
		Bag b1 = new Bag(BAG_LARGE);
		
		// Print if the bag is empty
		System.out.printf("Bag is empty: %s\n", b1.isEmpty());
		
		// Add BAG_SMALL items
		System.out.println("Populating bag...");
		for(int i = 0; i < BAG_LARGE; i++) {
			b1.add("test" + i);
		}
		
		// Print if the bag is empty
		System.out.printf("Bag is empty: %s\n", b1.isEmpty());
		
		// Check if bag contains an item
		System.out.println("Checking if bag contains \"test5\"");
		if( b1.contains("test5") ) {
			System.out.println("Bag contains \"test5\"");
			// Remove the item
			System.out.println("Removing \"test5\" from the bag...");
			b1.remove("test5");
		} else {
			System.out.println("Bag does not contain \"test5\"");
		}
		
		// Remove 10 random items
		System.out.println("Removing a random element...");
		for(int i = 0; i < 10; i++) {
			b1.removeRandom();
		}
		
		// Print the size
		System.out.printf("Bag Size: %d\n", b1.size());
		
		// Create duplicate bag
		Bag b2 = new Bag(BAG_LARGE);
		
		// Add all elements
		System.out.println("Adding all elements of bag 1 to bag 2");
		b2.addAll(b1);
		
		// Make them unequal
		System.out.println("Removing a random element from bag 2");
		b2.removeRandom();
		System.out.printf("Bags are equal: %s\n", b1.equals(b2));
		
		// Compute the union of the two bags
		System.out.printf("Computing the union of bag 1 (%d elements) and bag 2 (%d elements)\n", b1.size(), b2.size());
		Bag b3 = b1.union(b2);
		System.out.printf("Bag 3 now contains %d elements\n", b3.size());
	}
}

class Bag {
	private Object[] bag;	// The bag
	private int count = 0;	// Number of elements in the bag
	
	/**
	 * Constructor to initialize a new bag
	 * @param size The maximum size of the bag
	 */
	public Bag(int size) {
		bag = new Object[size];
	}
	
	/**
	 * Add an element to the bag
	 * @param item Item to add
	 */
	public void add(Object item) {
		double start = System.nanoTime();
		int counter = 0;
		if(count < bag.length) {
			counter++; // comparing count to the actual bag size
			bag[count++] = item;
			counter++; // assigning item to bag[count++]
		} else {
			System.err.println("Error: Bag is full");
			System.exit(1);
		}
		
		/* Not printing statistics to reduce the output to the
		 * console for large bags (i.e. 100,000 elements).
		 * To print statistics, simply uncomment the line below.
		 */
		// printStatistics("add()", counter, start, System.nanoTime());
	}
	
	/**
	 * Print statistics about method execution
	 * @param method Name of the method
	 * @param counter Count for basic operations
	 * @param start Start time (nano seconds)
	 * @param stop End time (nano seconds)
	 */
	private void printStatistics(String method, int counter, double start, double stop) {
		System.out.printf("Ran %s in %fms with %d operations executed\n", method, (stop - start) / 1000000, counter);
	}
	
	/**
	 * Add all the elements of the supplied bag
	 * @param b Bag containing elements to add
	 */
	public void addAll(Bag b) {
		double start = System.nanoTime();
		int counter = 0;
		
		// Iterate through all elements
		for(int i = 0; i < b.size(); i++) {
			counter++; // comparing i to b.size();
			
			// Add element to the bag
			this.add( b.get(i) );
		}
		
		// Output statistics
		printStatistics("addAll()", counter, start, System.nanoTime());
	}
	
	/**
	 * Get the object at the specified index from the bag
	 * @param index Index of the object
	 * @return Object
	 */
	public Object get(int index) {
		return bag[index];
	}
	
	/**
	 * Remove the selected object from the bag
	 * @param item Object to remove from the bag
	 */
	public void remove(Object item) {
		double start = System.nanoTime();
		int counter = 0;
		
		// Iterate through all elements
		for(int i = 0; i < count; i++) {
			counter++;
			
			// Find the corresponding object
			if(bag[i].equals(item)) {
				counter++;
				
				// Reorder the bag
				for(int j = i; j < count - 1; j++) {
					counter++;
					bag[j] = bag[j+1];
					counter++;
				}
				
				// Set the final element to null
				bag[count - 1] = null;
				counter++;
				
				// Update the element count
				count--;
				counter++;
				
				// Output statistics
				printStatistics("remove()", counter, start, System.nanoTime());
				return;
			}
		}
		
		// Could not find the item in the bag, exiting with error
		System.err.printf("Error: Item \"%s\" does not exist in the bag.\n", item);
		System.exit(1);
	}
	
	/**
	 * Remove a random element from the bag
	 */
	public void removeRandom() {
		if(count > 0) {
			// Select a random index
			int index = (int)(Math.random() * count);
			
			// Remove the object at the corresponding index
			remove( get(index) );
		} else {
			// Bag is empty
			System.err.println("Error: The bag is empty.");
			System.exit(1);
		}
	}
	
	/**
	 * Check if the bag contains the provided object
	 * @param item Object
	 * @return true/false
	 */
	public boolean contains(Object item) {
		double start = System.nanoTime();
		int counter = 0;
		
		// Iterate through all elements
		for(int i = 0; i < count; i++) {
			counter++;
			
			// Find the corresponding object
			if(bag[i].equals(item)) {
				counter++;
				
				// Output statistics
				printStatistics("contains()", counter, start, System.nanoTime());
				
				// Found the item, returning true
				return true;
			}
		}
		
		// Output statistics
		printStatistics("contains()", counter, start, System.nanoTime());
		
		// Could not find the item, returning false
		return false;
	}
	
	/**
	 * Perform a union of two bags
	 * @param b2 Bag to combine with the current instance
	 * @return Bag containing the elements of the current instance and b2
	 */
	public Bag union(Bag b2) {
		double start = System.nanoTime();
		int counter = 0;
		
		// Create a new bag large enough to fit
		// the elements of both bag 1 and bag 2
		Bag b3 = new Bag(this.size() + b2.size());
		counter++;
		
		// Add all the elements of the first bag to the new bag
		b3.addAll(this);
		
		// Add all the elements of the second bag to the new bag
		b3.addAll(b2);
		
		// Output statistics
		printStatistics("union()", counter, start, System.nanoTime());
		
		// Return the new bag
		return b3;
	}
	
	/**
	 * Check if a bag has the same elements as this instance
	 * @param b Bag to compare the current instance to
	 * @return true if bags contain the same elements
	 */
	public boolean equals(Bag b) {
		double start = System.nanoTime();
		int counter = 0;
		
		// Check that the bags are equal in size
		if( b.size() != count ) {
			counter++;
			
			// Output statistics
			printStatistics("equals()", counter, start, System.nanoTime());
			
			// Bags not equal in size, therefore, not equal; returning false
			return false;
		}
		
		// Iterate through the bag
		for(int i = 0; i < b.size(); i++) {
			counter++;
			
			// Check that the current instance contains
			// the elements of the external bag
			if( !this.contains( b.get(i) ) ) {
				// Output statistics
				printStatistics("equals()", counter, start, System.nanoTime());
				
				// Could not find a common element, returning false
				return false;
			}
		}
		
		// Output statistics
		printStatistics("equals()", counter, start, System.nanoTime());
		
		// Bags are equal, returning true
		return true;
	}
	
	/**
	 * Check if the bag is empty
	 * @return true if the bag is empty
	 */
	public boolean isEmpty() {
		return count == 0;
	}
	
	/**
	 * Get the size of the bag
	 * @return number of elements in the bag
	 */
	public int size() {
		return count;
	}
}