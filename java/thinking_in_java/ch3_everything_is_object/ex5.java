/** Exercise 5
* Modify ex 4 so the values
* of the data in DataOnly are assigned to and printed
* in main()
*/
public class ex5 {
  int i;
  double d;
  boolean b;
  public static void main(String[] args) {
    ex5 data = new ex5();
    data.i = 2;
    data.d = 3.2;
    data.b = true;
    System.out.println(data.i);
    System.out.println(data.d);
    System.out.println(data.b);
  }
}