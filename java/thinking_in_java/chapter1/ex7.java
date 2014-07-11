/** Exercise 7
* Turn the Incrementable code fragments into a working program
*/
public class ex7 {
  static int i = 0;
  static void increment() { ex7.i++; }

  public static void main(String[] args) {
    System.out.println(ex7.i);
    ex7.increment();
    System.out.println(ex7.i);
  }
}