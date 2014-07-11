/** Exercise 2
* Create a class containting and int and a char that are not 
* initialized and print their values to verify that Java 
* performs default initialization */
public class ex1 {
  int i;
  char c;

  public ex1() {
    System.out.println(i);
    System.out.println(c);
  }

  public static void main(String[] args) {
    new ex1();
  }
}

// i should be defaulted to 0, c should be defaulted to blank

   