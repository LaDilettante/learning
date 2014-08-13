/** Exercise 3
* Create a class containing a <em>float</em>
* and use it to demonstrate aliasing during method calls
*/
class FloatNumber {
  float f;
}

public class Ex3_AliasingInMethod {
  /** The key idea is that f(FloatNumber fnum) does not
  * copy fnum into the local scope, but pass the reference.
  * Therefore, f() will modify the fnum outside of it.
  */
  static void f(FloatNumber fnum) {
    fnum.f = 2.2f;
  }

  public static void main(String[] args) {
    FloatNumber x = new FloatNumber();
    x.f = 1.1f;
    System.out.println("Before reassigning, x.f is " + x.f);
    f(x);
    System.out.println("After reassigning, x.f is " + x.f);
  }
}