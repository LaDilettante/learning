/** Exercise 8
* Write a program to demonstrate that no matter how many objects
* you create of a particular class, there is only one instance
* of a particular static field in that class
*/
public class Ex8 {
  static int i;
  void increment() { i++; }

  public static void main(String[] args) {
    Ex8 object1 = new Ex8();
    Ex8 object2 = new Ex8();
    object1.increment();
    System.out.println(object1.i == object2.i);
    object2.i++; // Can increment this way as well
    System.out.println(object1.i == object2.i);
  }
}