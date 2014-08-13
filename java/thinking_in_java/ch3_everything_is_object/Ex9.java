/** Exercise 9
* Write a program to demonstrate that
* autoboxing works for all the primitive types
* and their wrappers.
*/
public class Ex9 {
  public static void main(String[] args) {
    Character ch = 'x';
    char c = ch;
    System.out.println(ch instanceof Character);
    // System.out.println(c instanceof char);
    // That doesn't work because c is a char, NOT a reference. WOW!
    System.out.println(c);
  }
}