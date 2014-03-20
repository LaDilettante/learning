public class PhraseOMatic {
	public static void main (String[] args) {

		// Make three sets of words too choose from
		String[] wordListOne = {"web-based", "pervasive", "dynamic"};
		String[] wordListTwo = {"empowered", "sticky"};
		String[] wordListThree = {"process", "tipping-point", "solution"};

		// Find out how many words are in each list
		int oneLength = wordListOne.length;
		int twoLength = wordListTwo.length;
		int threeLength = wordListThree.length;

		// Generate three random numbers
		int rand1 = (int) (Math.random() * oneLength);
		int rand2 = (int) (Math.random() * twoLength);
		int rand3 = (int) (Math.random() * threeLength);

		// Now build a phrase!
		String phrase = wordListOne[rand1] + " " + wordListTwo[rand2] + " " + 
			wordListThree[rand3];

		// Print out the phrase
		System.out.println("What we need is a " + phrase);
	}
}