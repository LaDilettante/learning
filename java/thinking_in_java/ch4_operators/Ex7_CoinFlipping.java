/** Exercise 7
* Write a program that simulates coin-flipping
*/
import java.util.Random;

public class Ex7_CoinFlipping {
  public static void main(String[] args) {
    Random rand = new Random();
    // float f = rand.nextFloat();
    // if (f < 0.5) {
    //   System.out.println("head");
    // } else {
    //   System.out.println("tail");
    // }
    boolean flip = rand.nextBoolean();
    System.out.print("OUTCOME: ");
    System.out.println(flip ? "HEAD" : "TAIL");
  }
}