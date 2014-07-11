/** Exercise 6
* Write a program that includes and calls the storage()
* method defined as a code fragment in this chapter
*/
public class ex6 {
  static int storage(String s) {
    return s.length() * 2;
  }

  public static void main(String[] args) {
    System.out.println(ex6.storage("a"));
  }
}